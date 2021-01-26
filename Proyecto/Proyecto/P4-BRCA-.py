from PIL import Image
import sys
import random
import matplotlib.pyplot as plt

def ObtenerVecindad8(i, j, img):
    V = []
    for x in range (i-1, i+2):
        for y in range (j-1, j+2):
            try:
                V.append(img.getpixel((x,y)))
            except:
                if (img.mode != 'L'):
                    V.append((0,0,0))
                else:
                    V.append(0)
    return V

def Grises (rutaimagen):
    imagen = Image.open(rutaimagen)
    imagenResultado = Image.new('L', imagen.size)
    ancho,alto = imagen.size
    for i in range (ancho):
        for j in range (alto):
            r,g,b = imagen.getpixel((i,j))
            prom = (r + g + b) // 3
            imagenResultado.putpixel((i,j),prom)
    return imagenResultado

def Robert(rutaimagen):
    imagen = Image.open(rutaimagen)
    if (imagen.mode != 'L'):
        imagen = Grises(rutaimagen)
    imgResultado = Image.new('L',imagen.size)
    ancho,alto = imagen.size
    g = 0
    for i in range (ancho):
        for j in range (alto):
            V = ObtenerVecindad8(i, j, imagen)
            Gx = V[4] - V[2]
            Gy = V[4] - V[0]
            g = abs(Gx) + abs (Gy)
            imgResultado.putpixel((i,j),g)
    imgResultado.save("Robert.jpg")
    imgResultado.show()
    return imgResultado

def Prewitt(rutaimagen):
    imagen = Image.open(rutaimagen)
    if (imagen.mode != 'L'):
        imagen = Grises(rutaimagen)
    imgResultado = Image.new('L',imagen.size)
    ancho,alto = imagen.size
    g = 0
    for i in range (ancho):
        for j in range (alto):
            V = ObtenerVecindad8(i, j, imagen)
            Gx = (V[0] + V[3] + V[6] - V[2] - V[5] - V[8]) // 3
            Gy = (V[6] + V[7] + V[8] - V[0] - V[1] - V[2]) // 3
            g = abs(Gx) + abs (Gy)
            imgResultado.putpixel((i,j),g)
    imgResultado.save("Prewitt.jpg")
    imgResultado.show()
    return imgResultado

def Sobel(rutaimagen):
    imagen = Image.open(rutaimagen)
    if (imagen.mode != 'L'):
        imagen = Grises(rutaimagen)
    imgResultado = Image.new('L',imagen.size)
    ancho,alto = imagen.size
    g = 0
    for i in range (ancho):
        for j in range (alto):
            V = ObtenerVecindad8(i, j, imagen)
            Gx = (V[0] + 2*V[3] + V[6] - V[2] - 2*V[5] - V[8]) // 4
            Gy = (V[6] + 2*V[7] + V[8] - V[0] - 2*V[1] - V[2]) // 4
            g = abs(Gx) + abs (Gy)
            imgResultado.putpixel((i,j),g)
    imgResultado.save("Sobel.jpg")
    imgResultado.show()
    return imgResultado

def Laplaciano4(rutaimagen):
    imagen = Image.open(rutaimagen)
    if (imagen.mode != 'L'):
        imagen = Grises(rutaimagen)
    imgResultado = Image.new('L',imagen.size)
    ancho,alto = imagen.size
    g = 0
    for i in range (ancho):
        for j in range (alto):
            V = ObtenerVecindad8(i, j, imagen)
            L = 4*V[4] - V[1] - V[3] - V[5] - V[7]
            imgResultado.putpixel((i,j),L)
    imgResultado.save("Laplaciano4.jpg")
    imgResultado.show()
    return imgResultado

def Laplaciano8(rutaimagen):
    imagen = Image.open(rutaimagen)
    if (imagen.mode != 'L'):
        imagen = Grises(rutaimagen)
    imgResultado = Image.new('L',imagen.size)
    ancho,alto = imagen.size
    g = 0
    for i in range (ancho):
        for j in range (alto):
            V = ObtenerVecindad8(i, j, imagen)
            L = 8*V[4] - V[0] - V[1] - V[2] - V[3] - V[5] - V[6] - V[7] - V[8]
            imgResultado.putpixel((i,j),L)
    imgResultado.save("Laplaciano8.jpg")
    imgResultado.show()
    return imgResultado
Laplaciano8("imagenes/baño.jpg")
