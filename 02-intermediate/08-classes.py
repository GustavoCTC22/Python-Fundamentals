# sintaxis
class Animal:
    def __init__(self, nombre, peso):
        self.nombre = nombre
        self.peso = peso
        print(self)

    def __str__(self):
        return f"{self.nombre} - {self.peso}"

    def comer(self):
        print(f"{self.nombre} está comiendo ")


gato = Animal("michi", "10kg")  # Creamos instancia u objeto de la clase
print(gato)
# print(str(gato))
# gato.comer()
