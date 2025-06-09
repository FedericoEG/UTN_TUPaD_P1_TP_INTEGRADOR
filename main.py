import random, time
from utils import show_welcome, validate_input, show_resume
from functions import insert_node_bts, search_node_bst, insert_node_b, search_node_b, search_and_chrono
from constants import B_TREE_GRADE

bts_tree = []
b_tree = []
grade = B_TREE_GRADE
random_values = []
search_value_true = 0
search_value_false = 0
med_value = 0

show_welcome()

while True:
  nodes = input("Ingrese un número entero mayor o igual que 1.000 y menor o igual que 5.000.000, para determinar la cantidad de elementos en los árboles: ")
  valid, number_of_elements = validate_input(nodes, 1000, 5000000)
  if valid:
    break
  else:
    print("Error: Debe ingresar un número entero válido mayor que 1.000 y menor que 5.000.")

while True:
  randome_grade = input("Ingrese un número entero mayor o igual que 3 y menor o igual que 9, para utilizar como el grado del árbol tipo B: ")
  valid, number_of_grade = validate_input(randome_grade, 3, 9, True)
  if valid:
    break
  else:
    print("Error: Debe ingresar un número entero válido mayor que 3 y menor que 9.")

if number_of_elements and number_of_grade:
  random_values = random.sample(range(1, number_of_elements+1), number_of_elements)
  grade = number_of_grade
  search_value_true = random.choice(random_values)
  search_value_false = random.randint(number_of_elements * 2, number_of_elements * 3)
  med_value = int(sum(random_values) / len(random_values))

for v in random_values:
    bts_tree = insert_node_bts(bts_tree, v)
    b_tree = insert_node_b(b_tree, v, grade)

bts_tree_ex, bts_tree_ex_find = search_and_chrono(bts_tree, search_value_true, search_node_bst)

bts_tree_unex, bts_tree_unex_find = search_and_chrono(bts_tree, search_value_false, search_node_bst)

bts_tree_med, bts_tree_med_find = search_and_chrono(bts_tree, med_value, search_node_bst)

b_tree_ex, b_tree_ex_find = search_and_chrono(b_tree, search_value_true, search_node_b)

b_tree_unex, b_tree_unex_find = search_and_chrono(b_tree, search_value_false, search_node_b)

b_tree_med, b_tree_med_find = search_and_chrono(b_tree, med_value, search_node_b)

show_resume(number_of_elements, grade, search_value_true, search_value_false, med_value, bts_tree_ex, bts_tree_unex, b_tree_ex, b_tree_unex, bts_tree_med, b_tree_med)