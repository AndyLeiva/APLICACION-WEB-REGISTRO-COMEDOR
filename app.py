from flask import Flask, jsonify, request
from Models import db, Estudiantes
from logging import exception

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database\\estudiantes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

db.init_app(app)


@app.route("/")
def home():
    return "<h1>Hola</h1>"

@app.route("/api/estudiantes", methods=["GET"])
def getEstudiantes():
    try:
        estudiantes = Estudiantes.query.all()
        toReturn = [estudiante.serialize() for estudiante in estudiantes]
        return jsonify(toReturn), 200

    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"msg":"Ha ocurrido un error"}), 500




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




if __name__ == "__main__":
    app.run(debug=True, port=4000)