import os
import webbrowser
import platform

# Guardamos el sistema operativo sobre el que está funcionando el scritp
sistema_operativo = platform.system()

# Códigos de escape ANSI para colores
COLOR_RESET = "\033[0m"
COLOR_VERDE = "\033[32m"
COLOR_AMARILLO = "\033[33m"
COLOR_ROJO = "\033[31m"
COLOR_CIAN = "\033[36m"
COLOR_NARANJA = "\033[38;5;208m"
TEXTO_NEGRITA = "\033[1m"
TEXTO_SUBRAYADO = "\033[4m"

def buscar_en_google():
    # Solicita al usuario el término de búsqueda
    busqueda = input(f"{COLOR_NARANJA}Escribe el término de búsqueda: {COLOR_RESET}")
    # Crea la URL de búsqueda en Google con el término ingresado
    url = f"https://www.google.com/search?q={busqueda}"
    # Abre la URL en el navegador web predeterminado
    webbrowser.open(url)
    print(f"{COLOR_AMARILLO}------------------------------------------{COLOR_RESET}")
    print(f"{COLOR_AMARILLO}| Búsqueda realizada en Google con éxito |{COLOR_RESET}")
    print(f"{COLOR_AMARILLO}------------------------------------------{COLOR_RESET}")

def borrar_pantalla():
    # Limpia la pantalla según el sistema operativo
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{COLOR_VERDE}---------------------------------{COLOR_RESET}")
    print(f"{COLOR_VERDE}| Pantalla borrada exitosamente |{COLOR_RESET}")
    print(f"{COLOR_VERDE}---------------------------------{COLOR_RESET}")

def guardar_comando():
    # Solicitamos al usuario que escriba el concepto a guardar
    comando = input(f"{COLOR_NARANJA}-> Escribe del concepto: {COLOR_RESET}")

    # Abre el archivo "comandos.txt" en modo lectura
    with open("comandos.txt", "r") as archivo:
        # Lee el contenido del archivo y comprueba si el concepto ya existe
        comandos_existentes = [line.split("\t")[0] for line in archivo]
        if comando in comandos_existentes:
            # Devuele el mensaje si el concepto existe dentro del archivo txt
            print(f"{COLOR_ROJO}------------------------------------------------{COLOR_RESET}")
            print(f"{COLOR_ROJO}| El concepto ya existe. Modifica su definción |{COLOR_RESET}")
            print(f"{COLOR_ROJO}------------------------------------------------{COLOR_RESET}")
            return
    # Solicitamos al usuario que escriba la definición del concepto
    definicion = input(f"{COLOR_NARANJA}-> Escribe la definición del concepto: {COLOR_RESET}")
    # Abre el archivo "comandos.txt" en modo de apendizaje (append)
    # El modo de apendizaje permite añadir contenido al final del archivo sin sobrescribirlo
    with open("comandos.txt", "a") as archivo:
        # Escribe el concepto y la definición en el archivo, separados por un tabulador "\t"
        # Añade también un salto de línea "\n" para separar los comandos en el archivo
        archivo.write(comando + "\t" + definicion + "\n")
    # Imprime un mensaje de confirmación indicando que el comando se ha guardado correctamente
    print(f"{COLOR_VERDE}--------------------------------{COLOR_RESET}")
    print(f"{COLOR_VERDE}| Concepto guardado con éxito!! |{COLOR_RESET}")
    print(f"{COLOR_VERDE}--------------------------------{COLOR_RESET}")

