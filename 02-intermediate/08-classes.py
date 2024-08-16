# sintaxis
class Animal:
    def __init__(self, nombre, peso):
        self.nombre = nombre
        self.peso = peso
        # print(self)

    def __str__(self):
        return f"{self.nombre} - {self.peso}"

    def comer(self):
        print(f"{self.nombre} está comiendo ")


# gato = Animal("michi", "10kg")  # Creamos instancia u objeto de la clase
# print(gato)
# print(str(gato))
# gato.comer()


# HERENCIA ---> Es la capacidad de heredar metodos y atributos de una clase padre


# Clase padre
class Automovil:
    def __init__(self, marca, modelo, color, velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad_maxima = velocidad_maxima

    def descripcion(self):
        return f"Automóvil {self.marca} {self.modelo} de color {self.color} con una velocidad máxima de {self.velocidad_maxima} km/h."


# Clase hija que hereda de Automovil
class ElectricoAutomovil(Automovil):
    def __init__(self, marca, modelo, color, velocidad_maxima, capacidad_bateria):
        # Llamamos al constructor de la clase padre
        super().__init__(marca, modelo, color, velocidad_maxima)
        # Atributo específico de la clase ElectricoAutomovil
        self.capacidad_bateria = capacidad_bateria

    def descripcion(self):
        # Reutilizamos el método de la clase padre y agregamos información adicional
        return (
            super().descripcion()
            + f" Tiene una batería de {self.capacidad_bateria} kWh."
        )


# Ejemplo de uso
automovil_electrico = ElectricoAutomovil("Tesla", "Model S", "Rojo", 250, 100)
print(automovil_electrico.descripcion())
