import os
import webbrowser

def buscar_en_google():
    # Solicita al usuario el término de búsqueda
    busqueda = input("Escribe el término de búsqueda: ")
    # Crea la URL de búsqueda en Google con el término ingresado
    url = f"https://www.google.com/search?q={busqueda}"
    # Abre la URL en el navegador web predeterminado
    webbrowser.open(url)
    print("------------------------------------")
    print("Búsqueda realizada en Google con éxito")
    print("------------------------------------")

def borrar_pantalla():
    # Limpia la pantalla según el sistema operativo
    os.system('cls' if os.name == 'nt' else 'clear')
    print("-----------------------------")
    print("Pantalla borrada exitosamente")
    print("-----------------------------")

def guardar_comando():
    # Solicita al usuario que ingrese el comando a guardar
    comando = input("Escribe el comando: ")
    # Solicita al usuario que ingrese la definición del comando
    definicion = input("Escribe la definición del comando: ")
    # Abre el archivo "comandos.txt" en modo de apendizaje (append)
    # El modo de apendizaje permite agregar contenido al final del archivo sin sobrescribirlo
    with open("comandos.txt", "a") as archivo:
        # Escribe el comando y la definición en el archivo, separados por un tabulador "\t"
        # Agrega también un salto de línea "\n" para separar los comandos en el archivo
        archivo.write(comando + "\t" + definicion + "\n")
    # Imprime un mensaje de confirmación indicando que el comando se ha guardado exitosamente
    print("------------------------------")
    print("Comando guardado con éxito!!")
    print("------------------------------")


def consultar_comandos():
    # Abre el archivo "comandos.txt" en modo de lectura (read)
    with open("comandos.txt", "r") as archivo:
        # Lee todas las líneas del archivo y las guarda en la variable "comandos" como una lista de strings
        comandos = archivo.readlines()
        # Verifica si hay comandos en la lista
        if comandos:
            print("Comandos guardados:")
            # Itera sobre cada comando en la lista de comandos con su índice correspondiente
            for i, comando in enumerate(comandos):
                # Elimina los espacios en blanco y caracteres de nueva línea al inicio y final del comando
                comando = comando.strip()
                # Divide el comando en una lista utilizando el tabulador "\t" como separador
                comando_info = comando.split("\t")
                # Verifica si el comando tiene al menos dos elementos en la lista (comando y definición)
                if len(comando_info) >= 2:
                    # Extrae el primer elemento de la lista como el comando
                    comando = comando_info[0]
                    # Une los elementos restantes de la lista como la definición, separados por un tabulador "\t"
                    definicion = "\t".join(comando_info[1:])
                    # Imprime el número de comando, el comando y su definición
                    print(f"{i+1}. Comando: {comando}")
                    print(f"   Definición: {definicion}")
                    # Imprime una línea de separación para cada comando
                    print("-" * 40)
                else:
                    # Imprime un mensaje de error indicando que el comando no tiene un formato válido
                    print(
                        "-------------------------------------------------------------------")
                    print(
                        f"El comando en la línea {i+1} no tiene un formato válido: {comando}")
                    print(
                        "-------------------------------------------------------------------")
        else:
            # Imprime un mensaje indicando que no hay comandos guardados
            print("--------------------------")
            print("¡¡ No hay comandos guardados !!")
            print("--------------------------")


