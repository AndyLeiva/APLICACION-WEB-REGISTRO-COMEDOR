from enum import unique
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Estudiantes(db.Model):
    rowid = db.Column(db.Integer, primary_key=True)
    cedula = db.Column(db.Integer, unique=True, nullable=False)
    nombre = db.Column(db.String(100))
    seccion = db.Column(db.String(10))

    def __str__(self):
        return "\nCedula: {}, Nombre: {}, Seccion: {}".format(
            self.cedula,
            self.nombre,
            self.seccion
        )

    def serialize(self):
        return{
            "rowid": self.rowid,
            "cedula": self.cedula,
            "nombre": self.nombre,
            "seccion": self.seccion

        }