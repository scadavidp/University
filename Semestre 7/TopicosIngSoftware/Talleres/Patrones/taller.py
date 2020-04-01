#!/usr/bin/env python3

from abc import ABCMeta, abstractstaticmethod
import json
import pymongo

connectionString = "mongodb+srv://scadavidp:asdf1234@cluster0-v8ta5.mongodb.net/test?retryWrites=true&w=majority"

basedb = pymongo.MongoClient(connectionString)
db = basedb.DBTallerPatrones
tipoItemsDB = db.TipoItems
itemsDB = db.Ttems
clientesDB = db.Clientes
facturasDB = db.Facturas

#Factory method para tipo items
class ItemType(metaclass=ABCMeta):
    @abstractstaticmethod
    def getItemTypeObj():
        """pass aka hacer algo"""
    
    @abstractstaticmethod
    def getItemType(self):
        """return el tipo aka descripcion que es mas facil categoria"""
        

class Electrodomestico(ItemType):
    typeObj = {}
    global tipoItemsDB
    def __init__(self):
        self.idType = 1
        self.descripcionType = "Electrodomestico"
        typeObj = {'Id Type': self.idType, 'Descripcion Type': self.descripcionType}
        x = tipoItemsDB.insert_one(typeObj)
        
    def getItemTypeObj(self):

        return json.dumps({'Id Type': self.idType, 'Descripcion Type': self.descripcionType})
    
    def getItemType(self):
        return str(self.descripcionType)
    
class Tecnologia(ItemType):
    typeObj = {}
    global tipoItemsDB
    def __init__(self):
        self.idType = 2
        self.descripcionType = "Tecnologia"
        typeObj = {'Id Type': self.idType, 'Descripcion Type': self.descripcionType}
        x = tipoItemsDB.insert_one(typeObj)

    def getItemTypeObj(self):
        return json.dumps({'Id Type': self.idType, 'Descripcion Type': self.descripcionType})
    
    def getItemType(self):
        return str(self.descripcionType)

class Ropa(ItemType):
    typeObj = {}
    global tipoItemsDB
    def __init__(self):
        self.idType = 3
        self.descripcionType = "Ropa"
        typeObj = {'Id Type': self.idType, 'Descripcion Type': self.descripcionType}
        x = tipoItemsDB.insert_one(typeObj)

    def getItemTypeObj(self):
        return json.dumps({'Id Type': self.idType, 'Descripcion Type': self.descripcionType})
    
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


#Cliente
class Cliente():
    def __init__(self, id, nombre, apellidos, genero, fechaNacimiento, estadoCivil):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.genero = genero
        self.fechaNacimiento = fechaNacimiento
        self.estadoCivil = estadoCivil
    #pass

    #Setters  
    def setId(self, id):
        self.id = id
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setApellidos(self, apellidos):
        self.apellidos = apellidos
    
    def setGenero(self, genero):
        self.genero = genero
    
    def setFechaNacimiento(self, fechaNacimiento):
        self.fechaNacimiento = fechaNacimiento
    
    def setEstadoCivil(self, estadoCivil):
        self.estadoCivil = estadoCivil

    #Getters
    def getId(self):
        return self.id
    
    def getNombre(self):
        return self.nombre
    
    def getApellidos(self):
        return self.apellidos

    def getGenero(self):
        return self.genero
    
    def getFechaNacimiento(self):
        return self.fechaNacimiento

    def getEstadoCivil(self):
        return self.estadoCivil

    def getDatosCliente(self):
        datos = {
            'id' : self.id,
            'nombre': self.nombre,
            'apellidos':self.apellidos,
            'genero': self.genero,
            'fecha de nacimiento': self.fechaNacimiento,
            'estado civil' : self.estadoCivil
        }
        #return json.dumps(datos)
        """datos = {}
        datos['id']= self.id
        datos['nombre'] = self.nombre
        datos['apellidos'] = self.apellidos
        datos['genero'] = self.genero
        datos['fecha de nacimiento'] = self.fechaNacimiento
        datos['estado civil'] = self.estadoCivil"""

        return datos

