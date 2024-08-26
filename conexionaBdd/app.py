import pymysql as mysql

userBD = "root"
passUser = "CTPI2024**"
baseDatos = "tienda"
host = "localhost"

miConexion = mysql.connect(host=host, user=userBD, passwd=passUser, db=baseDatos)


def insertar():
    try:
        # creando
        producto = (15, "nevera", 250000, "Electrodomestico")
        cursor = miConexion.cursor()
        consulta = "insert into productos values(null, %s,%s,%s,%s)"
        resultado = cursor.execute(consulta, producto)
        miConexion.commit()

        if(cursor.rowcount == 1):
            print("Producto insertado")
        
    except miConexion.Error as error:
        print(str(error))
        
# insertar()

def listar():
    try:
        cursor=miConexion.cursor()
        consulta = "select * from productos"
        cursor.execute(consulta)
        productos = cursor.fetchall()
        if(len(productos) >0):
            for p in productos:
                print(p)
        else:
            print("En el momento no hay productos registrados")
    except miConexion.Error as error:
        print(str(error))
    
listar()
    
 