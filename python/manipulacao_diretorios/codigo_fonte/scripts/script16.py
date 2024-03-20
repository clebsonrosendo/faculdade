frase1 = "Eu amo comer amoras no café da manhã"
frase2 = "Amora  abacaxi    abacate     banana"
frase3 = "Carro#moto#avião"


class quebraDeFrases:

    def quebra(self, separator = None):
        return print(self.split(separator))


quebraDeFrases.quebra(frase1)
quebraDeFrases.quebra(frase2)
quebraDeFrases.quebra(frase3, "#")
