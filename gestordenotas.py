# Se utiliza la funcion def ya que es una funcion que nos permite utilizar nuevamente un bloque 
# de codigo cuando sea necesario realizar la llamada 
def registrar_curso():
    print("Registrar nuevo curso")

def mostrar_cursos():
    print("Mostrar todos los cursos y notas")

def calcular_promedio():
    print("Calcular promedio general")

def contar_aprobados_reprobados():
    print("Contar cursos aprobados y reprobados")

def buscar_curso_lineal():
    print("Buscar curso por nombre")

def actualizar_nota():
    print("Actualizar nota de un curso")

def eliminar_curso():
    print("Eliminar un curso")

def ordenar_por_nota():
    print("Ordenar cursos por nota")

def ordenar_por_nombre():
    print("Ordenar cursos por nombre")

def buscar_curso_binario():
    print("Buscar curso por nombre")

def simular_cola_revision():
    print("Simular cola de solicitudes de revisión")

def mostrar_historial_cambios():
    print("Mostrar historial de cambios")

# Muestra el Menú principal en la consola para que el usuario pueda 
while True: 
    print("\n=== GESTOR DE NOTAS ACADÉMICAS ===")
    print("1. Registrar nuevo curso")
    print("2. Mostrar todos los cursos y notas")
    print("3. Calcular promedio general")
    print("4. Contar cursos aprobados y reprobados")
    print("5. Buscar curso por nombre")
    print("6. Actualizar nota de un curso")
    print("7. Eliminar un curso")
    print("8. Ordenar cursos por nota")
    print("9. Ordenar cursos por nombre")
    print("10. Buscar curso por nombre")
    print("11. Simular cola de solicitudes de revisión")
    print("12. Mostrar historial de cambios")
    print("13. Salir")

# se utiliza la funcion opcion para definir una entrada mediante numeracion para que puedan ingresar 
#la numeracion de una de las opciones que necesitan seleccionar para ingresar data 
    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":
        registrar_curso()
    elif opcion == "2":
        mostrar_cursos()
    elif opcion == "3":
        calcular_promedio()
    elif opcion == "4":
        contar_aprobados_reprobados()
    elif opcion == "5":
        buscar_curso_lineal()
    elif opcion == "6":
        actualizar_nota()
    elif opcion == "7":
        eliminar_curso()
    elif opcion == "8":
        ordenar_por_nota()
    elif opcion == "9":
        ordenar_por_nombre()
    elif opcion == "10":
        buscar_curso_binario()
    elif opcion == "11":
        simular_cola_revision()
    elif opcion == "12":
        mostrar_historial_cambios()
    elif opcion == "13":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida, intente de nuevo.")