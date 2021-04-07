import pygame


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

    def __init__(self, ganancia, tiempoParaGanancia, mejoraPorAumentoDeNivel, posY):
        self.ganancia = ganancia
        self.tiempoParaGanancia = tiempoParaGanancia
        self.mejoraPorAumentoDeNivel = mejoraPorAumentoDeNivel
        self.posY = posY

    def subirNivel(self):
        self.nivel += 1
        self.ganancia *= self.mejoraPorAumentoDeNivel

    def generarGanancia(self):
        global totalMoney

        self.tiempoTranscurrido += 1
        # print("Tiempo transcurrido: " + str(self.tiempoTranscurrido))
        if self.tiempoTranscurrido >= self.tiempoParaGanancia:
            self.tiempoTranscurrido = 0
            totalMoney += self.ganancia
            self.dineroGanado += self.ganancia

    def mostrarClicker(self):
        font = pygame.font.Font('freesansbold.ttf', 22)

        textoPuntos = font.render('Se generan ' + str(self.ganancia) + ' puntos cada ' + str(self.tiempoParaGanancia)
                                  + ' segundos. Total generado: ' + str(self.dineroGanado), True,
                                  colorTexto, colorFondo)

        textRect = textoPuntos.get_rect()
        textRect.topleft = (self.posX, self.posY)
        ventana.blit(textoPuntos, textRect)


def mostrarTotalMoney():
    font = pygame.font.Font('freesansbold.ttf', 22)

    textoPuntos = font.render('Total Money: ' + str(totalMoney), True, colorTexto, colorFondo)

    textRect = textoPuntos.get_rect()
    textRect.center = (posXTotalMoney, posYTotalMoney)
    ventana.blit(textoPuntos, textRect)


pygame.init()

# --- VENTANA ---
anchoVentana = 700
altoVentana = 700

colorCelda = (50, 50, 50)
colorTexto = (255, 255, 255)
colorFondo = (0, 0, 0)
colorBoton = (1, 111, 106)

# Dinero total
totalMoney = 0

# Posicion de dinero total
posXTotalMoney = anchoVentana / 2
posYTotalMoney = 30

ventana = pygame.display.set_mode((anchoVentana, altoVentana))
ventana.fill(colorFondo)
pygame.display.set_caption("MemoTest")

run = True

clickers = [Clicker(10, 5, 1.1, 60), Clicker(20, 3, 1.3, 90), Clicker(25, 2, 1.4, 120)]

tiempoTotal = 0

while run:

    for unClicker in clickers:
        unClicker.generarGanancia()
        unClicker.mostrarClicker()

    mostrarTotalMoney()

    pygame.display.update()

    print("Tiempo total: " + str(tiempoTotal))
    tiempoTotal += 1
    pygame.time.delay(1000 * 1)
