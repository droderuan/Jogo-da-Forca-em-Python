from Palavra import Palavra
from Menu import Menu
import subprocess as sp

while(True):
    tentativa = 0
    Menu.MenuInicial()
    try:
        opcao = int(input("\n"))
    except ValueError:
        print("opcao invalida")
    else:
        if opcao == 1:
            jogo = Palavra()
            while tentativa < 6:
                sp.call('cls', shell=True)
                jogo.ExibirAcertosErros()
                print("Restam %d tentativas" % (6-tentativa))
                if not jogo.receber_letra():
                    tentativa += 1
                if jogo.Ganhar():
                    Menu.Ganhou()
                    sp.call('cls', shell=True)
                    break
                if tentativa == 6:
                    Menu.Perdeu()
                    sp.call('cls', shell=True)
        elif opcao == 2:
            break