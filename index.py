import os
import webbrowser
import platform

# Códigos de escape ANSI para colores
COLOR_RESET = "\033[0m"
COLOR_VERDE = "\033[32m"
COLOR_AMARILLO = "\033[33m"
COLOR_ROJO = "\033[31m"
COLOR_CIAN = "\033[36m"
COLOR_NARANJA = "\033[38;5;208m"
TEXTO_NEGRITA = "\033[1m"
TEXTO_SUBRAYADO = "\033[4m"

# Función para pausar la ejecución
def pausa():
    input("Pulsa Intro para continuar...")

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

def guardar_concepto():
    # Solicitamos al usuario que escriba el concepto a guardar
    comando = input(f"{COLOR_NARANJA}-> Escribe del concepto: {COLOR_RESET}")

    # Verifica si el comando no está vacío
    if not comando.strip():
        print(f"{COLOR_ROJO}El comando no puede estar vacío.{COLOR_RESET}")
        pausa()
        return

    # Verificamos si el archivo "conceptos.txt" existe
    if not os.path.exists(conceptos):
        # Si el archivo no existe, lo creamos
        with open(conceptos, "w") as archivo:
            archivo.write("")  # Escribimos una cadena vacía para crear el archivo

    # Abre el archivo "conceptos.txt" en modo lectura
    with open(conceptos, "r") as archivo:
        # Lee el contenido del archivo y comprueba si el concepto ya existe
        comandos_existentes = [line.split("\t")[0] for line in archivo]
        if comando in comandos_existentes:
            # Devuele el mensaje si el concepto existe dentro del archivo txt
            print(f"{COLOR_ROJO}------------------------------------------------{COLOR_RESET}")
            print(f"{COLOR_ROJO}| El concepto ya existe. Modifica su definción |{COLOR_RESET}")
            print(f"{COLOR_ROJO}------------------------------------------------{COLOR_RESET}")
            pausa()
            return
    # Solicitamos al usuario que escriba la definición del concepto
    definicion = input(f"{COLOR_NARANJA}-> Escribe la definición del concepto: {COLOR_RESET}")

    # Verifica si la definición no está vacía
    if not definicion.strip():
        print(f"{COLOR_ROJO}La definición no puede estar vacía.{COLOR_RESET}")
        pausa()
        return

    # Abre el archivo "conceptos.txt" en modo de apendizaje (append)
    # El modo de apendizaje permite añadir contenido al final del archivo sin sobrescribirlo
    with open(conceptos, "a") as archivo:
        # Escribe el concepto y la definición en el archivo, separados por un tabulador "\t"
        # Añade también un salto de línea "\n" para separar los comandos en el archivo
        archivo.write(comando + "\t" + definicion + "\n")
    # Imprime un mensaje de confirmación indicando que el comando se ha guardado correctamente
    print(f"{COLOR_VERDE}--------------------------------{COLOR_RESET}")
    print(f"{COLOR_VERDE}| Concepto guardado con éxito!! |{COLOR_RESET}")
    print(f"{COLOR_VERDE}--------------------------------{COLOR_RESET}")
    pausa()

