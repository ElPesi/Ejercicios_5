def gradeConvertor(celsius, fahrenheit):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit
    
if __name__ == "__main__":
    celsius = float(input("Ingresar temperatura en celsius: "))
    fahrenheit = gradeConvertor(celsius,0)
    print(f"La temperatura en fahrenheit es: {fahrenheit}")

