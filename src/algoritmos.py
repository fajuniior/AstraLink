"""
Módulo de algoritmos do AstraLink.

Aqui ficam as funções de programação dinâmica, cálculo de rotas, comparação
com Dijkstra, estatísticas da rede e exportação de resultados.
"""

import csv
import json
import os
from heapq import heappop, heappush
from math import inf

try:
    from .grafo import encontrar_aresta, obter_arestas_unicas
except ImportError:
    from grafo import encontrar_aresta, obter_arestas_unicas


CRITERIOS_DISPONIVEIS = {
    "1": "tempo",
    "2": "custo",
    "3": "risco",
    "4": "energia",
    "5": "score"
}

NOMES_CRITERIOS = {
    "tempo": "menor tempo operacional",
    "custo": "menor custo estimado",
    "risco": "menor risco de missão",
    "energia": "menor consumo energético",
    "score": "melhor equilíbrio entre tempo, custo, risco e energia"
}

PESOS_SCORE_COMPOSTO = {
    "tempo": 0.35,
    "custo": 1.10,
    "risco": 4.50,
    "energia": 0.025
}


# ============================================================
# CÁLCULO DE PESOS
# ============================================================

def calcular_peso(aresta, criterio):
    """
    Calcula o peso usado pelos algoritmos conforme o critério escolhido.

    O score composto combina tempo, custo, risco e energia. O risco recebe
    peso maior porque segurança e confiabilidade são prioridades em operações
    espaciais críticas.
    """
    if criterio == "score":
        return (
            aresta["tempo"] * PESOS_SCORE_COMPOSTO["tempo"] +
            aresta["custo"] * PESOS_SCORE_COMPOSTO["custo"] +
            aresta["risco"] * PESOS_SCORE_COMPOSTO["risco"] +
            aresta["energia"] * PESOS_SCORE_COMPOSTO["energia"]
        )
    return aresta[criterio]


# ============================================================
# FLOYD-WARSHALL: PROGRAMAÇÃO DINÂMICA
# ============================================================

def floyd_warshall(vertices, grafo, criterio, bloqueados=None):
    """
    Calcula menores caminhos entre todos os pares de vértices.

    Esta é a parte principal de Programação Dinâmica do projeto. A recorrência é:
    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    """
    if bloqueados is None:
        bloqueados = set()

    codigos = [codigo for codigo in vertices if codigo not in bloqueados]
    distancias = {origem: {destino: inf for destino in codigos} for origem in codigos}
    proximo = {origem: {destino: None for destino in codigos} for origem in codigos}

    for codigo in codigos:
        distancias[codigo][codigo] = 0
        proximo[codigo][codigo] = codigo

    for origem in codigos:
        for aresta in grafo.get(origem, []):
            destino = aresta["destino"]
            if destino in bloqueados:
                continue
            peso = calcular_peso(aresta, criterio)
            if peso < distancias[origem][destino]:
                distancias[origem][destino] = peso
                proximo[origem][destino] = destino

    for intermediario in codigos:
        for origem in codigos:
            for destino in codigos:
                alternativa = distancias[origem][intermediario] + distancias[intermediario][destino]
                if alternativa < distancias[origem][destino]:
                    distancias[origem][destino] = alternativa
                    proximo[origem][destino] = proximo[origem][intermediario]

    return distancias, proximo


def reconstruir_caminho(origem, destino, proximo):
    """Reconstrói um caminho calculado por Floyd-Warshall."""
    if origem not in proximo or destino not in proximo[origem]:
        return []
    if proximo[origem][destino] is None:
        return []

    caminho = [origem]
    atual = origem
    while atual != destino:
        atual = proximo[atual][destino]
        if atual is None:
            return []
        caminho.append(atual)
    return caminho


# ============================================================
# DIJKSTRA: COMPARAÇÃO ALGORÍTMICA
# ============================================================

