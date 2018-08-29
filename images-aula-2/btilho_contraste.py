import cv2
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize

# Mostrar a imagem e o histograma
def mostra_fig(img):
    plt.figure()
    plt.imshow(img, cmap='gray', norm=Normalize(0,255))
    plt.figure()
    plt.hist(img.ravel(), bins=256)
    plt.xlim([0,255])

# 1. Carregar a imagem como tons de cinza
imgray = cv2.imread("pizza.jpg", cv2.IMREAD_GRAYSCALE)
mostra_fig(imgray)

# 2. Diminuir ou aumentar o brilho
brilho = -50
imgray2 = cv2.add(imgray, brilho)
mostra_fig(imgray2)

# 3. Aumentar o contraste
mult = 2
soma = -100
imgray3 = cv2.convertScaleAbs(imgray,alpha=mult,beta=soma)
mostra_fig(imgray3)

# 4. Diminuir o contraste
mult = 0.2
soma = 120
imgray4 = cv2.convertScaleAbs(imgray,alpha=mult,beta=soma)
mostra_fig(imgray4)


# 5. Equalização de histograma
imgray5 = cv2.equalizeHist(imgray4)
mostra_fig(imgray5)
