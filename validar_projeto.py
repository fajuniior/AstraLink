"""Script interno de validação do projeto AstraLink."""

from src.dados import obter_conexoes, obter_vertices
from src.grafo import construir_grafo, contar_arestas
from src.algoritmos import (
    comparar_floyd_dijkstra,
    exportar_rota_csv,
    exportar_rota_json,
    floyd_warshall,
    gerar_estatisticas_rede,
    gerar_mapa_mermaid,
    gerar_mapa_textual,
    reconstruir_caminho,
)

vertices = obter_vertices()
grafo = construir_grafo(vertices, obter_conexoes())

print("vertices", len(vertices))
print("arestas", contar_arestas(grafo))

distancias, proximo = floyd_warshall(vertices, grafo, "risco")
caminho = reconstruir_caminho("MAN", "LFACT", proximo)
print("rota_risco", caminho)
print("peso_risco", distancias["MAN"]["LFACT"])

resultado = comparar_floyd_dijkstra(vertices, grafo, "MAN", "LFACT", "risco")
print("comparacao_mesmo_resultado", resultado["mesmo_resultado"])

exportar_rota_json("exports/exemplo_rota_biohub_regolithworks.json", vertices, grafo, caminho, "risco", distancias["MAN"]["LFACT"])
exportar_rota_csv("exports/exemplo_rota_biohub_regolithworks.csv", vertices, grafo, caminho)
gerar_mapa_textual(vertices, grafo, "exports/mapa_astralink.txt")
gerar_mapa_mermaid(vertices, grafo, "exports/mapa_astralink.mmd")

estatisticas = gerar_estatisticas_rede(vertices, grafo)
print("densidade", round(estatisticas["densidade"], 4))
print("top_grau", estatisticas["top_grau"][:3])
