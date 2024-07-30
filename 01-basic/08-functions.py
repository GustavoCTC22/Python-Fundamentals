#Sintaxis
# def function_name(params):
# ____codigo

#Ejemplo 1
def say_hello_customized(name):
    print(f"Bienvenid@ {name}")

say_hello_customized("Vanessa")
#Ejemplo 2

#Valores por defecto
def multiply(a, b = 15):
    return a * b

multiply(10, 4)

# Ejemplo 3
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def get_state(bmi):
    if bmi < 18.5:
        return "Bajo peso"
    elif 18.5 <= bmi < 24.9:
        return "Peso normal"
    elif 25 <= bmi < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidad"
    
def body_mass_index():
    weight = float(input("¿Cuánto pesas? "))
    height = float(input("¿Cuánto mides? "))

    bmi = calculate_bmi(weight, height)
    result = get_state(bmi)
    print(result)

def main():
    body_mass_index()

main()

