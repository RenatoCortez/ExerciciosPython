'''FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA
ÁREA, QUE RECEBA AS DIMENSÕES DE UM TERRENO RETANGULAR
(LARGURA E COMPRIMENTO) E MOSTRE A ÁREA DO TERRENO.'''

def area(larg, comp):
    a = larg * comp
    print(f'A área do terreno {larg} x {comp} é de {a}m²')


print('Controle de Terrenos')
print('-=' * 20)
l = float(input('Largura(m): '))
c = float(input('Comprimento(m): '))
area(l, c)