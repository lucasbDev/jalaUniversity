# Descreva pelo menos 3 objetos que representam um polígono, escreva seus atributos e seus métodos. 

class Poligono:
  def __init__(self, paramSide, paramNumberOfSide, paramApothem, numbersVertices):
    self.atribSide = paramSide
    self.atribNumberOfSide = paramNumberOfSide
    self.atribApothem = paramApothem
   

  def calculatePerimeter(self):
    perimeter = self.atribSide * self.atribNumberOfSide
    return perimeter


  def calculateArea(self):
    area = (self.calculatePerimeter() * self.atribApothem) / 2
    return area


triangulo = Poligono(5, 3, 5)
quadrado = Poligono(4, 4, 2)
print(quadrado.calculateArea())

"""Para obter as propriedades e métodos necessários
    vamos considerar que você deseja desenvolver uma loja online
    onde venderemos esses patos. Então, com esse contexto, considere
    quais propriedades e métodos precisamos conhecer"""

class PatoDeBorracha: 
  def __init__(self, cor, tamanho, peso):
        self.cor = cor
        self.tamanho = tamanho
        self.peso = peso

  def emitirSom(self):
      print("Quack!")

  def flutuar(self):
      print("sniff sniff") 

  def esguicharAgua(self):
      print("chuá chuá!")

patinho = PatoDeBorracha("blue", "30cm", "22kg")

PatoDeBorracha.emitirSom(patinho)

""""O aplicativo será capaz de reconhecer vários tipos de ave, portanto, é necessária
    uma boa abstração para começar a implementar o aplicativo, identificar as propriedades 
    e métodos que representam uma ave."""

class Passaro:
  def __init__(self, name, species, color, size):
    self.name = name
    self.species = species
    self.color  = color 
    self.size = size


  def voar(self):
    print(f"o {self.name} consegue voar!")
  
  def swin(self):
    print(f"o {self.name} consegue nadar!")

  def whistle(self):
    print(f"o {self.name} consegue assobiar!")  
  
    

papagaio = Passaro("Amazona vinacea", "Papagaio", "Azul", "130cm")
Passaro.voar(papagaio)


""""Pessoas, uma pessoa tem um número n de características como nome,
    sobrenome, idade, data de nascimento, cor do cabelo, etc. Mas, dependendo do caso
    precisamos aumentar ou remover atributos. Com isso em mente, estamos construindo uma
    aplicação para uma escola, onde precisamos abstrair todos os atributos que definem um Aluno
    preencher a classe Aluno com todos os atributos necessários. """

class Aluno:
    def __init__(self, nome, idade, genero, turma, notas):
        self.nome = nome
        self.idade = idade
        self.genero = genero
        self.turma = turma
        self.notas = notas
        
    def imprimirFichaAluno(self):
        print("Nome:", self.nome)
        print("Idade:", self.idade)
        print("Gênero:", self.genero)
        print("Turma:", self.turma)
        print("Notas:", self.notas)

aluno1 = Aluno("Yuri", 26, "Male", "A1", [9.5])

Aluno.imprimirFichaAluno(aluno1)

#Temos uma oficina mecânica, onde todos os dias vários carros passam por inspeção e são reparados, sob esta ideia o nosso mecânico define um carro com as seguintes propriedades:

class Car:
    def __init__(self,  color, brand, price, model, country, type ):
        self.color = color
        self.brand = brand
        self.price =  price
        self.model = country
        self.type =  type
        self.repaired = False
        self.moving = True


    def set_moving(self,moving):
        return self.moving

    def get_moving(self,moving):
        return self.moving
    
    def set_color(self,color):
        return self.color
    
    def get_brand(self):
        return self.brand
    
    def set_price(self,price):
        return self.price
    
    def get_model(self):
        return self.model
    
    def get_country(self):
        return self.country

    def get_type(self):
        return self.type

    def turnOn(self):
        if self.moving:
            print(f"O carro {self.brand} {self.model} está ligando")
        else:
            print(f"O carro {self.brand} {self.model} vai ser reparado!")

    def paintChange(self):
        if self.color:
          print(f"Alteramos a Cor do {self.brand} {self.model} ")
        else:
          print(f"A pintura eestá boa!")

car_1 = Car("Blue", "Toyota",300000, "SW4", "BR", "SUV")


Car.paintChange(car_1)