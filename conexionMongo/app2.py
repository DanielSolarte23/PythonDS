import pymongo
import pymongo.errors

miconexion = pymongo.MongoClient("mongodb://localhost:27017")


#obtener acceso a la base de datos
baseDatos = miconexion["Tienda"]
print (type(baseDatos))

#crear objeto para acceder a la coleccion productos

productos  = baseDatos ["Productos"]
print (type(productos))

# tareas del club a la base de datos

def agregar():
    try:
        codigo = 21
        nombre = "botas"
        precio = 100000
        categoria = "calzado"
        producto = {
            "codigo": codigo,
            "nombre": nombre,
            "precio": precio,
            "categoria": categoria
        }
        resultado = productos.insert_one(producto)
        if(resultado.acknowledged):
            print(f'producto agregado correctamente con id {resultado.inserted_id}')
    except pymongo.errors as error:
        print (str(error))
        
        
        
def consultarporCodigo ():
    try:
        codigoAConsultar = int (input("ingrese codigo del producto a consultar"))
        consulta = {"codigo":codigoAConsultar}
        producto = productos.find_one(consulta)
        if(producto):
            print(f"Codigo: {producto["codigo"]}")    
            print(f"nombre: {producto["nombre"]}")    
            print(f"precio: {producto["precio"]}")    
            print(f"categoria: {producto["categoria"]}") 
        else:
            print("no se encontro producto")   
    except pymongo.errors as error:
        print(str(error)) 
        
        
        
def listar():
    try:
        listaproductos = productos.find()
        if (len(listaproductos>0)):
            for p in listaproductos:
                print(f"Codigo: {p["codigo"]}")    
                print(f"nombre: {p["nombre"]}")    
                print(f"precio: {p["precio"]}")    
                print(f"categoria: {p["categoria"]}") 
                print ("*" * 50)
        else:
            print("no hay prodcutos")
    except pymongo.errors as error:
        print(str(error)) 
        
    
    
def actualizar () :
    try:
        criterio = {"codigo":10}
        datosAactualizar = {
            "precio": 90000,
            "nombre":"panta" 
        }
        consulta = {"$set":datosAactualizar}
        resultado = productos.update_one(criterio,consulta)
        if( resultado.acknowledged):
            print("no exite producto con ese codigo")
    except pymongo.errors as error:
        print(str(error)) 
        
        
        
def eliminar ():
    try:
        criterio = {"codigo":10}
        resultado = productos.delete_one(criterio)
        if (resultado.deleted_count >0):
            print ("producto eliminado correctamente")
        else:
            print ("no existe el producto que quieres eliminar")    
    
    except pymongo.errors as error:
        print(str(error))
        
        
agregar()
#consultarporCodigo()
#listar()
#actualizar()
#eliminar()