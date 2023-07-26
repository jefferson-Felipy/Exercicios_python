"""Importando da biblioteca random apenas a função randint() para a criação de numeros
 inteiros aleatorios_"""
from random import randint as R

"""Criando a classe Random_number_hit_game:
    -> Essa classe é a representação de um jogo de acerto de números aleatorios, onde 
    o usuario irá chutar um número de 1 á 10, e vai tentar acertar o número aleatorio gerado
    dentro dessa faixa de valores.
    -> Ele terá tres tentativas para acertar esse valor, caso nao consiga, ele perde o jogo.
    ->Se ele acertar o número aleatorio gerado pela máquina, é exibido a mensagem de parabens.
"""
class Random_number_hit_game:
    #Contrução do constructor_
    def __init__(self) -> None:
        #Duas variáveis irão receber o mesmo valor inicial_
        self.Entered_value = self.Number_random = 0
        self.attemps = 3
        self.return_back = ""

    #painel do jogo_
    def Panel(self):
        print("  --------------- GAME OF PANEL -----------------  ")
        print("  ----------- You have - 3 - attemps ------------")

    """Método em que o usuário irá digitar o número que ele acha que é o certo_
    Foi utilizado um tratamento de dados para que o usuário digite um valor inteiro 
    dentro da faixa especificada_"""
    def Fill_Number(self):
        while True:
            try:
                self.Entered_value = int(input("Enter the desired number: "))

                if(1 <= self.Entered_value <= 10):
                    break
                else: 
                    raise ValueError

            except ValueError:
                print(f"Invalid {self.Entered_value} value, try again!")

    #Método que irá gerar um número aleatorio e vai armazenar na variavel self.Number_random_
    def Number_Random(self):
        self.Number_random = R(1, 10)

    #Método que irá compapar os valores, verificando se sao igual ou diferentes_
    def Compare_Values(self):
        while self.attemps > 0:
            if(self.Entered_value != self.Number_random):

                if(self.Entered_value < self.Number_random):
                    print(f"Value {self.Entered_value} smaller than the generated random number!")
                
                elif(self.Entered_value > self.Number_random):
                    print(f"Value {self.Entered_value} greater than the generated random number!")
            
                self.attemps -= 1
                if self.attemps > 0:
                    print(f"You own just more {self.attemps} attepms!")
                    self.Fill_Number()
                else:
                     print(f"You lost all attempts! The generated number was {self.Number_random}!")
                    
            else: 
                print("     ======================================================")
                print(f"Congratulations, you got the random number right, which was {self.Number_random}!")
                print("     ======================================================")
        
            if(self.attemps == 0 or self.Entered_value == self.Number_random):
                print("Do you want to return to play?")
                self.return_back = input("S/N: ").lower()

                if(self.return_back == "s"): 
                    self.attemps = 3
                    self.Number_Random()
                    self.Fill_Number()
                else: break

if __name__ == "__main__":
    variable = Random_number_hit_game()
    variable.Panel()
    variable.Fill_Number()
    variable.Number_Random()
    variable.Compare_Values()