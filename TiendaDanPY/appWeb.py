from flask import Flask, request, render_template, redirect
from werkzeug.utils import secure_filename
import os

#crear un objeto de tipo Flask
app = Flask(__name__)

app.config["UPLOAD_FOLDER"]="./static/imagenes"

contactos=[
        ["Maria","Rojas","mrojas@gmail.com"],
        ["Monik","Galindo","mgalindo@gmail.com"],
        ["Juan","Perez","jperez@gmail.com"],
        ]


#definir ruta
@app.route('/')
def index():
    #return "Hola Mundo...."
    mensaje="Hola Mundo..."
    return render_template("inicio.html", mensaje="Hola mundo...")
    

@app.route('/saludo/<nombre>', methods=['GET'])
def saludo(nombre):
    return  f"Hola {nombre}...."

@app.route('/otroSaludo/<string:mensaje>')
def  otroSaludo(mensaje):
    return f"Hola {mensaje}...."

@app.route('/producto/<nombreProducto>')
def  producto(nombreProducto):
    codigo = request.args.get('codigo')
    precio = request.args.get('precio')
    return f"Producto {nombreProducto} con código {codigo} y precio {precio}"

@app.route('/tabla') 
def mostrarTabla():    
    return render_template("tabla.html",contactos=contactos )    

@app.route("/vistaRegistrarContacto")
def vistaRegistrarContacto():
    return  render_template("frmContacto.html")

@app.route('/agregarContacto', methods=['POST'])
def agregarContacto():
    if request.method=='POST':
        nombre=request.form['txtNombre']
        apellido=request.form['txtApellido']
        correo=request.form['txtCorreo']       
        #datos de la foto
        archivo = request.files["fileFoto"]
        nombreArchivo = secure_filename(archivo.filename)
        listaNombreArchivo = nombreArchivo.rsplit(".",1)
        extension = listaNombreArchivo[1].lower()
        #obtener la posición del contacto agregado
        posicionUltimoAgregado = len(contactos)-1
        # crear nombre Foto        
        nombreFoto = str(posicionUltimoAgregado) + "." + str(extension)
        archivo.save(os.path.join(app.config["UPLOAD_FOLDER"],nombreFoto))
        contacto =[nombre,apellido,correo, nombreFoto]
        contactos.append(contacto)
        mensaje="Contacto agregado correctamente"
        return render_template("tabla.html", contactos=contactos)
        #return redirect('/tabla')

          

if  __name__ == '__main__':
    app.run(port=3000,debug=True)

