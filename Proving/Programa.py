import json
import os
import Validacion
import sys
#Definiendo variables a usar
docentes = []
categorias = []
informes_mensuales = []
#Cargar datos de prueba
def Cargar_testing():
    global docentes, categorias, informes_mensuales

    # Datos iniciales de prueba
    docentes = [
        {'codigo': 45685, 'nombre': 'Juan Perez', 'email': 'juan@example.com', 'fecha_nacimiento': '1980-05-15', 'categoria': 'A', 'estado': 'Activo'},
        {'codigo': 45222, 'nombre': 'Maria Garcia', 'email': 'maria@example.com', 'fecha_nacimiento': '1985-12-22', 'categoria': 'B', 'estado': 'Inactivo'}
    ]

    categorias = [
        {'codigo': 'A', 'nombre': 'Categoria A', 'valor_hora': 50000.0},
        {'codigo': 'B', 'nombre': 'Categoria B', 'valor_hora': 40000.0}
    ]

    informes_mensuales = [
        {'fecha': '2023-04-01', 'codigo_docente': 45685, 'asignatura': 'Matematicas', 'horas_trabajadas': 20},
        {'fecha': '2023-04-01', 'codigo_docente': 45222, 'asignatura': 'Fisica', 'horas_trabajadas': 15}
    ]
    
#Funciones para crear archivos json o leerlos
def Crear_json_Docentes():
    global docentes
    if not os.path.exists("Docentes.json") or os.stat("Docentes.json").st_size == 0:
            Doncentes_Js =  open("Docentes.json", "w")
            print("Desea cargar datos de prueba de docentes? si/no")
            Opcion = Validacion.Opcion(tuple(["si", "no"]))
            if Opcion == "si":
                Cargar_testing()
                json.dump(docentes, Doncentes_Js)
                Doncentes_Js.close()
            else:
                Doncentes_Js.close()
    else:
        return
def Crear_json_Categorias():
    global categorias
    if not os.path.exists("Categorias.json") or os.stat("Categorias.json").st_size == 0:
            categorias_Js =  open("Categorias.json", "w")
            print("Desea cargar datos de prueba de Categorias? si/no")
            Opcion = Validacion.Opcion(tuple(["si", "no"]))
            if Opcion == "si":
                Cargar_testing()
                json.dump(categorias, categorias_Js)
                categorias_Js.close()
            else:
                categorias_Js.close()
    else:
        return
def Crear_json_Informes():
    global informes_mensuales
    if not os.path.exists("Informes.json") or os.stat("Informes.json").st_size == 0:
            informes_Js =  open("Informes.json", "w")
            print("Desea cargar datos de prueba de Informes? si/no")
            Opcion = Validacion.Opcion(tuple(["si", "no"]))
            if Opcion == "si":
                Cargar_testing()
                json.dump(informes_mensuales, informes_Js)
                informes_Js.close()
            else:
                informes_Js.close()
    else:
        return
#Funcion para imprimir datos en forma de tabla
def imprimir_tabla(diccionarios):
    # Obtener todas las claves presentes en los diccionarios
    claves = set().union(*(d.keys() for d in diccionarios))

    # Calcular la longitud máxima de las claves
    longitud_maxima_clave = max(len(str(clave)) for clave in claves)

    # Calcular la distancia entre columnas
    distancia_columnas = longitud_maxima_clave + 4
    if distancia_columnas <20:
        distancia_columnas = 20

    # Imprimir encabezados
    encabezados = "".join(f"{clave:>{distancia_columnas}}" for clave in sorted(claves))
    print(encabezados)

    # Imprimir línea de separación
    separacion = "-" * (len(claves) * distancia_columnas - 3)
    print(separacion)

    # Imprimir filas con valores
    for diccionario in diccionarios:
        fila = "".join(f"{str(diccionario.get(clave, '')):>{distancia_columnas}}" for clave in sorted(claves))
        print(fila)

