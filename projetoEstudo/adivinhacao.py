print("*********************************")
print("Bem vindo ao jogo da Adivinhação!")
print("*********************************")

numero_secreto = 50
tentativas = 3

for rodada in range(1, tentativas + 1):
    print("Tentativa {} de {}". format(rodada, tentativas))
    userguess_str = input("Digite um número entre 1 e 100: ")
    print("Voce digitou", userguess_str)
    userguess = int(userguess_str)

    if (userguess < 1 or userguess > 100):
        print("Voce deve digitar um número entre 1 e 100!")
        continue

    acertou = userguess == numero_secreto
    maior = userguess > numero_secreto
    menor = userguess < numero_secreto

    if (acertou):
        print("Voce acertou!")
        break
    else:
        if(maior):
            print("Voce errou! O seu chute foi maior que o numero secreto.")
        elif(menor):
            print("Voce errou! o seu chute foi menor que o numero secreto.")

print("Fim do jogo!")