def consultar_conceptos():
    # Verifica si el archivo "conceptos.txt" existe
    if not os.path.exists(conceptos):
        print(f"{COLOR_ROJO}El archivo en el que se guardan los conceptos no existe.{COLOR_RESET}")
        pausa()
        return
    
    # Abre el archivo "conceptos.txt" en modo de lectura (read)
    with open(conceptos, "r") as archivo:
        # Lee todas las líneas del archivo y las guarda en la variable "comandos" como una lista de strings
        comandos = archivo.readlines()
        # Verifica si hay conceptos en la lista
        if comandos:
            print(f"{COLOR_CIAN}-----------------------{COLOR_RESET}")
            print(f"{COLOR_CIAN}| Conceptos guardados: |{COLOR_RESET}")
            print(f"{COLOR_CIAN}-----------------------{COLOR_RESET}")
            # Itera sobre cada concepto en la lista de comandos con su índice correspondiente
            for i, comando in enumerate(comandos):
                # Elimina los espacios en blanco y caracteres de nueva línea al inicio y final del concepto
                comando = comando.strip()
                # Divide el concepto en una lista utilizando el tabulador "\t" como separador
                comando_info = comando.split("\t")
                # Verifica si el concepto tiene al menos dos elementos en la lista (comando y definición)
                if len(comando_info) >= 2:
                    # Extrae el primer elemento de la lista como el concepto
                    comando = comando_info[0]
                    # Une los elementos restantes de la lista como la definición, separados por un tabulador "\t"
                    definicion = "\t".join(comando_info[1:])
                    # Imprime el número de comando, el concepto y su definición
                    print(f"{TEXTO_NEGRITA}{i+1}. Concepto:{COLOR_RESET} {comando}")
                    print(f"{TEXTO_NEGRITA}   Definición: {COLOR_RESET}{definicion}")
                    # Imprime una línea de separación para cada comando
                    print("-" * 40)
                else:
                    # Imprime un mensaje de error indicando que el concepto no tiene un formato válido
                    print(
                        f"{COLOR_ROJO}-------------------------------------------------------------------{COLOR_RESET}")
                    print(
                        f"{COLOR_ROJO}El concepto en la línea {i+1} no tiene un formato válido: {comando}{COLOR_RESET}")
                    print(
                        f"{COLOR_ROJO}-------------------------------------------------------------------{COLOR_RESET}")
            pausa()
        else:
            # Imprime un mensaje indicando que no hay conceptos guardados
            print(f"{COLOR_ROJO}------------------------------------{COLOR_RESET}")
            print(f"{COLOR_ROJO}| ¡¡ No hay conceptos guardados !! |{COLOR_RESET}")
            print(f"{COLOR_ROJO}------------------------------------{COLOR_RESET}")
            pausa()


def editar_concepto():
    # Verifica si el archivo "conceptos.txt" existe
    if not os.path.exists(conceptos):
        print(f"{COLOR_ROJO}El archivo en el que se guardan los conceptos no existe.{COLOR_RESET}")
        pausa()
        return
    
    # Abre el archivo "conceptos.txt" en modo de lectura (read)
    with open(conceptos, "r") as archivo:
        # Lee todas las líneas del archivo y las guarda en la variable "comandos" como una lista de strings
        comandos = archivo.readlines()

    if comandos:
        # Si existen conceptos en la lista
        print(f"{COLOR_AMARILLO}----------------------------------------{COLOR_RESET}")
        print(f"{COLOR_AMARILLO}| Conceptos disponibles para editar: |{COLOR_RESET}")
        print(f"{COLOR_AMARILLO}----------------------------------------{COLOR_RESET}")

        # Itera sobre cada concepto en la lista con su índice correspondiente
        for i, comando in enumerate(comandos):
            # Elimina los espacios en blanco al principio y al final del comando
            comando = comando.strip()
            # Divide el comando en sus componentes (concepto y definición) utilizando el tabulador "\t" como separador
            comando_info = comando.split("\t")
            if len(comando_info) >= 2:
                # Si el concepto tiene un formato válido (concepto y definición), extrae el concepto y su definición
                comando = comando_info[0]
                definicion = "\t".join(comando_info[1:])
                # Imprime el número del concepto, el nombre del concepto y su definición
                print(f"{i+1}. Concepto: {comando}")
                print(f"   Definición: {definicion}")
                # Imprime una línea de separación para cada concepto
                print("-" * 40)
            else:
                # Si el concepto no tiene un formato válido, imprime un mensaje de error
                print(f"{COLOR_ROJO}-------------------------------------------------------------------{COLOR_RESET}")
                print(f"{COLOR_ROJO}El concepto en la línea {i+1} no tiene un formato válido: {comando}{COLOR_RESET}")
                print(f"{COLOR_ROJO}-------------------------------------------------------------------{COLOR_RESET}")

        # Solicita al usuario el número del concepto a editar y resta 1 para obtener el índice correspondiente
        while True:
            seleccion = input(f"{COLOR_NARANJA}-> Escribe el número del concepto a editar (o '0' para cancelar): {COLOR_RESET}")
            if seleccion == "0":
                return  # Si la selección es 0, se cancela la edición
            try:
                numero_comando = int(seleccion) - 1
                if numero_comando >= 0 and numero_comando < len(comandos):
                    break  # Si la selección es un número válido, se sale del bucle
                else:
                    print(f"{COLOR_ROJO}----------------------------{COLOR_RESET}")
                    print(f"{COLOR_ROJO}| ¡¡ Selección inválida !! |{COLOR_RESET}")
                    print(f"{COLOR_ROJO}----------------------------{COLOR_RESET}")
            except ValueError:
                print(f"{COLOR_ROJO}--------------------------------------------{COLOR_RESET}")
                print(f"{COLOR_ROJO}| ¡¡ Debes ingresar un número válido !! |{COLOR_RESET}")
                print(f"{COLOR_ROJO}--------------------------------------------{COLOR_RESET}")

        comando_actual = comandos[numero_comando].strip()
        comando_info = comando_actual.split("\t")
        if len(comando_info) >= 2:
            comando = comando_info[0]
            definicion = "\t".join(comando_info[1:])
            print(f"-> Concepto actual: {comando}")
            print(f"-> Definición actual: {definicion}")
            nuevo_comando = input(f"{COLOR_NARANJA}* Teclea el nuevo nombre para el concepto (o pulsa Intro para mantener el actual): {COLOR_RESET}")
            nueva_definicion = input(f"{COLOR_NARANJA}* Escribe la nueva definición (o pulsa Intro para mantener la actual): {COLOR_RESET}")
            if nuevo_comando == "":
                nuevo_comando = comando
            if nueva_definicion == "":
                nueva_definicion = definicion
            comandos[numero_comando] = nuevo_comando + "\t" + nueva_definicion + "\n"
            with open(conceptos, "w") as archivo:
                archivo.writelines(comandos)
            print(f"{COLOR_VERDE}----------------------------------{COLOR_RESET}")
            print(f"{COLOR_VERDE}| Concepto editado correctamente |{COLOR_RESET}")
            print(f"{COLOR_VERDE}----------------------------------{COLOR_RESET}")
        else:
            print(
                f"{COLOR_ROJO}-----------------------------------------------------------------------------------------{COLOR_RESET}")
            print(
                f"{COLOR_ROJO}El concepto en la línea {numero_comando + 1} no tiene un formato válido: {comando_actual}{COLOR_RESET}")
            print(
                f"{COLOR_ROJO}-----------------------------------------------------------------------------------------{COLOR_RESET}")
    else:
        print(f"{COLOR_ROJO}------------------------------{COLOR_RESET}")
        print(f"{COLOR_ROJO}| No hay conceptos guardados |{COLOR_RESET}")
        print(f"{COLOR_ROJO}------------------------------{COLOR_RESET}")


