class Kid:

    def __init__(self, name:str, age: int):
        self.__name: str = name
        self.__age: int = age

    def __str__(self):
        return f"{self.__name}:{self.__age}"
    
    def getName(self):
        return self.__name
    
    def getAge(self):
        return self.__age
    
class Trampoline:

    def __init__(self):
        self.__playing:list[Kid|None] = []
        self.__waiting:list[Kid|None] = []

    def __str__(self):
        esperando = ", ".join([str(x) for x in self.__waiting])
        pulando = ", ".join([str(x) for x in self.__playing]) 
        return f"[{esperando}] => [{pulando}]"
    
    def arrive(self, kid: Kid):
        self.__waiting.insert(0, kid)

    def enter(self):
        self.__playing.insert(0, self.__waiting.pop())

    def leave(self):
        if self.__playing == []:
            return 
        
        else:
            self.__waiting.insert(0, self.__playing.pop())
       
    def remove(self, nome:str):
        for kid in self.__playing:
            if kid.getName() == nome:
                self.__playing.remove(kid)
                return 
            
        for kid in self.__waiting:
            if kid.getName() == nome:
                self.__waiting.remove(kid)
                return 
            
        print(f"fail: {nome} nao esta no pula-pula")
        

    def show(self):
        print(self)

def main():
    kid = Kid(" ", 0)
    trampoline = Trampoline()

    while True:
        linha = input()
        arg:list[str] = linha.split(" ")
        print("$" + linha)

        if arg[0] == "end":
            break
        elif arg[0] == "show":
            trampoline.show()
        elif arg[0] == "arrive":
            name:str = arg[1]
            age:int = int(arg[2])
            kid = Kid(name, age)
            trampoline.arrive(kid)
        elif arg[0] == "enter":
            trampoline.enter()
        elif arg[0] == "leave":
            trampoline.leave()
        elif arg[0] == "remove":
            nome:str = arg[1]
            trampoline.remove(nome)
    
main()