# ORBITA SEGURA

Sistema de Monitoramento e Prevencao de Colisoes com Detritos Espaciais

**FIAP - Global Solution - 1o Semestre (Python)**

---

## Integrantes do grupo

- Matheus Tasso Djamdjian - RM 57076
- Daniel Silva Boccia - RM 569617
- Matheus Augusto da Silva - RM 572976
- Kaik Sales de Amorim - RM 571558

---

## 1. Definicao do problema

O ambiente orbital da Terra esta cada vez mais saturado. Estima-se que
existam mais de 36.000 objetos com mais de 10 cm em orbita, alem de
milhoes de fragmentos menores resultantes de explosoes de estagios de
foguetes, testes anti-satelite (ASAT). Esses detritos viajam a cerca de
28.000 km/h e representam uma ameaca direta a satelites operacionais,
a Estacao Espacial Internacional (ISS) e a futuras missoes tripuladas.

O risco nao e apenas tecnico, mas tambem economico (satelites custam
centenas de milhes de dolares) e estrategico (perda de servicos de
comunicacao, GPS, meteorologia e observacao da Terra). A sindrome de
Kessler descreve um cenario em que colisoes geram cada vez mais detritos,
inviabilizando o uso da orbita baixa.

O **ORBITA SEGURA** é um sistema simplificado em Python que:

1. Cataloga detritos espaciais conhecidos e satelites em operacao.
2. Registra eventos de aproximacao (conjunctions) entre eles.
3. Classifica o nivel de risco de cada evento (BAIXO, MODERADO, ALTO, CRITICO).
4. Recomenda manobras de mitigacao viaveis conforme o combustivel disponivel.
5. Calcula o valor financeiro em risco nos eventos de alta criticidade.

---

## 2. Estrutura de dados (4 listas com 20 itens cada)

| Lista | Conteudo | Campos |
|-------|----------|--------|
| `detritos` | 20 detritos espaciais rastreados | NORAD, nome, origem, altitude (km), tamanho (cm) |
| `satelites` | 20 satelites operacionais | nome, operadora, funcao, orbita, valor (US$ milhoes) |
| `aproximacoes` | 20 eventos de aproximacao | data/hora, satelite, detrito, distancia (m), probabilidade (%) |
| `manobras` | 20 manobras de mitigacao | tipo, combustivel (kg), tempo (h), eficacia (%), risco |

---

## 3. Como executar

Requisitos: **Python 3.10 ou superior** (necessario para `match / case`).

```bash
python orbita_segura.py
```

## 4. Estrutura do repositorio

```
gs-python-1s/
|-- orbita_segura.py   # codigo principal
|-- README.md          # esta documentacao
```