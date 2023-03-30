#Exercício

""" Os alunos devem incrementar o código com variáveis e métodos
    se acharem necessário e, ao final, imprimir na tela todo o histórico
    do aluno com todas as notas e médias, inclusive informando se o status
    do aluno foi: "aprovado por média", "aprovado na final" ou "reprovado".
    consideram que a média aritimética para aprovação é 7,0 (sete) e após final 5,0 (cinco) """

class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.notas = []
        self.media = 0
        self.situacao = ""
    
    def adicionar_nota(self, nota):
        self.notas.append(nota)
    
    def calcular_media(self):
        if len(self.notas) > 0:
              self.media = round(sum(self.notas) / len(self.notas))
        else:
            self.media = 0
        
        return self.media
    
    def verificar_situacao(self):
        if self.media >= 7:
            self.situacao = "aprovado por média"
        elif self.media >= 5:
            self.situacao = "aprovado na final"
        else:
            self.situacao = "reprovado"
        
        return self.situacao
    
    def imprimir_historico(self):
        print("Histórico de notas de", self.nome)
        for nota in self.notas:
            print("- Nota:", nota)
        
        self.calcular_media()
        self.verificar_situacao()
        print("Média:", self.media)
        print("Situação:", self.situacao)
aluno1 = Aluno("João")

# adicionando notas
aluno1.adicionar_nota(8)
aluno1.adicionar_nota(7.5)
aluno1.adicionar_nota(6)

# imprimindo o histórico
aluno1.imprimir_historico()