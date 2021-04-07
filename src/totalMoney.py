import pygame


class TotalMoney:
    # Dinero total
    totalMoney = 0

    # Posicion de dinero total
    posXTotalMoney = 20
    posYTotalMoney = 30

    colorCelda = (50, 50, 50)
    colorTexto = (255, 255, 255)
    colorFondo = (0, 0, 0)
    colorBoton = (1, 111, 106)

    def mostrarTotalMoney(self, ventana):
        font = pygame.font.Font('freesansbold.ttf', 22)

        textoPuntos = font.render('Total Money: ', True, self.colorTexto, self.colorFondo)

        textRect = textoPuntos.get_rect()
        textRect.center = (self.posXTotalMoney, self.posYTotalMoney)
        ventana.blit(textoPuntos, textRect)

    def sumarTotalMoney(self, cantidad):
        self.totalMoney += cantidad
