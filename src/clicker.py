from publicVariables import PublicVariables


class Clicker:
    # Posicion
    posX = 30
    posY = 60

    # Dinero
    ganancia = 10
    dineroGanado = 0

    # Tiempos
    tiempoTranscurrido = 0
    tiempoParaGanancia = 5

    # Niveles
    nivel = 1
    mejoraPorAumentoDeNivel = 1.1

    def subirNivel(self):
        self.nivel += 1
        self.ganancia *= self.mejoraPorAumentoDeNivel

    def generarGanancia(self):
        global totalMoney

        self.tiempoTranscurrido += 1
        print("Tiempo transcurrido: " + str(self.tiempoTranscurrido))
        if self.tiempoTranscurrido >= self.tiempoParaGanancia:
            self.tiempoTranscurrido = 0
            totalMoney += self.ganancia
            self.dineroGanado += self.ganancia

    def mostrarClicker(self, ventana, pygame):
        font = pygame.font.Font('freesansbold.ttf', 22)

        textoPuntos = font.render('Se generan ' + str(self.ganancia) + ' puntos cada ' + str(self.tiempoParaGanancia)
                                  + ' segundos. Total generado: ' + str(self.dineroGanado), True,
                                  PublicVariables.colorTexto, PublicVariables.colorFondo)

        textRect = textoPuntos.get_rect()
        textRect.topleft = (self.posX, self.posY)
        ventana.blit(textoPuntos, textRect)