#Gestion de docentes
#1. Ingresar Docente
def Ingresar_Doc():
    codigo, val = Validacion.Caracter_lim(Validacion.Es_entero("Digite el codigo del docente, este debe ser numerico y tener maximo 5 caracteres: "),1,5)
    if val == False:
        while True:
            codigo ,val = Validacion.Caracter_lim(Validacion.Es_entero("Digite el codigo del docente, este debe ser numerico y tener maximo 5 caracteres: "),1,5)
            if val == True:
                break
    
    nombre = input("Ingrese el nombre del docente: ")
    email = input("Ingrese el email del docente: ")
    fecha_nacimiento = input("Ingrese la fecha de nacimiento del docente (YYYY-MM-DD): ")
    categoria = input("Ingrese el código de la categoría del docente: ")
    #Verifica que la categoria Exista
    categorias_Js =  open("Categorias.json", "r")
    Lista_Doc = json.load(categorias_Js)
    if Validacion.Existe_En(Lista_Doc, categoria, "codigo") == False:
        while True:
            print("La categoria ingresada NO exite entre las categorias registrasdas")
            print("Escriba 1 para ingresar otra o 2 para añadir una categoria")
            val = Validacion.Opcion(tuple(["1","2"]))
            if val == "1":
                categoria = input("Ingrese el código de la categoría del docente: ")
                Avaible = []
                for x, e in enumerate(Lista_Doc):
                    Avaible.append({"Codigos": Lista_Doc[x].get("codigo"), "Nombre": Lista_Doc[x].get("nombre")})
                print("Las opciones validas son las siguientes: \n")
                imprimir_tabla(Avaible)
                if Validacion.Existe_En(Lista_Doc, categoria, "codigo") == True:
                    categorias_Js.close()
                    break
            if val == "2":
                categorias_Js.close()
                Ingresar_categoria()
                break
    print("Ingrese el estado del docente (Activo/Inactivo): ")
    estado = Validacion.Opcion(tuple(["Activo", "Inactivo"]))
    nuevo_docente = {'codigo': codigo, 'nombre': nombre, 'email': email, 'fecha_nacimiento': fecha_nacimiento, 'categoria': categoria, 'estado': estado}
    #Ya que a veces se guarda el estado como none, verificamos si es asi y solicitamos la informacion al usuario otra vez
    while nuevo_docente.get("estado") == None:
        estado = Validacion.Opcion(tuple(["Activo", "Inactivo"]))
        nuevo_docente = {'codigo': codigo, 'nombre': nombre, 'email': email, 'fecha_nacimiento': fecha_nacimiento, 'categoria': categoria, 'estado': estado}
    Archivo_Docentes = open("Docentes.json", "r")
    data = json.load(Archivo_Docentes)
    data.append(nuevo_docente)
    Archivo_Docentes.close()
    Archivo_Docentes = open("Docentes.json", "w")
    json.dump(data, Archivo_Docentes)
    Archivo_Docentes.close()
    print("Docente Añadido satisfactoriamente")

#Funcion para eliminar  docentes
def Eliminar_docentes():
    #Verificamos que el codigo sea posible:
    codigo, val = Validacion.Caracter_lim(Validacion.Es_entero("Digite el codigo del docente a eliminar, este debe ser numerico y tener maximo 5 caracteres: "),1,5)
    if val == False:
        while True:
            codigo ,val = Validacion.Caracter_lim(Validacion.Es_entero("Digite el codigo del docente, este debe ser numerico y tener maximo 5 caracteres: "),1,5)
            if val == True:
                break
    #Buscamos el codigo en la lista de docentes.
    Archivo_Docentes = open("Docentes.json", "r")
    data = json.load(Archivo_Docentes)
    Archivo_Docentes.close()
    for x, e in enumerate(data):
        if e.get("codigo") == codigo:
            data.pop(x)
            Archivo_Docentes = open("Docentes.json", "w")
            json.dump(data, Archivo_Docentes)
            Archivo_Docentes.close()
            print("Se elimino el docente Correctamente")
            return
    else: print("El codigo no Coincide con ninguno")
