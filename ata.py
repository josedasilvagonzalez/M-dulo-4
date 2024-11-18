import math

def calcular_quadrado():
    print("\n=== Quadrado ===")
    escolha=input("Deseja calcular a (A)rea ou o (P)erímetro?  ").strip().upper()
    if escolha == "A":
        base=float(input("Digite a base do quadrado: "))
        altura=float(input("Digite a altura do quadrado: "))
        area=base*altura
        print(f"A área do quadrado é: {area}")
    elif escolha == "P":
        base=float(input("Digite a base do quadrado: "))
        altura=float(input("Digite a altura do quadrado: "))
        perimetro=2*(base+altura)
        print(f"O perímetro do quadrado é: {perimetro}")
    else:
        print("Não existe essa opção.")

def calcular_circulo():
    print("\n=== Círculo ===")
    escolha=input("Deseja calcular a (A)rea ou o (P)erímetro? ").strip().upper()
    if escolha == "A":
        raio=float(input("Digite o raio do circulo: "))
        area=2*3.14*raio**2
        print(f"A area do circulo é {area}")
    elif escolha == "P":
        raio=float(input("Digite o raio do circulo: "))
        area=2*3.14 *raio**2
        print(f"O perímetro(circuferencia)do circulo é {area}")
    else:
        print("Não existe essa opção.")
def calcular_triangulo():
    print("\n=== Triângulo ===")
    escolha=input("Deseja calcular a (A)rea ou o (P)erímetro? ").strip().upper()
    if escolha=="A":
        base=float(input("Digite a base do triângulo: "))
        altura=float(input("Digite a altura do triângulo"))
        area=base*altura/2
        print(f"A area do triangulo é {area}")
    elif escolha=="P":
        lado1=float(input("Digite o comprimento do primeiro lado: "))
        lado2=float(input("Digite o comprimento do segundo lado: "))
        lado3=float(input("Digite o comprimento do terceiro lado: "))
        perimetro=lado1+lado2+lado3
        print(f"O perimetro do triangulo é {perimetro} ")
    else:
        print("Não existe essa opção.")
def calcular_trapezio():
    print("\n=== Trapézio ===")
    escolha=input("Deseja calcular a (A)rea ou o (P)erímetro? ").strip().upper()
    if escolha=="A":
        area=float(input("Digite a area do trapézio: "))        
        basemaior=float(input("Digite a base maior do trapézio: "))
        basemenor=float(input("Digite a base menor do trapézio: "))
        altura=float(input("Digite a altura do trapézio"))
        area=(basemaior+basemenor)*altura/2
        print(f"A area do trapézio é {area}")
    elif escolha=="P":
        altura=float(input("Digite a altura do trapézio: "))
        basemaior=float(input("Digite a base maior do trapézio:"))
        basemenor=float(input("Digite a base menor do trapézio:"))
        lado_obliquo = math.sqrt(altura**2 + ((basemaior - basemenor) / 2)**2)
        perimetro = basemaior + basemenor + 2 * lado_obliquo
        print(f"O perimetro do trapézio é {perimetro} ")
    else:
        print("Não existe essa opção.")

def calcular_pentagono():
    print("\n=== Pentágono ===")
    escolha=input("Deseja calcular a (A)rea ou o (P)erímetro? ").strip().upper()
    if escolha=="A":
        comprimento=input("Digite o comprimento de um lado do pentágono: ")
        altura=input("Digite a altura do pentágono")
        area=(5*comprimento*altura)/2
        print(f"A area do pentagono é {area}")
    elif escolha=="P":
        comprimento=input("Digite o comprimento de um lado do pentágono: ")
        perimetro=comprimento*5
        print(f"O perimetro do pentágono é {perimetro}")

def main():
    while True:
        print("--------------------------------------")
        print("--  \033[94mCálculo de areas e perimetros!\033[0m  --")
        print("--                                  --")
        print("--1. Quadrado                       --")
        print("--2. Círculo                        --")
        print("--3. Triângulo                      --")
        print("--4. Trapézio                       --")
        print("--5. Pentágono                      --")
        print("--0. Sair                           --")
        print("--                                  --")
        print("--------------------------------------")
        escolha = input("Escolha uma forma geométrica (1-5)ou 0: ").strip()
        if escolha=='1':
            calcular_quadrado()
        elif escolha=='2':
            calcular_circulo()
        elif escolha=='3':
            calcular_triangulo()
        elif escolha=='4':
            calcular_trapezio()
        elif escolha=='5':
            calcular_pentagono()
        elif escolha=='0':
            print("Saindo!")
            break
        else:
            print("Essa opção não existe. tenta novamente!")
if __name__ == "__main__":
    main()
        
        
                
