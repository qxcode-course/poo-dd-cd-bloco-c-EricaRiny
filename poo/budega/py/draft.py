class Person:

    def __init__(self, name:str):
        self.__name:str = name

    def __str__(self):
        return f"{self.__name}"
    
class Market:

    def __init__(self, counterCount: int):
        self.__counterCount:int = counterCount
        self.__counters:list[Person|None] = []
        self.__queue:list[Person|None] = []

        for counter in range(counterCount):
            self.__counters.append(None)

    def __str__(self):
        counters = ", ".join(["-----" if counter is None else str(counter) for counter in self.__counters])
        queue = ", ".join([str(queue) for queue in self.__queue])
        return f"Caixas: [{counters}]\nEspera: [{queue}]"

    def arrive(self, pessoa:Person):
        self.__queue.append(pessoa)

    def call(self, index:int):
        if self.__counters[index] != None:
            print("fail: caixa ocupado")
            return 
        if not self.__queue:
            print("fail: sem clientes")
            return 
       
        self.__counters[index] = self.__queue[0]
        self.__queue.pop(0)

    def finish(self, index:int):
        if index >= self.__counterCount:
            print("fail: caixa inexistente")
            return 
        elif self.__counters[index] == None:
            print("fail: caixa vazio")
            return
        self.__counters[index] = None
        
    def show(self):
        print(self)

def main():
    person = Person(" ")
    market = Market(0)

    while True:

        linha = input()
        arg:list[str] = linha.split(" ")
        print("$" + linha)

        if arg[0] == "end":
            break
        elif arg[0] == "init":
            counterCount:int = int(arg[1])
            market = Market(counterCount)
        elif arg[0] == "show":
            market.show()
        elif arg[0] == "arrive":
            nome: str = arg[1]
            pessoa = Person(nome)
            market.arrive(pessoa)
        elif arg[0] == "call":
            index:int = int(arg[1])
            market.call(index)
        elif arg[0] == "finish":
            index:int = int(arg[1])
            market.finish(index)
main()