def consultar_comandos():
    # Abre el archivo "comandos.txt" en modo de lectura (read)
    with open("comandos.txt", "r") as archivo:
        # Lee todas las líneas del archivo y las guarda en la variable "comandos" como una lista de strings
        comandos = archivo.readlines()
        # Verifica si hay comandos en la lista
        if comandos:
            print(f"{COLOR_CIAN}-----------------------{COLOR_RESET}")
            print(f"{COLOR_CIAN}| Comandos guardados: |{COLOR_RESET}")
            print(f"{COLOR_CIAN}-----------------------{COLOR_RESET}")
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
                    print(f"{TEXTO_NEGRITA}{i+1}. Comando:{COLOR_RESET} {comando}")
                    print(f"{TEXTO_NEGRITA}   Definición: {COLOR_RESET}{definicion}")
                    # Imprime una línea de separación para cada comando
                    print("-" * 40)
                else:
                    # Imprime un mensaje de error indicando que el comando no tiene un formato válido
                    print(
                        f"{COLOR_ROJO}-------------------------------------------------------------------{COLOR_RESET}")
                    print(
                        f"{COLOR_ROJO}El comando en la línea {i+1} no tiene un formato válido: {comando}{COLOR_RESET}")
                    print(
                        f"{COLOR_ROJO}-------------------------------------------------------------------{COLOR_RESET}")
        else:
            # Imprime un mensaje indicando que no hay comandos guardados
            print(f"{COLOR_ROJO}-----------------------------------{COLOR_RESET}")
            print(f"{COLOR_ROJO}| ¡¡ No hay comandos guardados !! {COLOR_RESET}")
            print(f"{COLOR_ROJO}-----------------------------------{COLOR_RESET}")


def editar_comando():
    # Solicita al usuario el número del comando a editar y resta 1 para obtener el índice correspondiente
    numero_comando = int(input(f"{COLOR_NARANJA}-> Escribe el número del comando a editar: {COLOR_RESET}")) - 1
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
            print(f"-> Comando actual: {comando}")
            print(f"-> Definición actual: {definicion}")
            # Solicita al usuario ingresar el nuevo comando (o presionar Enter para mantener el actual)
            nuevo_comando = input(f"{COLOR_NARANJA}* Teclea el nuevo comando (o presione Enter para mantener el actual): {COLOR_RESET}")
            # Solicita al usuario ingresar la nueva definición (o presionar Enter para mantener la actual)
            nueva_definicion = input(f"{COLOR_NARANJA}* Escribe la nueva definición (o presione Enter para mantener la actual): {COLOR_RESET}")
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
            print(f"{COLOR_VERDE}--------------------------------{COLOR_RESET}")
            print(f"{COLOR_VERDE}| Comando editado exitosamente |{COLOR_RESET}")
            print(f"{COLOR_VERDE}--------------------------------{COLOR_RESET}")
        else:
            print(
                f"{COLOR_ROJO}-----------------------------------------------------------------------------------------{COLOR_RESET}")
            print(
                f"{COLOR_ROJO}El comando en la línea {numero_comando + 1} no tiene un formato válido: {comando_actual}{COLOR_RESET}")
            print(
                f"{COLOR_ROJO}-----------------------------------------------------------------------------------------{COLOR_RESET}")
    else:
        print(f"{COLOR_ROJO}-------------------------------------------------------------------------------{COLOR_RESET}")
        print(f"{COLOR_ROJO}| Número de comando inválido. ¡¡ Fíjate un poco y escribe un número válido !! |{COLOR_RESET}")
        print(f"{COLOR_ROJO}-------------------------------------------------------------------------------{COLOR_RESET}")


def buscar_comandos():
    # Solicita al usuario que seleccione una opción de búsqueda (por definición o por nombre)
    opcion = input(
        "1. Buscar por definición\n2. Buscar por nombre\nSelecciona una opción: ")
    if opcion == "1":
        # Si la opción seleccionada es 1 (buscar por definición)
        definicion = input(f"{COLOR_NARANJA}Escribe la definición a buscar: {COLOR_RESET}")
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
                print(f"{COLOR_ROJO}-------------------------------------------------{COLOR_RESET}")
                print(f"{COLOR_ROJO}| No se encontraron comandos con esa definición |{COLOR_RESET}")
                print(f"{COLOR_ROJO}-------------------------------------------------{COLOR_RESET}")
    elif opcion == "2":
        # Si la opción seleccionada es 2 (buscar por nombre)
        nombre = input(f"{COLOR_NARANJA}-> Escribe el nombre a buscar: {COLOR_RESET}")
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
                print(f"{COLOR_ROJO}---------------------------------------------{COLOR_RESET}")
                print(f"{COLOR_ROJO}| No se encontraron comandos con ese nombre |{COLOR_RESET}")
                print(f"{COLOR_ROJO}---------------------------------------------{COLOR_RESET}")
    else:
        print(f"{COLOR_ROJO}------------------------------------------------------------------------{COLOR_RESET}")
        print(f"{COLOR_ROJO}| ¡¡ Opción inválida !! No seas cabezón y selecciona una opción válida |{COLOR_RESET}")
        print(f"{COLOR_ROJO}------------------------------------------------------------------------{COLOR_RESET}")


