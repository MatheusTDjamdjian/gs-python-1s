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

# ============================================================================
# LISTA 4 - MANOBRAS DISPONIVEIS (20 itens)
# Estrutura: [Tipo Manobra, Combustivel (kg), Tempo (h), Eficacia (%), Risco]
# ============================================================================
manobras = [
    ["Delta-V leve",            2.5,  0.5,  65, "BAIXO"],
    ["Delta-V moderado",        5.0,  1.0,  80, "BAIXO"],
    ["Delta-V intenso",        12.0,  2.0,  95, "MODERADO"],
    ["Mudanca de altitude +5km",8.5,  3.5,  88, "MODERADO"],
    ["Mudanca de altitude -5km",7.8,  3.0,  86, "MODERADO"],
    ["Reentrada controlada",   45.0, 12.0,  99, "ALTO"],
    ["Reorientacao de painel",  0.0,  0.2,  35, "BAIXO"],
    ["Hibernacao temporaria",   0.5,  0.1,  20, "BAIXO"],
    ["Boost orbital",          15.0,  4.5,  92, "MODERADO"],
    ["Frenagem aerodinamica",   3.2,  6.0,  70, "MODERADO"],
    ["Manobra evasiva rapida",  9.5,  0.3,  85, "ALTO"],
    ["Ajuste de inclinacao",   18.0,  5.5,  90, "ALTO"],
    ["Spin stabilization",      1.2,  0.4,  45, "BAIXO"],
    ["Desacoplamento de modulo",0.0,  1.5,  60, "ALTO"],
    ["Propulsao ionica leve",   0.8, 24.0,  75, "BAIXO"],
    ["Propulsao ionica forte",  2.1, 36.0,  88, "BAIXO"],
    ["Manobra Hohmann",        22.0,  8.0,  96, "MODERADO"],
    ["Reposicionamento GEO",   30.0, 18.0,  94, "MODERADO"],
    ["Captura por braco rob.",  0.3,  2.5,  55, "ALTO"],
    ["Ejecao de carga util",    0.0,  0.8,  40, "ALTO"]
]

# ============================================================================
# FUNCOES (def) - Logica do sistema
# ============================================================================

def exibir_detritos():
    """Exibe todos os detritos rastreados usando estrutura de repeticao for."""
    print("\n=== DETRITOS ESPACIAIS RASTREADOS ===")
    print(f"{'#':<3}{'NORAD':<8}{'NOME':<22}{'ORIGEM':<24}{'ALT(km)':<10}{'TAM(cm)':<8}")
    print("-" * 75)
    for i in range(len(detritos)):
        d = detritos[i]
        print(f"{i+1:<3}{d[0]:<8}{d[1]:<22}{d[2]:<24}{d[3]:<10}{d[4]:<8}")


def exibir_satelites():
    """Exibe todos os satelites monitorados."""
    print("\n=== SATELITES OPERACIONAIS MONITORADOS ===")
    print(f"{'#':<3}{'NOME':<22}{'OPERADORA':<12}{'FUNCAO':<16}{'ORB':<6}{'VALOR(US$M)':<12}")
    print("-" * 75)
    for i, s in enumerate(satelites):
        print(f"{i+1:<3}{s[0]:<22}{s[1]:<12}{s[2]:<16}{s[3]:<6}{s[4]:<12}")


def exibir_aproximacoes():
    """Exibe eventos de aproximacao com classificacao de risco."""
    print("\n=== EVENTOS DE APROXIMACAO REGISTRADOS ===")
    print(f"{'#':<3}{'DATA/HORA':<18}{'SATELITE':<22}{'DETRITO':<22}{'DIST(m)':<10}{'PROB(%)':<8}{'RISCO':<10}")
    print("-" * 100)
    for i, a in enumerate(aproximacoes):
        nome_sat = satelites[a[1]][0]
        nome_det = detritos[a[2]][1]
        risco = classificar_risco(a[3], a[4])
        print(f"{i+1:<3}{a[0]:<18}{nome_sat:<22}{nome_det:<22}{a[3]:<10}{a[4]:<8}{risco:<10}")
        
def exibir_manobras():
    """Exibe catalogo de manobras de mitigacao."""
    print("\n=== MANOBRAS DE MITIGACAO DISPONIVEIS ===")
    print(f"{'#':<3}{'TIPO':<28}{'COMB(kg)':<10}{'TEMPO(h)':<10}{'EFIC(%)':<10}{'RISCO':<10}")
    print("-" * 75)
    for i, m in enumerate(manobras):
        print(f"{i+1:<3}{m[0]:<28}{m[1]:<10}{m[2]:<10}{m[3]:<10}{m[4]:<10}")


def classificar_risco(distancia, probabilidade):
    """Classifica nivel de risco com base em distancia e probabilidade.
       Usa estrutura de condicao if/elif/else."""
    if probabilidade >= 10.0 or distancia < 50:
        return "CRITICO"
    elif probabilidade >= 5.0 or distancia < 150:
        return "ALTO"
    elif probabilidade >= 1.0 or distancia < 500:
        return "MODERADO"
    else:
        return "BAIXO"


def recomendar_acao(nivel_risco):
    """Recomenda acao com base no nivel de risco. Usa match/case."""
    match nivel_risco:
        case "CRITICO":
            return "EMERGENCIA - Executar manobra evasiva imediata"
        case "ALTO":
            return "MANOBRAR - Planejar manobra nas proximas horas"
        case "MODERADO":
            return "ALERTAR - Notificar operadora e monitorar"
        case "BAIXO":
            return "MONITORAR - Continuar observacao de rotina"
        case _:
            return "INDEFINIDO - Reavaliar dados"


def calcular_risco_colisao():
    """Percorre todas as aproximacoes e gera relatorio de risco.
       Usa for, contadores e classificacao."""
    print("\n=== RELATORIO DE RISCO DE COLISAO ===")
    contadores = {"CRITICO": 0, "ALTO": 0, "MODERADO": 0, "BAIXO": 0}
    criticos = []

    for i, evento in enumerate(aproximacoes):
        risco = classificar_risco(evento[3], evento[4])
        contadores[risco] += 1
        if risco == "CRITICO":
            criticos.append(i)

    print(f"Total de eventos analisados: {len(aproximacoes)}")
    print(f"  CRITICO : {contadores['CRITICO']}")
    print(f"  ALTO    : {contadores['ALTO']}")
    print(f"  MODERADO: {contadores['MODERADO']}")
    print(f"  BAIXO   : {contadores['BAIXO']}")

    if criticos:
        print("\n!!! EVENTOS CRITICOS DETECTADOS !!!")
        for idx in criticos:
            ev = aproximacoes[idx]
            print(f"  > {ev[0]} | {satelites[ev[1]][0]} x {detritos[ev[2]][1]}")
            print(f"    Distancia: {ev[3]}m | Probabilidade: {ev[4]}%")
            print(f"    Acao: {recomendar_acao('CRITICO')}")