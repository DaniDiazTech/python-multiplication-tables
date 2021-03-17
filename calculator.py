"""
Multiplication table program

Made for 7-8 y/o kids
"""
import random


class BaseTable():

    def __init__(self):

        self.score = 0
        self.lives = 3

    def print_start_table(self):
        print(
            """
=========================================
    Programa de tablas de multiplicar
=========================================

Tienes que responder correctamente a la
siguientes multiplicación para ganar.


Tienes 3 vidas, que iras perdiendo si respondes mal.

Responde bien a 5 multiplicaciones y ganaras.
"""
        )

    def print_current_score(self):

        print(f"Tu puntaje actual es {self.score}")

    def get_random_numbers(self):

        first_number = random.randint(1, 10)
        second_number = random.randint(1, 10)

        return first_number, second_number

    def print_score(self):
        print(f"Ahora tienes {self.score} puntos")
    
    def print_lives(self):
        print(f"Te quedan {self.lives} vidas")

    def run_challenge(self):

        first, second = self.get_random_numbers()

        input_text = "Escribe el resultado de la operación >>>"

        result = first * second

        print("La multiplicación a realizar es: ")

        print(f"{first} x {second}")

        user_result = 0

        while 1:
            try:
                user_input = int(input(input_text))

                user_result = user_input

                break
            except ValueError:
                print("Lo siento tu respuesta tiene que ser un número")

        if not user_result == result:
            print("Lo siento, tu respuesta es incorrecta",
                  "Pierdes una vida :(", sep="\n")
            self.lives -= 1

        else:
            print("Correcto!, tu respuesta es correcta has ganado un punto")
            self.score += 1

        self.print_score()
        self.print_lives()


class Game(BaseTable):
    def run(self):
        self.print_start_table()

        while 1:
            if self.lives <= 0 or self.score >= 5:
                if self.lives <= 0:
                    print("Lo siento has perdido! Pero si quieres puedes volver a jugar")
                elif self.score >= 5:
                    print("Perfecto, lo has logrado!, si quieres puedes volver a jugar")
                
                while 1:
                    decission = input("Quieres volver a jugar? [si, no]")

                    if decission.startswith("s") or decission.startswith("S"):
                        print("Vuelves a jugar!")

                        self.score = 0
                        self.lives = 3

                        self.run()
                        break

                    elif decission.startswith("n") or decission.startswith("N"):
                        print("Perfecto, gracias por jugar!")
                        break
                    
                    else:
                        print("Lo siento no te he entendido, puedes volver a escribir tu decisión?")

                break

            else:
                self.run_challenge()


if __name__ == "__main__":
    new_game = Game()

    new_game.run()
