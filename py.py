def actualizar():

try:
    producto = consultarPorCodigo()
    cursor = miConexion.cursor()
    nuevoPrecio = producto[3]* 1.20
    codigoProductoActualizar = producto[1]
    ProductoActualizar = (nuevoPrecio, codigoProductoActualizar)
    consulta = "update productos set proPrecio=%s where procodigo  =%s"
    resultado = cursor.execute(consulta, productoActualizar)
    miConexion.commit() )
i f ( cursor - :
print( "Producto actualizado")
else:
print('iProb1emas a1 actualizar")
except miConexion. Error - as error:
print(str(error))