def editar_comando():
    # Solicita al usuario el número del comando a editar y resta 1 para obtener el índice correspondiente
    numero_comando = int(input("Escribe el número del comando a editar: ")) - 1
    # Abre el archivo "comandos.txt" en modo de lectura (read)
    with open("comandos.txt", "r") as archivo:
        # Lee todas las líneas del archivo y las guarda en la variable "comandos" como una lista de strings
        comandos = archivo.readlines()
    if numero_comando >= 0 and numero_comando < len(comandos):
        # Verifica si el número de comando es válido
        comando_actual = comandos[numero_comando].strip()
        # Divide el comando en sus componentes (comando y definición) utilizando el tabulador "\t" como separador
        comando_info = comando_actual.split("\t")
        if len(comando_info) >= 2:
            # Si el comando tiene un formato válido (comando y definición), extrae el comando y la definición
            comando = comando_info[0]
            definicion = "\t".join(comando_info[1:])
            # Imprime el comando actual y su definición
            print(f"Comando actual: {comando}")
            print(f"Definición actual: {definicion}")
            # Solicita al usuario ingresar el nuevo comando (o presionar Enter para mantener el actual)
            nuevo_comando = input("Teclea el nuevo comando (o presione Enter para mantener el actual): ")
            # Solicita al usuario ingresar la nueva definición (o presionar Enter para mantener la actual)
            nueva_definicion = input("Escribe la nueva definición (o presione Enter para mantener la actual): ")
            if nuevo_comando == "":
                nuevo_comando = comando  # Si no se ingresa un nuevo comando, se mantiene el actual
            if nueva_definicion == "":
                nueva_definicion = definicion  # Si no se ingresa una nueva definición, se mantiene la actual
            # Actualiza el comando en la lista de comandos con el nuevo comando y la nueva definición
            comandos[numero_comando] = nuevo_comando + "\t" + nueva_definicion + "\n"
            # Abre el archivo "comandos.txt" en modo de escritura (write)
            with open("comandos.txt", "w") as archivo:
                # Escribe las líneas actualizadas de comandos en el archivo
                archivo.writelines(comandos)
            print("-----------------------------")
            print("Comando editado exitosamente.")
            print("-----------------------------")
        else:
            print(
                "-----------------------------------------------------------------------------------------")
            print(
                f"El comando en la línea {numero_comando + 1} no tiene un formato válido: {comando_actual}")
            print(
                "-----------------------------------------------------------------------------------------")
    else:
        print("----------------------------------------------------------------")
        print("Número de comando inválido. ¡¡ Fíjate un poco y escribe un número válido !!")
        print("----------------------------------------------------------------")


def buscar_comandos():
    # Solicita al usuario que seleccione una opción de búsqueda (por definición o por nombre)
    opcion = input(
        "1. Buscar por definición\n2. Buscar por nombre\nSelecciona una opción: ")
    if opcion == "1":
        # Si la opción seleccionada es 1 (buscar por definición)
        definicion = input("Escribe la definición a buscar: ")
        # Abre el archivo "comandos.txt" en modo de lectura (read)
        with open("comandos.txt", "r") as archivo:
            # Lee todas las líneas del archivo y las guarda en la variable "comandos" como una lista de strings
            comandos = archivo.readlines()
            # Variable para rastrear si se encontraron comandos con la definición buscada
            encontrados = False
            # Itera sobre cada comando en la lista de comandos con su índice correspondiente
            for i, comando in enumerate(comandos):
                # Verifica si la definición buscada se encuentra en el comando actual (ignorando mayúsculas y minúsculas)
                if definicion.lower() in comando.lower():
                    # Divide el comando en sus componentes (comando y definición) utilizando el tabulador "\t" como separador
                    comando, definicion = comando.strip().split("\t")
                    # Imprime el número de comando, el comando y su definición
                    print(f"{i+1}. Comando: {comando}")
                    print(f"   Definición: {definicion}")
                    # Imprime una línea de separación para cada comando encontrado
                    print("-" * 40)
                    # Actualiza la variable "encontrados" para indicar que se encontraron comandos
                    encontrados = True
            # Si no se encontraron comandos con la definición buscada, imprime un mensaje
            if not encontrados:
                print("----------------------------------------------")
                print("No se encontraron comandos con esa definición.")
                print("----------------------------------------------")
    elif opcion == "2":
        # Si la opción seleccionada es 2 (buscar por nombre)
        nombre = input("Ingresa el nombre a buscar: ")
        # Abre el archivo "comandos.txt" en modo de lectura (read)
        with open("comandos.txt", "r") as archivo:
            # Lee todas las líneas del archivo y las guarda en la variable "comandos" como una lista de strings
            comandos = archivo.readlines()
            # Variable para rastrear si se encontraron comandos con el nombre buscado
            encontrados = False
            # Itera sobre cada comando en la lista de comandos con su índice correspondiente
            for i, comando in enumerate(comandos):
                # Verifica si el nombre buscado se encuentra en el primer elemento del comando actual (ignorando mayúsculas y minúsculas)
                if nombre.lower() in comando.lower().split('\t')[0]:
                    # Divide el comando en sus componentes (comando y definición) utilizando el tabulador "\t" como separador
                    comando, definicion = comando.strip().split("\t")
                    # Imprime el número de comando, el comando y su definición
                    print(f"{i+1}. Comando: {comando}")
                    print(f"   Definición: {definicion}")
                    print("-" * 40)
                    encontrados = True
            if not encontrados:
                print("------------------------------------------")
                print("No se encontraron comandos con ese nombre.")
                print("------------------------------------------")
    else:
        print("---------------------------------------------------------")
        print("¡¡ Opción inválida !! No seas cabezón y selecciona una opción válida.")
        print("---------------------------------------------------------")


