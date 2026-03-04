import pyautogui

# Tenta localizar o centro da imagem
try:
    localizacao = pyautogui.locateCenterOnScreen('botao.png', confidence=0.9)
    if localizacao:
        print(f"Imagem encontrada em: {localizacao}")
        pyautogui.click(localizacao) # Clica no centro
    else:
        print("Imagem não encontrada.")
except pyautogui.ImageNotFoundException:
    print("Imagem não encontrada na tela.")
