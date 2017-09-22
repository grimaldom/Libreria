import sqlite3
import os


# AQUI CREAMOS LA BASE DE DATOS
db = sqlite3.connect('datos/libros')
cursor = db.cursor()
try:
    cursor.execute('''CREATE TABLE books(id INTEGER PRIMARY KEY,autor TEXT, titulo TEXT, publicacion DATE)''')
    db.commit()

except sqlite3.OperationalError:
    print ("Oops! This was an operational error. Try again...")

except sqlite3.NameError:
    print ("Name Error")

except sqlite3.ValueError:
    print ("value error")

except sqlite3.IOError:
    print ("IO error")




def menu():
    """
    Función que limpia la pantalla y muestra nuevamente el menu
    """
    os.system('cls')  # NOTA para windows tienes que cambiar clear por cls\
    print("*** Mi bliblioteca ***")
    print("Selecciona una opción")
    print("\t1 - Agregar")
    print("\t2 - Editar Autor")
    print("\t3 - Quitar")
    print("\t4 - Litar")
    print("\t5 - Consultar")
    print("\t6 - salir")


while True:
    # Mostramos el menu
    menu()

    # solicituamos una opción al usuario
    opcionMenu = input("inserta un numero:  ")

    if opcionMenu == "1":
        autor = input("Autor: ")
        titulo = input ("Titulo: ")
        publicacion = input("Publicacion: ")

        cursor.execute ('''INSERT INTO books(autor, titulo, publicacion)
                        VALUES (:autor, :titulo, :publicacion)''',
                        {'autor':autor, 'titulo':titulo, 'publicacion':publicacion})

        db.commit()

        print("")
        input("pulsa una tecla para regresar al menu principal")
    elif opcionMenu == "2":
        cursor.execute('''SELECT id, autor FROM books''')
        resultado = cursor.fetchall()
        for fila in resultado:
                print("{0} : {1}".format(fila[0], fila[1]))
        id = input("ID de usuario a modificar: ")
        for fila in resultado:
            if int(id) == int(fila[0]):
                nuevo_autor = input("Autor Nuevo: ")
                cursor.execute('''UPDATE books SET autor = ? WHERE
                                id = ?''', (nuevo_autor, id))
        db.commit()

        print("")
        input("pulsa una tecla para regresar al menu principal")

    elif opcionMenu == "3":

        cursor.execute('''SELECT id, autor FROM books''')
        resultado = cursor.fetchall()
        for fila in resultado:
                print("{0} : {1}".format(fila[0], fila[1]))
        id = input("ID de Autor a eliminar: ")
        for fila in resultado:
            if int(id) == int(fila[0]):
                cursor.execute('''DELETE FROM books WHERE id = ?''', (id,))

        db.commit()

        print("")
        input("pulsa una tecla para regresar al menu principal")

    elif opcionMenu == "4":
        print("*** Mi bliblioteca ***\n")
        cursor.execute('''SELECT autor, titulo, publicacion FROM books''')
        resultado = cursor.fetchall()
        for fila in resultado:
            print("{0}, {1}, {2}".format(fila[0], fila[1], fila[2]))

        db.commit()

        print("")
        input("pulsa una tecla para regresar al menu principal")
    elif opcionMenu == "5":
        def Smenu():
            return """          *** Consultas ***
        Selecciona una opción
        \t1 - Autores
        \t2 - Titulos
        \t3 - Publicaciones
        \t4 - salir"""
        frace = Smenu()
        print(frace)
        while True:
            # Mostramos el sub menu
            Smenu()

            # solicituamos una opción al usuario
            opcionSMenu = input("inserta un numero:  ")

            if opcionSMenu == "1":
                print("\n*** Autores ***\n")
                cursor.execute('''SELECT autor FROM books''')
                for registro in cursor:
                    print(registro)


                print("")
                input("pulsa una tecla para regresar al sub menu")
                frace = Smenu()
                print(frace)
            elif opcionSMenu == "2":
                print("\n*** Titulos ***\n")
                cursor.execute('''SELECT titulo FROM books''')
                for registro in cursor:
                    print(registro)

                print("")
                input("pulsa una tecla para regresar al sub menu")
                frace = Smenu()
                print(frace)

            elif opcionSMenu == "3":
                print("\n*** Publicaciones ***\n")
                cursor.execute('''SELECT publicacion FROM books''')
                for registro in cursor:
                    print(registro)


                print("")
                input("pulsa una tecla para regresar al sub menu")
                frace = Smenu()
                print(frace)

            elif opcionSMenu == "4":
                print("test")

                break
            else:
                print("")
                input("No has pulsado ninguna opción correcta...\npulsa una tecla para regresar al submenu")

            print("")
            input("pulsa una tecla para regresar al submenu")
    elif opcionMenu == "6":
        break
    else:
        print("")
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para regresar al menu principal")





db.close()
