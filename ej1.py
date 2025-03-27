def calculadora_imc(peso, altura):
    imc = peso / (altura * altura)
    return imc

if __name__ == "__main__":

    peso = float(input("Introduce tu peso en kg: "))
    altura = float(input("Introduce tu altura en metros: "))
    imc = calculadora_imc(peso, altura)
    print(f"Tu IMC es {imc}")

    calculadora_imc(peso, altura)
    
if imc < 18.5:
    print("Bajo peso")
elif imc < 25:
    print("Peso normal")
elif imc < 30:
    print("Sobrepeso")
elif imc < 35:
    print("Obesidad grado I")