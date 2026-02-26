import pyautogui
import tkinter as tk
import keyboard as teclado

""" Vou aprender sobre o tkinter e depois voltar com esse código
# Função para pegar a posição do mouse a cada 0,1 segundos (100ms)
def posicao_mouse():
    # Pega a posição atual
    x, y = pyautogui.position()
    # Atualiza o texto da label
    label.config(text=f"X: {x}, Y: {y}")
    # Função se chama após 100ms
    root.after(100, posicao_mouse)
"""

# Função para verificar se a tecla "ESC" foi precionada para fechar o programa
def fecha_programa():
    # Se a tecla 'esc' for pressionada, fecha a janela
    if teclado.is_pressed('esc'):
        root.destroy()
    else:
        # Verifica novamente a cada 100ms
        root.after(100, fecha_programa)


# Configuração da Janela
# Essa linha é o objeto da janela com o identificador "root"
root = tk.Tk()
# Título da janela
root.title("SABADOOU")
# Define um tamanho fixo para a janelinha
root.geometry("300x100")
# Mantém a janela sempre no topo
root.attributes("-topmost", True)


# Configuração do texto dentro da janela
# tkinter.Label([endereço da mensagem], [atributos do texto (ex.: text; font; padx; pady)])
label = tk.Label(root, font=("Arial", 16), padx=15, pady=15)
# Comando para mandas as configurações de "Label" para a janela
label.pack()

posicao_mouse()
fecha_programa()

# Comando para abrir janela e rodar em loop "infinito" até fechar
root.mainloop()



""" Notas:
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
