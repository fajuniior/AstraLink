# AstraLink

**AstraLink** é um sistema em Python puro que modela uma rede de economia espacial por meio de um **grafo ponderado**. O projeto conecta bases terrestres, satélites, relés orbitais, fábricas em microgravidade, depósitos de propelente, hubs lunares, minas, robôs e infraestrutura de comunicação profunda para calcular rotas estratégicas entre ativos.

A proposta acadêmica do sistema é demonstrar como **grafos** e **Programação Dinâmica** podem apoiar decisões logísticas em cenários complexos. No AstraLink, cada vértice representa um ativo espacial ou terrestre, enquanto cada aresta representa uma conexão operacional com pesos de **tempo**, **custo**, **risco**, **energia** e **distância**.

## Problema resolvido

Em uma economia espacial realista, diferentes ativos precisam colaborar para transportar dados, energia, peças, recursos, suporte médico e informações ambientais. O problema é que uma rede desse tipo pode ter muitas rotas possíveis entre origem e destino, e cada rota apresenta vantagens e desvantagens diferentes.

> O AstraLink resolve esse problema ao calcular automaticamente a melhor rota entre dois ativos da rede, considerando critérios como menor tempo, menor custo, menor risco, menor consumo de energia ou melhor score composto.

## Estrutura modular do projeto

O projeto foi reorganizado em módulos para deixar o código mais profissional, legível e fácil de manter. O arquivo `src/main.py` ficou responsável apenas por iniciar o sistema, enquanto os dados, o grafo, os algoritmos e o menu foram separados em arquivos próprios.

```text
astralink/
├── main.py
├── README.md
├── ENTREGA_DO_PROJETO.md
├── validar_projeto.py
├── docs/
│   └── EXPLICACAO_ACADEMICA.md
├── exports/
│   ├── exemplo_rota_biohub_regolithworks.csv
│   ├── exemplo_rota_biohub_regolithworks.json
│   ├── mapa_astralink.mmd
│   └── mapa_astralink.txt
└── src/
    ├── __init__.py
    ├── main.py
    ├── dados.py
    ├── grafo.py
    ├── algoritmos.py
    └── menu.py
```

| Arquivo | Responsabilidade principal |
|---|---|
| `src/dados.py` | Armazena os vértices e as conexões da rede espacial. |
| `src/grafo.py` | Monta a estrutura do grafo, adiciona arestas e consulta conexões. |
| `src/algoritmos.py` | Implementa Floyd-Warshall, Dijkstra, cálculo de rotas, estatísticas, exportação e mapa textual. |
| `src/menu.py` | Controla a interface interativa exibida no terminal. |
| `src/main.py` | Inicia o programa quando executado a partir da pasta `src`. |
| `main.py` | Facilita a execução do projeto a partir da raiz do repositório. |

## Como executar

O projeto usa apenas bibliotecas padrão do Python. Portanto, não é necessário instalar dependências externas. Para executar pela raiz do repositório, use:

```bash
python main.py
```

Também é possível executar diretamente o ponto de entrada da pasta `src`:

```bash
python src/main.py
```

## Funcionalidades implementadas

| Funcionalidade | Descrição |
|---|---|
| Menu interativo | Permite navegar pelas opções do sistema pelo terminal. |
| Listagem de vértices | Mostra os ativos da rede, suas categorias, regiões e funções. |
| Listagem de conexões | Mostra todas as arestas com distância, tempo, custo, risco e energia. |
| Cálculo de melhor rota | Usa Floyd-Warshall para encontrar a rota ideal segundo o critério escolhido. |
| Comparação de critérios | Compara rotas por tempo, custo, risco, energia e score composto. |
| Análise de hubs críticos | Identifica nós importantes por grau de conexão e centralidade aproximada. |
| Simulação de falha | Recalcula rotas quando um ativo fica indisponível. |
| Comparação Floyd-Warshall x Dijkstra | Mostra diferenças de uso entre os dois algoritmos de menor caminho. |
| Exportação JSON/CSV | Salva rotas calculadas em arquivos reutilizáveis. |
| Estatísticas da rede | Mostra quantidade de vértices, arestas, densidade e categorias. |
| Mapa visual simples | Gera mapa textual e arquivo Mermaid da rede. |

## Exemplo real de execução

O exemplo abaixo corresponde a uma rota real calculada pelo sistema com o critério **menor risco**. Ele foi incluído para facilitar a compreensão do professor sem a necessidade de executar imediatamente o projeto.

| Entrada | Valor usado |
|---|---|
| Origem | BioHub Amazônia |
| Código de origem | `MAN` |
| Destino | Fábrica Lunar RegolithWorks |
| Código de destino | `LFACT` |
| Critério | Menor risco |

A rota encontrada é:

```text
BioHub Amazônia
→ Satélite Nexus-4
→ Relay Orbital Atlas
→ Fábrica Lunar RegolithWorks
```

| Métrica | Resultado |
|---|---:|
| Tempo total | 18h |
| Risco total | 3 |
| Energia total | 420 MWh |
| Custo estimado | US$ 22,8 milhões |
| Distância acumulada | 417.800 km |

Essa rota apresenta risco total baixo porque usa um canal prioritário entre o BioHub Amazônia e o Satélite Nexus-4, uma subida protegida para o Relay Orbital Atlas e um canal logístico protegido até a Fábrica Lunar RegolithWorks.

