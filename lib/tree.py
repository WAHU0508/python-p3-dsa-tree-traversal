class Tree:
  def __init__(self, root = None):
    self.root = root
  
  def get_element_by_id(self, id):
    return self.depth_first_traversal(self.root, id)
    
  def depth_first_traversal(self, node, id):
    """1. Check if the current node's id matches the id_value."""
    if node['id'] == id:
      return node

    """2. Traverse through each child node."""
    for child in node['children']:
      result = self.depth_first_traversal(child, id)
      if result:
        return result
    """3. If no matching node is found, return none."""
    return None

  

