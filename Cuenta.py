class Cuenta():
    
    def __init__(self, titular='', cantidad=0):
        self.__titular = titular
        self.__cantidad = cantidad
        
    @property
    def titular(self):
        return self.__titular
    
    @titular.setter
    def titular(self, titular):
        self.__titular=titular
        
    @property
    def cantidad(self):
        return self.__cantidad
    
    @cantidad.setter
    def cantidad(self,cantidad):
        self.__cantidad = cantidad
        
    def mostrar(self):
         print (f'Los datos de la cuenta son:')
         print (f'Titular : {self.__titular}')
         print (f'Su cuenta tiene pesos: {self.__cantidad}')
        
    def ingresar(self, cantidad):
        if cantidad >=0:
            self.__cantidad =self.__cantidad + cantidad
            print(f'El titular {self.__titular} a depositado la suma de : {self.__cantidad}')
            
    def retirar(self,cantidad):
        self.__cantidad =self.__cantidad - cantidad
        print(f'El titular: {self.__titular} a retirado la suma de: {self.__cantidad - cantidad}')
        
        
#cliente1 = Cuenta('Pepe Galleta', 0)





