# Explicação Acadêmica — AstraLink

## Visão geral

O **AstraLink** é um projeto em Python puro que representa uma rede de economia espacial por meio de um **grafo ponderado**. O sistema foi construído para mostrar, de forma prática, como grafos e Programação Dinâmica podem ser aplicados à tomada de decisão em uma infraestrutura complexa formada por ativos terrestres, orbitais, lunares e de espaço profundo.

A ideia central é transformar um cenário futurista de logística espacial em um problema computacional claro. Nesse modelo, cada ativo da rede é um vértice e cada conexão operacional entre ativos é uma aresta. Como cada aresta possui pesos diferentes, o sistema consegue calcular rotas conforme critérios de tempo, custo, risco, energia ou score composto.

## Problema trabalhado

Em uma economia espacial, diversos ativos precisam colaborar em tempo real. Satélites de observação ajudam a prever desastres naturais, relés orbitais transmitem dados críticos, centros médicos dependem de comunicação confiável, depósitos de propelente abastecem missões e fábricas lunares produzem componentes para manter a infraestrutura ativa.

O problema é que, quando existe uma missão entre dois pontos da rede, há várias rotas possíveis. Uma rota pode ser rápida, mas cara. Outra pode ser barata, mas arriscada. Uma terceira pode consumir menos energia, porém levar mais tempo. O AstraLink resolve esse problema ao calcular a melhor rota conforme o objetivo escolhido pelo usuário.

> Em termos computacionais, o projeto resolve um problema de menor caminho em grafo ponderado, com múltiplos critérios de avaliação.

## Estrutura do grafo

O grafo do AstraLink é **não direcionado** e **ponderado**. Ele é não direcionado porque as conexões podem ser percorridas nos dois sentidos, representando comunicação, transporte ou fluxo operacional entre ativos. Ele é ponderado porque cada conexão possui valores associados.

| Elemento do grafo | Representação no projeto |
|---|---|
| Vértice | Um ativo da economia espacial, como uma base, satélite, relé, fábrica, mina ou robô. |
| Aresta | Uma conexão operacional entre dois ativos. |
| Peso | Um valor numérico associado à conexão, como tempo, custo, risco ou energia. |
| Caminho | Uma sequência de vértices usada para ir da origem ao destino. |
| Rota ótima | O caminho com menor peso segundo o critério escolhido. |

A rede possui **35 vértices** e **54 conexões**, ultrapassando o requisito de mais de 30 informações/conexões. Esses dados estão organizados no arquivo `src/dados.py`, o que evita misturar dados fixos com lógica algorítmica.

## Modularização do código

A versão atual do projeto foi modularizada para melhorar a qualidade da implementação. A separação por responsabilidades facilita manutenção, leitura, testes e apresentação acadêmica.

| Módulo | Papel técnico |
|---|---|
| `dados.py` | Guarda os dados da rede espacial, incluindo vértices e conexões. |
| `grafo.py` | Constrói o grafo, adiciona arestas, conta conexões e localiza arestas específicas. |
| `algoritmos.py` | Implementa Floyd-Warshall, Dijkstra, cálculo de totais, estatísticas, exportação e mapa. |
| `menu.py` | Concentra a interface interativa e as opções apresentadas ao usuário. |
| `main.py` | Serve como ponto de entrada do programa. |

Essa organização segue uma lógica profissional porque cada arquivo tem uma responsabilidade clara. Caso seja necessário alterar os dados da rede, basta editar `dados.py`. Caso seja necessário mudar o algoritmo, a alteração fica em `algoritmos.py`. Caso seja necessário ajustar textos ou opções do terminal, a modificação fica em `menu.py`.

## Programação Dinâmica com Floyd-Warshall

O algoritmo principal do projeto é **Floyd-Warshall**, usado para calcular os menores caminhos entre todos os pares de vértices. Esse algoritmo é associado à Programação Dinâmica porque constrói soluções maiores a partir de soluções menores já calculadas.[1]

A recorrência usada é:

```text
dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
```

Essa fórmula compara duas possibilidades. A primeira é manter o caminho conhecido entre `i` e `j`. A segunda é verificar se passar pelo vértice intermediário `k` melhora esse caminho. Se a rota passando por `k` for melhor, o algoritmo atualiza a matriz de distâncias.

| Símbolo | Significado |
|---|---|
| `i` | Vértice de origem. |
| `j` | Vértice de destino. |
| `k` | Vértice intermediário testado. |
| `dist[i][j]` | Melhor distância conhecida entre `i` e `j`. |
| `dist[i][k] + dist[k][j]` | Distância alternativa passando por `k`. |

No AstraLink, essa abordagem é útil porque o sistema permite comparar várias origens e destinos. Após calcular as distâncias, o programa também reconstrói o caminho usando uma matriz auxiliar chamada `proximo`.

## Critérios de otimização

O usuário pode escolher diferentes critérios para calcular a rota. Essa escolha altera o peso usado pelo algoritmo, mas mantém a mesma estrutura do grafo.

| Critério | O que minimiza | Exemplo de uso |
|---|---|---|
| Tempo | Horas operacionais acumuladas. | Emergência médica ou resposta rápida a desastre. |
| Custo | Custo financeiro estimado em milhões de dólares. | Missões com orçamento limitado. |
| Risco | Soma dos níveis de risco dos trechos. | Operações críticas que priorizam segurança. |
| Energia | Consumo energético total em MWh. | Cenários de sustentabilidade ou escassez energética. |
| Score composto | Equilíbrio entre tempo, custo, risco e energia. | Decisões estratégicas que não devem depender de um único fator. |