class ClienteDao(metaclass=ABCMeta):
    @abstractstaticmethod
    def getClientes():
        pass

    @abstractstaticmethod
    def updateCliente():
        pass

    @abstractstaticmethod
    def deleteCliente():
        pass

    @abstractstaticmethod
    def addCliente():
        pass

clientes = []
class ClienteBD(ClienteDao):
    global clientes
    global clientesDB
    
    
    """def __init__(self):
        self.clientes = lista"""

    def getClientes(self):
        lista = []
        """for cliente in clientes:
            lista.append(cliente.getDatosCliente())"""
        for x in clientesDB.find():
            #print(x)
            lista.append(x)
        #print(lista)     
        return lista
    
    def updateCliente(self, c):
        """for cliente in clientes:
            if cliente.getId() == c.getId():
                cliente.setNombre(c.getNombre())
                cliente.setApellidos(c.getApellidos())
                cliente.setGenero(c.getGenero())
                cliente.setFechaNacimiento(c.getFechaNacimiento())
                cliente.setEstadoCivil(c.getEstadoCivil())
                break"""
        for cliente in clientesDB.find():
            if cliente['id'] == c.getId():
                newValues = {"$set": c.getDatosCliente()}
                clientesDB.update_one(cliente, newValues)
        
    def deleteCliente(self, cliente):
        """for i in range (len(clientes) -1):
            if clientes[i].getId() == cliente:
                clientes.remove(clientes[i])
                break"""
        for c in clientesDB.find():
            if c['id'] == cliente:
                clientesDB.delete_one(c)
    
    def addCliente(self, cliente):
        clientes.append(cliente)
        x=clientesDB.insert_one(cliente.getDatosCliente())


    
    
        



if __name__ == "__main__":
    #test de fabrica de Tipo items 
    """print("Que tipo de item quiere crear \nElectrodomestico, Tecnologia o Ropa:")
    tipo = input()
    tipoItem = factoryItemType.getTipoItem(str(tipo))
    print(tipoItem.getItemTypeObj())"""

    #test fabrica Items:
    """print("Que tipo de item quiere crear \nNevera, Computador o Camisa:")
    item = input()
    newItem = ItemFactory.getItem(item)
    print(newItem.getItemsInfo())"""

    #test dao clientes
    """database = ClienteBD()

    c1 = Cliente(1, "jose", "algo", "hombre", "12345", "soltero")
    c2 = Cliente(2, "alfredo", "algd2", "hombre", "1643", "casado")
    c3 = Cliente(3, "maria", "algo3", "mujer", "12535", "soltera")

    print(database.getClientes())

    database.addCliente(c1)
    database.addCliente(c2)
    database.addCliente(c3)

    print(database.getClientes())

    c2.setNombre("Pedro")
    c2.setEstadoCivil("soltero")
    database.updateCliente(c2)

    print(database.getClientes())

    database.deleteCliente(1)

    print(database.getClientes())"""

    #test dao pero con Mongo
    c1 = Cliente(1, "jose", "algo", "hombre", "12345", "soltero")
    c2 = Cliente(2, "alfredo", "algd2", "hombre", "1643", "casado")
    c3 = Cliente(3, "maria", "algo3", "mujer", "12535", "soltera")

    database = ClienteBD()
    database.addCliente(c1)
    database.addCliente(c2)
    database.addCliente(c3)
    print(database.getClientes())

    c2.setNombre("Pedro")
    c2.setEstadoCivil("soltero")
    database.updateCliente(c2)
    print("Base de datos despues de la actualizacion del cliente" + str(c2.getId()))
    print(database.getClientes())

    #database = ClienteBD()
    database.deleteCliente(1)
    database.deleteCliente(2)
    database.deleteCliente(3)
    print(database.getClientes())
