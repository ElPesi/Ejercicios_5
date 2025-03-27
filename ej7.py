def calculadora_descuento():
    precio_original = float(input("Ingresa el precio original del artículo: "))
    porcentaje_descuento = float(input("Ingresa el porcentaje de descuento: "))
    descuento = precio_original * (porcentaje_descuento / 100)
    precio_final = precio_original - descuento
    print(f"El precio final después de un descuento del {porcentaje_descuento}% es: ${precio_final}")

if __name__ == "__main__":
    calculadora_descuento()