def buscar_concepto():
    # Verifica si el archivo "conceptos.txt" existe
    if not os.path.exists(conceptos):
        print(f"{COLOR_ROJO}El archivo en el que se guardan los conceptos no existe.{COLOR_RESET}")
        pausa()
        return
    
    # Solicita al usuario que seleccione una opción de búsqueda (por definición o por nombre)
    opcion = input(
        f"{TEXTO_NEGRITA}1. Buscar por definición\n2. Buscar por nombre\nSelecciona una opción: {COLOR_RESET}")
    if opcion == "1":
        # Si la opción seleccionada es 1 (buscar por definición)
        definicion = input(f"{COLOR_NARANJA}Escribe la definición a buscar: {COLOR_RESET}")
        # Abre el archivo "conceptos.txt" en modo de lectura (read)
        with open(conceptos, "r") as archivo:
            # Lee todas las líneas del archivo y las guarda en la variable "comandos" como una lista de strings
            comandos = archivo.readlines()
            # Variable para rastrear si se encontraron conceptos con la definición buscada
            encontrados = False
            # Itera sobre cada concepto en la lista con su índice correspondiente
            for i, comando in enumerate(comandos):
                # Verifica si la definición buscada se encuentra en el concepto actual (ignorando mayúsculas y minúsculas)
                if definicion.lower() in comando.lower():
                    # Divide el comando en sus componentes (concepto y definición) utilizando el tabulador "\t" como separador
                    comando, definicion = comando.strip().split("\t")
                    # Imprime el número del concepto, el nombre del concepto y su definición
                    print(f"{i+1}. Concepto: {comando}")
                    print(f"   Definición: {definicion}")
                    # Imprime una línea de separación para cada concepto encontrado
                    print("-" * 40)
                    # Actualiza la variable "encontrados" para indicar que se encontraron conceptos
                    encontrados = True
                    pausa()
            # Si no se encontraron conceptos con la definición buscada, imprime un mensaje
            if not encontrados:
                print(f"{COLOR_ROJO}--------------------------------------------------{COLOR_RESET}")
                print(f"{COLOR_ROJO}| No se encontraron conceptos con esa definición |{COLOR_RESET}")
                print(f"{COLOR_ROJO}--------------------------------------------------{COLOR_RESET}")
                pausa()
    elif opcion == "2":
        # La opción seleccionada es 2 buscar por nombre
        nombre = input(f"{COLOR_NARANJA}-> Escribe el nombre a buscar: {COLOR_RESET}")
        # Abre el archivo "conceptos.txt" en modo de lectura (read)
        with open(conceptos, "r") as archivo:
            # Lee todas las líneas del archivo y las guarda en la variable "comandos" como una lista de strings
            comandos = archivo.readlines()
            # Variable para rastrear si se encontraron conceptos con el nombre buscado
            encontrados = False
            # Itera sobre cada concepto en la lista con su índice correspondiente
            for i, comando in enumerate(comandos):
                # Verifica si el nombre buscado se encuentra en el primer elemento del concepto actual (ignorando mayúsculas y minúsculas)
                if nombre.lower() in comando.lower().split('\t')[0]:
                    # Divide el comando en sus componentes (concepto y definición) utilizando el tabulador "\t" como separador
                    comando, definicion = comando.strip().split("\t")
                    # Imprime el número de concepto, el nombre del concepto y su definición
                    print(f"{i+1}. Concepto: {comando}")
                    print(f"   Definición: {definicion}")
                    print("-" * 40)
                    encontrados = True
                    pausa()
            if not encontrados:
                print(f"{COLOR_ROJO}----------------------------------------------{COLOR_RESET}")
                print(f"{COLOR_ROJO}| No se encontraron conceptos con ese nombre |{COLOR_RESET}")
                print(f"{COLOR_ROJO}----------------------------------------------{COLOR_RESET}")
                pausa()
    else:
        print(f"{COLOR_ROJO}------------------------------------------------------------------------{COLOR_RESET}")
        print(f"{COLOR_ROJO}| ¡¡ Opción inválida !! No seas cabezón y selecciona una opción válida |{COLOR_RESET}")
        print(f"{COLOR_ROJO}------------------------------------------------------------------------{COLOR_RESET}")
        pausa()


