class Client:
    
    def __init__(self, id: str, phone: int):
        self.__id = id
        self.__phone = phone

    def getPhone(self):
        return self.__phone
    
    def getId(self):
        return self.__id
    
    def __str__(self):
        return f"{self.__id}:{self.__phone}"
    
    def show(self):
        print(self)

class Theater:
    
    def __init__(self, capacidade:int):
        self.lugares: list[Client | None] = []
        self.capacidade:int = capacidade

        for _ in range(capacidade):
            self.lugares.append(None)
    
    def __str__(self):

        lugares = " ".join(["-" if x is None else str(x) for x in self.lugares])
        return f"[{lugares}]"

    def show(self):
        print(self)

    def reserve(self, cliente:Client, index:int):
        if index>self.capacidade:
            print("fail: cadeira nao existe")
            return 
        elif self.lugares[index] != None:
            print("fail: cadeira ja esta ocupada")
            return
        for i in self.lugares: 
           if i != None and cliente.getId() == i.getId():
               print("fail: cliente ja esta no cinema")
               return
           
        self.lugares[index] = cliente

    def cancel(self, id:str):

        for i, cliente in enumerate(self.lugares):
            if cliente != None and cliente.getId() == id:
                self.lugares[i] = None
                break
            else:
                print("fail: cliente nao esta no cinema")
                break
            
def main(): 
    theater = Theater(0)
    cliente = Client(" ", 0)
    
    while True:
        linha = input()
        args: list[str] = linha.split(" ")
        print("$" + linha)

        if args[0] == "end":
            break
        elif args[0] == "show":
            theater.show()
        elif args[0] == "init":
            capacidade:int = int(args[1])
            theater = Theater(capacidade)
        elif args[0] == "reserve":
            nome:str = args[1]
            phone:int = int(args[2])
            index: int = int(args[3])
            cliente= Client(nome, phone)
            theater.reserve(cliente, index)
        elif args[0] == "cancel":
            id:str = args[1]
            theater.cancel(id)

main()