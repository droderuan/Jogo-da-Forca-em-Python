from re import search

class ValidarPalavra(object):

    '''@staticmethod tambem pode ser usado sozinho para definir como metodo estatico
       com @classmethod, deve ser posto e primeiro argumento deve ser cls'''
    @classmethod
    def Verificar(cls, word):
        if search(r'\d|\W', word):
            return False
        else:
            return True

    @classmethod
    def VerificarLetra(cls, word):
        if search(r'\d|\W', word) or len(word)>1:
            return False
        else:
            return True