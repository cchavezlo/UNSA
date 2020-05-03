import matplotlib.pyplot as plt
import cv2
import numpy as np

 
def out_celulas_malas(img, imageFile):
	#_, threshold_binary = cv2.threshold(neg, 90, 150, cv2.THRESH_BINARY) 
	#cv2.imshow('thresholdin', threshold_binary)

	#Obtengo el tamaño de la imagen
    h, w = img.shape

    #IMREAD_GRAYSCALE = Carga la imagen a escala de Grises.
    imgGray = cv2.imread(imageFile, cv2.IMREAD_GRAYSCALE)
    for i in range(h):
        for j in range(w):
            if(img[i][j]>=193 and img[i][j]<=195 ):
                imgGray[i][j]=255
            else:
                imgGray[i][j]=0
    cv2.imshow('Sin Celulas Muertas',imgGray)




def No_saludables(img):
    h, w = img.shape
    gray = cv2.imread('thresh2.png', cv2.IMREAD_GRAYSCALE)
    for i in range(h):
        for j in range(w):
            if(img[i][j]<=170):#Le ponemos el valor de 170 guiandonos de nuestro histograma
                gray[i][j]=255
            else:
                gray[i][j]=0
    cv2.imshow('Sin celulas saludables',gray)




if __name__ == "__main__":

	imageFile = 'thresh1.png'
	image = cv2.imread(imageFile, cv2.IMREAD_GRAYSCALE)
	cv2.imshow('Imagen Fuente',image)
	out_celulas_malas(image, imageFile)  


	hist = cv2.calcHist([image], [0], None, [256], [0, 256])
	
	plt.plot(hist, color='blue' )
	plt.xlabel('Intensidad')
	plt.ylabel('Pixeles Total')
	plt.show()

	cv2.destroyAllWindows()

 
 '''
# Cargamos la imagen del disco duro
imagen = cv2.imread('thresh3.png')

#convertimos la imagen a escala de grises 
imgCopia = cv2.imread('thresh3.png', cv2.IMREAD_GRAYSCALE)

resultado = cv2.imread('thresh3.png')


cv2.waitKey()

cv2.imshow('Imagen original', imagen)
cv2.imshow('Imagen a escala de grises', imgCopia)
cv2.imwrite('grises_thresh3.png',imgCopia)

histB = cv2.calcHist([imagen], [0], None, [256], [0, 256])
histG = cv2.calcHist([imagen], [1], None, [256], [0, 256])
histR = cv2.calcHist([imagen], [2], None, [256], [0, 256])
histN = cv2.calcHist([imgCopia], [0], None, [256], [0, 256])


height, width, chanels= imagen.shape
limi=200 #limite inicial
limf=230 #limite final

#combierte los colores de la cosecha lo verde en negro
for i in range(height):
    for j in range(width):
        if(imagen[i][j][0]>limi or imagen[i][j][1]>limf or imagen[i][j][2]<limi):        
            resultado[i][j]=0

        
cv2.imshow('imagen final',resultado)
cv2.waitKey()
cv2.imwrite('salida_thresh3.png',resultado)


plt.plot(histN, color='black' )
plt.xlabel('intensidad de iluminacion')
plt.ylabel('cantidad de pixeles')
plt.show()
''' 
