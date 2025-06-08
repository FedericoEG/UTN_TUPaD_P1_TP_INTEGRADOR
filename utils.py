from colorama import Fore, Back, Style

from os import system as os_system
from platform import system as pl_system

# from constants import OPTIONS

def clear_console():
  if pl_system() == "Windows":
    os_system('cls')
  else:
    os_system('clear')

def show_welcome():
  clear_console()
  print(Fore.GREEN + f"======================= Bienvenido =======================")
  print(Fore.GREEN + f"Esta es una aplicación creada por alumnos de la comisión\n14 de la Tecnicatura Universitaria en programación\ndictada por la UTN. Corresponde al trabajo integrador de\nla materia PROGRAMACIÓN I. Se realizará una comparativa\nde un árbol BTS y un árbol tipo B. Ambos árboles tendrán\nla misma cantidad de elementos y se realizará la búsqueda\nde un elemento al azar y de uno no comprendido en los\nárboles con el fin de obtener parámetros de tiempo.")
  print(Fore.RESET)

def validate_input(input_value, min_value, max_value):
    try:
        value = int(input_value)
        if min_value <= value <= max_value:
            return True, value
        else:
            return False, None
    except ValueError:
        return False, None

def show_resume(nodes, grade, existing_elem, unexisting_elem, bts_tree_ex, bts_tree_unex, b_tree_ex, b_tree_unex):
  clear_console()
  print(Fore.MAGENTA + f"======================= Análisis de Datos =======================")
  print()
  print(f"Cantidad de elementos en los árboles: {nodes}")
  print(f"Grado del árbol tipo B: {grade}")
  print(f"Elemento existente buscado en ámbos árboled: {existing_elem}")
  print(f"Elemento NO existente buscado en ámbos árboled: {unexisting_elem}")
  print(f"Tiempo en árbol BTS para elemento existente: {bts_tree_ex: .9f}")
  print(f"Tiempo en árbol B para elemento existente: {b_tree_ex: .9f}")
  print(f"Tiempo en árbol BTS para elemento NO existente: {bts_tree_unex: .9f}")
  print(f"Tiempo en árbol B para elemento NO existente: {b_tree_unex: .9f}")
  print()
  print(Fore.MAGENTA + f"======================= Análisis de Datos =======================" + Fore.RESET)