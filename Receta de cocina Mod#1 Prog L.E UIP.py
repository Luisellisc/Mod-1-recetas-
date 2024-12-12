import sqlite3

def create_database():
    conn = sqlite3.connect("recetas.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS recetas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT UNIQUE NOT NULL,
            ingredientes TEXT NOT NULL,
            pasos TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
          
def agregar_receta():
    nombre = input("Ingrese el nombre de la receta: ")
    ingredientes = input("Ingrese los ingredientes (separar por comas): ")
    pasos = input("Ingrese los pasos para hacer receta (separar por comas): ")

    conn = sqlite3.connect('recetas.db')
    c =  conn.cursor()
    try:
        c.execute(
            "INSERT INTO recetas (nombre, ingredientes, pasos) VALUES(?,?,?)",
            (nombre, ingredientes, pasos)
        )
        conn.commit()
        print("\nReceta agregada con exito.\n")
    except sqlite3.IntegrityError:
        print("\nHay un Error: Ya existe una receta con ese nombre.\n")
    conn.close()


def actualizar_receta():
    nombre = input("Ingrese el nombre de la receta que desea actualizar: ")

    conn = sqlite3.connect("recetas.db")
    c = conn.cursor()
    c.execute("SELECT * FROM recetas WHERE nombre = ?", (nombre,))
    receta = c.fetchone()

    if receta:
        print("\nReceta encontrada:")
        print(f"Ingredientes: {receta[2]}\nPasos: {receta[3]}\n")

        nuevos_ingredientes = input("Ingrese los nuevos ingredientes (dejar vacío para no cambiar): ")
        nuevos_pasos = input("Ingrese los nuevos pasos (dejar vacío para no cambiar): ")

        nuevos_ingredientes = nuevos_ingredientes if nuevos_ingredientes else receta[2]
        nuevos_pasos = nuevos_pasos if nuevos_pasos else receta[3]

        c.execute(
            "UPDATE recetas SET ingredientes = ?, pasos = ? WHERE nombre = ?",
            (nuevos_ingredientes, nuevos_pasos, nombre)
        )
        conn.commit()
        print("\nReceta actualizada con exito.\n")
    else:
        print("\nOcurrio un Error: No se encontró ninguna receta con ese nombre.\n")
    conn.close()

def eliminar_receta():
    nombre = input("Ingrese el nombre de la receta que desea eliminar: ")

    conn = sqlite3.connect("recetas.db")
    c = conn.cursor()
    c.execute("SELECT * FROM recetas WHERE nombre = ?", (nombre,))
    receta = c.fetchone()

    if receta:
        c.execute("DELETE FROM recetas WHERE nombre = ?", (nombre,))
        conn.commit()
        print("\nReceta eliminada con exito.\n")
    else:
        print("\nOcurrio un Error: No se encontró ninguna receta con ese nombre.\n")
    conn.close()

def ver_recetas():
    conn = sqlite3.connect("recetas.db")
    c = conn.cursor()
    c.execute("SELECT nombre FROM recetas")
    recetas = c.fetchall()

    if recetas:
        print("\nLista de recetas:")
        for receta in recetas:
            print(f"- {receta[0]}")
        print()
    else:
        print("\nNo hay recetas registradas.\n")
    conn.close()

def buscar_receta():
    nombre = input("Ingrese el nombre de la receta: ")

    conn = sqlite3.connect("recetas.db")
    c = conn.cursor()
    c.execute("SELECT ingredientes, pasos FROM recetas WHERE nombre = ?", (nombre,))
    receta = c.fetchone()

    if receta:
        print("\nIngredientes:")
        print(receta[0])
        print("\nPasos:")
        print(receta[1])
        print()
    else:
        print("\nHay un Error: No se encontró ninguna receta con ese nombre.\n")
    conn.close()

def menu():
    while True:
        print("\n Libro de Recetas ")
        print("a) Agregar nueva receta")
        print("b) Actualizar receta ")
        print("c) Eliminar receta ")
        print("d) Ver recetas")
        print("e) Buscar ingredientes y pasos de receta")
        print("f) Salir")

        opcion = input("Seleccione una opción: ").lower()
        if opcion == 'a':
            agregar_receta()
        elif opcion == 'b':
            actualizar_receta()
        elif opcion == 'c':
            eliminar_receta()
        elif opcion == 'd':
            ver_recetas()
        elif opcion == 'e':
            buscar_receta()
        elif opcion == 'f':
            print("\nSaliendo del programa.")
            break
        else:
            print("\nOpción no válida. Elija una opcion del menu.\n")

if __name__ == "__main__":
    create_database()
    menu()
    

