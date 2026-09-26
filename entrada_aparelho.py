import locale


class Entrada_Aparelhos:
    prefixos = {
        "T": 10**12,
        "G": 10**9,
        "M": 10**6,
        "K": 10**3,
        "-": 10**0,
        "m": 10**-3,
        "u": 10**-6,
        "n": 10**-9,
        "p": 10**-12,
    }

    def __init__(
        self,
        nome_aparelho: str,
        potencia: str,
        horas_ligado: int | float,
        dias_usados: int,
    ):
        self.aparelho = nome_aparelho
        self.__valor_potencia = self.__validar_entrada(potencia)
        self._preco, self._valor_consumido = self.__calcular_preco(
            self.__valor_potencia, horas_ligado, dias_usados
        )

    def __validar_entrada(self, valor: str):
        if not isinstance(valor, str):
            raise AttributeError("O valor não é uma string!")

        if "," in valor:
            valor = valor.replace(",", ".")

        elif not "w" in valor:
            valor += "w"
        try:
            valor = (
                float(valor[: len(valor) - 2])
                * Entrada_Aparelhos.prefixos[valor[len(valor) - 2]]
            )
        except KeyError:
            valor = (
                int(valor.replace("W", "").replace("w", ""))
                * Entrada_Aparelhos.prefixos["-"]
            )
        return valor

    def __calcular_preco(self, potencia, hora, dias):
        locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
        valor_Kwh = 0.653
        consumo = (potencia * hora * dias) / 1000
        custo = consumo * valor_Kwh
        return f"{locale.currency(custo,True)}", f"{consumo} /kWh"
