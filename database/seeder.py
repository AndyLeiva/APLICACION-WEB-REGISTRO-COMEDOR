import sqlite3 as sql

DB_PATH = "database/estudiantes.db"

def crearBD():
    conexion = sql.connect(DB_PATH)
    cursor = conexion.cursor()
    cursor.execute("""CREATE TABLE estudiantes (
        cedula integer,
        nombre text,
        seccion text
    )""")
    conexion.commit()
    conexion.close()

def agregarValores():
    conexion = sql.connect(DB_PATH)
    cursor = conexion.cursor()
    datos = [
        (1234,"Andy","10-1"),
        (2345,"Allison","10-1")
    ]
    cursor.executemany("""INSERT INTO estudiantes VALUES (?,?,?)""", datos)
    conexion.commit()
    conexion.close()




if __name__ == "__main__":
    crearBD()
    agregarValores()