## Explicação detalhada do score composto

O **score composto** foi criado para representar uma decisão operacional equilibrada. Em muitos problemas reais, escolher apenas o menor tempo ou o menor custo pode gerar uma decisão ruim. Uma rota muito rápida pode ser arriscada, e uma rota barata pode consumir energia demais ou depender de ativos instáveis.

A fórmula usada é:

```text
score = tempo × 0,35 + custo × 1,10 + risco × 4,50 + energia × 0,025
```

| Fator | Peso | Interpretação acadêmica |
|---|---:|---|
| Tempo | 0,35 | Reduzir tempo é importante, mas nem sempre deve superar segurança. |
| Custo | 1,10 | O custo precisa influenciar a decisão para manter viabilidade econômica. |
| Risco | 4,50 | O risco recebe maior peso porque segurança e confiabilidade são prioridades em operações espaciais críticas. |
| Energia | 0,025 | Energia é considerada, mas em escala compatível com seus valores numéricos maiores. |

O peso do risco é propositalmente maior porque falhas em operações espaciais podem comprometer satélites, cargas, infraestrutura, dados sensíveis ou vidas humanas. O score composto, portanto, evita que a rota escolhida seja apenas a mais rápida ou barata quando isso aumentaria demais o risco.

## Exemplo prático de execução

Um exemplo real do sistema é a consulta entre o **BioHub Amazônia** e a **Fábrica Lunar RegolithWorks**, usando o critério de **menor risco**.

| Entrada | Valor |
|---|---|
| Origem | BioHub Amazônia (`MAN`) |
| Destino | Fábrica Lunar RegolithWorks (`LFACT`) |
| Critério | Menor risco |

A rota calculada pelo AstraLink é:

```text
BioHub Amazônia
→ Satélite Nexus-4
→ Relay Orbital Atlas
→ Fábrica Lunar RegolithWorks
```

| Resultado | Valor |
|---|---:|
| Tempo total | 18h |
| Risco total | 3 |
| Energia total | 420 MWh |
| Custo estimado | US$ 22,8 milhões |
| Distância acumulada | 417.800 km |

Esse exemplo é interessante academicamente porque mostra uma rota que prioriza segurança. A solução escolhe apenas três trechos, todos com risco baixo, conectando um hub ambiental terrestre a uma fábrica lunar por meio de infraestrutura orbital protegida.

## Comparação entre Floyd-Warshall e Dijkstra

A versão atual inclui uma comparação entre **Floyd-Warshall** e **Dijkstra**. O Dijkstra é um algoritmo clássico para encontrar menores caminhos a partir de uma origem em grafos ponderados com pesos não negativos.[2]

| Algoritmo | Quando é mais adequado | Como aparece no projeto |
|---|---|---|
| Floyd-Warshall | Quando se deseja calcular rotas entre todos os pares de vértices. | É o algoritmo principal usado no cálculo de rotas. |
| Dijkstra | Quando se deseja calcular uma rota específica a partir de uma origem. | É usado como comparação na opção 10 do menu. |

Essa comparação adiciona maturidade técnica ao projeto, pois demonstra que o algoritmo escolhido não é arbitrário. Floyd-Warshall é adequado para uma rede em que muitas consultas podem ser feitas, enquanto Dijkstra é eficiente para consultas pontuais.

## Exportação JSON/CSV e mapa simples

O projeto também possui exportação de rotas em **JSON** e **CSV**. JSON é adequado para guardar dados estruturados em formato hierárquico, enquanto CSV é útil para dados tabulares e compatibilidade com planilhas.[3] [4]

| Recurso | Arquivo gerado | Finalidade |
|---|---|---|
| Exportação JSON | `exports/exemplo_rota_biohub_regolithworks.json` | Registrar rota, critério, códigos, nomes e totais. |
| Exportação CSV | `exports/exemplo_rota_biohub_regolithworks.csv` | Registrar os trechos da rota em tabela. |
| Mapa textual | `exports/mapa_astralink.txt` | Mostrar a lista de adjacências de modo legível. |
| Mapa Mermaid | `exports/mapa_astralink.mmd` | Permitir visualização simples da rede em editores compatíveis. |

Esses recursos são diferenciais porque transformam o sistema em uma solução mais completa, permitindo análise posterior, apresentação visual e integração com outras ferramentas.

## Conclusão

O AstraLink atende aos requisitos acadêmicos ao apresentar um problema claro, utilizar grafos ponderados, empregar Programação Dinâmica com Floyd-Warshall, conter mais de 30 informações/conexões, usar funções, listas, dicionários, laços, tratamento de erro e interação com usuário.

Além disso, a versão modularizada melhora a qualidade técnica do projeto. Os diferenciais de comparação com Dijkstra, exportação JSON/CSV, estatísticas da rede e mapa simples tornam a solução mais profissional e mais convincente para apresentação.

## Referências

[1]: https://www.geeksforgeeks.org/dsa/floyd-warshall-algorithm-dp-16/ "GeeksforGeeks — Floyd Warshall Algorithm"
[2]: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm "Wikipedia — Dijkstra's algorithm"
[3]: https://docs.python.org/3/library/json.html "Python Documentation — json"
[4]: https://docs.python.org/3/library/csv.html "Python Documentation — csv"
