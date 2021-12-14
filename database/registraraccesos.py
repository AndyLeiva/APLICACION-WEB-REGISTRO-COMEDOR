import sqlite3 as sql

DB_PATH = "database/registros.db"

def crearBD():
    conexion = sql.connect(DB_PATH)
    cursor = conexion.cursor()
    cursor.execute("""CREATE TABLE registros (
        cedula integer,
        nombre text,
        seccion text,
        fecha text
    )""")
    conexion.commit()
    conexion.close()

def agregarValores(cedula, nombre, seccion, fecha):
    conexion = sql.connect(DB_PATH)
    cursor = conexion.cursor()
    instruccion = f"INSERT INTO Registros VALUES({cedula}, '{nombre}', '{seccion}', '{fecha}')"
    cursor.execute(instruccion)
    conexion.commit()
    conexion.close()




if __name__ == "__main__":
    #crearBD()
    agregarValores()