def eliminar_concepto():
    # Abre el archivo "conceptos.txt" en modo de lectura (read)
    with open(conceptos, "r") as archivo:
        # Lee todas las líneas del archivo y las guarda en la variable "comandos" como una lista de strings
        comandos = archivo.readlines()
    if comandos:
        # Si existen conceptos en la lista
        print(f"{COLOR_AMARILLO}----------------------------------------{COLOR_RESET}")
        print(f"{COLOR_AMARILLO}| Conceptos disponibles para eliminar: |{COLOR_RESET}")
        print(f"{COLOR_AMARILLO}----------------------------------------{COLOR_RESET}")
        # Itera sobre cada concepto en la lista con su índice correspondiente
        for i, comando in enumerate(comandos):
            # Elimina los espacios en blanco al principio y al final del comando
            comando = comando.strip()
            # Divide el comando en sus componentes (concepto y definición) utilizando el tabulador "\t" como separador
            comando_info = comando.split("\t")
            if len(comando_info) >= 2:
                # Si el concepto tiene un formato válido (concepto y definición), extrae el concepto y su definición
                comando = comando_info[0]
                definicion = "\t".join(comando_info[1:])
                # Imprime el número del concepto, el nombre del concepto y su definición
                print(f"{i+1}. Concepto: {comando}")
                print(f"   Definición: {definicion}")
                # Imprime una línea de separación para cada concepto
                print("-" * 40)
                
            else:
                # Si el concepto no tiene un formato válido, imprime un mensaje de error
                print(f"{COLOR_ROJO}-------------------------------------------------------------------{COLOR_RESET}")
                print(f"{COLOR_ROJO}El concepto en la línea {i+1} no tiene un formato válido: {comando}{COLOR_RESET}")
                print(f"{COLOR_ROJO}-------------------------------------------------------------------{COLOR_RESET}")
        pausa()
        # Solicita al usuario seleccionar el número del concepto que quiere eliminar
        seleccion = input(f"{COLOR_NARANJA}-> Selecciona el número del concepto que quieras eliminar (o '0' para cancelar): {COLOR_RESET}")
        if seleccion == "0":
            return  # Si la selección es 0, se cancela la eliminación
        try:
            seleccion = int(seleccion)
            if seleccion >= 1 and seleccion <= len(comandos):
                # Si la selección es un número válido, elimina el concepto correspondiente de la lista de conceptos
                del comandos[seleccion-1]
                # Abre el archivo "conceptos.txt" en modo de escritura (write)
                with open(conceptos, "w") as archivo:
                    # Escribe las líneas actualizadas de conceptos en el archivo
                    archivo.writelines(comandos)
                print(f"{COLOR_VERDE}-----------------------------------------{COLOR_RESET}")
                print(f"{COLOR_VERDE}| ¡¡ Concepto eliminado exitosamente !! |{COLOR_RESET}")
                print(f"{COLOR_VERDE}-----------------------------------------{COLOR_RESET}")
                pausa()
            else:
                print(f"{COLOR_ROJO}----------------------------{COLOR_RESET}")
                print(f"{COLOR_ROJO}| ¡¡ Selección inválida !! |{COLOR_RESET}")
                print(f"{COLOR_ROJO}----------------------------{COLOR_RESET}")
                pausa()
        except ValueError:
            print(f"{COLOR_ROJO}----------------------------{COLOR_RESET}")
            print(f"{COLOR_ROJO}| ¡¡ Selección inválida !! |{COLOR_RESET}")
            print(f"{COLOR_ROJO}----------------------------{COLOR_RESET}")
            pausa()
    else:
        print(f"{COLOR_AMARILLO}------------------------------{COLOR_RESET}")
        print(f"{COLOR_AMARILLO}| No hay conceptos guardados |{COLOR_RESET}")
        print(f"{COLOR_AMARILLO}------------------------------{COLOR_RESET}")
        pausa()

