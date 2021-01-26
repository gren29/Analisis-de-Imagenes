from PIL import Image, ImageTk
import sys
import random
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

rutaimagen = ""

def cerrar():
    raiz.quit()
    raiz.destroy()

def abrirVentana():
    global rutaimagen
    imagen = tk.Toplevel()
    rutaimagen = filedialog.askopenfilename(title = "abrir",initialdir = "/Users/RSR/Desktop/")
    imagenView = ImageTk.PhotoImage(file = str(rutaimagen))
    tk.Label(imagen, image = imagenView).pack()
    imagen.mainloop()

def abrir_imagen(ruta):
    imagen = Image.open(ruta)
    return imagen

def cerrar_imagen(imagen):
    imagen.close()

def crear_imagen(tipo_imagen,tamanio):
    nueva_imagen = Image.new(tipo_imagen, tamanio)
    return nueva_imagen

def guardar_imagen(imagen,datos,nombre_imagen):
    imagen.putdata(datos)
    imagen.save(nombre_imagen)
    #imagen.show()

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
    
def binarizar_imagen(img_inicial,umbral):
    foto = abrir_imagen(img_inicial)#se abre la imagen inicial
    if foto.mode != 'L':
        foto=foto.convert('L')
    datos=foto.getdata()
    datos_binarios=[]
    for x in datos:
        if x<umbral:
            datos_binarios.append(0)
            continue
        #si es mayor o igual a umbral se agrega 1 en ves de 0
        #podria hacerse con 255 en ves de 1
        datos_binarios.append(1)

    nueva_imagen = crear_imagen('1', foto.size)
    guardar_imagen(nueva_imagen,datos_binarios,"img_binaria_umbral_"+str(umbral)+".jpg")
    cerrar_imagen(nueva_imagen)
    foto.close()

def Grises(rutaimagen):
    imagen = Image.open(rutaimagen)
    imagenResultado = Image.new('L', imagen.size)
    ancho,alto = imagen.size
    for i in range (ancho):
        for j in range (alto):
            r,g,b = imagen.getpixel((i,j))
            prom = (r + g + b) // 3
            imagenResultado.putpixel((i,j),prom)
    imagenResultado.save("grises.jpg")
    #imagenResultado.show()

def Sobel(rutaimagen):
    imagen = Image.open(rutaimagen)
    if imagen.mode != 'L':
        imagen=imagen.convert('L')
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
    imgResultado.save("sobel.jpg")
    #imgResultado.show()

def FiltroMin(rutaimagen):
    imagen = Image.open(rutaimagen)
    if (imagen.mode != 'L'):
        imagen = Grises(rutaimagen)
    imgResultado = Image.new('L',imagen.size)
    ancho,alto = imagen.size
    g = 0
    for i in range (ancho):
        for j in range (alto):
            V = ObtenerVecindad8(i, j, imagen)
            g = min(V)
            imgResultado.putpixel((i,j),g)
    imgResultado.save("filtroMin.jpg")
    #imgResultado.show()

def Dilatacion(rutaimagen):
    EE = [255, 255, 255,
          255, 255, 255,
          255, 255, 255]
    imagen = Image.open(rutaimagen)
    imagen = imagen.convert('1')
    imagenResultado = Image.new('1', imagen.size)
    ancho,alto = imagen.size
    for i in range (ancho):
        for j in range (alto):
            aux = 0
            g = imagen.getpixel((i,j))
            if (g == 255):
                for x in range (i-1, i+2):
                    for y in range (j-1, j+2):
                        try:
                            imagenResultado.putpixel((x,y),EE[aux])
                            aux += 1
                        except:
                            aux += 1
    imagenResultado.save("dilatacion.jpg")
    #imagenResultado.show()

def Erosion(rutaimagen):
    EE = [255, 255, 255,
          255, 255, 255,
          255, 255, 255]
    imagen = Image.open(rutaimagen)
    imagen = imagen.convert('1')
    imagenResultado = Image.new('1', imagen.size)
    ancho,alto = imagen.size
    for i in range (ancho):
        for j in range (alto):
            V = ObtenerVecindad8(i, j, imagen)
            aux = 0
            for x in range (9):
                if (V[x] == EE[x]):
                    aux += 1
            if (aux > 5):
                imagenResultado.putpixel((i,j),255)
            else:
                imagenResultado.putpixel((i,j),0)
    imagenResultado.save("erosion.jpg")
    #imagenResultado.show()

def suma_imagenes_rgb(img_1,img_2):#obtiene una imagen en escala de grises a partir de una imagen RGB
    imagen = abrir_imagen(img_1).convert("RGB")#se abre la imagen inicial
    datos = imagen.getdata()#se obtienen las matrices de la imagen
    imagen2 = abrir_imagen(img_2)#se abre la imagen inicial
    datos2 = imagen2.getdata()#se obtienen las matrices de la imagen

    resultante = [((datos[x][0] + datos2[x][0] ) // 2,(datos[x][1] + datos2[x][1] ) // 2,(datos[x][2] + datos2[x][2] ) // 2) for x in range(len(datos))]

    imagen_suma = crear_imagen('RGB', imagen.size)#se indica que es una imagen en escala de grises del tamaño de la imagen inicial

    guardar_imagen(imagen_suma,resultante,"suma_rgb.jpg")#se guardan los datos de la imagen nueva

    cerrar_imagen(imagen_suma)#se cierra la imagen creada
    cerrar_imagen(imagen)
    cerrar_imagen(imagen2)

def Filtrado ():
    global rutaimagen
    Grises(str(rutaimagen))#paso 1
    Sobel("grises.jpg")#paso  2
    binarizar_imagen("sobel.jpg",34)#paso 3
    Dilatacion("img_binaria_umbral_34.jpg")#paso 4 
    FiltroMin("dilatacion.jpg")#paso 5
    Erosion("filtroMin.jpg")#paso 6
    suma_imagenes_rgb("erosion.jpg",str(rutaimagen))#se muestra el resultado sobre la imagen

    imagen = tk.Toplevel()
    imagenView = ImageTk.PhotoImage(file = "suma_rgb.jpg")
    tk.Label(imagen, image = imagenView).pack()
    imagen.mainloop()

raiz = tk.Tk()
raiz.geometry('1200x800')
raiz.config(bg = "white")
raiz.title("Analisis Imagenes")

Titulo = tk.Label(raiz, text = "Proyecto Final", font = ("Times New Roman",20), bg="#25DBFF", fg="white", width="500",heigh="1")
Titulo.pack()

tk.Button(raiz, text = "Abrir Imagen", bg="#25DBFF", command = abrirVentana).place(relx = 0.04, rely = 0.10, relwidth = 0.13, relheight = 0.05 )

tk.Button(raiz, text = "Aplicar Filtros", bg="#25DBFF", command = Filtrado).place(relx = 0.04, rely = 0.18, relwidth = 0.13, relheight = 0.05 )

tk.Button(raiz, text = "Salir", bg="#25DBFF", command = cerrar).place(relx = 0.04, rely = 0.26, relwidth = 0.13, relheight = 0.05 )
raiz.mainloop()