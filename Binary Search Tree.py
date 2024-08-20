class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.key)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Insert a node into the binary search tree
    def _insert(self, node, key):
        if node is None:
            return TreeNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node

    def insert(self, key):
        self.root = self._insert(self.root, key)
        
    # Search for a node in the binary search tree
    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)
    
    def search(self, key):
        return self._search(self.root, key)

    # Delete a node from the binary search tree
    def _delete(self, node, key):
        if node is None:
            return node
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key) 
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left   
            node.key = self._min_value(node.right)
            node.right = self._delete(node.right, node.key)   
        return node

    def delete(self, key):
        self.root = self._delete(self.root, key)

    # Find the minimum value in the binary search tree
    def _min_value(self, node):
        while node.left is not None:
            node = node.left
        return node.key

    def find_min(self):
        if self.root is None:
            return None
        return self._min_value(self.root)

    # Find the maximum value in the binary search tree
    def _max_value(self, node):
        while node.right is not None:
            node = node.right
        return node.key

    def find_max(self):
        if self.root is None:
            return None
        return self._max_value(self.root)

    # In-order traversal of the binary search tree
    def _inorder_traversal(self, node, result, level=0):
        if node:
            self._inorder_traversal(node.left, result, level+1)
            result.append((node.key, level))  # Store key with its level
            self._inorder_traversal(node.right, result, level+1)

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

# Main execution
bst = BinarySearchTree()

nodes = list(map(int, input("Enter the values to insert into the tree (separated by spaces): ").split()))

# Insert nodes into the BST
for node in nodes:
    bst.insert(node)

print("In-order Traversal with positions (key, level):", bst.inorder_traversal())

while True:
    print("\nChoose an action:")
    print("1. Insert a new node")
    print("2. Delete a node")
    print("3. Search for a node")
    print("4. Print in-order traversal")
    print("5. Find minimum value")
    print("6. Find maximum value")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        new_key = int(input("Enter the value to insert: "))
        bst.insert(new_key)
        print("Node inserted.")
    elif choice == '2':
        delete_key = int(input("Enter the value to delete: "))
        bst.delete(delete_key)
        print(f"Node with value {delete_key} deleted.")
    elif choice == '3':
        search_key = int(input("Enter the value to search: "))
        search_result = bst.search(search_key)
        print(f"Search for {search_key}: {search_result if search_result else 'Not found'}")
    elif choice == '4':
        print("In-order Traversal with positions (key, level):", bst.inorder_traversal())
    elif choice == '5':
        print("Minimum value in the tree:", bst.find_min())
    elif choice == '6':
        print("Maximum value in the tree:", bst.find_max())
    elif choice == '7':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please choose a number between 1 and 7.")
