"""
ORBITA SEGURA - Sistema de Monitoramento e Prevencao de Colisoes com Detritos Espaciais
Global Solution - FIAP - 1o Semestre
Integrantes:
    Matheus Tasso Djamdjian   - RM 57076
    Daniel Silva Boccia        - RM 569617
    Matheus Augusto da Silva   - RM 572976
    Kaik Sales de Amorim       - RM 571558
"""

# ============================================================================
# LISTA 1 - DETRITOS ESPACIAIS RASTREADOS (20 itens)
# Estrutura: [ID NORAD, Nome do Objeto, Origem, Altitude (km), Tamanho (cm)]
# ============================================================================
detritos = [
    [25730, "Fengyun-1C Frag A",   "China ASAT 2007",      865,  12],
    [33759, "Cosmos 2251 Frag",    "Colisao Iridium 2009", 790,  18],
    [34427, "Iridium 33 Frag",     "Colisao 2009",         780,   9],
    [11871, "Delta 1 R/B",         "EUA Estagio 1975",     950,  85],
    [16615, "Ariane 1 Debris",     "ESA Estagio 1986",    1450,  45],
    [22675, "Cosmos 1408 Frag",    "Russia ASAT 2021",     480,  15],
    [27006, "Pegasus HAPS",        "EUA Estagio 2001",     645,  30],
    [38746, "CZ-4B R/B Frag",      "China Estagio 2012",   780,  22],
    [43286, "Falcon 9 Upper",      "SpaceX 2018",          540,  60],
    [40115, "Briz-M Tank",         "Russia Estagio 2014",  690,  75],
    [25400, "SL-16 R/B",           "Russia Estagio 1992", 1010,  90],
    [16193, "Titan Transtage",     "EUA Estagio 1965",   35780, 120],
    [37728, "ENVISAT Frag",        "ESA Falha 2012",       790,  25],
    [27424, "Aqua Debris",         "EUA Erosao 2002",      705,   8],
    [29275, "GOES-13 Frag",        "EUA Impacto MMOD",   35790,  14],
    [42758, "Long March 7 Frag",   "China 2017",           450,  35],
    [44432, "Vega Upper Stage",    "ESA Estagio 2019",     720,  55],
    [45623, "Starlink Debris",     "SpaceX Falha 2020",    550,  10],
    [46289, "OneWeb Frag",         "UK Falha 2021",       1200,  16],
    [48274, "CZ-5B R/B",           "China Reentrada 2021", 380,  95]
]

# ============================================================================
# LISTA 2 - SATELITES OPERACIONAIS MONITORADOS (20 itens)
# Estrutura: [Nome, Operadora, Funcao, Orbita, Valor Estimado (US$ milhoes)]
# ============================================================================
satelites = [
    ["Starlink-3421",    "SpaceX",   "Comunicacao",   "LEO",   1.5],
    ["Amazonia-1",       "INPE",     "Observacao",    "LEO",  85.0],
    ["CBERS-4A",         "INPE",     "Observacao",    "LEO", 100.0],
    ["GPS IIF-12",       "USAF",     "Navegacao",     "MEO", 245.0],
    ["Galileo FOC-22",   "ESA",      "Navegacao",     "MEO", 220.0],
    ["GOES-16",          "NOAA",     "Meteorologico", "GEO", 500.0],
    ["Hubble Space Tel", "NASA",     "Cientifico",    "LEO",2500.0],
    ["ISS",              "NASA/ROS", "Tripulada",     "LEO",150000.0],
    ["Sentinel-2A",      "ESA",      "Observacao",    "LEO", 165.0],
    ["Landsat-9",        "NASA",     "Observacao",    "LEO", 750.0],
    ["SGDC-1",           "Visiona",  "Comunicacao",   "GEO", 600.0],
    ["Intelsat-37e",     "Intelsat", "Comunicacao",   "GEO", 400.0],
    ["Iridium NEXT-148", "Iridium",  "Comunicacao",   "LEO",  80.0],
    ["OneWeb-0224",      "OneWeb",   "Comunicacao",   "LEO",   1.2],
    ["Terra (EOS AM-1)", "NASA",     "Cientifico",    "LEO", 800.0],
    ["JWST",             "NASA",     "Cientifico",    "L2",10000.0],
    ["Tiangong CSS",     "CNSA",     "Tripulada",     "LEO",8000.0],
    ["Beidou-3 M24",     "CNSA",     "Navegacao",     "MEO", 200.0],
    ["GLONASS-K2",       "Roscosmos","Navegacao",     "MEO", 180.0],
    ["Amazonas Nexus",   "Hispasat", "Comunicacao",   "GEO", 320.0]
]

# ============================================================================
# LISTA 3 - EVENTOS DE APROXIMACAO (CONJUNCTIONS) (20 itens)
# Estrutura: [Data/Hora, idx_satelite, idx_detrito, Distancia (m), Probabilidade (%)]
# ============================================================================
aproximacoes = [
    ["2026-06-01 08:23",  0,  0,  120,  4.50],
    ["2026-06-01 14:11",  7,  2,   45, 12.30],
    ["2026-06-02 03:55",  1, 13,  890,  0.20],
    ["2026-06-02 19:40",  4,  3,  650,  0.80],
    ["2026-06-03 06:12", 12, 17,  210,  3.10],
    ["2026-06-03 22:08",  6,  6,  340,  1.50],
    ["2026-06-04 11:30",  9,  9,   85,  8.70],
    ["2026-06-05 04:47",  3, 11,  980,  0.10],
    ["2026-06-05 16:22",  2,  1,  155,  5.20],
    ["2026-06-06 09:18",  8,  5,   62, 15.40],
    ["2026-06-06 21:55", 14,  8,  410,  1.20],
    ["2026-06-07 13:33", 10, 14,  720,  0.45],
    ["2026-06-08 00:09", 13, 18,  195,  3.80],
    ["2026-06-08 18:44",  5, 15,  550,  0.95],
    ["2026-06-09 07:27", 11, 19,   30, 22.10],
    ["2026-06-09 23:01", 16,  4,  840,  0.25],
    ["2026-06-10 10:36", 17,  7,  290,  2.40],
    ["2026-06-11 02:18", 19, 10,  475,  1.10],
    ["2026-06-11 15:50", 18, 12,  105,  6.30],
    ["2026-06-12 05:42", 15, 16,  680,  0.55]
]