#Funcion para buscar a un profesor, categoria o informe
def Buscar_Docente(): 
    #Verificamos que el codigo sea posible:
    codigo, val = Validacion.Caracter_lim(Validacion.Es_entero("Digite el codigo del docente a buscar, este debe ser numerico y tener maximo 5 caracteres: "),1,5)
    if val == False:
        while True:
            codigo ,val = Validacion.Caracter_lim(Validacion.Es_entero("Digite el codigo del docente a buscar, este debe ser numerico y tener maximo 5 caracteres: "),1,5)
            if val == True:
                break
    #Buscamos el codigo en la lista de docentes.
    Archivo_Docentes = open("Docentes.json", "r")
    data = json.load(Archivo_Docentes)
    Archivo_Docentes.close()
    Yes = False
    for x, e in enumerate(data):
        if e.get("codigo") == codigo:
            print("El docente es: \n ", data[x])
            Yes = True
        elif x == len(data)-1 and Yes == False:
            print("No encontrado")
#Funcion para cambiar el estado del docente
def Cambiar_estado_docente():
    #Verificamos que el codigo sea posible:
    codigo, val = Validacion.Caracter_lim(Validacion.Es_entero("Digite el codigo del docente a cambiar estado, este debe ser numerico y tener maximo 5 caracteres: "),1,5)
    if val == False:
        while True:
            codigo ,val = Validacion.Caracter_lim(Validacion.Es_entero("Digite el codigo del docente a cambiar estado, este debe ser numerico y tener maximo 5 caracteres: "),1,5)
            if val == True:
                break
    Archivo_Docentes = open("Docentes.json", "r")
    data = json.load(Archivo_Docentes)
    Archivo_Docentes.close()
    for x, e in enumerate(data):
        if e.get("codigo") == codigo:
            print("El docente es: \n ", data[x].get("nombre"))
            print("El docente estado del docente es: ", e.get("estado") )
            if e.get("estado") == "Activo":
                e["estado"] = "Inactivo"
            else:
                e["estado"] = "Activo"
                print(e["estado"])
            Archivo_Docentes = open("Docentes.json", "w")
            json.dump(data, Archivo_Docentes)
            Archivo_Docentes.close()
            print("Se cambio el docente a: ", e.get("estado"))
            return
    else: print("El codigo no Coincide con ninguno")
            
#Funcion para ver ya sean Docentes, categorias o informes.
def Ver(Nombre_Archivo):
    Archivo = open(Nombre_Archivo, "r")
    Lista = json.load(Archivo)
    Archivo.close()
    imprimir_tabla(Lista)
#gestion de categorias
#Funcion para añadir categorias  
def Ingresar_categoria():
    codigo = input("Ingrese el código de la categoría: ")
    nombre = input("Ingrese el nombre de la categoría: ")
    valor_hora = Validacion.Es_flotante("Ingrese el valor de la hora cátedra: ")
    nueva_categoria = {'codigo': codigo, 'nombre': nombre, 'valor_hora': valor_hora}
    Categoria_JS = open("Categorias.json", "r")
    Lista = json.load(Categoria_JS)
    Lista.append(nueva_categoria)
    Categoria_JS.close()
    Categoria_JS = open("Categorias.json", "w")
    json.dump(Lista, Categoria_JS)
    Categoria_JS.close()
    print("Se añadio la categoria satisfactoriamente")
#funcion para eliminar categorias
def Eliminar_Categoria():
    codigo = input("Ingrese el código de la categoría: ")
    Archivo_Categorias = open("Categorias.json", "r")
    data = json.load(Archivo_Categorias)
    Archivo_Categorias.close()
    for x, e in enumerate(data):
        if e.get("codigo") == codigo:
            data.pop(x)
            Archivo_Categorias = open("categorias.json", "w")
            json.dump(data, Archivo_Categorias)
            Archivo_Categorias.close()
            print("Se elimino la categoria Correctamente")
            return
    else: print("El codigo no Coincide con ninguna")
