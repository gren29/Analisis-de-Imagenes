from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

raiz = Tk()
raiz.geometry('500x500')
raiz.title("Proyecto")

ancho_button = 10
alto_button = 10


botonA = Button(raiz,text = "Filtro").place(x = 0,y = 0)
botonB = Button(raiz,text = "Filtro B").place(x = 50, y = 0)
botonC = Button(raiz,text = "Filtro C").place(x = 100, y = 0)
botonD = Button(raiz,text = "Filtro D").place(x = 150, y = 0)

def abrirArchivo():
    archivo = filedialog.askopenfilename(title = "abrir",initialdir = "/Users/RSR/Desktop/")
    print(archivo)
    #imagen  = Image.open(archivo)
    im = ImageTk.PhotoImage(Image.open(archivo))
    my_label = Label(raiz,image = im)
    my_label.pack()
    imagen.show()


imageButton = Button(raiz, text = "Abrir Archivo", command = abrirArchivo).place(x = 0,y =20)



raiz.mainloop()