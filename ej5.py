import random

def guessNumber():
    num = random.randint(1, 100)
    print("Que onda loco a ver si adivinas el numero")
    print("El numero esta entre 1 y 100.")
    return num

if __name__ == "__main__":
    num = guessNumber()
    
    while True:
        guess = input("Ingresa tu numero: ")
        
        if int(guess) == num:
            print("¡Felicidades, adivinaste el numero!")
            break
        elif int(guess) < num:
            print("Tu numero es muy bajo.")
        else:
            print("Tu numero es muy alto.")
            
    print(f"El numero era {num}.") 