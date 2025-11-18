import pyautogui as pg
from time import sleep
import pyperclip
from utils import tab

def abrir_whatsapp():
    pg.press("WIN")
    pg.write("Whatsapp")
    pg.press("ENTER")
    sleep(3)


def acessar_grupo():
    pg.click(x=297, y=116) # posição da barra de busca do whatsapp
    sleep(1)
    pg.write("IV congresso")
    sleep(3)
    for i in range(2):
        print(i)
        tab()
    sleep(2)
    pg.press("ENTER")
    sleep(2)


# 15 tabs até a area de membros
def acessar_os_contatos():
    pg.click(x=633, y=57)
    sleep(2)
    #acessa a area de pesquisar membros
    # for i in range(17):
    #     tab()
    #     sleep(0.5)
    tab(quantas_vezes=17)
    pg.press("ENTER")
    sleep(2)
    

def acessar_contato():
    tab(quantas_vezes=3) #primeiro tab pra pular o numero da acadiprev
    pg.press("DOWN")
    for i in range(1):
        pg.press("ENTER")
        pg.press("DOWN")
        pg.press("ENTER")
        copiar_numero()
        sleep(0.5)

  
def copiar_numero():
    posicao_comeco_do_numero = 1569, 312
    posicao_final_do_numero =  1687, 314
    pg.moveTo(posicao_comeco_do_numero)
    pg.dragTo(posicao_final_do_numero, duration=1.0, button='left')
    pg.hotkey('crtl', 'c')
    print(pyperclip.paste())
    
    
def main():
# steps:
    abrir_whatsapp()
    acessar_grupo()
    acessar_os_contatos()
    acessar_contato()
    sleep(2)
    pg.click(x=1884, y=16)

if __name__ == '__main__':
    main()