#crear una tabla llamada Alumnos que constará de tres columnas: la columna id de tipo entero, la 
# columna nombre que será de tipo texto y la columna apellido que también será de tipo texto.

#Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que insertar 8 alumnos a 
# la tabla.

#Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola.

import sqlite3

def main():
    inserta_datos(1,'Ana','Lopez')
    inserta_datos(2,'Susana','Olivarez')
    inserta_datos(3,'Diego','Lopez')
    inserta_datos(4,'Karol','Jimenez')
    inserta_datos(5,'Homero','Jimeno')
    inserta_datos(6,'Cecilio','Kato')
    inserta_datos(7,'Cornelio','Rancho')
    inserta_datos(8,'Chila','Suarez')
    
def inserta_datos(ide, nom, ape):
    conn = sqlite3.connect('database/databasealumnos.db', isolation_level=None)
    cursor = conn.cursor()

    query = '''INSERT INTO alumnos(id, nombre, apellido) VALUES(?, ?, ?)'''

    rows = cursor.execute(query, (ide,nom,ape))

    cursor.close()
    conn.close()

if __name__=='__main__':
    main()


conn = sqlite3.connect('database/databasealumnos.db')
cursor = conn.cursor()
query = f'SELECT * FROM alumnos WHERE nombre="Homero"'
rows = cursor.execute(query)

for info in rows:
    print(info)

cursor.close()
conn.close()
    