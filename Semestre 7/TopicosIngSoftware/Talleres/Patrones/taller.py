from abc import ABCMeta, abstractstaticmethod
import json

#Factory method para tipo items
class ItemType(metaclass=ABCMeta):
    @abstractstaticmethod
    def getItemTypeObj():
        """pass aka hacer algo"""
    
    @abstractstaticmethod
    def getItemType(self):
        """return el tipo aka descripcion que es mas facil categoria"""
        

class Electrodomestico(ItemType):
    def __init__(self):
        self.idType = 1
        self.descripcionType = "Electrodomestico"

    def getItemTypeObj(self):
        return {'Id Type': self.idType, 'Descripcion Type': self.descripcionType}
    
    def getItemType(self):
        return str(self.descripcionType)
    
class Tecnologia(ItemType):
    def __init__(self):
        self.idType = 2
        self.descripcionType = "Tecnologia"

    def getItemTypeObj(self):
        return {'Id Type': self.idType, 'Descripcion Type': self.descripcionType}
    
    def getItemType(self):
        return str(self.descripcionType)

class Ropa(ItemType):
    def __init__(self):
        self.idType = 3
        self.descripcionType = "Ropa"

    def getItemTypeObj(self):
        return {'Id Type': self.idType, 'Descripcion Type': self.descripcionType}
    
    def getItemType(self):
        return str(self.descripcionType)

class factoryItemType():

    @staticmethod
    def getTipoItem(tipoitem):
        try:
            if tipoitem == 'Electrodomestico' or tipoitem == 'electrodomestico':
                return Electrodomestico()
            elif tipoitem == 'Tecnologia' or tipoitem == 'tecnologia':
                return Tecnologia()
            elif tipoitem == 'Ropa' or tipoitem == 'ropa':
                return Ropa()
            else:
                raise Exception("Este tipo de item no existe")
        except Exception as err:
            print(err)



#Factory method para Items:
class Items(metaclass=ABCMeta):
    @abstractstaticmethod
    def getItemsInfo():
        """hacer algo, retornar toda la informacion del Item"""
    
    @abstractstaticmethod
    def guardarItem():
        """se debe almacenar en una BD"""

class Nevera(Items):
    def __init__(self, descripcion, valorUnidad):
        self.tipoItem = "Electrodomestico"
        self.id = 1
        self.descripcion = descripcion
        self.valorUnidad = valorUnidad
    
    def getItemsInfo(self):
        info = "{} con un valor de:  {} USD\nCategoria: {}\nId: {}"
        return info.format(self.descripcion, self.valorUnidad, self.tipoItem, self.id)
    
    def guardarItem(self):
        informacion = {
            'tipo Item' : self.tipoItem,
            'id' : self.id,
            'descripcion' : self.descripcion,
            'valor unidad' : self.valorUnidad
        }
        return json.dumps(informacion)

class Computador(Items):
    def __init__(self, descripcion, valorUnidad):
        self.tipoItem = "Tecnologia"
        self.id = 2
        self.descripcion = descripcion
        self.valorUnidad = valorUnidad
    
    def getItemsInfo(self):
        info = "{} con un valor de:  {} USD\nCategoria: {}\nId: {}"
        return info.format(self.descripcion, self.valorUnidad, self.tipoItem, self.id)
    
    def guardarItem(self):
        informacion = {
            'tipo Item' : self.tipoItem,
            'id' : self.id,
            'descripcion' : self.descripcion,
            'valor unidad' : self.valorUnidad
        }
        return json.dumps(informacion)

class Camisa(Items):
    def __init__(self, descripcion, valorUnidad):
        self.tipoItem = "Ropa"
        self.id = 3
        self.descripcion = descripcion
        self.valorUnidad = valorUnidad
    
    def getItemsInfo(self):
        info = "{} con un valor de:  {} USD\nCategoria: {}\nId: {}"
        return info.format(self.descripcion, self.valorUnidad, self.tipoItem, self.id)
    
    def guardarItem(self):
        informacion = {
            'tipo Item' : self.tipoItem,
            'id' : self.id,
            'descripcion' : self.descripcion,
            'valor unidad' : self.valorUnidad
        }
        return json.dumps(informacion)

class ItemFactory():
    @staticmethod
    def getItem(tipoitem):
        try:
            if tipoitem == 'Nevera' or tipoitem == 'nevera':
                print("Ingrese la descripcion de la nevera: ")
                descripcion = input()
                print("Ingrese el valor de la nevera: ")
                valor = input()
                return Nevera(descripcion, valor)
            elif tipoitem == 'Computador' or tipoitem == 'computador':
                print("Ingrese la descripcion del computador: ")
                descripcion = input()
                print("Ingrese el valor del computador: ")
                valor = input()
                return Computador(descripcion, valor)
            elif tipoitem == 'Camisa' or tipoitem == 'camisa':
                print("Ingrese la descripcion de la camisa: ")
                descripcion = input()
                print("Ingrese el valor de la camisa: ")
                valor = input()
                return Camisa(descripcion, valor)
            else:
                raise Exception("Este tipo de item no existe")
        except Exception as err:
            print(err)




if __name__ == "__main__":
    #test de fabrica de Tipo items 
    """
    print("Que tipo de item quiere crear \nElectrodomestico, Tecnologia o Ropa:")
    tipo = input()
    tipoItem = factoryItemType.getTipoItem(tipo)
    print(tipoItem.getItemTypeObj())  """
    #test fabrica Items:
    print("Que tipo de item quiere crear \nNevera, Computador o Camisa:")
    item = input()
    newItem = ItemFactory.getItem(item)
    print(newItem.getItemsInfo())
