'''CRIE UM PROGRAMA ONDE O USUÁRIO POSSA DIGITAR
VÁRIOS VALORES NUMÉRICOS E CADASTRE-OS EM UMA LISTA,
CASO O NÚMERO JÁ EXISTA LÁ DENTRO, ELE NÃO SERÁ ADICIONADO.
NO FINAL, SERÃO EXIBIDOS TODOS OS VALORES ÚNICOS DIGITADOS,
EM ORDEM CRESCENTE.'''

valores = list() #LISTA VAZIA
while True: #LOOPING INFINITO ATÉ A PARADA -> BREAK
    n = int(input('Digite um valor: '))
    if n not in valores: #ENQUANTO O NÚMERO NÃO ESTIVER DENTRO DE VALORES
        valores.append(n) #ADICIONAR MAIS UM VALOR NA LISTA
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado, não vou adicionar.')
    r = str(input('Quer continuar[S/N]?'))
    if r in 'Nn':
        break
print('=-=' * 15)
valores.sort() #COLOCA EM ORDEM CRESCENTE
print(f'Você digitou os valores {valores}')