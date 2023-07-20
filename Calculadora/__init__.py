from funcoes import Soma
from funcoes import Subtracao
from funcoes import Divisao
from funcoes import Multiplicacao
from funcoes import Exponencial

def calcule():
    resultado = 0
    a = input("Digite o primeiro número: ")
    while a.isdigit() != True:
        print("Preciso que digite um número.")
        a = input("Digite novamente: ")    
    a = float(a)
    b = input("Digite o segundo número: ")
    while b.isdigit() != True:
        print("Preciso que digite um número.")
        b = input("Digite novamente: ")    
    b = float(b)
    operacao = input("""Qual operação gostaria de ralizar?
                     use:
                        + para soma
                        - para subtração
                        / para divisão
                        * para multiplica
                        ** para exponenciação
                    """)
    if operacao not in ['+','-','/','*','**']:
        print("Operação não identificada!")
        resultado = "Não foi possivel realizar a operação."
    elif operacao == '+':
        print(f"a soma é {soma(a,b)}")
        resultado = soma(a,b)
    elif operacao == '-':
        print(f"a subtração é {subtracao(a,b)}")
        resultado = subtracao(a,b)
    elif operacao == '/':
        print(f"a divisão é {divisao(a,b)}")
        resultado = divisao(a,b)
    elif operacao == '*':
        print(f"a multiplicação é {multiplicacao(a,b)}")
        resultado = multiplicacao(a,b)
    elif operacao == '**':
        print(f"a exponecial é {exponencial(a,b)}")
        resultado = exponencial(a,b)
    return resultado