## Explicação do score composto

O **score composto** combina múltiplos fatores operacionais para gerar uma rota equilibrada. Em vez de otimizar apenas um indicador isolado, ele considera simultaneamente tempo, custo, risco e energia. Essa abordagem é útil quando a melhor decisão não é necessariamente a rota mais rápida ou mais barata, mas a rota com melhor equilíbrio entre eficiência e segurança.

| Fator | Peso no score | Justificativa |
|---|---:|---|
| Tempo | 0,35 | Rotas mais rápidas ajudam em emergências e reduzem atrasos operacionais. |
| Custo | 1,10 | O custo financeiro influencia a viabilidade econômica da missão. |
| Risco | 4,50 | O risco recebe peso maior porque segurança e confiabilidade são prioridades em operações espaciais críticas. |
| Energia | 0,025 | O consumo energético afeta sustentabilidade, disponibilidade operacional e autonomia. |

A fórmula usada no código é:

```text
score = tempo × 0,35 + custo × 1,10 + risco × 4,50 + energia × 0,025
```

Com isso, uma rota muito barata, mas perigosa, pode perder para uma rota um pouco mais cara e muito mais segura. Essa decisão deixa o modelo mais coerente com missões críticas, nas quais falhas podem causar prejuízos técnicos, econômicos e humanos.

## Floyd-Warshall e Programação Dinâmica

O algoritmo **Floyd-Warshall** é usado para calcular os menores caminhos entre todos os pares de vértices de um grafo ponderado. Ele funciona por uma lógica de Programação Dinâmica, pois testa gradualmente se um vértice intermediário melhora o caminho entre dois outros vértices.[1]

A recorrência usada no projeto é:

```text
dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
```

Na prática, isso significa que o sistema verifica se passar pelo nó intermediário `k` torna o caminho entre `i` e `j` melhor do que o caminho conhecido anteriormente. Essa lógica é adequada para o AstraLink porque o sistema pode precisar comparar muitas rotas diferentes dentro da mesma rede.

## Comparação entre Floyd-Warshall e Dijkstra

O projeto também inclui uma comparação com **Dijkstra**, algoritmo clássico para encontrar menores caminhos a partir de uma origem em grafos ponderados com pesos não negativos.[2]

| Algoritmo | Melhor uso no projeto | Característica principal |
|---|---|---|
| Floyd-Warshall | Quando se deseja consultar rotas entre muitos pares de vértices. | Calcula todos os pares de rotas em uma execução. |
| Dijkstra | Quando se deseja uma rota pontual entre uma origem e um destino. | Parte de uma origem e expande os caminhos mais promissores. |

No menu, a opção **10** permite comparar os dois algoritmos para a mesma origem, destino e critério. Essa funcionalidade é um diferencial acadêmico porque mostra consciência sobre alternativas algorítmicas, em vez de apenas apresentar uma solução única.

## Exportação e arquivos gerados

O AstraLink exporta rotas em **JSON** e **CSV**. O formato JSON é útil para salvar estruturas hierárquicas de dados, enquanto CSV é um formato amplamente usado para dados tabulares e planilhas.[3] [4]

| Arquivo gerado | Finalidade |
|---|---|
| `exports/exemplo_rota_biohub_regolithworks.json` | Guarda a rota exemplo com nomes, códigos, critério e totais. |
| `exports/exemplo_rota_biohub_regolithworks.csv` | Guarda os trechos da rota exemplo em formato tabular. |
| `exports/mapa_astralink.txt` | Mostra uma lista de adjacências legível no terminal. |
| `exports/mapa_astralink.mmd` | Representa a rede em Mermaid para visualização em editores compatíveis. |

## Requisitos acadêmicos atendidos

| Requisito | Situação | Evidência no projeto |
|---|---:|---|
| Definição clara do problema | Atendido | O README e o menu explicam a rede espacial e o problema de rotas. |
| Uso de grafos | Atendido | O projeto usa um grafo ponderado com vértices e arestas. |
| Mais de 30 informações/conexões | Atendido | A rede possui 35 vértices e 54 conexões. |
| Programação Dinâmica | Atendido | Floyd-Warshall usa a recorrência `dist[i][j]`. |
| Funções com `def` | Atendido | O sistema está dividido em várias funções por módulo. |
| Modularização | Atendido | O código foi separado em `dados.py`, `grafo.py`, `algoritmos.py` e `menu.py`. |
| Estruturas de dados | Atendido | Usa listas, dicionários, tuplas e conjuntos. |
| Laços de repetição | Atendido | Usa `for` e `while` em menus e algoritmos. |
| Tratamento de erro | Atendido | Usa `try/except` para leitura de números inteiros. |
| Interação com usuário | Atendido | O menu permite escolher origem, destino, critério e simulações. |
| Diferenciais técnicos | Atendido | Inclui Dijkstra, JSON/CSV, estatísticas e mapa Mermaid. |

## Referências

[1]: https://www.geeksforgeeks.org/dsa/floyd-warshall-algorithm-dp-16/ "GeeksforGeeks — Floyd Warshall Algorithm"
[2]: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm "Wikipedia — Dijkstra's algorithm"
[3]: https://docs.python.org/3/library/json.html "Python Documentation — json"
[4]: https://docs.python.org/3/library/csv.html "Python Documentation — csv"
