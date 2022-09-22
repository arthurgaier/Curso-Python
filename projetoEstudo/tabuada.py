multiplicador_str = input("Bem vindo a tabuada, digite um número: ")
multiplicador = int(multiplicador_str)
denominador = 1


while (denominador <= 10):
    resultado = multiplicador * denominador
    print("{} X {} = {}". format(multiplicador, denominador, resultado))
    denominador = denominador + 1