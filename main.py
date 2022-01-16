import tkinter as tk
from tkinter.filedialog import askopenfile, asksaveasfilename
class Editor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Editor de texto Chingon')
        self.iconbitmap('skull.ico')
        self.rowconfigure(0, minsize=600, weight=1)
        self.columnconfigure(1, minsize=600, weight=1)
        self.campoTexto = tk.Text(self, wrap=tk.WORD)
        self.archivo = None
        self.archivoAbierto = False
        self._crearComponentes()
        self._crearMenu()

    def _crearMenu(self):
        menuApp = tk.Menu(self)
        self.config(menu=menuApp)
        menuArchivo = tk.Menu(menuApp, tearoff=False)
        menuApp.add_cascade(label='archivo', menu=menuArchivo)
        menuArchivo.add_command(label='Abrir', command=self._abrirArchivo)
        menuArchivo.add_command(label='Guardar', command=self._guardar)
        menuArchivo.add_command(label='Guardar como...', command=self._guardarComo)
        menuArchivo.add_separator()
        menuArchivo.add_command(label='Salir', command=self.quit)

    def _abrirArchivo(self):
        self.archivoAbierto = askopenfile(mode='r+', filetypes=[('Archivos de texto', '*.txt')])
        self.campoTexto.delete(1.0, tk.END)
        if not self.archivoAbierto:
            return
        with open(self.archivoAbierto.name, 'r+') as self.archivo:
            texto = self.archivo.read()
            self.campoTexto.insert(1.0, texto)
            self.title(f'*Editor texto - {self.archivo.name}')
    def _guardar(self):
        if self.archivoAbierto:
            with open(self.archivoAbierto.name, 'w') as self.archivo:
                texto = self.campoTexto.get(1.0, tk.END)
                self.archivo.write(texto)
                self.title(f'Editor texto - {self.archivo.name}')
        else:
            self._guardarComo()
    def _guardarComo(self):
        self.archivo = asksaveasfilename(
            defaultextension='txt',
            filetypes=[('Archivos de texto', '*.txt'), ('Todos los archivos', '*.*')]
        )
        if not self.archivo:
            return
        with open(self.archivo, 'w') as archivo:
            texto = self.campoTexto.get(1.0, tk.END)
            archivo.write(texto)
            self.title(f'Editor texto - {archivo.name}')
            self.archivoAbierto = archivo

    def _crearComponentes(self):
        #definicion de primer cuadro de botones
        frameBotones = tk.Frame(self, relief=tk.RAISED, bd=2)
        #creacion de botones
        abrirbtn = tk.Button(frameBotones, text='Abrir', command=self._abrirArchivo)
        guardarbtn = tk.Button(frameBotones, text='Guardar', command=self._guardar)
        guardarComobtn = tk.Button(frameBotones, text='Guardar como...', command=self._guardarComo)
        #publicacion de frame
        frameBotones.grid(row=0, column=0, sticky='ns')
        #publicacion de campo de texto
        self.campoTexto.grid(row=0, column=1, sticky='nswe')
        # publicacion de botones
        abrirbtn.grid(row=0, column=0, sticky='we', padx=5, pady=5)
        guardarbtn.grid(row=1, column=0, sticky='we', pady=5, padx=5)
        guardarComobtn.grid(row=2, column=0, sticky='we', padx=5, pady=5)








if __name__ == '__main__':
    editor = Editor()
    editor.mainloop()