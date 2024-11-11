from ESP_ENG import run as ESP_ENG_RUN
from ENG_ESP import run as ENG_ESP_RUN

if __name__ == '__main__':
    running = True
    print("Bienvenido al traductor de USQL-SQL")
    while running == True:
        opcion = int(input("Elija la traduccion que quiera hacer:\n1. ESP a ENG\n2. ENG a ESP\nRespuesta: "))
        if opcion == 1:
            ESP_ENG_RUN()
        if opcion == 2:
            ENG_ESP_RUN()