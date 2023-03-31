# Dado um inteiro n, determine se o número é par ou ímpar, se for par, imprima "O número é par" ou "The number is even"
number = int(input("Digite um número: "))

if number %2 == 0:
  print(f"O numéro: {number} é Par")
else:
    print("The number is even")

""" Na classe a seguir, implemente o método get_weather,
    receba como parâmetro a temperatura do local em graus Fahrenheit
    imprima O clima é ideal para sair sem casaco se a temperatura for maior ou igual
    a 65 graus Fahrenheit , caso contrário, imprima Fique em casa, está frio lá fora
    antes de usar as condicionais converta esse valor para graus Celsius. """ 

class WeatherMachine:
    
    def get_weather(self, temperature):
        # Convert Fahrenheit to Celsius
        temperature_celsius = (temperature - 32) * 5/9
        
        if temperature_celsius >= 18.33:
            print("O clima é ideal para sair sem casaco")
        else:
            print("Fique em casa, está frio lá fora")
        
weather_machine = WeatherMachine()
weather_machine.get_weather(152)



"""O que faremos é implementar uma versão básica do jogo na próxima célula.
Você receberá duas entradas que serão player_1 e player_2 nessa ordem, por enquanto
considere que você só pode inserir uma das opções válidas listadas acima, imprima quem
 ganhou com base nas regras e usando as condicionais que já aprendemos."""

def pedra_papel_tesoura_lagarto_spock(player_1, player_2):
    # Verifica se as entradas são válidas
    if player_1 not in ("pedra", "papel", "tesoura", "lagarto", "spock"):
        print("Entrada inválida para player_1")
        return
    if player_2 not in ("pedra", "papel", "tesoura", "lagarto", "spock"):
        print("Entrada inválida para player_2")
        return
    if player_1 == player_2:
        print("Empate!")
    elif (player_1 == "pedra" and (player_2 == "tesoura" or player_2 == "lagarto")) or \
         (player_1 == "papel" and (player_2 == "pedra" or player_2 == "spock")) or \
         (player_1 == "tesoura" and (player_2 == "papel" or player_2 == "lagarto")) or \
         (player_1 == "lagarto" and (player_2 == "papel" or player_2 == "spock")) or \
         (player_1 == "spock" and (player_2 == "pedra" or player_2 == "tesoura")):
        print("Player 1 venceu!")
    else:
        print("Player 2 venceu!")

pedra_papel_tesoura_lagarto_spock("pedra", "tesoura")