users = [
  ["Nohemi", 77], #user
  ["Wendy", 87],
  ["Diana", 12],
  ["Claudia", 81]
]

#lambda ---> función en una línea

nombres = list(map(lambda user: user[0], users))
# nombres = map(lambda user: user[0], users)
print(nombres)


numeros = [1, 2, 3, 4, 5]
resultado = list(map(lambda x: x * 2, numeros))
print(resultado)

#Iterables en python pendiente