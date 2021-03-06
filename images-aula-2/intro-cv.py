import cv2
import matplotlib.pyplot as plt

img = cv2.imread('pizza.jpg')
plt.imshow(img[:,:,::-1])
plt.xticks([]), plt.yticks([])
plt.show()

# Mostra o valor [B, G, R]
img[0, 0, 0]

# Converte para preto e branco
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(imgGray, cmap='gray')
plt.show()

# Cria nova janela com histograma
plt.figure()
plt.hist(imgGray.ravel(), bins=256)

# Controlar brilho da imagem
imgGray2 = cv2.add(imgGray, 50)
plt.figure()
plt.imshow(imgGray2, cmap='gray')

# Cria nova janela com histograma
plt.figure()
plt.hist(imgGray2.ravel(), bins=256)

# Ajustando contraste
mult = 2
adit = -200
imgGray3 = cv2.convertScaleAbs(imgGray, alpha=mult, beta=adit)

plt.figure()
plt.imshow(imgGray3, cmap='gray')

plt.figure()
plt.hist(imgGray3.ravel(), bins=256)

# Ajustando contraste
mult = 0.5
adit = 0
imgGray3 = cv2.convertScaleAbs(imgGray, alpha=mult, beta=adit)


plt.figure()
plt.imshow(imgGray3, cmap='gray')



plt.figure()
plt.hist(imgGray3.ravel(), bins=256)