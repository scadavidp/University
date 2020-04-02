#!/usr/bin/env python3

from abc import ABCMeta, abstractstaticmethod
import json
import pymongo
from datetime import date

connectionString = "mongodb+srv://scadavidp:asdf1234@cluster0-v8ta5.mongodb.net/test?retryWrites=true&w=majority"

basedb = pymongo.MongoClient(connectionString)
db = basedb.DBTallerPatrones
tipoItemsDB = db.TipoItems
itemsDB = db.Items
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
        i = itemsDB.insert_one(informacion)
        return ("El item: " + self.descripcion + "Ha sido guardado con exito")
        #return json.dumps(informacion)

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
        i = itemsDB.insert_one(informacion)
        return ("El item: " + self.descripcion + "Ha sido guardado con exito")
        #return json.dumps(informacion)

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
        i = itemsDB.insert_one(informacion)
        return ("El item: " + self.descripcion + "Ha sido guardado con exito")
        # return json.dumps(informacion)

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
        
    def deleteCliente(self, idcliente):
        """for i in range (len(clientes) -1):
            if clientes[i].getId() == cliente:
                clientes.remove(clientes[i])
                break"""
        for c in clientesDB.find():
            if c['id'] == idcliente:
                clientesDB.delete_one(c)
    
    def addCliente(self, cliente):
        if clientesDB.count() != 0:
            for c in clientesDB.find():
                if c['id'] == cliente.getId():
                    raise Exception ("Este cliente ya fue añadido")
                else:
                    clientes.append(cliente)
                    x=clientesDB.insert_one(cliente.getDatosCliente())
        else:
            clientes.append(cliente)
            x=clientesDB.insert_one(cliente.getDatosCliente())

        
"""
class Factura(object):
    facturaResumen = {}
    """"""def __init__(self, nroFactura, fechaFactura, cliente, totalFactura, estado, items):
        self.nroFactura = nroFactura
        self.fechaFactura = fechaFactura
        self.cliente = cliente
        self.totalFactura = totalFactura
        self.estado = estado
        self.items = items
        crearFactura(facturaResumen)""""""

    def crearFactura(self):
        facturaResumen['nroFactura'] = self.nroFactura
        facturaResumen['fechaFactura'] = self.fechaFactura
        facturaResumen['cliente'] = self.cliente.getDatosCliente()
        facturaResumen['totalFactura'] = self.totalFactura
        facturaResumen['estado'] = self.estado
        facturaResumen['items'] = self.items
        f=facturasDB.insert_one(facturaResumen)
        return facturaResumen
    
    def __init__(self, nroFactura, fechaFactura):
        self.nroFactura = 0
        self.fechaFactura = ""
        self.cliente = {}
        self.totalFactura = 0
        self.estado = "Pendiente"
        self.items = []
        #crearFactura(facturaResumen)
    
    def setCliente(self, cliente):
        self.cliente = cliente
    
    def addItems(self,item):
        self.items.append(item)
    
    def getItemsFactura(self):
        return self.items
    
    def getTotalFactura(self):
        total = self.totalFactura
        totalItems = getItemsFactura()
        for item in totalItems:
            total += float(item.valorUnidad)
        self.totalFactura = total
        #return total
    
    def getFacturaResumen(self):
        return facturaResumen
"""



"""        
class App:
    
    clienteFactura = {}


    def imprimirFactura(self, factura):
        factura.getTotalFactura()
        factura.crearFactura()
        print(json.dump(factura.getFacturaResumen()))


    def agregarItems(self, factura):
        print("desea añadir items a la factura, (ingrese si o no)")
        r = input()
        while(r=="si"):
            print("Ahora añada los items a la factura:")
            for item in itemsDB:
                print(item.getItemsInfo())
                print("Ingrese el id del item que desea añadir a la factura")
                idItem = input()
                print("Cuantas unidades")
                unidadesItem = input()
                for it in itemsDB.find_one():
                    if it['id'] == idItem:
                        for i in range(unidadesItem):
                            factura.addItems(it)
            print("desea añadir mas items a la factura, (ingrese si o no)")
            r == input()
        
                

        

    def crearNuevaFactura(self, factura):
        print("Cual es el cliente, ingrese el id del cliente")
        cid = input()
        for c in clientesDB.find_one():
            if c['id'] == cid:
                clienteFactura = c
                factura.addCliente(clienteFactura)
                break
        agregarItems(factura)
        imprimirFactura(factura)
        

            
    nro = 0
    newFactura = object
    print("Desea crear una nueva factura, para si ingrese si para no ingrese no, escriba cerrar para cerrar el programa")
    respuesta = input()
    while(respuesta != 'cerrar'):
        nro+=1
        if respuesta == "si":
            #ejecucion del programa
            newfactura = Factura(nro, date.today()) 
            crearNuevaFactura(newFactura)
        elif respuesta == "no":
            respuesta == 'cerrar'"""


