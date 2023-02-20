numeros_validos = None
operadores_permitidos = '+-/*'

n1 = 0
n2 = 0

while True:
    numero_1 = input('Digite um numero: ')
    numero_2 = input('Digite um numero: ')
    operador = input('Digite o operador [+-/*]: ')
    
    try:
        n1 = float(numero_1)
        n2 = float(numero_2)
        numeros_validos = True
        
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue
    
    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue
    
    if len(operador) > 1:
        print('Digite apenas um operador')
        continue
    
    print('Realizando sua conta. Confira o resultado abaixo: ')
    if operador == '+':
        print(f'{n1} + {n2} =', n1 + n2)
    
    if operador == '-':
        print(f'{n1} - {n2} =', n1 - n2)
    
    if operador == '*':
        print(f'{n1} * {n2} =', n1 * n2)
        
    if operador == '/':
        print(f'{n1} / {n2} =', n1 / n2)
    
    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair:
        break
