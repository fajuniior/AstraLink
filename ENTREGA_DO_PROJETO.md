# Entrega do Projeto — AstraLink

## Identificação do projeto

O projeto entregue se chama **AstraLink**. O nome foi simplificado para ficar mais fácil de apresentar oralmente e para deixar a identidade do sistema mais direta. A ideia do AstraLink é representar uma rede inteligente de logística e comunicação espacial usando **grafos ponderados** e **Programação Dinâmica**.

A versão atual foi reorganizada em módulos, ganhou documentação mais clara, exemplo real de execução e diferenciais técnicos, como comparação com Dijkstra, exportação em JSON/CSV, estatísticas da rede e mapa simples em Mermaid.

## Ideia principal

O AstraLink simula uma infraestrutura de economia espacial formada por bases terrestres, satélites, relés orbitais, estações, depósitos de propelente, fábricas lunares, centros médicos, sistemas de defesa contra detritos, robôs e hubs de comunicação profunda.

Cada ponto da rede é representado como um **vértice**. Cada conexão entre dois pontos é representada como uma **aresta**. Como as conexões possuem tempo, custo, risco, energia e distância, o sistema consegue calcular qual rota é mais adequada para uma missão específica.

> A pergunta central respondida pelo projeto é: qual é a melhor rota entre dois ativos da rede espacial considerando um critério operacional escolhido pelo usuário?

## Estrutura final do código

A modularização foi feita para que o projeto pareça mais profissional e fique mais fácil de explicar ao professor. O arquivo `main.py` da raiz apenas inicia o sistema. A lógica principal fica separada em módulos dentro da pasta `src`.

| Arquivo | Responsabilidade |
|---|---|
| `src/dados.py` | Define os vértices e conexões da rede AstraLink. |
| `src/grafo.py` | Constrói e consulta a estrutura do grafo. |
| `src/algoritmos.py` | Implementa Floyd-Warshall, Dijkstra, score composto, estatísticas, exportação e mapa. |
| `src/menu.py` | Mostra o menu interativo e chama as funções do sistema. |
| `src/main.py` | Executa o menu quando o projeto é iniciado pela pasta `src`. |
| `main.py` | Permite executar o sistema diretamente pela raiz do projeto. |

## Como executar

Para executar pela raiz do projeto, use:

```bash
python main.py
```

Também é possível executar com:

```bash
python src/main.py
```

Não é necessário instalar bibliotecas externas, pois o projeto usa apenas recursos padrão do Python.

## Exemplo de apresentação ao professor

Um exemplo simples para demonstrar o funcionamento é calcular a rota do **BioHub Amazônia** até a **Fábrica Lunar RegolithWorks** usando o critério **menor risco**.

| Campo | Valor |
|---|---|
| Origem | BioHub Amazônia |
| Destino | Fábrica Lunar RegolithWorks |
| Critério | Menor risco |

A rota calculada é:

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

Esse exemplo é bom para apresentação porque mostra que o sistema não escolhe a rota aleatoriamente. Ele escolhe a rota de menor risco total com base nos pesos cadastrados nas conexões.

## Explicação do algoritmo principal

O projeto usa o algoritmo **Floyd-Warshall**, que calcula os menores caminhos entre todos os pares de vértices. Ele utiliza uma ideia de Programação Dinâmica, pois vai melhorando as respostas aos poucos ao testar vértices intermediários.

A fórmula central é:

```text
dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
```

Essa fórmula significa que o sistema verifica se a rota de `i` até `j` fica melhor quando passa por um ponto intermediário `k`. Se ficar melhor, a distância é atualizada.

## Explicação do score composto

O **score composto** é um critério que combina tempo, custo, risco e energia em um único valor. Ele é útil quando a melhor decisão não deve depender de apenas um fator.

```text
score = tempo × 0,35 + custo × 1,10 + risco × 4,50 + energia × 0,025
```

| Fator | Por que entra no score |
|---|---|
| Tempo | Missões mais rápidas podem ser importantes em emergências. |
| Custo | A rota precisa ser financeiramente viável. |
| Risco | A segurança é prioridade em operações espaciais críticas. |
| Energia | A sustentabilidade e o consumo operacional também importam. |

O risco recebe peso maior porque, em um contexto espacial, uma falha pode comprometer a missão, os equipamentos, os dados e a segurança dos envolvidos. Por isso, a rota mais segura pode ser preferida mesmo quando não é a mais barata.

## Diferenciais implementados

| Diferencial | Onde aparece |
|---|---|
| Comparação Floyd-Warshall x Dijkstra | Opção 10 do menu. |
| Exportação JSON/CSV | Opção 11 do menu e pasta `exports`. |
| Estatísticas da rede | Opção 12 do menu. |
| Mapa visual simples | Opção 13 do menu e arquivo `exports/mapa_astralink.mmd`. |
| Exemplo real documentado | README e este documento de entrega. |
| Código modularizado | Pasta `src` com arquivos separados por responsabilidade. |

## Pontos fortes para destacar na apresentação

O primeiro ponto forte é que o projeto não é apenas um cadastro de informações. Ele implementa um algoritmo clássico de grafos com Programação Dinâmica para resolver um problema realista de rotas.

O segundo ponto forte é que a rede possui 35 vértices e 54 conexões, superando o requisito mínimo de informações. Cada conexão tem vários pesos, o que torna o problema mais interessante do que uma simples lista de caminhos.

O terceiro ponto forte é a modularização. A separação entre dados, grafo, algoritmos e menu mostra organização e facilita manutenção futura.

O quarto ponto forte são os diferenciais opcionais. A comparação com Dijkstra mostra conhecimento algorítmico, e a exportação JSON/CSV permite usar os resultados fora do terminal.

## Checklist final

| Requisito | Situação |
|---|---:|
| Nome atualizado para AstraLink | Concluído |
| Código modularizado | Concluído |
| Exemplo real no README | Concluído |
| Explicação detalhada do score composto | Concluído |
| Comparação Floyd-Warshall x Dijkstra | Concluído |
| Exportação JSON/CSV | Concluído |
| Estatísticas da rede | Concluído |
| Mapa simples da rede | Concluído |
| Testes de execução | Concluído |

## Conclusão

O AstraLink está pronto para entrega acadêmica. O projeto demonstra conhecimento de grafos, Programação Dinâmica, organização modular de código, manipulação de estruturas de dados, interação com usuário e documentação profissional.
