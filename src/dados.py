"""
Módulo de dados do AstraLink.

Este arquivo concentra os dados da rede espacial: vértices e conexões.
Separar os dados do restante da lógica torna o projeto mais organizado,
mais fácil de manter e mais adequado para um repositório acadêmico.
"""


def obter_vertices():
    """Retorna os ativos espaciais e terrestres usados como vértices do grafo."""
    return {
        "GRU": {
            "nome": "Porto Espacial Atlântico-BR",
            "categoria": "Terra / lançamento",
            "pais_regiao": "Brasil",
            "funcao": "Ponto de lançamento e redistribuição de cargas críticas para a América do Sul."
        },
        "CAPE": {
            "nome": "Complexo Cabo Canaveral",
            "categoria": "Terra / lançamento",
            "pais_regiao": "Estados Unidos",
            "funcao": "Base de lançamento de alto volume para missões orbitais e cis-lunares."
        },
        "KOUROU": {
            "nome": "Plataforma Equatorial Kourou",
            "categoria": "Terra / lançamento",
            "pais_regiao": "Guiana Francesa",
            "funcao": "Base equatorial eficiente para envio de satélites e cápsulas logísticas."
        },
        "SVAL": {
            "nome": "Estação Polar Svalbard",
            "categoria": "Terra / comunicação",
            "pais_regiao": "Noruega",
            "funcao": "Recepção polar de dados climáticos e telemetria de satélites."
        },
        "NAI": {
            "nome": "Hub Climático Nairobi",
            "categoria": "Terra / impacto social",
            "pais_regiao": "Quênia",
            "funcao": "Centro de resposta a secas, enchentes e segurança alimentar no continente africano."
        },
        "MAN": {
            "nome": "BioHub Amazônia",
            "categoria": "Terra / sustentabilidade",
            "pais_regiao": "Brasil",
            "funcao": "Centro de monitoramento ambiental, biodiversidade e agricultura regenerativa."
        },
        "MUM": {
            "nome": "Rede Médica Mumbai",
            "categoria": "Terra / saúde",
            "pais_regiao": "Índia",
            "funcao": "Hub de telemedicina para emergências populacionais de grande escala."
        },
        "TOK": {
            "nome": "Centro Robótico Tóquio",
            "categoria": "Terra / robótica",
            "pais_regiao": "Japão",
            "funcao": "Laboratório de robótica avançada para manutenção remota e missões autônomas."
        },
        "SYD": {
            "nome": "Base Drone Oceania",
            "categoria": "Terra / resposta rápida",
            "pais_regiao": "Austrália",
            "funcao": "Centro de drones para entrega emergencial, busca e salvamento."
        },
        "ATA": {
            "nome": "Fazenda Solar Atacama",
            "categoria": "Terra / energia",
            "pais_regiao": "Chile",
            "funcao": "Geração energética limpa para apoiar lançamentos e enlaces orbitais."
        },
        "NSEA": {
            "nome": "Parque Eólico Mar do Norte",
            "categoria": "Terra / energia",
            "pais_regiao": "Europa",
            "funcao": "Fonte renovável para abastecer estações de rastreamento e computação climática."
        },
        "NEXUS4": {
            "nome": "Satélite Nexus-4",
            "categoria": "Órbita baixa / comunicação",
            "pais_regiao": "Global",
            "funcao": "Satélite de baixa órbita para conectividade, dados críticos e roteamento inteligente."
        },
        "NEXUS5": {
            "nome": "Satélite Nexus-5",
            "categoria": "Órbita baixa / comunicação",
            "pais_regiao": "Global",
            "funcao": "Camada redundante de conectividade orbital para reduzir falhas regionais."
        },
        "CLIMA": {
            "nome": "Constelação AuroraClima",
            "categoria": "Órbita baixa / clima",
            "pais_regiao": "Global",
            "funcao": "Satélites de observação terrestre para prever desastres ambientais."
        },
        "ISS": {
            "nome": "Laboratório Orbital Aster",
            "categoria": "Órbita baixa / pesquisa",
            "pais_regiao": "Internacional",
            "funcao": "Ambiente de microgravidade para pesquisa médica, materiais e biotecnologia."
        },
        "FOUNDRY": {
            "nome": "Microfábrica Orbital Vulcan",
            "categoria": "Órbita baixa / manufatura",
            "pais_regiao": "Global",
            "funcao": "Produção de peças leves e componentes críticos em microgravidade."
        },
        "FUEL": {
            "nome": "Depósito Propelente LEO",
            "categoria": "Órbita baixa / logística",
            "pais_regiao": "Global",
            "funcao": "Armazena propelente para rebocadores, satélites e missões cis-lunares."
        },
        "ATLAS": {
            "nome": "Relay Orbital Atlas",
            "categoria": "Órbita GEO / comunicação",
            "pais_regiao": "Atlântico",
            "funcao": "Relé geoestacionário de alta estabilidade para América, África e Europa."
        },
        "PACIFIC": {
            "nome": "Relay Orbital Pacífico",
            "categoria": "Órbita GEO / comunicação",
            "pais_regiao": "Pacífico",
            "funcao": "Relé geoestacionário de alta estabilidade para Ásia, Oceania e costa oeste americana."
        },
        "SHIELD": {
            "nome": "Escudo Anti-Detritos LEO",
            "categoria": "Órbita baixa / segurança",
            "pais_regiao": "Global",
            "funcao": "Rede de sensores e interceptadores para reduzir risco de colisões espaciais."
        },
        "MEDSAT": {
            "nome": "Satélite MedLink",
            "categoria": "Órbita média / saúde",
            "pais_regiao": "Global",
            "funcao": "Nó de telemedicina e priorização de dados clínicos em regiões remotas."
        },
        "AGRO": {
            "nome": "Satélite AgroIA",
            "categoria": "Órbita baixa / agricultura",
            "pais_regiao": "Global",
            "funcao": "IA embarcada para detectar pragas, seca, produtividade e uso de água."
        },
        "SAR": {
            "nome": "Satélite SAR Emergência",
            "categoria": "Órbita baixa / emergência",
            "pais_regiao": "Global",
            "funcao": "Radar de abertura sintética para enxergar através de nuvens e fumaça."
        },
        "ENERGY": {
            "nome": "Usina Solar Orbital Helios",
            "categoria": "Órbita alta / energia",
            "pais_regiao": "Global",
            "funcao": "Coleta energia solar espacial e envia feixes controlados para nós autorizados."
        },
        "GATE": {
            "nome": "Gateway Lunar Artemis",
            "categoria": "Cis-lunar / logística",
            "pais_regiao": "Lua",
            "funcao": "Porto orbital entre Terra, Lua e missões de longa distância."
        },
        "ICE": {
            "nome": "Mina de Gelo Shackleton",
            "categoria": "Lua / recursos",
            "pais_regiao": "Polo Sul Lunar",
            "funcao": "Extração de gelo para água, oxigênio e combustível."
        },
        "LFACT": {
            "nome": "Fábrica Lunar RegolithWorks",
            "categoria": "Lua / manufatura",
            "pais_regiao": "Lua",
            "funcao": "Transforma regolito em peças, blindagens e módulos de infraestrutura."
        },
        "LIA": {
            "nome": "Centro IA LunaMind",
            "categoria": "Lua / inteligência artificial",
            "pais_regiao": "Lua",
            "funcao": "IA para prever falhas, otimizar rotas e coordenar robôs autônomos."
        },
        "ROVER": {
            "nome": "Frota Rover Minerva",
            "categoria": "Lua / robótica",
            "pais_regiao": "Lua",
            "funcao": "Robôs móveis para inspeção, mineração e transporte local."
        },
        "TOUR": {
            "nome": "Terminal Turismo Orbital Selene",
            "categoria": "Cis-lunar / turismo",
            "pais_regiao": "Lua",
            "funcao": "Nó comercial de turismo espacial e serviços premium."
        },
        "METAL": {
            "nome": "Refinaria Astrometal",
            "categoria": "Lua / indústria",
            "pais_regiao": "Lua",
            "funcao": "Processamento de metais extraídos para manutenção espacial."
        },
        "AST": {
            "nome": "Entreposto Asteroide Ícaro",
            "categoria": "Asteroide / mineração",
            "pais_regiao": "Cinturão próximo",
            "funcao": "Coleta experimental de metais raros para cadeias produtivas espaciais."
        },
        "MARS": {
            "nome": "Relé Marte Phobos",
            "categoria": "Marte / comunicação",
            "pais_regiao": "Órbita de Marte",
            "funcao": "Nó de comunicação e testes para futuras missões marcianas."
        },
        "DEEP": {
            "nome": "Backbone Deep Space",
            "categoria": "Espaço profundo / comunicação",
            "pais_regiao": "Sistema Solar interno",
            "funcao": "Rede de comunicação de longa distância para missões além da Lua."
        },
        "TUG": {
            "nome": "Rebocador Cislunar Atlas",
            "categoria": "Cis-lunar / transporte",
            "pais_regiao": "Entre Terra e Lua",
            "funcao": "Veículo reutilizável para mover cargas entre órbitas."
        }
    }