#Funcion para consultar Categorias
def Buscar_Categorias():
    codigo = input("Ingrese el código de la categoría: ")
    Archivo_Categorias = open("Categorias.json", "r")
    data = json.load(Archivo_Categorias)
    Archivo_Categorias.close()
    for x, e in enumerate(data):
        if e.get("codigo") == codigo:
            print("La información de la categoria es la siguiente: \n ", data[x])
            return
    else: print("El codigo no Coincide con ninguna")
#Gestión de informes
#Función para añadir Informes
def Ingresar_informe_mensual():
    fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
    codigo =Validacion.Es_entero("Ingrese el código del docente: ")
    #Verifica que el docente Exista y si no existe le permite ingrasar uno nuevo
    Docentes_Js =  open("Docentes.json", "r")
    Lista_Doc = json.load(Docentes_Js)
    Avaible = []
    for x, e in enumerate(Lista_Doc):
        Avaible.append({"codigo": Lista_Doc[x].get("codigo"), "Nombre": Lista_Doc[x].get("nombre")})
    print("Las opciones disponibles son: \n")
    imprimir_tabla(Avaible)
    if Validacion.Existe_En(Avaible, codigo, "codigo") == False:
        while True:
            print("El docente ingresado NO exite entre los registrasdos")
            print("Escriba 1 para ingresar otro o 2 para añadir un nuevo Docente")
            val = Validacion.Opcion(tuple(["1","2"]))
            if val == "1":
                codigo = Validacion.Es_entero("Ingrese el código del docente: ")
                if Validacion.Existe_En(Lista_Doc, codigo, "codigo") == True:
                    Docentes_Js.close()
                    break
                print("Las opciones validas son las siguientes: \n", Avaible)
            if val == "2":
                Docentes_Js.close()
                Ingresar_Doc()
                return
    asignatura = input("Ingrese el nombre de la asignatura: ")
    horas_trabajadas = int(input("Ingrese el número de horas trabajadas: "))
    nuevo_informe = {'fecha': fecha, 'codigo_docente': codigo, 'asignatura': asignatura, 'horas_trabajadas': horas_trabajadas}
    Informes_JS = open("Informes.json", "r")
    Lista_Informe = json.load(Informes_JS)
    Informes_JS.close()
    Lista_Informe.append(nuevo_informe)
    Informes_JS = open("Informes.json", "w")
    json.dump(Lista_Informe, Informes_JS)
    Informes_JS.close()
#Funcion para eliminar informes mensuales
def Eliminar_informe():
        #Verificamos que el codigo sea posible:
    codigo, val = Validacion.Caracter_lim(Validacion.Es_entero("Digite el codigo del docente a eliminar, este debe ser numerico y tener maximo 5 caracteres: "),1,5)
    if val == False:
        while True:
            codigo ,val = Validacion.Caracter_lim(Validacion.Es_entero("Digite el codigo del docente, este debe ser numerico y tener maximo 5 caracteres: "),1,5)
            if val == True:
                break
    #Buscamos el codigo en la lista de docentes.
    Archivo_Informes = open("Informes.json", "r")
    data = json.load(Archivo_Informes)
    Archivo_Informes.close()
    for x, e in enumerate(data):
        if e.get("codigo_docente") == codigo:
            data.pop(x)
            Archivo_Informes = open("Informes.json", "w")
            json.dump(data, Archivo_Informes)
            Archivo_Informes.close()
            print("Se elimino el informe Correctamente")
            return
    else: print("El codigo no Coincide con ninguno")

#Funcion para liquidar honorarios

