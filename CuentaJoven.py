from Cuenta import Cuenta

class CuentaJoven(Cuenta):
    def __init__(self, titular='', cantidad=0, bonificacion=0):
        super().__init__(titular, cantidad)
        self._bonificacion=bonificacion
        self._titular=titular
        self._cantidad=cantidad
        
    @property
    def titular(self):
        return super().titular
    @titular.setter
    def titular(self,titular):
        self._titular=titular
        
    @property
    def cantidad(self):
        return super().cantidad
    
    @cantidad.setter
    def cantidad(self,cantidad):
        self._cantidad=cantidad
    
    @property
    def bonificacion(self):
        return self._bonificacion
    
    @bonificacion.setter
    def bonificacion(self,bonificacion):
        self._bonificacion = bonificacion
        
    def es_titular_valido(self):
        int(input('Ingrese su edad:'))
        if self._edad >=18 and self._edad <=25:
            print(True)
        else:
            print(False)
            
    def porcentaje_bonificacion(self, porcentaje):
        bonificacion = self._cantidad*(porcentaje/100)
        print(f'La bonificación de {self._nombre} es: {bonificacion}')
    
    def retirar(self,cantidad):
        self._cantidad =self._cantidad - cantidad
        
    def validar_titular(self):
        nombre=input('Ingrese el nombre del titular: ')
        if nombre==self._titular:
            print('El titular es correcto')
        else:
            print('Nombre ingresado incorrecto')
        
    def mostrar(self):
        print('Cuenta joven')
        print (f'Titular : {self._titular}')
        print (f'Su cuenta tiene pesos: {self._cantidad}')
        print (f'La bonificación de su cuenta es : {self._bonificacion} %')
        

#cliente2 = CuentaJoven('Pepe Galleta', 240000, 10 )
