import pyautogui as pg
from time import sleep
import pyperclip
from utils import tab

def abrir_whatsapp():
    pg.press("WIN")
    pg.write("Whatsapp")
    pg.press("ENTER")
    sleep(1.5)


def acessar_grupo():
    pg.click(x=297, y=116) # posição da barra de busca do whatsapp
    sleep(1)
    pg.write("IV congresso")
    sleep(2)
    tab(quantas_vezes=2)
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
        sleep(1)
        copiar_contato()
        sleep(0.5)

  
def copiar_contato():            
    posicao_nome_do_contato = 1615, 274
    posicao_numero_do_contato = 1600, 314 
    pg.moveTo(posicao_nome_do_contato, duration=0.2)
    
    # 1. Triplo clique para selecionar o nome do contato
    pg.tripleClick() 
    
    # 2. Copiar
    pg.hotkey('ctrl', 'c')
    nome_do_contato_copiado = pyperclip.paste()
    print("nome=", nome_do_contato_copiado)
    
     # 1. Triplo clique para selecionar o numero do contato
    pg.moveTo(posicao_numero_do_contato, duration=0.2)
    pg.tripleClick() 
    
    # 2. Copiar
    pg.hotkey('ctrl', 'c')
    numero_do_contato_copiado = pyperclip.paste()
    print("numero=", numero_do_contato_copiado)
    
    
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