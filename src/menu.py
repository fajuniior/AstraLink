"""
Módulo de interface do AstraLink.

Este arquivo concentra o menu interativo e a experiência do usuário no terminal.
A separação melhora a organização do projeto e deixa main.py como ponto de entrada.
"""

try:
    from .algoritmos import (
        CRITERIOS_DISPONIVEIS,
        NOMES_CRITERIOS,
        PESOS_SCORE_COMPOSTO,
        calcular_totais,
        comparar_floyd_dijkstra,
        dijkstra,
        exportar_rota_csv,
        exportar_rota_json,
        floyd_warshall,
        gerar_estatisticas_rede,
        gerar_mapa_mermaid,
        gerar_mapa_textual,
        reconstruir_caminho,
    )
    from .dados import obter_conexoes, obter_vertices
    from .grafo import construir_grafo, contar_arestas, encontrar_aresta, obter_arestas_unicas
except ImportError:
    from algoritmos import (
        CRITERIOS_DISPONIVEIS,
        NOMES_CRITERIOS,
        PESOS_SCORE_COMPOSTO,
        calcular_totais,
        comparar_floyd_dijkstra,
        dijkstra,
        exportar_rota_csv,
        exportar_rota_json,
        floyd_warshall,
        gerar_estatisticas_rede,
        gerar_mapa_mermaid,
        gerar_mapa_textual,
        reconstruir_caminho,
    )
    from dados import obter_conexoes, obter_vertices
    from grafo import construir_grafo, contar_arestas, encontrar_aresta, obter_arestas_unicas


# ============================================================
# FUNÇÕES GERAIS DE INTERFACE
# ============================================================

def carregar_rede():
    """Carrega os vértices, conexões e grafo do AstraLink."""
    vertices = obter_vertices()
    conexoes = obter_conexoes()
    grafo = construir_grafo(vertices, conexoes)
    return vertices, grafo


def exibir_cabecalho():
    """Mostra o título principal do sistema."""
    print("=" * 72)
    print("ASTRALINK".center(72))
    print("Grafo inteligente para economia espacial e impacto na Terra".center(72))
    print("=" * 72)


def pausar():
    """Pausa simples para melhorar a experiência no terminal."""
    input("\nPressione ENTER para continuar...")


