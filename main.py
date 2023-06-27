def eh_incognita(valor):
    try:
        float(valor)
        return False
    except ValueError:
        return True
operacoes_opostas = {
    "+": "-",
    "-": "+",
    "*": "/",
    "/": "*",
}
# V = D / T
#Operações validas [+,-,*,/]
def operar(formula):
    #Encontrar o "=" e dividir em duas partes
    partes = formula.split('=')
    # ['V', 'D', 'T']
    #Encontre o operador no lado direito
    expresaao = partes[1]
    operacoes_validas = ['+', '-', '*', '/']
    for op in operacoes_validas:
        valores = expresaao.split(op)
        if len(valores) > 1:
            #encontramos o operador
            operador = op
            break
    valores = [v.strip() for v in valores]
    valore = partes[0].strip()
    #Decidir que operação sera feito
    if eh_incognita(valore):
        A = float(valores[0])
        B = float(valores[1])
    elif eh_incognita(valores[0]):
        A = float(valore)
        B = float(valores[1])
        op = operacoes_opostas[op]
    elif eh_incognita(valores[1]):
        if op == '/' or op == '-':
            A = float(valores[0])
            B = float(valore)
        else:
            op = operacoes_opostas[op]
            A = float(valore)
            B = float(valores[0])
    #Retornar o valor da operação
    if op == '+':
        return A + B
    elif op == '-':
        return A - B
    elif op == '*':
        return A * B
    else:
        return A / B

if  __name__ == '__main__':
    print (operar("8 = D / 2"))