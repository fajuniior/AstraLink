"""
Módulo de estrutura de grafo do AstraLink.

Este arquivo contém funções responsáveis por montar e consultar o grafo.
A lógica de algoritmos fica separada em algoritmos.py, mantendo este módulo
focado na estrutura de vértices e arestas.
"""


def adicionar_aresta(grafo, origem, destino, distancia_km, tempo_horas, custo_milhoes,
                     risco, energia_mwh, descricao):
    """
    Adiciona uma conexão bidirecional ao grafo.

    Cada aresta possui múltiplos pesos para permitir análises por tempo, custo,
    risco, energia ou score composto.
    """
    conexao = {
        "destino": destino,
        "distancia_km": distancia_km,
        "tempo": tempo_horas,
        "custo": custo_milhoes,
        "risco": risco,
        "energia": energia_mwh,
        "descricao": descricao
    }
    grafo.setdefault(origem, []).append(conexao)

    conexao_inversa = conexao.copy()
    conexao_inversa["destino"] = origem
    grafo.setdefault(destino, []).append(conexao_inversa)


def construir_grafo(vertices, conexoes):
    """Constrói o grafo a partir do catálogo de vértices e da lista de conexões."""
    grafo = {codigo: [] for codigo in vertices}
    for conexao in conexoes:
        adicionar_aresta(grafo, *conexao)
    return grafo


def contar_arestas(grafo):
    """Conta arestas sem duplicar conexões bidirecionais."""
    return sum(len(conexoes) for conexoes in grafo.values()) // 2


def obter_arestas_unicas(grafo):
    """Retorna uma lista de arestas únicas, sem repetir o sentido inverso."""
    arestas = []
    vistas = set()

    for origem, conexoes in sorted(grafo.items()):
        for aresta in conexoes:
            destino = aresta["destino"]
            chave = tuple(sorted([origem, destino]))
            if chave in vistas:
                continue
            vistas.add(chave)
            arestas.append((origem, destino, aresta))

    return arestas


def encontrar_aresta(grafo, origem, destino):
    """Localiza os dados de uma aresta específica entre origem e destino."""
    for aresta in grafo.get(origem, []):
        if aresta["destino"] == destino:
            return aresta
    return None


def codigos_ordenados(vertices):
    """Retorna os códigos dos vértices em ordem alfabética."""
    return sorted(vertices.keys())
