users = ["claudia", "shirley", "paola", "leidy", "liz", "lucy", "rut"]

# FILTER
#               retorno |    iteración   |   condicion
filtered_list = [user for user in users if  len(user) >= 5]   
print(filtered_list)

# MAP
mapped_list = [user[0].upper() + "." for user in users]
print(mapped_list)


result = []
for user in users:
  if len(user) >= 5:
    result.append(user)

print(result)