from main import pg
from time import sleep

def pegar_posicao():
    sleep(3)
    return pg.position()
    
posicao_x_y = pegar_posicao()
print(posicao_x_y)