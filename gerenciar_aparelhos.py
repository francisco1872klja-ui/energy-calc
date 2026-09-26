from entrada_aparelho import *
import os


def menu():
    hora = ["Horas", "Dias", "Min"]
    for k, i in enumerate(hora, 1):
        print(f"{k}.{i}")
    return hora


class Gerenciar_aparelho:

    def __init__(self):
        self.aparelhos = []

    def cadastrar_aparelho(self):
        parametros = ("Hora", "Dia")
        nome = input("Qual o nome do aparelho?: ")
        potencia = input("Qual a potencia do aparelho?: ")
        hora = None
        dia = None

        for i in parametros:
            os.system("cls")
            prefix = menu()
            escolha = int(input(f"Qual informação para {i}?: "))
            if i == "Hora":
                info = float(input(f"Quantas {prefix[escolha - 1]} ligado?: "))
                if escolha == 1:
                    hora = info
                elif escolha == 2:
                    hora = info * 24
                elif escolha == 3:
                    hora = info / 60

            if i == "Dia":
                info = float(input(f"Quantas {prefix[escolha - 1]} ligado?: "))

                if escolha == 1:
                    dia = info / 24
                elif escolha == 2:
                    dia = info
                elif escolha == 3:
                    dia = info / 1440

        self.aparelhos.append(Entrada_Aparelhos(nome, potencia, hora, dia))

    def ver_aparelhos(self):
        for i, k in enumerate(self.aparelhos, 1):
            print(f"{i}.{k.aparelho}({k._valor_consumido}): {k._preco}")

    def aparelho_Caro(self):
        cont = 0

        nome = self.aparelhos[0].aparelho
        mais_caro = self.aparelhos[0]._preco[3:].replace(",", ".")

        while cont != len(self.aparelhos) - 1:
            cont += 1
            if float(mais_caro) < float(
                self.aparelhos[cont]._preco[3:].replace(",", ".")
            ):
                nome = self.aparelhos[cont].aparelho
                mais_caro = self.aparelhos[cont]._preco[3:].replace(",", ".")
        return nome, mais_caro
