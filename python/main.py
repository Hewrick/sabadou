import pyautogui
import tkinter as tk        # Referência: https://www.tutorialspoint.com/python/python_gui_programming.htm ; https://hub.asimov.academy/blog/o-que-e-tkinter/ ; https://docs.python.org/3/library/tkinter.html
import keyboard as teclado



# Função para pegar a posição do mouse a cada 0,1 segundos (100ms)
def posicao_mouse():
    x, y = pyautogui.position() # Pega a posição atual
    label_posicao_mouse.config(text=f"{x}, {y}")
    janela.after(100, posicao_mouse)

# Função para verificar se a tecla "ESC" foi precionada para fechar o programa
def fecha_programa():
    # Se a tecla 'esc' for pressionada, fecha a janela
    if teclado.is_pressed('esc'):
        janela.destroy()
    else:
        janela.after(100, fecha_programa) # Verifica novamente a cada 100ms



#   == Configurações de tudo na janela ==
# Configuração da Janela
janela = tk.Tk() # Criação do objeto da janela
janela.title("SABADOOU")
janela.geometry("500x300") # Define um tamanho fixo para a janela




# Layout base 
menu = tk.Frame() # Estudar como desenvolver janela a partir de classes (sim, aqui no python)

titulo = tk.Label(janela, text="Automatix", font=("Consolas", 18))
titulo.place(x=15,y=10)

btn_addAcao = tk.Button(menu, text="✚")
btn_addAcao.pack()



# Configuração do label da posição do mouse
label_posicao_mouse = tk.Label(janela, font=("Consolas", 16))
label_posicao_mouse.pack()


#   == Iniciando o programa ==
# btn = 1 then posicao_mouse()
#layout_base()
fecha_programa()
posicao_mouse()

janela.mainloop() # Comando para abrir janela e rodar em loop "infinito" até fechar



""" Notas:
    - Como o programa é do tipo de loop infinito, preciso aprender a fazer funções para esse tipo de programa, mas parece ser simples lidar com isso;
    - É importante usar o objeto da janela como uma variável "root = tkinter.Tk()", 
assim é possível fazer alterações nos atributos da janela 
    - "pyautogui.FAILSAFE = True" não funciona enquanto "tkinter.Tk().mainloop()" estiver ativo 
    - "tkinter.Tk().mainloop()" precisa ser a última linha a ser executada. É como se fosse o "return"
"""


""" #   == Código para printar a posição do mouse ==
# Configuração de segurança
pyautogui.FAILSAFE = True

posicaoMouse = pyautogui.position()
time.sleep(3)
print(posicaoMouse)
"""

"""# Esse comando mostra as coordenadas em tempo real no terminal!
pyautogui.displayMousePosition() # Aperte Ctrl+C no terminal para parar
"""
