from tkinter import *
from functools import partial
import re

class calculadora():
  def __init__(self):
    self.letra = "Helvetica 12 bold"
    self.f_pantalla = "ds-digital 12 bold"

  def inicio(self):
    self.interfaz()


  def interfaz(self):
    def cambiar_color(event):
      if type(event.widget) == type(btn): 
          event.widget.config(relief='groove')

    def restaurar_color(event): 
      if type(event.widget) == type(btn): 
          event.widget.config(relief='flat')

    frame_principal = Frame(main_window, bg='#000')
    frame_principal.grid(row=1, column=1, padx=2, pady=2)

    # Pantalla
    pantalla_nmr = StringVar()
    pantalla_nmr.set(0)

    pantalla = Entry(frame_principal, textvariable=pantalla_nmr, justify='right', font=self.f_pantalla, bg='black', fg='#00e5ff', highlightthickness=1, highlightbackground='#c7c7c7')
    pantalla.grid(row=1,column=1, columnspan=4, ipady=4, padx=5,pady=5, sticky='we')
    self.pantalla = pantalla

    # Botones
    num_pad = [[u"\u00AB", 'C', '=', '+'],
               [7, 8, 9, '-'],
               [4, 5, 6, 'x'],
               [1, 2, 3, '/'],
               ['+/-', 0, '.', '%']]
    contador=0
    for index, lista in enumerate(num_pad):
      for index_2, valor in enumerate(lista):
        
        btn = Button(frame_principal, text=valor, relief='flat', activebackground='lightblue', fg='white', font=self.letra, activeforeground='white', width=48, height=48, image=fondo_lista[contador], compound='center', command=partial(self.calcular, valor))
        btn.grid(row=index+2,column=index_2+1, padx=2,pady=2)

        root.bind("<Button-1>", cambiar_color)
        root.bind("<ButtonRelease-1>", restaurar_color)
        contador+=1


  def calcular(self, valor):
    if self.pantalla.get() == '0':
      if type(valor) == int:
        self.pantalla.delete(0,END)
        self.pantalla.insert('end', valor)
      else:
        pass
    else:
      # Simbolo
      if valor in ('+', '-', 'x', '/','%'):
        nmr_uno = self.pantalla.get()
        if nmr_uno[-1] in ('+', '-', 'x', '/'):
          pass
        else:
          self.pantalla.insert('end', valor)
      
      # Punto
      elif valor == '.':
        nmr_anterior = self.pantalla.get()
        nmr_lista = re.split("\+|\*|-|/|%", nmr_anterior)

        if ('+' in nmr_anterior or '-' in nmr_anterior or '/' in nmr_anterior or '*' in nmr_anterior or '%' in nmr_anterior) and '.' not in nmr_lista[-1]:
          nmr_anterior = f'{nmr_anterior}.'
          self.pantalla.insert('end', valor)

        if not '.' in nmr_anterior:
          self.pantalla.insert('end', valor)

      # Negativo y Positivo
      elif valor == '+/-':
        nmr_anterior = self.pantalla.get()

        if '-' == nmr_anterior[0]:
          print(nmr_anterior[0])
          nmr = nmr_anterior[:0] + nmr_anterior[0+1:]
          self.pantalla.delete(0,END)
          self.pantalla.insert('end', nmr)

        else:
          nmr = f"-{nmr_anterior}"
          self.pantalla.delete(0,END)
          self.pantalla.insert('end', nmr)

      # Calcular
      elif valor == '=':
        nmr = self.pantalla.get()

        # Porcentaje
        if '%' in nmr:
          x = re.split("%", nmr)
          y = float(x[0]) / 100
          porcentaje = y*float(x[1])

          self.pantalla.delete(0, END)
          self.pantalla.insert(END, porcentaje)

        # Resultado
        else:
          try:
            resultado = eval(self.pantalla.get())
            self.pantalla.delete(0,END)
            self.pantalla.insert('end', resultado)
          except Exception as e:
            print(e)

      # Limpiar ultimo valor
      elif valor == u"\u00AB":
        nmr = self.pantalla.get()[:-1]
        self.pantalla.delete(0, END)
        self.pantalla.insert(END, nmr)

      # Limpiar todo
      elif valor == 'C':
        self.pantalla.delete(0, END)
        self.pantalla.insert(END, 0)

      # Agregar valor
      else:
        self.pantalla.insert('end', valor)


root = Tk()
root.title('7C-Dora')
root.resizable(False, False)
root.iconbitmap('img/logox32.ico')

# pyinstaller.exe --onefile --windowed --icon=logox64.ico main.py

f1 = PhotoImage(file=r'img/20.png')
f2 = PhotoImage(file=r'img/19.png')
f3 = PhotoImage(file=r'img/18.png')
f4 = PhotoImage(file=r'img/17.png')

f5 = PhotoImage(file=r'img/16.png')
f6 = PhotoImage(file=r'img/15.png')
f7 = PhotoImage(file=r'img/14.png')
f8 = PhotoImage(file=r'img/13.png')

f9 = PhotoImage(file=r'img/12.png')
f10 = PhotoImage(file=r'img/11.png')
f11 = PhotoImage(file=r'img/10.png')
f12 = PhotoImage(file=r'img/9.png')

f13 = PhotoImage(file=r'img/8.png')
f14 = PhotoImage(file=r'img/7.png')
f15 = PhotoImage(file=r'img/6.png')
f16 = PhotoImage(file=r'img/5.png')

f17 = PhotoImage(file=r'img/4.png')
f18 = PhotoImage(file=r'img/3.png')
f19 = PhotoImage(file=r'img/2.png')
f20 = PhotoImage(file=r'img/1.png')

fondo_lista = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20]

main_window = Frame(root)
main_window.pack()

c = calculadora()
c.inicio()

root.mainloop()