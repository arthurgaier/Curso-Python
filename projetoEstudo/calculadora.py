print("***********************")
print("Bem vindo a calculadora")
print("***********************")

print(" [1] - SOMA\n [2] - MULTIPLICAÇÃO\n [3] - DIVISÃO\n [4] - SUBTRAÇÃO\n")
operacao_str = input("Digite o numero correspondente a operação:")
operacao = int(operacao_str)

numero_str = input("Digite o primeiro valor:")
numero = int(numero_str)
numero2_str = input("Digite o segundo valor:")
numero2 = int(numero2_str)


if (operacao == 1):
    resultado = numero + numero2
    print("{} + {} = {}". format(numero, numero2, resultado))
elif (operacao == 2):
    resultado = numero * numero2
    print("{} X {} = {}". format(numero, numero2, resultado))
elif (operacao == 3):
    resultado = numero / numero2
    print("{} \ {} = {}". format(numero, numero2, resultado))
elif (operacao == 4):
    resultado = numero - numero2
    print("{} - {} = {}". format(numero, numero2, resultado))

print("Muito obrigado!")