import pyautogui as robozin
import time

# Configuração de Segurança
# Se algo der errado, arraste o mouse para o canto superior esquerdo da tela rápido.
# Isso vai cancelar o script na hora (é o seu "botão de pânico").
robozin.FAILSAFE = True

# Pequena pausa para você dar o Play e tirar a mão do mouse
time.sleep(2)

# Pressiona a tecla Windows
robozin.press('win')

# Espera o menu iniciar abrir (meio segundo)
time.sleep(0.5)

# Digita o nome do programa
# O 'interval' faz parecer que um humano está digitando
robozin.write('calculadora', interval=0.1)

# Aperta Enter para abrir
robozin.press('enter')

print("ROBO ENCERRADO")