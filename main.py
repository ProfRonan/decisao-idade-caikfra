valor = input('Digite um valor: ')
inteiro = int(valor)
if inteiro < 0:
    print("Impossível!")
elif inteiro < 18:
    print('Não precisa se alistar.')
elif 18 < inteiro < 65:
    print('Não esqueça de votar na próxima eleição.')
elif 65 < inteiro:
    print('Vá descansar.')
else:
    print('Eita!')