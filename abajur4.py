import tkinter as tk

class Abajur:
    def __init__(self):
        self.__lampada = False  
        self.__intensidade = 0  

    def __liga_desliga_lampada(self):
        self.__lampada = self.__intensidade > 0  

    def __controla_intensidade(self):
        self.__intensidade += 1
        if self.__intensidade > 3:
            self.__intensidade = 0  

    def tocar_botao(self):
        self.__controla_intensidade()  
        self.__liga_desliga_lampada()  

    def mostrar_status(self):
        estado_lampada = "acessa" if self.__lampada else "apagada"
        intensidade_luz = ["apagada", "fraca", "media", "forte"]
        intensidade = intensidade_luz[self.__intensidade]
        return f'A lampada esta {estado_lampada}, intensidade: {intensidade}'


def acionar_abajur():
    abajur.tocar_botao()
    status = abajur.mostrar_status()
    label_status.config(text=status)  


janela = tk.Tk()
janela.title("Controle do Abajur")


abajur = Abajur()


label_status = tk.Label(janela, text=abajur.mostrar_status(), font=("Arial", 16))
label_status.pack(pady=20)


botao = tk.Button(janela, text="Tocar Botão", command=acionar_abajur, font=("Arial", 14))
botao.pack(pady=10)


janela.mainloop()
