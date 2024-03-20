import tkinter as tk


contador = 0


def contadorLabel(lbl_rotulo):
    def funcao_contar():
        global contador
        contador = contador + 1
        lbl_rotulo.config(text=str(contador))
        lbl_rotulo.after(1000, funcao_contar)
        funcao_contar()


janela = tk.Tk()
janela.title('Contagem segundos')
lbl_rotulo = tk.Label(janela, fg="green")
lbl_rotulo.pack()
contadorLabel(lbl_rotulo)
btnAcao = tk.Button(janela, text='Clique aqui para interromper')
btnAcao.pack()
janela.mainloop()
