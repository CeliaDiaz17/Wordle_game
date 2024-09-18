import random

palabras = ["gatos", "perro", "casas", "papel", "movil", "libro", "arbol", "pluma", "color"]

def elegir_palabra():
    return random.choice(palabras)

def juego_wordle():
    palabra = elegir_palabra()
    #print(palabra)
    intentos = 5
        
    print("Bienvenido/a a Wordle!")
    print(f"En {intentos} intentos tienes que adivinar una palabra de 5 letras. Suerte!")
    
    while intentos > 0:
        intento = input("Introduce un intento de 5 letras:")
        
        if len(intento) != 5:
            print("Por favor, introduce una palabra de 5 letras.")
            continue
            
        if intento == palabra:
            print("¡Felicidades! Has acertado la palabra.")
            return
        
        resultado = ""
        for i in range(5):
            if intento[i] == palabra[i]:
                resultado += "🟩"
            elif intento[i] in palabra:
                resultado += "🟨"
            else:
                resultado += "🟥"
        
        print(resultado)
        intentos -= 1
        print(f"Te quedan {intentos} intentos.")
    
    print(f"Lo siento, has perdido. La palabra era {palabra}.")
    
if __name__ == "__main__":
    juego_wordle()