compra = input()
prazo = int(input())

if compra == 'domingo':
    compra = 1
elif compra == 'segunda':
    compra = 2
elif compra == 'terca':
    compra = 3
elif compra == 'quarta':
    compra = 4
elif compra == 'quinta':
    compra = 5
elif compra == 'sexta':
    compra = 6
elif compra == 'sabado':
    compra = 7
    
entrega = compra + prazo
if entrega > 7:
    entrega -= 7

if prazo == 0:
    print(f'chega hoje!')
else:
    if entrega == 1:
        entrega = 'domingo'
        print(f'sera entregue {entrega}')
    elif entrega == 2:
        entrega = 'segunda'
        print(f'sera entregue {entrega}')
    elif entrega == 3:
        entrega = 'terca'
        print(f'sera entregue {entrega}')
    elif entrega == 4:
        entrega = 'quarta'
        print(f'sera entregue {entrega}')
    elif entrega == 5:
        entrega = 'quinta'
        print(f'sera entregue {entrega}')
    elif entrega == 6:
        entrega = 'sexta'
        print(f'sera entregue {entrega}')
    elif entrega == 7:
        entrega = 'sabado'
        print(f'sera entregue {entrega}')