import time
from agente import AgenteTemperaturaAprendizado

# t_min bem pequeno para os testes não demorarem (Regra 1)
agente = AgenteTemperaturaAprendizado(Td=25, epsilon=1.5, t_min=0.2, k=4.0)

# ----------------------------------------------------------------------
# Cada leitura: (Ta, U, presenca, pausa_em_segundos, descricao)
# ----------------------------------------------------------------------

cenarios = {
    "Cenario 1 - Oscilacao dentro da margem (Regra 5 / 6)": [
        (24.9, 50, True, 0.3, "dentro de epsilon"),
        (25.4, 50, True, 0.3, "dentro de epsilon"),
        (24.6, 50, True, 0.3, "dentro de epsilon"),
    ],
    "Cenario 2 - Calor extremo, forca ligar (Regra 5)": [
        (28, 50, True, 0.3, "acima de Td+epsilon"),
        (30, 50, True, 0.3, "continua acima"),
        (32, 50, True, 0.3, "continua acima"),
    ],
    "Cenario 3 - Resfriamento gradual, chega a desligar (Regra 5)": [
        (30, 50, True, 0.3, "quente"),
        (27, 50, True, 0.3, "esfriando"),
        (24, 50, True, 0.3, "dentro da faixa"),
        (22, 50, True, 0.3, "abaixo de Td-epsilon"),
    ],
    "Cenario 4 - Mudanca brusca de temperatura (Regra 2)": [
        (25, 50, True, 0.3, "referencia"),
        (28.5, 50, True, 0.3, "subiu mais de 2 graus -> Liga na hora"),
        (24.0, 50, True, 0.3, "caiu mais de 2 graus -> Desliga na hora"),
    ],
    "Cenario 5 - Ambiente vazio (Regra 3)": [
        (29, 50, False, 0.3, "quente mas sem presenca -> prioriza desligar"),
        (29, 50, False, 0.3, "continua sem presenca"),
    ],
    "Cenario 6 - Umidade alta com presenca (Regra 4)": [
        (23, 80, True, 0.3, "temperatura ok mas U>70 -> forca ligar"),
    ],
}

for nome, leituras in cenarios.items():
    print("\n" + "=" * 70)
    print(nome)
    print("=" * 70)

    for Ta, U, presenca, pausa, descricao in leituras:
        agente.perceber(Ta, U, presenca)
        resultado = agente.decidir()

        print(f"""
Ta={Ta:>5} | U={U:>3} | presenca={presenca!s:5} | ({descricao})
  -> Regra aplicada : {resultado['regra']}
  -> Acao            : {resultado['acao']}
  -> Ligado          : {resultado['ligado']}
  -> dTa/dt          : {resultado['dTa_dt']}
  -> Erro termico    : {resultado['erro']}
  -> Energia acum.   : {resultado['energia_acumulada']:.2f} s
  -> r_down / r_up   : {resultado['r_down']} / {resultado['r_up']}
  -> Tempo de espera : {resultado['tempo_espera']:.2f} s
  -> Funcao objetivo : {resultado['funcao_objetivo']:.2f}
""")

        time.sleep(pausa)

    medias = agente.medias_ultimas_10()
    print("MEDIAS DO CENARIO (ultimas 10 leituras globais):", medias)

print("\n" + "=" * 70)
print("HISTORICO COMPLETO REGISTRADO:", len(agente.historico), "leituras")
print("=" * 70)
