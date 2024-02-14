class fruits:
    def __init__(self,name,price,colour):
        self.name=name
        self.price=price
        self.colour=colour
    def onyesha (self):
        print(f"my favourite fruit is the {self.name}"
              f" , it costs ksh.{self.price}"
              f" and its {self.colour} in colour")
myobj=fruits("appple",30 , "red",)
myobj.onyesha()

myobj2=fruits("mango",340 , "yellow",)
myobj2.onyesha()
