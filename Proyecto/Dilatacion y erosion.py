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
    imagenResultado.show()

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
            if (V == EE):
                imagenResultado.putpixel((i,j),255)
            else:
                imagenResultado.putpixel((i,j),0)                            
    imagenResultado.save("erosion.jpg")
    imagenResultado.show()