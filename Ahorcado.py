import random

class Ahorcado:
    def __init__(self):
        self.palabras = self.cargar_palabras()
        self.palabra_secreta = self.seleccionar_palabra()
        self.intentos_restantes = 6
        self.letras_acertadas = ["_"] * len(self.palabra_secreta)
        self.letras_usadas = []

    def cargar_palabras(self):
        with open("palabras.txt", "r") as archivo:
            palabras = archivo.readlines()
        return [palabra.strip().lower() for palabra in palabras]

    def seleccionar_palabra(self):
        return random.choice(self.palabras)

    def mostrar_progreso(self):
        print(" ".join(self.letras_acertadas))
        print(f"Intentos restantes: {self.intentos_restantes}")
        print(f"Letras usadas: {', '.join(self.letras_usadas)}")

    def jugar(self):
        print("\nJUEGO AHORCADO")
        while "_" in self.letras_acertadas and self.intentos_restantes > 0:
            self.mostrar_progreso()
            letra = input("Ingrese la letra: ").lower()
            if letra in self.letras_usadas:
                print("Ya utilizaste esta letra.\n")
                continue
            self.letras_usadas.append(letra)
            if letra in self.palabra_secreta:
                print("Vas bien\n")
                for i in range(len(self.palabra_secreta)):
                    if self.palabra_secreta[i] == letra:
                        self.letras_acertadas[i] = letra
            else:
                print("Incorrecto.\n")
                self.intentos_restantes -= 1
        if "_" not in self.letras_acertadas:
            print(f"¡Felicidades! la palabra fue: {self.palabra_secreta}")
        else:
            print(f"¡Perdiste! La palabra era: {self.palabra_secreta}")

# Ejemplo de uso
juego = Ahorcado()
juego.jugar()