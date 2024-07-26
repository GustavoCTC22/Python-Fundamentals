#Sintaxis
obj1 = {
  "name": "claudia",
  "apellido": "avilez",
  "edad": 23,
}
#Ejemplos

#Case 1: Copy of dict
#INCORRECT COPY
obj3 = {"edad": 15}
obj4 = obj3

print(obj3)
print(obj4)

obj3["pais"] = "brasil"
print("=" * 20)

print(obj3)
print(obj4)

# CORRECT
original_dict = {"a": 1, "b": [2, 3], "c": {"d": 4}}
shallow_copy = original_dict.copy() 
print(shallow_copy)

shallow_copy["name"] = "hola"

print(shallow_copy)
print(original_dict)

obj1 = {"a": 15}
obj2 = dict(obj1)

print(obj1)
print(obj2)

print("=" * 20)
obj1["b"] = 20

print(obj1)
print(obj2)
print("=" * 20)
