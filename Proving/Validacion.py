def Es_entero (Texto):
    while True:
        try:
            Value = int(input(Texto))
            return Value
        except ValueError:
            print("El dato ingresado No es un entero, ","Digite un valor entero ")
def Es_flotante (Texto):
    while True:
        try:
            Value = float(input(Texto))
            return Value
        except ValueError:
            print("El darto ingresado ", Value, " No es un float, ","Digite un valor flotante ")

#Funcion para verificar sí el valor ingresado está dentro de las opciones requeridas (Las opciones deben ser ingresadas en una tupla)
def Opcion(Opciones):
    Opcion_user = input("digite una opción: ")
    for x , e in enumerate(Opciones):
        if Opcion_user == e:
            return Opcion_user
    else:
        print(" Su opcion es invalida")
        Opcion(Opciones)
#Función para definir el limite de caracteres que puede tener una entrada
def Caracter_lim(Valor, Inicio, Final):
    while True:
        if len(str(Valor)) >=Inicio and len(str(Valor)) <= Final:
            return Valor , True
        else:
            print("El dato No se encuentra en el rango adecuando, Ingrese uno nuevo")
            return False , False

#Verificar si ese dato existe en un diccionario
def Existe_En( Dicionario, Dato, clave):
    for x, e in enumerate(Dicionario):
        if Dicionario[x].get(str(clave)) == Dato:
            return True
    else:
        return False

