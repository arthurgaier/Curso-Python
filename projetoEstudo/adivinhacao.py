print("*********************************")
print("Bem vindo ao jogo da Adivinhação!")
print("*********************************")

numero_secreto = 50

userguess_str = input("Digite o seu número: ")
userguess = int(userguess_str)

print("Voce digitou", userguess_str)

acertou = userguess == numero_secreto
maior   = userguess > numero_secreto
menor   = userguess < numero_secreto

if (acertou):
    print("Voce acertou!")
else:
    if(maior):
        print("Voce errou! O seu chute foi maior que o numero secreto.")
    elif(menor):
        print("Voce errou! o seu chute foi menor que o numero secreto.")

print("*********************************")
print("Fim do jogo!")
print("*********************************")
