child_1 = {
  'value': 2,
  'children': []
}

child_2 = {
  'value': 3,
  'children': []
}

child_3 = {
  'value': 4,
  'children': []
}

root = {
  'value': 1,
  'children': [child_1, child_2, child_3]
}
def breadth_first_traversal(node):
  result = []
  nodes_to_visit = [node]

  while len(nodes_to_visit) > 0:
    # 1. Remove the first node from the `nodes_to_visit` list
    print(f" 1. {nodes_to_visit}")
    node = nodes_to_visit.pop(0)
    # 2. Add its value to the result list
    result.append(node['value'])
    # 3. Add its children (if any) to the END of the `nodes_to_visit` list
    print(f" 2. {nodes_to_visit}")
    nodes_to_visit = nodes_to_visit + node['children']
    print(f" 3. {nodes_to_visit}")

  return result



def depth_first_traversal(node):
    result = []
    nodes_to_visit = [node]

    while len(nodes_to_visit) > 0:
        print(f" 1. {nodes_to_visit}")
        node = nodes_to_visit.pop(0)
        result.append(node['value'])
        print(f" 2. {nodes_to_visit}")
        nodes_to_visit = node['children'] + nodes_to_visit
        print(f" 3. {nodes_to_visit}")
    return result
    
print(depth_first_traversal(root))