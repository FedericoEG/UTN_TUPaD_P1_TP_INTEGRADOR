import random, time
from utils import show_welcome, validate_input, show_resume
from functions import insert_node_bts, search_node_bst, insert_node_b, search_node_b
from constants import B_TREE_GRADE

bts_tree = []
b_tree = []
grade = B_TREE_GRADE

show_welcome()

while True:
  nodes = input("Ingrese un número entero mayor o igual que 1.000 y menor o igual que 5.000, para determinar la cantidad de elementos en los árboles: ")
  valid, number_of_elements = validate_input(nodes, 1000, 5000)
  if valid:
    break
  else:
    print("Error: Debe ingresar un número entero válido mayor que 1.000 y menor que 5.000.")

while True:
  randome_grade = input("Ingrese un número entero mayor o igual que 3 y menor o igual que 9, para utilizar como el grado del árbol tipo B: ")
  valid, number_of_grade = validate_input(randome_grade, 3, 9)
  if valid:
    break
  else:
    print("Error: Debe ingresar un número entero válido mayor que 3 y menor que 9.")

random_values = random.sample(range(1, 5001), number_of_elements)
grade = number_of_grade
search_value_true = random.choice(random_values)
search_value_false = 6000

for v in random_values:
    bts_tree = insert_node_bts(bts_tree, v)
    b_tree = insert_node_b(b_tree, v, grade)

bts_start = time.time()
bts_search = search_node_bst(bts_tree, search_value_true)
bts_stop = time.time()
bts_tree_ex = bts_stop - bts_start

bts_start = time.time()
bts_search = search_node_bst(bts_tree, search_value_false)
bts_stop = time.time()
bts_tree_unex = bts_stop - bts_start

b_start = time.time()
b_search = search_node_b(b_tree, search_value_true)
b_stop = time.time()
b_tree_ex = b_stop - b_start

b_start = time.time()
b_search = search_node_b(b_tree, search_value_false)
b_stop = time.time()
b_tree_unex = b_stop - b_start

show_resume(number_of_elements, grade, search_value_true, search_value_false, bts_tree_ex, bts_tree_unex, b_tree_ex, b_tree_unex)