def eliminar_comando():
    # Abre el archivo "comandos.txt" en modo de lectura (read)
    with open("comandos.txt", "r") as archivo:
        # Lee todas las líneas del archivo y las guarda en la variable "comandos" como una lista de strings
        comandos = archivo.readlines()
    if comandos:
        # Si existen comandos en la lista
        print("Comandos disponibles para eliminar:")
        # Itera sobre cada comando en la lista de comandos con su índice correspondiente
        for i, comando in enumerate(comandos):
            # Elimina los espacios en blanco al principio y al final del comando
            comando = comando.strip()
            # Divide el comando en sus componentes (comando y definición) utilizando el tabulador "\t" como separador
            comando_info = comando.split("\t")
            if len(comando_info) >= 2:
                # Si el comando tiene un formato válido (comando y definición), extrae el comando y la definición
                comando = comando_info[0]
                definicion = "\t".join(comando_info[1:])
                # Imprime el número de comando, el comando y su definición
                print(f"{i+1}. Comando: {comando}")
                print(f"   Definición: {definicion}")
                # Imprime una línea de separación para cada comando
                print("-" * 40)
            else:
                # Si el comando no tiene un formato válido, imprime un mensaje de error
                print("-------------------------------------------------------------------")
                print(f"El comando en la línea {i+1} no tiene un formato válido: {comando}")
                print("-------------------------------------------------------------------")
        # Solicita al usuario seleccionar el número del comando que desea eliminar
        seleccion = input("Selecciona el número del comando que deseas eliminar (o '0' para cancelar): ")
        if seleccion == "0":
            return  # Si la selección es 0, se cancela la eliminación
        try:
            seleccion = int(seleccion)
            if seleccion >= 1 and seleccion <= len(comandos):
                # Si la selección es un número válido, elimina el comando correspondiente de la lista de comandos
                del comandos[seleccion-1]
                # Abre el archivo "comandos.txt" en modo de escritura (write)
                with open("comandos.txt", "w") as archivo:
                    # Escribe las líneas actualizadas de comandos en el archivo
                    archivo.writelines(comandos)
                print("-------------------------------")
                print("¡¡ Comando eliminado exitosamente !!")
                print("-------------------------------")
            else:
                print("-------------------")
                print("¡¡ Selección inválida !!")
                print("-------------------")
        except ValueError:
            print("-------------------")
            print("¡¡ Selección inválida !!")
            print("-------------------")
    else:
        print("--------------------------")
        print("No hay comandos guardados.")
        print("--------------------------")

# Menú principal
while True:
    print("-----------------------")
    print("| MENÚ - SIN GLUTEN - |")
    print("-----------------------")
    print("1. Guardar comando")
    print("2. Consultar comandos")
    print("3. Editar comando")
    print("4. Buscar comandos")
    print("5. Eliminar comando")
    print("6. Buscar en Google")
    print("7. Borrar pantalla")
    print("8. Salir")
    opcion = input("Selecciona una opción: ")
    if opcion == "1":
        guardar_comando()
    elif opcion == "2":
        consultar_comandos()
    elif opcion == "3":
        editar_comando()
    elif opcion == "4":
        buscar_comandos()
    elif opcion == "5":
        eliminar_comando()
    elif opcion == "6":
        buscar_en_google()
    elif opcion == "7":
        borrar_pantalla()
    elif opcion == "8":
        break
    else:
        print("Opción inválida. ¡¡ No seas ocurrente y selecciona una opción válida!!.")
