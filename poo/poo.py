class Vehiculo:
    # constructor
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.ruedas = 4
        self.encendido = False

    def encender(self):
        self.encendido = True
        print("Estoy encendido")

    def acelerar(self):
        print("Estoy acelerando")

    def frenar(self):
        print("Estoy frenando")

    def info(self):
        print(
            f"Mi vehiculo Marca: {self.marca}, Modelo: {self.modelo}, Ruedas: {self.ruedas}, Encendido: {self.encendido}")


class Motos(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)

    def caballito(self):
        print("Estoy haciendo caballito")

    def info(self):
        print(
            f"Mi Moto Marca: {self.marca}, Modelo: {self.modelo} Encendido: {self.encendido}")


print("Usos de clases")
v1 = Vehiculo("Ford", "f150")
v2 = Vehiculo("Kia", "Rio")
v3 = Vehiculo("Chevrolet", "Aveo")
v1.info()
v3 = Motos("Marca2", "Modelo2")
v3.caballito()
v3.info()
