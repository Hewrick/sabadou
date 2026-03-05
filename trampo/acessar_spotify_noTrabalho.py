import pyautogui as robo
import time

# Configuração de valores do PyAutoGUI
robo.FAILSAFE = True
robo.PAUSE = 0.8

# Iniciando valores
interrogacao = {
    robo.keyDown('shift'),
    robo.press('/'), # Tente '/' ou a tecla onde fica o '?' no seu layout
    robo.keyUp('shift')
}
user = 'pedrohenrique0709.0709@gmail.com'
senha = 'Murzzi?657'


def maximiza():
    if robo.getActiveWindow():
        robo.getActiveWindow().maximize()
    # Outro método: pyautogui.hotkey('win', 'up') 
    # Outro método: pyautogui.hotkey('win', 'up') 
    # Outro método: getWindowsWithTitle("Chrome")[0]
    

robo.press('win')
robo.write('chrome')
robo.click(740, 440)
maximiza()
time.sleep(1)

# Acessando site
robo.write('spotify.com')
robo.press('enter')
time.sleep(5)

# Clica em "Entrar"
robo.click(1300, 118)
time.sleep(5)
# Entra com email de usuário
robo.press('tab')
robo.write(user)
robo.press('enter')

# Entra com senha de usuário
for i in range(1,10):
    robo.press('tab')
robo.press('enter')

for i in range(0, 7):
    robo.press('tab')
robo.write(senha)
robo.press('enter')
