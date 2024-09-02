import sqlite3

baseDatos = "negocio.db"

miConexion = sqlite3.connect(baseDatos)

# insertar categorias


def inserrtarCategoria():
    try:
        nombre = "Calzado"
        cursor = miConexion.cursor()
        categorias = (nombre,)
        consulta = "insert into categorias values(null, ?)"
        cursor.execute(consulta, categorias)
        miConexion.commit()
        if (cursor.rowcount == 1):
            print(f"Categoria insertada con if {cursor.lastrowid}")
    except miConexion.Error as error:
        miConexion.rollback()
        print(f"Error: {error}")

# inserrtarCategoria()


def listarCategorias():
    try:
        cursor = miConexion.cursor()

        consulta = "select * from categorias"
        cursor.execute(consulta)
        categorias = cursor.fetchall()
        if (len(categorias) > 0):
            for c in categorias:
                print(c)
            else:
                print("En el momento no hay categorias registradas")
    except miConexion.Error as error:
        print(str(error))

# listarCategorias()


def insertarProducto():
    try:
        cursor = miConexion.cursor()
        # productos = (11, "Camisa", 119000, 2)
        codigo = int(input("ingrese codigo de producto"))
        nombre = input("Nombre del producto: ")
        precio = int(input("Precio del producto: "))
        categorias = listarCategorias()
        categoria = input(
            "Seleccionar categorias Ingresando numero de categoria:")
        productos = (codigo, nombre, precio, categoria)
        consulta = "insert into Productos values(null, ?,?,?,?)"
        cursor.execute(consulta, productos)
        miConexion.commit()
        if (cursor.rowcount == 1):
            print(f"Producto insertado con id {cursor.lastrowid}")
    except miConexion.Error as error:
        miConexion.rollback()
        print(str(error))

# insertarProducto()


def listaProductosName():
    try:
        cursor = miConexion.cursor()
        consulta = "select p.proCodigo, p.proNombre, p.proPrecio, c.cartNombre from Productos p inner join Categorias c on p.proCategoria = c.idCategoria"
        cursor.execute(consulta)
        productos = cursor.fetchall()
        for p in productos:
            print(p)

    except miConexion.Error as error:
        print(str(error))

listaProductosName()