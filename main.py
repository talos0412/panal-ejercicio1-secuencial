import time

def recolectar_nectar(abeja, flor, tiempo):
    print(f"{abeja} está recolectando néctar de la {flor}.")
    time.sleep(tiempo)
    print(f"{abeja} ha terminado de recolectar néctar de la {flor}.")
    
if __name__ == "__main__":
    ab1="Abeja Obrera #1"
    print("Iniciando la recolección en solitario de néctar...")
    inicio=time.time()
    
    recolectar_nectar(ab1, "Rosa", 2)
    recolectar_nectar(ab1, "Girasol", 3)
    recolectar_nectar(ab1, "Tulipán", 1)

    fin=time.time()
    print(f"Tiempo total de recolección: {fin - inicio:.2f} segundos.")