from ValidarPalavra import ValidarPalavra as vp

class Palavra(object):

    def __init__(self):
        self.word = self.Setword()
        self.tentativas = []
        self.acertos = [[0 for x in range(2)] for y in range(len(self.word))]
        for x in range(len(self.word)):
            self.acertos[x][0] = x

    def Setword(self):
        palavra = str(input("Digite a palavra para adivinharem: ")).lower()
        print("Palavra aceita!") if vp.Verificar(palavra) else print("Palavra invalida")
        return palavra

    def receber_letra(self):
        acerto = False
        letra = str(input("Digite uma letra: ")).lower()
        if vp.VerificarLetra(letra):
            acerto = self.verificar_acerto(letra, acerto)
            if not letra in self.tentativas:
                self.tentativas.append(letra)
            return acerto
        else:
            print("Digito invalido")

    def verificar_acerto(self, letra, acerto):
        if letra in self.word and not letra in self.tentativas:
            print("Contem!!\n")
            self.acertos[self.word.index(letra)][1] = letra
            return True

    def ExibirAcertosErros(self):
        print("\nAcertos: ", end='')
        for letra in self.word:
            if letra == self.acertos[self.word.index(letra)][1]:
                print(letra, end=' ')
            else:
                print("_", end=" ")
        print('\nTentativas:', end=' ')
        for letra in self.tentativas:
            print(letra, end=' ')
        print('\n')

    def Ganhar(self):
        acerto = 0
        for letra in self.word:
            if letra == self.acertos[self.word.index(letra)][1]:
                acerto += 1
        if acerto == len(self.word):
            return True