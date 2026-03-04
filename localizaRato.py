import pyautogui as robo
import tkinter

def posicao_mouse():
    x, y = robo.position()
    label_position.config(text=f'{x}, {y}')
    root.after(100, posicao_mouse)
    

root = tkinter.Tk()
root.title('Posição do Mouse')
root.geometry('150x80')
root.attributes('-topmost', True)

label_position = tkinter.Label(root, font=('Consolas', 20))
label_position.pack()

posicao_mouse()

root.mainloop()