def Liquidación_honorarios():
    #Cargar los datos en una listas donde se pueda extraer la información
    Archivo_Docentes = open("Docentes.json", "r")
    Lista_Docente = json.load(Archivo_Docentes)
    Archivo_Docentes.close()
    Archivo_Categorias = open("Categorias.json", "r")
    Lista_Categorias = json.load(Archivo_Categorias)
    Archivo_Categorias.close()
    Archivo_Informes = open("Informes.json","r")
    Lista_Informes = json.load(Archivo_Informes)
    Archivo_Informes.close()
    Liquidacion = []
    for x, e in enumerate(Lista_Docente):
        nombre = Lista_Docente[x].get("nombre")
        if Lista_Docente[x].get("estado") == "Activo":
            for k, l in enumerate(Lista_Informes):
                if l.get("codigo_docente") == Lista_Docente[x].get("codigo"):
                    horas_laboradas = float(Lista_Informes[k].get("horas_trabajadas"))
            for i, j in enumerate(Lista_Categorias):
                if j.get("codigo") == Lista_Docente[x].get("categoria"):
                    Val_hora = float(Lista_Categorias[i].get("valor_hora"))
            Valor_Pagar = horas_laboradas*Val_hora
            Liquidacion.append({"nombre": nombre,"Valor_pagar": Valor_Pagar})
        horas_laboradas= 0
        Val_hora = 0
    imprimir_tabla(Liquidacion)

# Menú principal
def menu_principal(): 

    while True:
        print("\nMenú principal:")
        print("1. Gestionar docentes")
        print("2. Gestionar categorías")
        print("3. Gestionar informes mensuales")
        print("4. Liquidar honorarios")
        print("5. Salir")
        opcion = input("Ingrese una opción: ")

        if opcion == '1':
            submenu_docentes()
        elif opcion == '2':
            submenu_categorias()
        elif opcion == '3':
            submenu_informes_mensuales()
        elif opcion == '4':
            print("Liquidaciones de honorarios:")
            Liquidación_honorarios()
        elif opcion == '5':
            print("Gracias por usar el servicio, Adios ")
            sys.exit()
        else:
            print("Opción inválida. Intente de nuevo.")

def submenu_docentes():
    while True:
        print("\nGestión de docentes:")
        print("1. Ingresar docente")
        print("2. Eliminar docente")
        print("3. Consultar docente")
        print("4. Ver Docentes")
        print("5. Cambiar estado docente")
        print("6. Volver al menú principal")
        opcion = input("Ingrese una opción: ")

        if opcion == '1':
            Ingresar_Doc()
        elif opcion == '2':
            Eliminar_docentes()
        elif opcion == '3':
            Buscar_Docente()
        elif opcion == '4':
            Ver("Docentes.json")
        elif opcion == '5':
            Cambiar_estado_docente()
        elif opcion == '6':
            menu_principal()
        else:
            print("Opción inválida. Intente de nuevo.")

def submenu_categorias():
    while True:
        print("\nGestión de categorías:")
        print("1. Ingresar categoría")
        print("2. Eliminar categoría")
        print("3. Ver categorías")
        print("4. Consultar categoría")
        print("5. Volver al menú principal")
        opcion = input("Ingrese una opción: ")

        if opcion == '1':
            Ingresar_categoria()
        elif opcion == '2':
            Eliminar_Categoria()
        elif opcion == '3':
            Ver("Categorias.json")
        elif opcion == '4':
            Buscar_Categorias()
        elif opcion == '5':
            menu_principal()
        else:
            print("Opción inválida. Intente de nuevo.")

def submenu_informes_mensuales():
    while True:
        print("\nGestión de informes mensuales:")
        print("1. Ingresar informe mensual")
        print("2. Eliminar informe mensual")
        print("3. Ver informes")
        print("4. Volver al menú principal")
        opcion = input("Ingrese una opción: ")
    
        if opcion == '1':
            Ingresar_informe_mensual()
        elif opcion == '2':
            Eliminar_informe()
        elif opcion == '3':  
            Ver("Informes.json")
        elif opcion == '4':
            menu_principal()
        else:
            print("Opción inválida. Intente de nuevo.")
# Iniciar el menú principal
Crear_json_Categorias()
Crear_json_Docentes()
Crear_json_Informes()
menu_principal()