def dijkstra(vertices, grafo, origem, destino, criterio, bloqueados=None):
    """Calcula a melhor rota de uma origem para um destino usando Dijkstra."""
    if bloqueados is None:
        bloqueados = set()

    if origem in bloqueados or destino in bloqueados:
        return inf, []

    distancias = {codigo: inf for codigo in vertices if codigo not in bloqueados}
    anteriores = {codigo: None for codigo in vertices if codigo not in bloqueados}
    distancias[origem] = 0
    fila_prioridade = [(0, origem)]

    while fila_prioridade:
        distancia_atual, atual = heappop(fila_prioridade)

        if distancia_atual > distancias[atual]:
            continue
        if atual == destino:
            break

        for aresta in grafo.get(atual, []):
            vizinho = aresta["destino"]
            if vizinho in bloqueados:
                continue
            nova_distancia = distancia_atual + calcular_peso(aresta, criterio)
            if nova_distancia < distancias[vizinho]:
                distancias[vizinho] = nova_distancia
                anteriores[vizinho] = atual
                heappush(fila_prioridade, (nova_distancia, vizinho))

    if distancias[destino] == inf:
        return inf, []

    caminho = []
    atual = destino
    while atual is not None:
        caminho.append(atual)
        atual = anteriores[atual]
    caminho.reverse()

    return distancias[destino], caminho


def comparar_floyd_dijkstra(vertices, grafo, origem, destino, criterio):
    """Compara Floyd-Warshall e Dijkstra para uma mesma rota."""
    distancias_fw, proximo_fw = floyd_warshall(vertices, grafo, criterio)
    caminho_fw = reconstruir_caminho(origem, destino, proximo_fw)
    peso_fw = distancias_fw[origem][destino] if caminho_fw else inf

    peso_dijkstra, caminho_dijkstra = dijkstra(vertices, grafo, origem, destino, criterio)

    return {
        "criterio": criterio,
        "floyd_warshall": {
            "peso": peso_fw,
            "caminho": caminho_fw,
            "uso_indicado": "Melhor quando se deseja consultar rotas entre muitos pares de vértices."
        },
        "dijkstra": {
            "peso": peso_dijkstra,
            "caminho": caminho_dijkstra,
            "uso_indicado": "Melhor quando se deseja uma rota pontual entre uma origem e um destino."
        },
        "mesmo_resultado": caminho_fw == caminho_dijkstra and abs(peso_fw - peso_dijkstra) < 0.0001
    }


# ============================================================
# CÁLCULO DE ROTAS E ESTATÍSTICAS
# ============================================================

def calcular_totais(grafo, caminho):
    """Calcula totais estimados de distância, tempo, custo, risco e energia."""
    totais = {
        "distancia_km": 0,
        "tempo": 0,
        "custo": 0,
        "risco": 0,
        "energia": 0,
        "trechos": 0
    }

    for indice in range(len(caminho) - 1):
        origem = caminho[indice]
        destino = caminho[indice + 1]
        aresta = encontrar_aresta(grafo, origem, destino)
        if aresta is None:
            continue
        totais["distancia_km"] += aresta["distancia_km"]
        totais["tempo"] += aresta["tempo"]
        totais["custo"] += aresta["custo"]
        totais["risco"] += aresta["risco"]
        totais["energia"] += aresta["energia"]
        totais["trechos"] += 1

    totais["risco_medio"] = totais["risco"] / totais["trechos"] if totais["trechos"] else 0
    return totais


def gerar_estatisticas_rede(vertices, grafo):
    """Gera estatísticas simples da rede espacial."""
    total_vertices = len(vertices)
    total_arestas = len(obter_arestas_unicas(grafo))
    max_arestas_possiveis = total_vertices * (total_vertices - 1) / 2
    densidade = total_arestas / max_arestas_possiveis if max_arestas_possiveis else 0

    categorias = {}
    for dados in vertices.values():
        categoria_base = dados["categoria"].split("/")[0].strip()
        categorias[categoria_base] = categorias.get(categoria_base, 0) + 1

    graus = []
    for codigo in vertices:
        graus.append((codigo, len(grafo.get(codigo, []))))
    graus.sort(key=lambda item: item[1], reverse=True)

    distancias, _ = floyd_warshall(vertices, grafo, "score")
    proximidades = []
    for origem in vertices:
        soma = 0
        alcancados = 0
        for destino in vertices:
            if origem != destino and distancias[origem][destino] < inf:
                soma += distancias[origem][destino]
                alcancados += 1
        media = soma / alcancados if alcancados else inf
        proximidades.append((origem, media))
    proximidades.sort(key=lambda item: item[1])

    return {
        "total_vertices": total_vertices,
        "total_arestas": total_arestas,
        "densidade": densidade,
        "categorias": categorias,
        "top_grau": graus[:8],
        "top_centralidade_score": proximidades[:8]
    }


