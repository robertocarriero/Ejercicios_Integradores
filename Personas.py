class Persona():
    def __init__(self, nombre='', edad=0, dni=0):
        self._nombre=nombre
        self._edad=edad
        self._dni=dni
        
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre=nombre
        
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, edad):
        self._edad=edad
        
    @property
    def dni(self):
        return self._dni
    
    @dni.setter
    def dni(self,dni):
        self._dni=dni
        
    def mostrar(self):
        print('El nombre del cliente es:')
        print(f'{self._nombre}')
        print(f'Su N° de DNI es: {self._dni}')
        print(f'Su edad es :{self._edad}')
        
    def Es_mayor_de_edad(self):
        if self._edad >= 18:
            print(f'{True}, Usted es mayor de edad')
            
        else:
            print(False)
            
    def validarNombre(self):
        if self._nombre==():
            print('Por favor ingrese un nombre')
        elif self._nombre==(''):
            print('Por favor ingrese un nombre valido')
        elif self._nombre!=str:
            print('Por favor ingrese un nombre valido')
        else:
            print('ha ingresado el nombre correcto')
            
    def validarEdad(self):
        if self._edad >0 and self._edad<120 :
            print(f'Su edad de {self._edad} años, está correcta')
        else:
            print(f'Su edad de {self._edad}, no es valida')
            
    def validarDocumento(self):
        if type(self._dni)!=int or (self._dni)<=0 or (self._dni)>100000000 or(self._dni)==():
            raise ValueError(f'El N° documento:{self._dni} que ha ingresado no es válido')
        else:
            print(f'El N° documento {self._dni} que ha ingresado es válido')
        
#cliente1 = Persona('pepe', 63, 12345543)


















