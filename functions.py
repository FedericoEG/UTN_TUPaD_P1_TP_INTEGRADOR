import time

def insert_node_bts(tree, value):
  if not tree:
    return [value,[],[]]
  if value == tree[0]:
    return tree
  if value < tree[0]:
    tree[1] = insert_node_bts(tree[1], value)
  else:
    tree[2] = insert_node_bts(tree[2], value)
  return tree

def search_node_bst(tree, value):
  if not tree:
    return False
  if value == tree[0]:
    return True
  if value < tree[0]:
    return search_node_bst(tree[1], value)
  else:
    return search_node_bst(tree[2], value)

def insert_node_b(tree, value, grade=3):
  if not tree:
    return [value, []]

  new_tree = insert_in_node(tree, value, grade)
  if isinstance(new_tree, tuple):
    prom_key, (left, right) = new_tree
    return [prom_key, [left, right]]

  return new_tree

def insert_in_node(node, value, grade):
  keys = node[:-1].copy()
  children = node[-1].copy()

  if not children:
    keys.append(value)
    keys.sort()

    if len(keys) == grade:
      mid = grade // 2
      prom_key = keys[mid]

      left_keys = keys[:mid]
      right_keys = keys[mid + 1:]

      left_node = left_keys + [[]]
      right_node = right_keys + [[]]

      return prom_key, (left_node, right_node)
    else:
      return keys + [[]]

  else:
    i = 0
    while i < len(keys) and value > keys[i]:
      i += 1

    resp = insert_in_node(children[i], value, grade)

    if isinstance(resp, tuple):
      prom_key, (left, right) = resp
      keys.insert(i, prom_key)
      children[i] = left
      children.insert(i + 1, right)

      if len(keys) == grade:
        mid = grade // 2
        prom_key = keys[mid]

        left_keys = keys[:mid]
        left_children = children[:mid + 1]
        left_node = left_keys + [left_children]

        right_keys = keys[mid + 1:]
        right_children = children[mid + 1:]
        right_node = right_keys + [right_children]

        return prom_key, (left_node, right_node)
      else:
        return keys + [children]
    else:
      children[i] = resp
      return keys + [children]

def search_node_b(node, value):
  if not node:
    return False

  keys = node[:-1]
  children = node[-1]

  i = 0
  while i < len(keys) and value > keys[i]:
    i += 1

  if i < len(keys) and value == keys[i]:
    return True

  if not children:
    return False

  return search_node_b(children[i], value)

def search_and_chrono(tree, value, search_func):
  start = time.time()
  search = search_func(tree, value)
  stop = time.time()
  seconds = stop - start
  return seconds, search