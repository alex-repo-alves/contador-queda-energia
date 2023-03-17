import time

# Verifica se a biblioteca pyautogui está instalada e a instala caso não esteja
try:
    import pyautogui
except ImportError:
    print("Biblioteca pyautogui não encontrada. Instalando...")
    pip.main(['install', 'pyautogui'])
    import pyautogui

# verifica se a biblioteca pygetwindow está instalada e instala caso não esteja
try:
    import pygetwindow as gw
except ImportError:
    print("pygetwindow não está instalada. Instalando...")
    pip.main(['install', 'pygetwindow'])
    import pygetwindow as gw

# Espera 5 segundos para dar tempo de mudar para a janela do Chrome
time.sleep(5)

# Encontra a janela do Chrome desejada
chrome_window = gw.getWindowsWithTitle('Document')[0]

# Seleciona a janela do Chrome
chrome_window.activate()

# Usa o atalho do teclado Ctrl+Tab para alternar entre abas
while True:
    pyautogui.hotkey('ctrl', 'tab')
    time.sleep(5)
