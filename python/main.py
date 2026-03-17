import pyautogui
import tkinter as tk        # Referência: https://www.tutorialspoint.com/python/python_gui_programming.htm ; https://hub.asimov.academy/blog/o-que-e-tkinter/ ; https://docs.python.org/3/library/tkinter.html
import keyboard as teclado



# Função para verificar se a tecla "ESC" foi precionada para fechar o programa
def fecha_programa():
    # Se a tecla 'esc' for pressionada, fecha a janela
    if teclado.is_pressed('esc'):
        app.destroy()
    else:
        app.after(100, fecha_programa) # Verifica novamente a cada 100ms

def adicionar_campo():
    btn_addAcao.pack()

# Função para pegar a posição do mouse a cada 0,1 segundos (100ms)
def posicao_mouse():
    x, y = pyautogui.position() # Pega a posição atual
    label_posicao_mouse.config(text=f"{x}, {y}")
    app.after(100, posicao_mouse)



#   == Configurações da Janela Principal ==
class App(tk.Tk):
    # Configuração iniciais da Janela principal
    def __init__(self):
        super().__init__()
        self.title("SABADOU")
        self.geometry("500x350") # Define um tamanho fixo para a janela

        titulo = tk.Label(self, text="SF Automation", font=("Consolas", 18))
        titulo.place(x=15,y=10)

        menu = tk.Frame() # Estudar como desenvolver janela a partir de classes (sim, aqui no python)
        
app = App()

btn_addAcao = tk.Button(app, command=adicionar_campo, text="✚", width=200, height=20)
btn_addAcao.place()

# Configuração do label da posição do mouse
label_posicao_mouse = tk.Label(app, font=("Consolas", 16))
label_posicao_mouse.place(x=390,y=10)


#   == Iniciando o programa ==
# btn = 1 then posicao_mouse()
fecha_programa()
posicao_mouse()

app.mainloop() # Comando para abrir janela e rodar em loop "infinito" até fechar
