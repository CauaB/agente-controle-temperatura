# agente.py

class AgenteTemperatura:
    def __init__(self):
        # Variáveis do modelo
        self.td_base = 22.0
        self.td = self.td_base
        self.ta = 24.0  # Temperatura ambiente inicial simulada
        self.ti = self.ta
        self.c_ligado = 0
        self.sigma = 0.5
        self.cam = 0.0  # 0.00 a 1.00
        self.ajuste_maximo = 3.0

        # Parâmetros de cálculo
        self.alpha = 1.0
        self.beta = 0.5
        self.k = 1.0  # Constante de fallback

        self.memoria = []
        self.tempo_espera = 0
        self.media_ref = None
        self.media_elev = None

    def perceber_e_agir(self, nova_ta, nova_cam):
        # Regra 1 e Regra 2: Verificação do ambiente e tempo de espera restante
        if self.tempo_espera > 0:
            self.tempo_espera -= 1
            fator_sigma = 5 if self.cam == 0.0 else 3
            l_limite = self.td + (fator_sigma * self.sigma)
            custo = (self.alpha * abs(self.ta - self.td)) + (self.beta * self.c_ligado)
            return {
                "Ta": round(self.ta, 2),
                "Td": round(self.td, 2),
                "Limiar": round(l_limite, 2),
                "Fator_Sigma": fator_sigma,
                "Sigma": self.sigma,
                "Alpha": self.alpha,
                "Beta": self.beta,
                "Variacao": round(abs(self.ta - self.td), 2),
                "Estado_Sistema": "LIGADO" if self.c_ligado == 1 else "DESLIGADO",
                "Acao": "Aguardar (Espera ativa)",
                "Custo": round(custo, 2)
            }

        self.ta = nova_ta
        self.cam = nova_cam

        # Regra 3: Ajustar temperatura desejada por ocupação
        self.td = self.td_base - (self.ajuste_maximo * self.cam)

        # Regra 7 e Regra 8: Calcular limite superior de acionamento
        fator_sigma = 5 if self.cam == 0.0 else 3
        l_limite = self.td + (fator_sigma * self.sigma)

        # Regra 6: Calcular o custo da situação atual
        custo = (self.alpha * abs(self.ta - self.td)) + (self.beta * self.c_ligado)

        # Regras 9, 11 e 13: Decisão do Agente (Ligar, Desligar ou Manter)
        acao = "Manter"
        if self.ta > l_limite:
            if self.c_ligado == 0:
                acao = "Ligar"
                self.c_ligado = 1
                self.ti = self.ta
        elif self.ta <= l_limite and self.c_ligado == 1:
            acao = "Desligar"
            self.c_ligado = 0
            self.ti = self.ta

        # Regras 10 e 12: Estimativa do Tempo de Espera
        if self.c_ligado == 1 and self.ta > self.td:
            if self.media_ref:
                self.tempo_espera = max(1, int((self.ta - self.td) / self.media_ref))
            else:
                self.tempo_espera = max(1, int(self.k * (self.ta - self.td)))
        elif self.c_ligado == 0 and self.ta < self.td:
            if self.media_elev:
                self.tempo_espera = max(1, int((self.td - self.ta) / self.media_elev))
            else:
                self.tempo_espera = max(1, int(self.k * (self.td - self.ta)))

        # Regra 4 e Regra 14: Registrar na memória e histórico
        registro = {
            "Ta": round(self.ta, 2),
            "Td": round(self.td, 2),
            "Limiar": round(l_limite, 2),
            "Fator_Sigma": fator_sigma,
            "Sigma": self.sigma,
            "Alpha": self.alpha,
            "Beta": self.beta,
            "Variacao": round(abs(self.ta - self.td), 2),
            "Estado_Sistema": "LIGADO" if self.c_ligado == 1 else "DESLIGADO",
            "Acao": acao,
            "Custo": round(custo, 2)
        }
        self.memoria.append(registro)

        # Simulação física do ambiente (Resfriamento/Aquecimento)
        if self.c_ligado == 1:
            self.ta -= 0.5
        else:
            self.ta += 0.2

        return registro