from flask import Flask, jsonify, request, render_template
from Models import db, Estudiantes
from logging import exception
import time
from database import registraraccesos


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database\\estudiantes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

db.init_app(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/buscarestudiante")
def buscar():
    return render_template("buscarestudiantes.html")

@app.route("/api/buscarestudiante")
def encontrado():
    return render_template("estudiante.html")


@app.route("/api/estudiantes", methods=["GET"])
def getEstudiantes():
    try:
        estudiantes = Estudiantes.query.all()
        toReturn = [estudiante.serialize() for estudiante in estudiantes]
        return jsonify(toReturn), 200 

    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"msg":"Ha ocurrido un error"}), 500


#Encontrar estudiante

@app.route("/api/findestudiante", methods=["GET"])
def getestudiante():
    try:
        fields = {}
        if "nombre" in request.args:
            fields["nombre"] = request.args["nombre"]
        
        if "cedula" in request.args:
            fields["cedula"] = request.args["cedula"]

        if "seccion" in request.args:
            fields["seccion"] = request.args["seccion"]

        estudiante = Estudiantes.query.filter_by(**fields).first()
        
        if not estudiante:
            return jsonify({"msg": "Este estudiante no existe"}), 200
        else:
            return jsonify(estudiante.serialize()), 200
    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un error"}), 500

#Agregar estudiante
@app.route("/api/addestudiante", methods=["POST"])

def addestudiante():
    try:
        nombre = request.form["nombre"]
        cedula = request.form["cedula"]
        seccion = request.form["seccion"]

        estudiante = Estudiantes(int(cedula),nombre, seccion)
        db.session.add(estudiante)
        db.session.commit()
        

        return jsonify(estudiante.serialize()), 200

    except Exception:
        exception("\n[SERVER]: Error in route /api/addestudiante. Log: \n")
        return jsonify({"ms":"Algo ha salido mal"}), 500


#Buscar estudiante        

@app.route("/api/registrarEstudianteAcceso", methods=["POST"])
def registrarEstudianteAcceso():
    try:
        nombreEstudiante = request.form["nombre"]

        estudiante = Estudiantes.query.filter(Estudiantes.nombre.like(f"%{nombreEstudiante}%")).first()
        if not estudiante:
            return render_template("error.html")
        else:
           
            nombre = estudiante.getNombre()
            print(nombre)
            cedula = estudiante.getCedula()
            print(cedula)
            seccion = estudiante.getSeccion()
            print(seccion)

            fecha = time.strftime("%x")
            registraraccesos.agregarValores(int(cedula),nombre, seccion, fecha)
            return render_template("datosestudiante.html", nombre = nombre, cedula = cedula, seccion = seccion, fecha = fecha)

    except Exception:
        exception("[SERVER]: Error in route /api/searchEstudiante ->")
        return jsonify({"msg": "Ha ocurrido un error"}), 500




if __name__ == "__main__":
    app.run(debug=True, port=4000)