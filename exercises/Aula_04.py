#refatore o código da aula 03

def pedra_papel_tesoura_lagarto_spock(player_1, player_2):
    vencedores = {
        "pedra": {"tesoura": "Player 1 venceu!", "lagarto": "Player 1 venceu!"},
        "papel": {"pedra": "Player 1 venceu!", "spock": "Player 1 venceu!"},
        "tesoura": {"papel": "Player 1 venceu!", "lagarto": "Player 1 venceu!"},
        "lagarto": {"papel": "Player 1 venceu!", "spock": "Player 1 venceu!"},
        "spock": {"pedra": "Player 1 venceu!", "tesoura": "Player 1 venceu!"}
    }
    
    # Verifica se as entradas são válidas
    if player_1 not in vencedores:
        print("Entrada inválida para player_1")
        return
    if player_2 not in vencedores:
        print("Entrada inválida para player_2")
        return
    
    if player_1 == player_2:
        print("Empate!")
    else:
        resultado = vencedores[player_1].get(player_2, "Player 2 venceu!")
        print(resultado)


pedra_papel_tesoura_lagarto_spock("lagarto", "tesoura")


""" vamos imaginar que escrevemos nossa própria implementação e, em vez de mostrar
uma exceção, mostraremos uma mensagem para o usuário dizendo : "O índice que você 
está lidando para inserir não está na lista", então deixamos essa classe, para que você complete o método get, para que,
se o índice não existir, você imprima a mensagem, caso contrário, retorne o valor."""

class MyList:
    def __init__(self, items):
        self.items = items

#função para buscar o item através do índice
    def get(self, index):
        if index < 0 or index >= len(self.items):
            print("O índice que você está tentando acessar não está na lista")
            return None
        else:
            return self.items[index]

my_list = MyList([1, 2, 3, 4, 5])
print(my_list.get(0))

""" Vamos continuar implementando a funcionalidade em nossa lista,
neste caso queremos um método delete, que primeiro verifica se o valor
que queremos excluir está na lista, caso contrário imprime uma mensagem
que diz: "O valor não está na lista", caso contrário remova o valor."""

class CustomList:
    def __init__(self, items):
        self.items = items
    
    def delete(self, index):
        if index not in self.items:
          print("O valor não está na lista")
          return None
        else:
          self.items.remove(index)
          print("O valor foi removido!")
          
class_one = CustomList(["Maria", "George", "Pablo", "Lucas", "Marco", "Tony", "Diego"])

class_one.delete("George")

""" Na classe seguinte que define uma sala de aula, temos
um método check_student, que recebe como parâmetro o nome do aluno,
você deve determinar se o aluno está presente ou não na lista. Retorna
True se o aluno estiver presente, caso contrário retorna False."""

class ClassRoom:
    def __init__(self,students):
        self.students = students
        
    def check_student(self, student):
      if student not in self.students:
        return False
      else:
        return True
      
class_one = ClassRoom(["Maria", "George", "Pablo", "Lucas", "Marco", "Tony", "Diego"])
  
class_one.check_student("Beto")