def obter_conexoes():
    """Retorna as conexões ponderadas da rede espacial."""
    return [
        ("GRU", "MAN", 2700, 4.0, 0.8, 2, 12, "Transporte aéreo e dados ambientais para proteção da Amazônia."),
        ("GRU", "ATA", 2400, 3.5, 0.9, 2, 10, "Corredor energético sul-americano para suporte de lançamentos limpos."),
        ("GRU", "KOUROU", 3200, 5.0, 1.4, 3, 18, "Rota logística entre bases sul-americanas e base equatorial."),
        ("KOUROU", "CAPE", 4100, 6.0, 1.9, 3, 22, "Integração entre complexos de lançamento do Atlântico."),
        ("MUM", "NAI", 4500, 7.0, 1.7, 3, 20, "Corredor humanitário de dados médicos e resposta climática."),
        ("TOK", "SYD", 7800, 9.5, 2.6, 4, 32, "Rede de robótica e drones para resposta rápida no Pacífico."),
        ("NSEA", "SVAL", 2100, 3.0, 0.7, 2, 8, "Energia renovável e telemetria polar."),
        ("NSEA", "ATLAS", 36000, 1.2, 6.0, 4, 85, "Enlace energético e dados com relé geoestacionário atlântico."),
        ("ATA", "ENERGY", 38000, 1.5, 5.8, 4, 75, "Recepção autorizada de energia solar orbital no Atacama."),
        ("CAPE", "NEXUS4", 2000, 2.0, 8.5, 5, 120, "Lançamento para inserir carga no satélite Nexus-4."),
        ("KOUROU", "NEXUS5", 2100, 2.1, 8.1, 5, 116, "Lançamento equatorial para conectividade orbital."),
        ("SVAL", "CLIMA", 1200, 0.4, 1.2, 2, 7, "Downlink polar de dados climáticos de alta frequência."),
        ("NAI", "AGRO", 1400, 0.5, 1.4, 2, 9, "Dados agrícolas e previsão de seca para segurança alimentar."),
        ("MAN", "AGRO", 1300, 0.5, 1.3, 2, 8, "Monitoramento orbital da floresta e de lavouras regenerativas."),
        ("MAN", "NEXUS4", 1800, 0.6, 1.0, 1, 20, "Conexão prioritária entre o BioHub Amazônia e o Satélite Nexus-4."),
        ("MUM", "MEDSAT", 1600, 0.6, 1.5, 2, 10, "Telemedicina espacial para triagem e diagnóstico remoto."),
        ("SYD", "SAR", 1700, 0.6, 1.5, 2, 11, "Radar orbital para enchentes, incêndios e resgates oceânicos."),
        ("TOK", "ISS", 2100, 2.3, 9.2, 5, 125, "Envio de experimentos robóticos ao laboratório orbital."),
        ("NEXUS4", "NEXUS5", 800, 0.2, 0.6, 1, 5, "Interconexão entre satélites Nexus para redundância."),
        ("NEXUS4", "ATLAS", 34000, 1.0, 3.8, 1, 45, "Subida protegida de dados do Nexus-4 para o Relay Orbital Atlas."),
        ("NEXUS5", "PACIFIC", 34000, 1.0, 3.8, 3, 45, "Subida de dados do Nexus-5 para o Relay Orbital Pacífico."),
        ("CLIMA", "ATLAS", 33000, 0.9, 3.5, 3, 42, "Roteamento de previsões climáticas para o Atlântico."),
        ("CLIMA", "SAR", 900, 0.2, 0.7, 1, 5, "Fusão entre imagens climáticas e radar de emergência."),
        ("MEDSAT", "PACIFIC", 32000, 0.8, 3.3, 3, 38, "Relé médico para Ásia e Oceania."),
        ("AGRO", "ATLAS", 33000, 0.9, 3.4, 3, 40, "Relé agrícola e ambiental para continentes atlânticos."),
        ("SAR", "PACIFIC", 32000, 0.8, 3.2, 3, 39, "Relé de emergência para a bacia do Pacífico."),
        ("ISS", "FOUNDRY", 500, 0.3, 1.1, 2, 12, "Transferência de protótipos de microgravidade para fabricação orbital."),
        ("FOUNDRY", "FUEL", 900, 0.4, 1.4, 2, 16, "Envio de componentes para manutenção do depósito de propelente."),
        ("FUEL", "TUG", 1200, 0.5, 1.8, 3, 25, "Abastecimento do rebocador cislunar reutilizável."),
        ("TUG", "GATE", 380000, 28.0, 22.0, 6, 380, "Transporte de carga entre órbita terrestre e Gateway Lunar."),
        ("GATE", "ICE", 1200, 2.0, 2.5, 4, 30, "Descida logística para extração de gelo no polo sul lunar."),
        ("GATE", "LFACT", 900, 1.8, 2.3, 4, 28, "Envio de materiais entre porto lunar e fábrica de regolito."),
        ("ICE", "LFACT", 500, 1.0, 1.2, 3, 15, "Abastecimento de água e oxigênio para manufatura lunar."),
        ("LFACT", "METAL", 350, 0.9, 1.0, 3, 14, "Fornecimento de estruturas e peças para refino de metais."),
        ("METAL", "AST", 1800000, 120.0, 45.0, 8, 1200, "Cadeia experimental entre indústria lunar e mineração asteroidária."),
        ("AST", "MARS", 56000000, 500.0, 180.0, 9, 9000, "Rota de longo prazo para materiais raros e comunicação marciana."),
        ("MARS", "DEEP", 5000000, 20.0, 25.0, 7, 600, "Backbone de comunicação entre Marte e espaço profundo."),
        ("DEEP", "TUG", 390000, 18.0, 18.0, 6, 360, "Enlace de navegação e dados para tráfego cislunar."),
        ("ATLAS", "LFACT", 382000, 16.4, 18.0, 1, 355, "Canal logístico protegido entre o Relay Orbital Atlas e a Fábrica Lunar RegolithWorks."),
        ("ATLAS", "DEEP", 385000, 4.0, 12.0, 5, 250, "Ponte de comunicação atlântica para missões profundas."),
        ("PACIFIC", "DEEP", 385000, 4.0, 12.0, 5, 250, "Ponte de comunicação pacífica para missões profundas."),
        ("LIA", "LFACT", 200, 0.4, 0.8, 2, 8, "Controle inteligente da manufatura lunar."),
        ("LIA", "GATE", 850, 1.2, 1.7, 3, 20, "IA lunar conectada ao porto orbital."),
        ("ROVER", "ICE", 120, 0.5, 0.4, 2, 5, "Rovers transportam gelo e fazem inspeção de crateras."),
        ("ROVER", "LIA", 180, 0.6, 0.5, 2, 6, "Frota robótica supervisionada por IA local."),
        ("TOUR", "GATE", 700, 1.1, 3.0, 4, 26, "Terminal comercial conectado ao Gateway Lunar."),
        ("TOUR", "CAPE", 382000, 34.0, 55.0, 7, 520, "Rota turística premium Terra-Lua operada comercialmente."),
        ("ENERGY", "FUEL", 30000, 1.2, 4.0, 4, 60, "Energia orbital para eletrólise, armazenamento e propelente."),
        ("ENERGY", "ATLAS", 15000, 0.7, 2.4, 3, 30, "Distribuição de energia e controle via Relay Orbital Atlas."),
        ("SHIELD", "FUEL", 1000, 0.4, 1.2, 2, 14, "Proteção do depósito de propelente contra detritos."),
        ("SHIELD", "NEXUS4", 600, 0.2, 0.6, 1, 5, "Sensores de detritos integrados ao Nexus-4."),
        ("SHIELD", "NEXUS5", 650, 0.2, 0.6, 1, 5, "Sensores de detritos integrados ao Nexus-5."),
        ("CAPE", "FUEL", 2200, 2.6, 10.0, 5, 135, "Missões diretas de reabastecimento a partir da Terra."),
        ("KOUROU", "ENERGY", 36000, 1.4, 5.5, 4, 70, "Controle equatorial de feixe energético orbital.")
    ]
