class Lead:

    def __init__(self, calibre: float, dureza:str, tamanho: int):
        self.__calibre: float = calibre
        self.__dureza: str = dureza
        self.__tamanho: int = tamanho
        
    def getCalibre(self):
        return self.__calibre
    
    def getDureza(self):
        return self.__dureza
    
    def getTamanho(self):
        return self.__tamanho
    
    def __str__(self):
        return f"{self.__calibre}:{self.__dureza}:{self.__tamanho}"
    
    def usePS(self):
        if self.__dureza == "HB":
            self.__tamanho -= 1
        elif self.__dureza == "2B":
            self.__tamanho -= 2
        elif self.__dureza == "4B":
            self.__tamanho -= 4
        elif self.__dureza == "6B":
            self.__tamanho -= 6
        if self.__tamanho < 10:
            self.__tamanho = 10
            print("fail: folha incompleta")

class Pencil:

    def __init__(self, calibre: int):
        self.__calibre:float = calibre
        self.__bico:Lead | None = None
        self.__tambor: list[Lead | None] = []


    def __str__(self):
        bico = str(self.__bico) if self.__bico is not None else ""
        tambor = "<" + "".join([f"[{str(x)}]" for x in self.__tambor]) + ">"
        return f"calibre: {self.__calibre}, bico: [{bico}], tambor: {tambor}"

    def show(self):
        print(self)


    def insert(self, lead:Lead):
        if lead.getCalibre() != self.__calibre:
            print("fail: calibre incompatível")
        else:
            self.__tambor.append(lead)

    def pull(self):
            if self.__bico != None:
                print("fail: ja existe grafite no bico")
                return 
            self.__bico = self.__tambor[0]
            self.__tambor.pop(0)

    def remove(self):
        self.__bico = None

    def write(self):
        if self.__bico == None:
            print("fail: nao existe grafite no bico")

        elif self.__bico.getTamanho() > 10:
            self.__bico.usePS()

        elif self.__bico.getTamanho() <= 10:
            print("fail: tamanho insuficiente")
            self.__bico = None
            
def main():
    lead = Lead(0," ", 0)
    pencil = Pencil(0)

    while True:
        linha = input()
        arg:list[str] = linha.split(" ")
        print("$" + linha)

        if arg[0] == "end":
            break
        elif arg[0] == "show":
            pencil.show()
        elif arg[0] == "init":
            calibre:float = float(arg[1])
            pencil = Pencil(calibre)
        elif arg[0] == "insert":
            calibre:float = float(arg[1])
            dureza:str = arg[2]
            tamanho:int = int(arg[3])
            lead = Lead(calibre, dureza, tamanho)
            pencil.insert(lead)
        elif arg[0] == "pull":
            pencil.pull()
        elif arg[0] == "remove":
            pencil.remove()
        elif arg[0] == "write":
            pencil.write()
main()