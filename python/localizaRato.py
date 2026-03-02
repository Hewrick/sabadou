import pyautogui
import tkinter as tk        # Referência: https://hub.asimov.academy/blog/o-que-e-tkinter/ ; https://docs.python.org/3/library/tkinter.html
import keyboard as teclado

# Função para pegar a posição do mouse a cada 0,1 segundos (100ms)
def posicao_mouse():
    x, y = pyautogui.position() # Pega a posição atual
    label_posicao_mouse.config(text=f"X: {x}, Y: {y}")
    janela.after(100, posicao_mouse) # Função se chama após 100ms

# Função para verificar se a tecla "ESC" foi precionada para fechar o programa
def fecha_programa(janela_escolhida):
    # Se a tecla 'esc' for pressionada, fecha a janela
    if teclado.is_pressed('esc'):
        janela_escolhida.destroy(janela_escolhida)
        janela2 = tk.Tk()
    else if teclado.is_pressed('esc') and janela2:
        janela2.destroy()
    else:
        janela.after(100, fecha_programa(janela_escolhida)) # Verifica novamente a cada 100ms


# Configuração da Janela
# Criação do objeto da janela
janela = tk.Tk()
janela.title("SABADOOU")
janela.geometry("300x100") # Define um tamanho fixo para a janela

janela.attributes("-topmost", True) # Mantém a janela sempre no topo


# Configuração do label da posição do mouse
label_posicao_mouse = tk.Label(janela, font=("Arial", 18), padx=15, pady=15)
label_posicao_mouse.pack()

posicao_mouse()
fecha_programa()

# Comando para abrir janela e rodar em loop "infinito" até fechar
janela.mainloop()



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
