import random
from modules.juego_guerra import JuegoGuerra

def main():
    
    n = random.randint(0, 1000)  
    print(f"Semilla utilizada: {n}")  
    
    juego = JuegoGuerra(random_seed=n)
    
    juego.iniciar_juego()

if __name__ == '__main__':
    main()