def eliminar_comando():
    # Abre el archivo "comandos.txt" en modo de lectura (read)
    with open("comandos.txt", "r") as archivo:
        # Lee todas las líneas del archivo y las guarda en la variable "comandos" como una lista de strings
        comandos = archivo.readlines()
    if comandos:
        # Si existen comandos en la lista
        print(f"{COLOR_AMARILLO}---------------------------------------{COLOR_RESET}")
        print(f"{COLOR_AMARILLO}| Comandos disponibles para eliminar: |{COLOR_RESET}")
        print(f"{COLOR_AMARILLO}---------------------------------------{COLOR_RESET}")
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
                print(f"{COLOR_ROJO}-------------------------------------------------------------------{COLOR_RESET}")
                print(f"{COLOR_ROJO}El comando en la línea {i+1} no tiene un formato válido: {comando}{COLOR_RESET}")
                print(f"{COLOR_ROJO}-------------------------------------------------------------------{COLOR_RESET}")
        # Solicita al usuario seleccionar el número del comando que desea eliminar
        seleccion = input(f"{COLOR_NARANJA}-> Selecciona el número del comando que quieras eliminar (o '0' para cancelar): {COLOR_RESET}")
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
                print(f"{COLOR_VERDE}----------------------------------------{COLOR_RESET}")
                print(f"{COLOR_VERDE}| ¡¡ Comando eliminado exitosamente !! |{COLOR_RESET}")
                print(f"{COLOR_VERDE}----------------------------------------{COLOR_RESET}")
            else:
                print(f"{COLOR_ROJO}----------------------------{COLOR_RESET}")
                print(f"{COLOR_ROJO}| ¡¡ Selección inválida !! |{COLOR_RESET}")
                print(f"{COLOR_ROJO}----------------------------{COLOR_RESET}")
        except ValueError:
            print(f"{COLOR_ROJO}----------------------------{COLOR_RESET}")
            print(f"{COLOR_ROJO}| ¡¡ Selección inválida !! |{COLOR_RESET}")
            print(f"{COLOR_ROJO}----------------------------{COLOR_RESET}")
    else:
        print(f"{COLOR_AMARILLO}-----------------------------{COLOR_RESET}")
        print(f"{COLOR_AMARILLO}| No hay comandos guardados |{COLOR_RESET}")
        print(f"{COLOR_AMARILLO}-----------------------------{COLOR_RESET}")

# Menú principal
while True:

    print(f"{COLOR_CIAN}-----------------------{COLOR_RESET}")
    print(f"{COLOR_CIAN}| MENÚ - SIN GLUTEN - |{COLOR_RESET}")
    print(f"{COLOR_CIAN}-----------------------{COLOR_RESET}")
    print(f"{TEXTO_SUBRAYADO} Bajo un sistema {sistema_operativo} {COLOR_RESET}")
    print("-----------------------")
    print(f"{TEXTO_NEGRITA}1. Guardar comando{COLOR_RESET}")
    print(f"{TEXTO_NEGRITA}2. Consultar comandos{COLOR_RESET}")
    print(f"{TEXTO_NEGRITA}3. Editar comando{COLOR_RESET}")
    print(f"{TEXTO_NEGRITA}4. Buscar comandos{COLOR_RESET}")
    print(f"{TEXTO_NEGRITA}5. Eliminar comando{COLOR_RESET}")
    print(f"{TEXTO_NEGRITA}6. Buscar en Google{COLOR_RESET}")
    print(f"{TEXTO_NEGRITA}7. Borrar pantalla{COLOR_RESET}")
    print(f"{TEXTO_NEGRITA}8. Salir{COLOR_RESET}")
    opcion = input(f"{COLOR_NARANJA}-> Selecciona una opción: {COLOR_RESET}")
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
        print(f"{COLOR_AMARILLO}--------------------------------------------------------------------------{COLOR_RESET}")
        print(f"{COLOR_AMARILLO}| Opción inválida. ¡¡ No seas ocurrente y selecciona una opción válida!! |{COLOR_RESET}")
        print(f"{COLOR_AMARILLO}--------------------------------------------------------------------------{COLOR_RESET}")
