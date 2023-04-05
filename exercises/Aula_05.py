"""  Scrabble é um jogo onde os jogadores marcam pontos soletrando palavras. 
     As palavras são pontuadas adicionando os valores de pontos de cada letra individual.
     Complete o método dentro da classe Game que, dada uma palavra, retorna a pontuação total 
     da palavra com base na seguinte divisão de pontos:"""


class Game:
    
    def __init__(self):
        self.scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
                       "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
                       "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
                       "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
                       "x": 8, "z": 10}
        
    def get_score(self, word):
        score = 0
        for letter in word.lower(): 
            if letter in self.scores:
                score += self.scores[letter]
        return score

game = Game()

score = game.get_score("Hello")

print(score)




""" A seguir apresentamos uma lista de números que representam os saldos de várias contas
 bancárias, o problema é que para mostrá-los ao cliente, precisamos que sejam mostrados em 
 porcentagem. Converta todos os números em porcentagem e imprima a nova lista."""

accounts = [0.12, 0.90, 0.89, 0.076, -0.87, 0.78, 0.65]
percentage_accounts = []

for account in accounts:
  percentage = account * 100
  percentage_accounts.append(percentage)

print(percentage_accounts)






""" Há uma string 𝑠 de comprimento 3, composta por letras maiúsculas e minúsculas.
    Verifique se é igual a "SIM" (sem aspas), onde cada letra pode ser em qualquer caso.
    Por exemplo, "YES", "yEs", "Yes" são todos permitidos.
    Imprima "SIM" se a condição for satisfeita, caso contrário, imprima "NÃO"""

s = input("Digite algo: ") 
s = s.upper() 

# Verifica se a string é igual a "SIM" em letras maiúsculas
if s == "SIM":
    print("SIM")
else:
    print("NÃO")


"""Até este ponto você já conhece muito bem a função print(). É algo muito divertido que podemos fazer em python e desenhar padrões. Desenhe o seguinte padrão e lembre-se que a solução deve incluir os loops que você aprendeu.

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*

"""

# coloque o seu código aqui

for i in range(1, 6):
    print("* " * i)

for i in range(4, 0, -1):
    print("* " * i)


""" Estamos testando um novo sistema de verificação de segurança, para o qual o usuário
    deve digitar sua senha e digitar um código de verificação, para o qual ele tem 3 tentativas,
    se falhar nas três tentativas, devemos imprimir Sua conta foi bloqueada, em caso você insira
    os dados corretos nas três tentativas que tiver, imprimiremos Seus dados foram verificados,
    use a função de entrada para que o usuário insira sua senha e seu código de verificação"""

password = "!@123"
verification_code = "9898"
tentativas = 0

while tentativas < 3:
    psw = input("Digite a sua senha: ")
    vr_code = input("Digite o código de verificação: ")
    if psw == password and vr_code == verification_code:
        print("Seus dados foram verificados!")
        break
    else:
        tentativas += 1
        if tentativas == 3:
            print("Sua conta foi bloqueada!")
        else:
            print("Senha ou código de verificação incorretos. Tentativas restantes:", 3 - tentativas)