# ============================================================
# EXPORTAÇÃO E MAPA VISUAL SIMPLES
# ============================================================

def exportar_rota_json(caminho_arquivo, vertices, grafo, caminho, criterio, peso):
    """Exporta uma rota calculada para JSON."""
    os.makedirs(os.path.dirname(caminho_arquivo), exist_ok=True)
    totais = calcular_totais(grafo, caminho)
    dados = {
        "sistema": "AstraLink",
        "criterio": criterio,
        "peso_otimizado": peso,
        "caminho_codigos": caminho,
        "caminho_nomes": [vertices[codigo]["nome"] for codigo in caminho],
        "totais": totais
    }

    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)


def exportar_rota_csv(caminho_arquivo, vertices, grafo, caminho):
    """Exporta os trechos de uma rota calculada para CSV."""
    os.makedirs(os.path.dirname(caminho_arquivo), exist_ok=True)
    with open(caminho_arquivo, "w", encoding="utf-8", newline="") as arquivo:
        campos = ["ordem", "origem", "destino", "tempo", "custo", "risco", "energia", "distancia_km", "descricao"]
        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()

        for indice in range(len(caminho) - 1):
            origem = caminho[indice]
            destino = caminho[indice + 1]
            aresta = encontrar_aresta(grafo, origem, destino)
            if aresta is None:
                continue
            escritor.writerow({
                "ordem": indice + 1,
                "origem": vertices[origem]["nome"],
                "destino": vertices[destino]["nome"],
                "tempo": aresta["tempo"],
                "custo": aresta["custo"],
                "risco": aresta["risco"],
                "energia": aresta["energia"],
                "distancia_km": aresta["distancia_km"],
                "descricao": aresta["descricao"]
            })


def gerar_mapa_textual(vertices, grafo, caminho_arquivo):
    """Gera um mapa textual simples da rede por lista de adjacências."""
    os.makedirs(os.path.dirname(caminho_arquivo), exist_ok=True)
    linhas = [
        "MAPA TEXTUAL DA REDE ASTRALINK",
        "=" * 72,
        "Cada linha mostra um ativo e suas conexões diretas.",
        ""
    ]

    for codigo in sorted(vertices):
        vizinhos = []
        for aresta in sorted(grafo.get(codigo, []), key=lambda item: item["destino"]):
            destino = aresta["destino"]
            vizinhos.append(f"{destino}({aresta['risco']}/10 risco, {aresta['tempo']}h)")
        linhas.append(f"[{codigo}] {vertices[codigo]['nome']}")
        linhas.append("  -> " + ", ".join(vizinhos))
        linhas.append("")

    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write("\n".join(linhas))


def gerar_mapa_mermaid(vertices, grafo, caminho_arquivo):
    """Gera um mapa visual simples em formato Mermaid."""
    os.makedirs(os.path.dirname(caminho_arquivo), exist_ok=True)
    linhas = ["graph LR"]

    for codigo, dados in vertices.items():
        nome_curto = dados["nome"].replace('"', "'")
        linhas.append(f'    {codigo}["{codigo}<br/>{nome_curto}"]')

    for origem, destino, aresta in obter_arestas_unicas(grafo):
        linhas.append(f'    {origem} ---|"Risco {aresta["risco"]}/10 · {aresta["tempo"]}h"| {destino}')

    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write("\n".join(linhas) + "\n")
