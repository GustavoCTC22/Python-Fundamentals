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
array_list = list(range(1,11))
print(array_list)
numbers1.extend(numbers2)
print(numbers1)
print(numbers2)

new_array = [1,2] * 10
print(new_array)

print(list("jezabel"))
union = [1,5,6] + [1,4,2]
print(union)