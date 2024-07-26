          #   0           1         2         3         4
students = ["jezabel", "ariane", "adriana", "paola", "mery"]
print(students, len(students))

#Agregar elemento al final y al inicio
students.append("wendy")
print(students, len(students))

students.insert(0,"lucy")
print(students, len(students))

#Eliminar elementos

students.pop() #borrar el ultimo
students.pop(0) # borrar el primero
print(students, len(students))

#Mas especifico
# students.remove("")
# print(students, len(students))

#Concatenar listas
numbers1 = [1,2,3,4]
numbers2 = [5,6,7,8]
numbers1.extend(numbers2)
print(numbers1)
print(numbers2)