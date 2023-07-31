#URNA ELETRONICA_
from random import randint as R

class UrnaEletronica:
    def __init__(self) -> None:
        self.senha = R(100,999)
        self.senha2 = 0
        self.candidato = 0
        self.confirma = self.voltar = ""
        self.lula = self.bolsonaro = self.nulo = 0
    
    def InsertPassword(self):
        print(f"Senha: {self.senha}")

        while True:
            try:
                self.senha2 = int(input("Ensira a senha de acesso a urna: "))

                if self.senha == self.senha2: break
                else: raise ValueError

            except ValueError:
                print("Senha Incorreta!")
    
    def EscolhaCandidatos(self):
        if self.senha == self.senha2:
            print("Lula - 13  |  Bolsonaro - 22  |  Nulo - 0")
            self.candidato = int(input("Escolha o candidato desejado: "))

            while self.candidato != 13 and self.candidato != 22 and self.candidato != 0:
                print(f"Voce digitou o candidato {self.candidato}, e esse numero é invalido!\nTente novamente: ")
                self.candidato = int(input())
            
    def CandEscolhido(self):
            if self.candidato == 13:
                print("Voce escolheu o candidato Lula")
                self.confirma = input("Deseja confirmar o voto?(s/n)").lower()
                if self.confirma == "s":
                    self.lula+=1
                    self.voltar = input("Voce confirmou o voto! Deseja voltar a urna:").lower()
                    if self.voltar == "s":
                        self.EscolhaCandidatos()

            elif self.candidato == 22:
                print("Voce escolheu o candidato bolsonaro, deseja confirmar o voto?(s/n)")
                self.confirma = input("Deseja confirmar o voto?(s/n)").lower()
                if self.confirma == "sim":
                    self.bolsonaro+=1
                    print("Voce confirmou o voto! Deseja voltar a urna? ")

            elif self.candidato == 0:
                print("Voce escolheu votar nulo, deseja confirmar o voto?(s/n)")
                self.confirma = input("Deseja confirmar o voto?(s/n)").lower()
                if self.confirma == "sim":
                    self.nulo+=1
                    print("Voce confirmou o voto! Deseja voltar a urna? ")

ex = UrnaEletronica()
ex.InsertPassword()
ex.EscolhaCandidatos()
ex.CandEscolhido()