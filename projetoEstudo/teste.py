print("Bem vindo a Calculadora de Notas")


media_str = input("Primeira nota:")
media = int(media_str)
media2_str = input("Segunda nota:")
media2 = int(media2_str)
media3_str = input("Terceira nota:")
media3 = int(media3_str)
media4_str = input("Quarta nota:")
media4 = int(media4_str)

mediafinal = media + media2 + media3 + media4
mediafinal2 = mediafinal / 4

print("Sua média final é: {}". format(mediafinal2))
