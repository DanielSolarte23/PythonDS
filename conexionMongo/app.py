import pymongo
import pymongo.errors

# Establecer conexión con MongoDB
try:
    miConexion = pymongo.MongoClient("mongodb://localhost:27017")
    print("Conexión exitosa a MongoDB")

    # Obtener acceso a la base de datos llamada "Tienda"
    basedatos = miConexion["Tienda"]
    print(f"Base de datos seleccionada: {basedatos.name}")
    
except pymongo.errors.ConnectionError as e:
    print(f"No se pudo conectar a MongoDB: {e}")


def agregar():
    try:
        # Conectarse a MongoDB
        miConexion = pymongo.MongoClient("mongodb://localhost:27017")
        
        # Seleccionar la base de datos y la colección
        basedatos = miConexion["Tienda"]
        coleccion = basedatos["Productos"]  # Cambia "Productos" por el nombre de tu colección

        # Datos del producto
        codigo = 12
        nombre = "Pantalla"
        precio = 525000
        categoria = "Electrodomestico"
        producto = {
            "codigo": codigo,
            "nombre": nombre,
            "precio": precio,
            "categoria": categoria
        }

        # Insertar el documento en la colección
        resultado = coleccion.insert_one(producto)

        # Verificar si la inserción fue exitosa
        if resultado.acknowledged:
            print("Producto agregado correctamente")
        
    except pymongo.errors.PyMongoError as error:
        print(f"Error al agregar el producto: {str(error)}")


def consultarProCodigo():
    try:
        codigoAconsultar = int(input("Ingrese el hpta producto a consultar"))
        consulta = {"codigo": codigoAconsultar}
        
        producto = Producto.find_one(consulta)
        if(producto):
            print(f"Codigo : {producto["codigo"]}")
            print(f"Nombre : {producto["nombre"]}")
            print(f"Precio : {producto["precio"]}")
            print(f"Categoria : {producto["categoria"]}")
        else:
            print("No se encontro el hpta producto")
        
    except pymongo.errors as error:
        print(str(error))

# agregar()