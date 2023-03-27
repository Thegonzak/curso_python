class Juego:

    def info(self, nombre, creado):
        self.nombre = nombre
        self.creado = creado
        self.__numero_jugadores = 2

    def encender(self):
        self.jugando = True

    def apagar(self):
        self.jugando = False


j1 = Juego("Resident Evil", "Shinji Mikami")
j1.encender()
j2 = Juego("Marvel's Spider-Man 2", "Insomniac Games")
j2.apagar()
j3 = Juego("The Last of Us Parte I", "Naughty Dog")
j2.encender()


print("Juegos")