class Factura():
    
    """def __init__(self, nroFactura, fechaFactura, cliente, totalFactura, estado, items):
        self.nroFactura = nroFactura
        self.fechaFactura = fechaFactura
        self.cliente = cliente
        self.totalFactura = totalFactura
        self.estado = estado
        self.items = items
        crearFactura(facturaResumen)"""

    def crearFactura(self):
        self.facturaResumen['nroFactura'] = self.nroFactura
        self.facturaResumen['fechaFactura'] = self.fechaFactura
        self.facturaResumen['cliente'] = self.cliente
        self.facturaResumen['totalFactura'] = self.totalFactura
        self.facturaResumen['estado'] = self.estado
        self.facturaResumen['items'] = self.items
        f=facturasDB.insert_one(self.facturaResumen)
        return self.facturaResumen
    
    def __init__(self, nroFactura):
        self.nroFactura = nroFactura
        self.fechaFactura = date.today().strftime("%d/%m/%Y")
        self.cliente = {}
        self.totalFactura = {}
        self.estado = "Pendiente"
        self.items = []
        self.facturaResumen = {}
        #crearFactura(facturaResumen)
    
    def setCliente(self, cliente):
        self.cliente = cliente
    
    def addItems(self,item):
        self.items.append(item)
    
    def getItemsFactura(self):
        return self.items
    
    def getTotalFactura(self):
        total = self.totalFactura
        for item in self.items:
            total += float(item.valorUnidad)
        self.totalFactura = total
        #return total
    
    def getFacturaResumen(self):
        return self.facturaResumen

    clienteFactura = {}


    def imprimirFactura(self):
        self.getTotalFactura()
        self.crearFactura()
        print(self.getFacturaResumen())


    def agregarItems(self):
        print("desea añadir items a la factura, (ingrese si o no)")
        r=input()
        while(r=="si"):
            print("Ahora añada los items a la factura:")
            for item in itemsDB.find():
                print(item)

            print("Ingrese el id del item que desea añadir a la factura")
            idItem = input()
            print("Cuantas unidades")
            unidadesItem = int(input())
            for it in itemsDB.find():
                if it['id'] == idItem:
                    for i in range(unidadesItem):
                        self.addItems(it)
            print(self.items)            
            print("desea añadir mas items a la factura, (ingrese si o no)")
            r=input()
            
        

    def crearNuevaFactura(self):
        print("Cual es el cliente, ingrese el id del cliente")
        cd = input()
        cid=int(cd)
        for cliente in clientesDB.find():
            if cliente['id'] == cid:
                clienteFactura = cliente
                self.setCliente(clienteFactura)
                break
        self.agregarItems()
        self.imprimirFactura()
   



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
    """c1 = Cliente(1, "jose", "algo", "hombre", "12345", "soltero")
    c2 = Cliente(2, "alfredo", "algd2", "hombre", "1643", "casado")
    c3 = Cliente(3, "maria", "algo3", "mujer", "12535", "soltera")"""
                                                                    
    """database = ClienteBD()
    database.addCliente(c1)
    database.addCliente(c2)
    database.addCliente(c3)
    print(database.getClientes())

    c2.setNombre("Pedro")
    c2.setEstadoCivil("soltero")
    database.updateCliente(c2)
    print("Base de datos despues de la actualizacion del cliente" + str(c2.getId()))
    print(database.getClientes())
"""
    """database = ClienteBD()
    database.deleteCliente(c1)
    database.deleteCliente(c2)
    database.deleteCliente(c3)
    print(database.getClientes())"""
    #----------------------------------------------------------------------------------------
    #APP
    #Prueba ejecucion programa
    #1 Crear tipos de items Done 
    """tipoItem = factoryItemType.getTipoItem("Electrodomestico")
    
    tipoItem = factoryItemType.getTipoItem("Tecnologia")
    
    tipoItem = factoryItemType.getTipoItem("Ropa")


    for x in tipoItemsDB.find():
        print(x)"""

    #2 Crear items: Done
    """newItem1 = ItemFactory.getItem("Nevera")
    newItem1.guardarItem()
    newItem2 = ItemFactory.getItem("Computador")
    newItem2.guardarItem()
    newItem3 = ItemFactory.getItem("Camisa")
    newItem3.guardarItem()
    for x in itemsDB.find():
        print(x)"""

    #3 Crear usuarios: Done
    """c1 = Cliente(1, "jose", "algo", "hombre", "12345", "soltero")
    c2 = Cliente(2, "alfredo", "algd2", "hombre", "1643", "casado")
    c3 = Cliente(3, "maria", "algo3", "mujer", "12535", "soltera")

    database = ClienteBD()
    database.addCliente(c1)
    database.addCliente(c2)
    database.addCliente(c3)
    print(database.getClientes())"""

    #4 Crear Factura
    nro = 0
    print("Desea crear una nueva factura, para si ingrese si para no ingrese no, escriba cerrar para cerrar el programa")
    respuesta = input()
    while(respuesta != 'cerrar'):
        nro+=1
        if respuesta == "si":
            #ejecucion del programa
            newfactura = Factura(nro) 
            newfactura.crearNuevaFactura()
        elif respuesta == "no":
            respuesta = 'cerrar'