# Menú principal
def main_menu():
    while True:
        borrar_pantalla()
        print(f"{COLOR_CIAN}-----------------------{COLOR_RESET}")
        print(f"{COLOR_CIAN}| MENÚ - SIN GLUTEN - |{COLOR_RESET}")
        print(f"{COLOR_CIAN}-----------------------{COLOR_RESET}")
        print(f"{TEXTO_SUBRAYADO} Bajo un sistema {sistema_operativo} {COLOR_RESET}")
        print("-----------------------")
        print(f"{TEXTO_NEGRITA}1. Guardar concepto{COLOR_RESET}")
        print(f"{TEXTO_NEGRITA}2. Consultar conceptos{COLOR_RESET}")
        print(f"{TEXTO_NEGRITA}3. Editar concepto{COLOR_RESET}")
        print(f"{TEXTO_NEGRITA}4. Buscar concepto{COLOR_RESET}")
        print(f"{TEXTO_NEGRITA}5. Eliminar concepto{COLOR_RESET}")
        print(f"{TEXTO_NEGRITA}6. Buscar en Google{COLOR_RESET}")
        print(f"{TEXTO_NEGRITA}7. Salir{COLOR_RESET}")
        opcion = input(f"{COLOR_NARANJA}-> Selecciona una opción: {COLOR_RESET}")
        if opcion == "1":
            guardar_concepto()
        elif opcion == "2":
            consultar_conceptos()
        elif opcion == "3":
            editar_concepto()
        elif opcion == "4":
            buscar_concepto()
        elif opcion == "5":
            eliminar_concepto()
        elif opcion == "6":
            buscar_en_google()
        elif opcion == "7":
            break
        else:
            print(f"{COLOR_AMARILLO}--------------------------------------------------------------------------{COLOR_RESET}")
            print(f"{COLOR_AMARILLO}| Opción inválida. ¡¡ No seas ocurrente y selecciona una opción válida!! |{COLOR_RESET}")
            print(f"{COLOR_AMARILLO}--------------------------------------------------------------------------{COLOR_RESET}")
            pausa()

if __name__ == "__main__":
    sistema_operativo = platform.system()
    conceptos = "conceptos.txt"
    main_menu()
