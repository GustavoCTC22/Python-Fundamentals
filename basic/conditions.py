#SINTAXIS
# if condition:
# ____codigo
# elif condition:
# ____codigo
# else:
# ____codigo
# NOTA: La identación es importante!!!!

#Usando el input:
edad = int(input("¿Cuántos años tienes?"))
if edad < 5:
    print("Eres un niño pequeño")
elif edad <12:
    print("Eres una niña")
elif edad < 18:
    print("Eres adolescente")
else:
    print("Eres mayor de edad")
    


#USANDO TERNARIO: si la condicion es verdadera se ejecuta lo de la izquierda y si es falsa se ejecuta lo de la derecha
number = 15
print("Es mayor que 10") if number > 10 else print("Es menor o igual que 10")
#OPERADORES AND -- OR -- NOT (LOGICA ALGEBRAICA)
True and False #FALSO
True and True #True
False and False #False
False and True #False
True or True #True
True or False #True
False or False #False
False or True #True
not True or not False #True
not True or not False #True
False or True and not False #True

# Igualdad ---> == 
# Desigualdad ---> !=