def ler_inteiro(mensagem, minimo=None, maximo=None):
    """Lê um número inteiro com tratamento de erro usando try/except."""
    while True:
        try:
            valor = int(input(mensagem).strip())
            if minimo is not None and valor < minimo:
                print(f"Digite um valor maior ou igual a {minimo}.")
                continue
            if maximo is not None and valor > maximo:
                print(f"Digite um valor menor ou igual a {maximo}.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


def mostrar_resumo_rede(vertices, grafo):
    """Exibe números gerais da rede."""
    print(f"Total de vértices/ativos: {len(vertices)}")
    print(f"Total de conexões/arestas: {contar_arestas(grafo)}")
    print("A rede possui mais de 30 informações/conexões, atendendo ao requisito acadêmico.")


def escolher_vertice(vertices, mensagem):
    """Solicita ao usuário um código de vértice existente."""
    while True:
        codigo = input(mensagem).strip().upper()
        if codigo in vertices:
            return codigo
        print("Código não encontrado. Digite um dos códigos disponíveis:")
        print(", ".join(sorted(vertices.keys())))


def escolher_criterio():
    """Permite ao usuário escolher o critério de otimização."""
    print("\nCritérios de otimização:")
    print("1 - Menor tempo operacional")
    print("2 - Menor custo estimado")
    print("3 - Menor risco de missão")
    print("4 - Menor consumo energético")
    print("5 - Melhor score composto")

    while True:
        opcao = input("Escolha o critério: ").strip()
        if opcao in CRITERIOS_DISPONIVEIS:
            return CRITERIOS_DISPONIVEIS[opcao]
        print("Opção inválida. Tente novamente.")


# ============================================================
# LISTAGENS E EXPLICAÇÕES
# ============================================================

def listar_vertices(vertices):
    """Lista todos os vértices do grafo de forma organizada."""
    print("\nVÉRTICES DA REDE")
    print("-" * 72)
    for codigo, dados in sorted(vertices.items()):
        print(f"[{codigo}] {dados['nome']}")
        print(f"     Categoria: {dados['categoria']} | Região: {dados['pais_regiao']}")
        print(f"     Função: {dados['funcao']}")


def listar_conexoes(vertices, grafo):
    """Lista todas as conexões sem duplicar arestas bidirecionais."""
    print("\nCONEXÕES DO GRAFO")
    print("-" * 72)
    for contador, (origem, destino, aresta) in enumerate(obter_arestas_unicas(grafo), start=1):
        print(f"{contador:02d}. {origem} -> {destino}")
        print(f"    {vertices[origem]['nome']}  <->  {vertices[destino]['nome']}")
        print(
            f"    Distância: {aresta['distancia_km']:,} km | Tempo: {aresta['tempo']} h | "
            f"Custo: US$ {aresta['custo']} mi | Risco: {aresta['risco']}/10 | "
            f"Energia: {aresta['energia']} MWh"
        )
        print(f"    Descrição: {aresta['descricao']}")


def explicar_modelo():
    """Apresenta a ideia, o problema e a estrutura de dados do projeto."""
    print("\nEXPLICAÇÃO DO PROJETO")
    print("-" * 72)
    print("Nome do sistema: AstraLink")
    print("\nIdeia principal:")
    print(
        "O sistema representa uma rede inteligente de economia espacial que conecta "
        "bases terrestres, satélites, usinas orbitais, hubs lunares, robôs e nós de "
        "comunicação profunda. A proposta é decidir rotas eficientes para levar dados, "
        "energia, recursos, componentes ou suporte médico a locais críticos na Terra e no espaço."
    )

    print("\nProblema resolvido:")
    print(
        "Em uma economia espacial real, ativos orbitais e lunares serão interdependentes. "
        "Se um desastre climático, uma falha orbital ou uma demanda médica ocorrer, "
        "será necessário escolher rapidamente qual caminho usar. O projeto resolve "
        "esse problema calculando rotas otimizadas por tempo, custo, risco, energia "
        "ou por um score composto."
    )

    print("\nEstrutura de dados:")
    print(
        "O grafo é implementado com dicionários e listas. Cada vértice representa um ativo "
        "estratégico, como uma base, satélite, fábrica orbital, mina lunar ou relé de "
        "comunicação. Cada aresta representa uma conexão operacional entre dois ativos, "
        "com pesos como distância, tempo, custo, risco e energia."
    )

    print("\nScore composto:")
    print(
        "O score composto combina tempo, custo, risco e energia para gerar uma rota "
        "equilibrada. O risco recebe peso maior porque segurança e confiabilidade são "
        "prioridades em operações espaciais críticas."
    )
    print(
        f"Pesos usados: tempo={PESOS_SCORE_COMPOSTO['tempo']}, custo={PESOS_SCORE_COMPOSTO['custo']}, "
        f"risco={PESOS_SCORE_COMPOSTO['risco']}, energia={PESOS_SCORE_COMPOSTO['energia']}."
    )


def sugerir_melhorias_futuras():
    """Mostra sugestões de evolução do projeto."""
    print("\nMELHORIAS FUTURAS")
    print("-" * 72)
    melhorias = [
        "Adicionar dados reais de satélites, clima e telemetria orbital.",
        "Criar uma interface web com mapa interativo da Terra, Lua e órbitas.",
        "Incluir IA preditiva para prever falhas, demanda médica e eventos climáticos.",
        "Permitir cadastro dinâmico de novos nós e conexões pelo usuário.",
        "Salvar simulações em banco de dados para análise posterior.",
        "Usar cenários de emergência, como tempestades solares, detritos espaciais ou enchentes.",
        "Comparar Floyd-Warshall, Dijkstra e A* em redes espaciais maiores.",
        "Adicionar cálculo de impacto ambiental e retorno econômico das rotas."
    ]
    for indice, melhoria in enumerate(melhorias, start=1):
        print(f"{indice}. {melhoria}")


def explicar_aderencia_gs():
    """Explica por que o projeto combina com a Global Solution."""
    print("\nADERÊNCIA À GLOBAL SOLUTION")
    print("-" * 72)
    print(
        "O AstraLink se encaixa na Global Solution porque une economia espacial, tecnologia, "
        "IA, inovação e impactos positivos na Terra. A solução mostra como satélites, "
        "robótica, energia orbital, bases lunares e manufatura espacial podem ser organizados "
        "em uma rede inteligente para apoiar medicina, agricultura, comunicação, sustentabilidade "
        "e resposta a emergências."
    )
    print(
        "\nA proposta também reflete a ideia de que resolver problemas extremos do espaço "
        "gera inovação útil na Terra. Ao modelar restrições como custo, risco, energia "
        "e distância, o projeto transforma a dificuldade do ambiente espacial em uma "
        "oportunidade de planejamento tecnológico e empreendedorismo."
    )


# ============================================================
# ROTAS, COMPARAÇÕES E EXPORTAÇÃO
# ============================================================

def detalhar_caminho(vertices, grafo, caminho):
    """Mostra os trechos e totais de uma rota encontrada."""
    if not caminho:
        print("Não há caminho disponível entre os vértices selecionados.")
        return

    totais = calcular_totais(grafo, caminho)

    print("\nROTA RECOMENDADA")
    print("-" * 72)
    print(" -> ".join(caminho))
    print("\nNós percorridos:")
    for codigo in caminho:
        print(f"[{codigo}] {vertices[codigo]['nome']}")

    print("\nTrechos:")
    for indice in range(len(caminho) - 1):
        origem = caminho[indice]
        destino = caminho[indice + 1]
        aresta = encontrar_aresta(grafo, origem, destino)
        if aresta is None:
            continue

        print(f"{indice + 1}. {origem} -> {destino}: {aresta['descricao']}")
        print(
            f"   Tempo: {aresta['tempo']} h | Custo: US$ {aresta['custo']} mi | "
            f"Risco: {aresta['risco']}/10 | Energia: {aresta['energia']} MWh"
        )

    print("\nTotais estimados da missão:")
    print(f"Distância acumulada: {totais['distancia_km']:,} km")
    print(f"Tempo operacional: {totais['tempo']:.2f} horas")
    print(f"Custo estimado: US$ {totais['custo']:.2f} milhões")
    print(f"Risco total: {totais['risco']}")
    print(f"Risco médio: {totais['risco_medio']:.2f}/10")
    print(f"Energia consumida: {totais['energia']:.2f} MWh")


def calcular_melhor_rota(vertices, grafo, exportar=False):
    """Fluxo de busca de rota otimizada escolhido pelo usuário."""
    listar_vertices(vertices)
    origem = escolher_vertice(vertices, "\nDigite o código de ORIGEM: ")
    destino = escolher_vertice(vertices, "Digite o código de DESTINO: ")

    if origem == destino:
        print("Origem e destino são iguais. A rota tem custo zero.")
        return

    criterio = escolher_criterio()
    distancias, proximo = floyd_warshall(vertices, grafo, criterio)
    caminho = reconstruir_caminho(origem, destino, proximo)

    print(f"\nCritério usado: {NOMES_CRITERIOS[criterio]}")
    peso = distancias[origem][destino] if caminho else 0
    if caminho:
        print(f"Peso otimizado calculado: {peso:.2f}")
    detalhar_caminho(vertices, grafo, caminho)

    if exportar and caminho:
        arquivo_base = f"exports/rota_{origem}_{destino}_{criterio}".lower()
        exportar_rota_json(f"{arquivo_base}.json", vertices, grafo, caminho, criterio, peso)
        exportar_rota_csv(f"{arquivo_base}.csv", vertices, grafo, caminho)
        print(f"\nArquivos exportados: {arquivo_base}.json e {arquivo_base}.csv")


def comparar_criterios(vertices, grafo):
    """Compara as rotas resultantes para todos os critérios disponíveis."""
    listar_vertices(vertices)
    origem = escolher_vertice(vertices, "\nDigite o código de ORIGEM: ")
    destino = escolher_vertice(vertices, "Digite o código de DESTINO: ")

    print("\nCOMPARAÇÃO DE CRITÉRIOS")
    print("-" * 72)
    for criterio in ["tempo", "custo", "risco", "energia", "score"]:
        distancias, proximo = floyd_warshall(vertices, grafo, criterio)
        caminho = reconstruir_caminho(origem, destino, proximo)
        print(f"\nCritério: {NOMES_CRITERIOS[criterio]}")
        if not caminho:
            print("Sem rota disponível.")
            continue
        print(f"Peso otimizado: {distancias[origem][destino]:.2f}")
        print("Rota: " + " -> ".join(caminho))


def comparar_algoritmos(vertices, grafo):
    """Compara Floyd-Warshall e Dijkstra para a mesma consulta."""
    listar_vertices(vertices)
    origem = escolher_vertice(vertices, "\nDigite o código de ORIGEM: ")
    destino = escolher_vertice(vertices, "Digite o código de DESTINO: ")
    criterio = escolher_criterio()

    resultado = comparar_floyd_dijkstra(vertices, grafo, origem, destino, criterio)

    print("\nCOMPARAÇÃO: FLOYD-WARSHALL x DIJKSTRA")
    print("-" * 72)
    print(f"Critério: {NOMES_CRITERIOS[criterio]}")
    print("\nFloyd-Warshall:")
    print(f"Peso: {resultado['floyd_warshall']['peso']:.2f}")
    print("Rota: " + " -> ".join(resultado["floyd_warshall"]["caminho"]))
    print(f"Indicação: {resultado['floyd_warshall']['uso_indicado']}")

    print("\nDijkstra:")
    print(f"Peso: {resultado['dijkstra']['peso']:.2f}")
    print("Rota: " + " -> ".join(resultado["dijkstra"]["caminho"]))
    print(f"Indicação: {resultado['dijkstra']['uso_indicado']}")

    if resultado["mesmo_resultado"]:
        print("\nOs dois algoritmos encontraram a mesma rota para este cenário.")
    else:
        print("\nOs algoritmos encontraram rotas diferentes, o que pode ocorrer em empates ou pesos equivalentes.")


def exportar_rota_interativa(vertices, grafo):
    """Calcula uma rota e exporta os resultados em JSON e CSV."""
    calcular_melhor_rota(vertices, grafo, exportar=True)


# ============================================================
# ANÁLISES, SIMULAÇÃO E MAPA
# ============================================================

def analisar_hubs_criticos(vertices, grafo):
    """Analisa hubs importantes pelo grau de conexão e por centralidade aproximada."""
    estatisticas = gerar_estatisticas_rede(vertices, grafo)

    print("\nANÁLISE DE HUBS CRÍTICOS")
    print("-" * 72)
    print("Top 8 por número de conexões diretas:")
    for posicao, (codigo, grau) in enumerate(estatisticas["top_grau"], start=1):
        print(f"{posicao}. {codigo} - {vertices[codigo]['nome']} | Conexões: {grau}")

    print("\nTop 8 por centralidade operacional baseada no score:")
    for posicao, (codigo, media) in enumerate(estatisticas["top_centralidade_score"], start=1):
        print(f"{posicao}. {codigo} - {vertices[codigo]['nome']} | Distância média de score: {media:.2f}")

    print("\nInterpretação:")
    print("Os hubs com alto grau e baixa distância média são pontos estratégicos da economia espacial.")
    print("Eles devem receber redundância, proteção contra falhas e prioridade de investimento.")


def mostrar_estatisticas(vertices, grafo):
    """Exibe estatísticas gerais da rede."""
    estatisticas = gerar_estatisticas_rede(vertices, grafo)

    print("\nESTATÍSTICAS DA REDE")
    print("-" * 72)
    print(f"Total de vértices: {estatisticas['total_vertices']}")
    print(f"Total de arestas: {estatisticas['total_arestas']}")
    print(f"Densidade do grafo: {estatisticas['densidade']:.4f}")

    print("\nVértices por categoria principal:")
    for categoria, quantidade in sorted(estatisticas["categorias"].items()):
        print(f"{categoria}: {quantidade}")


def simular_interrupcao(vertices, grafo):
    """Simula a queda de um nó e recalcula rotas sem esse vértice."""
    listar_vertices(vertices)
    bloqueado = escolher_vertice(vertices, "\nDigite o código do nó que ficará INDISPONÍVEL: ")
    print(f"Nó bloqueado: {bloqueado} - {vertices[bloqueado]['nome']}")

    origem = escolher_vertice(vertices, "Digite o código de ORIGEM da missão: ")
    destino = escolher_vertice(vertices, "Digite o código de DESTINO da missão: ")

    if origem == bloqueado or destino == bloqueado:
        print("A origem ou o destino está bloqueado. A missão não pode ser planejada nesse cenário.")
        return

    criterio = escolher_criterio()
    distancias, proximo = floyd_warshall(vertices, grafo, criterio, bloqueados={bloqueado})
    caminho = reconstruir_caminho(origem, destino, proximo)

    print("\nSIMULAÇÃO DE RESILIÊNCIA")
    print("-" * 72)
    print(f"Nó indisponível: {bloqueado}")
    print(f"Critério: {NOMES_CRITERIOS[criterio]}")
    if caminho:
        print(f"Peso otimizado recalculado: {distancias[origem][destino]:.2f}")
    detalhar_caminho(vertices, grafo, caminho)


def gerar_mapa(vertices, grafo):
    """Gera arquivos de mapa textual e Mermaid da rede."""
    caminho_txt = "exports/mapa_astralink.txt"
    caminho_mmd = "exports/mapa_astralink.mmd"
    gerar_mapa_textual(vertices, grafo, caminho_txt)
    gerar_mapa_mermaid(vertices, grafo, caminho_mmd)
    print("\nMAPA VISUAL SIMPLES GERADO")
    print("-" * 72)
    print(f"Mapa textual: {caminho_txt}")
    print(f"Mapa Mermaid: {caminho_mmd}")
    print("O arquivo Mermaid pode ser visualizado em editores compatíveis com diagramas Mermaid.")


# ============================================================
# MENU PRINCIPAL
# ============================================================

def exibir_menu():
    """Mostra as opções do menu principal."""
    print("\nMENU PRINCIPAL")
    print("1  - Ver ideia, problema e explicação do grafo")
    print("2  - Listar vértices/ativos da rede")
    print("3  - Listar conexões/arestas da rede")
    print("4  - Calcular melhor rota entre dois ativos")
    print("5  - Comparar rotas por todos os critérios")
    print("6  - Analisar hubs críticos da economia espacial")
    print("7  - Simular falha/interrupção de um nó")
    print("8  - Ver melhorias futuras")
    print("9  - Ver por que o projeto se encaixa na Global Solution")
    print("10 - Comparar Floyd-Warshall e Dijkstra")
    print("11 - Exportar rota em JSON e CSV")
    print("12 - Ver estatísticas da rede")
    print("13 - Gerar mapa visual simples da rede")
    print("0  - Sair")


def executar_sistema():
    """Função principal do programa."""
    vertices, grafo = carregar_rede()

    while True:
        exibir_cabecalho()
        mostrar_resumo_rede(vertices, grafo)
        exibir_menu()
        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            explicar_modelo()
            pausar()
        elif opcao == "2":
            listar_vertices(vertices)
            pausar()
        elif opcao == "3":
            listar_conexoes(vertices, grafo)
            pausar()
        elif opcao == "4":
            calcular_melhor_rota(vertices, grafo)
            pausar()
        elif opcao == "5":
            comparar_criterios(vertices, grafo)
            pausar()
        elif opcao == "6":
            analisar_hubs_criticos(vertices, grafo)
            pausar()
        elif opcao == "7":
            simular_interrupcao(vertices, grafo)
            pausar()
        elif opcao == "8":
            sugerir_melhorias_futuras()
            pausar()
        elif opcao == "9":
            explicar_aderencia_gs()
            pausar()
        elif opcao == "10":
            comparar_algoritmos(vertices, grafo)
            pausar()
        elif opcao == "11":
            exportar_rota_interativa(vertices, grafo)
            pausar()
        elif opcao == "12":
            mostrar_estatisticas(vertices, grafo)
            pausar()
        elif opcao == "13":
            gerar_mapa(vertices, grafo)
            pausar()
        elif opcao == "0":
            print("\nEncerrando o AstraLink. Até a próxima missão!")
            break
        else:
            print("\nOpção inválida. Tente novamente.")
            pausar()
