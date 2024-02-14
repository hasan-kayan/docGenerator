import os

def create_directory_tree(directory="."):
    tree = f"Directory Tree for: {directory}\n"
    tree += traverse_directory(0, directory)
    return tree

def traverse_directory(indent_level, directory):
    tree = ""
    for item in os.listdir(directory):
        full_path = os.path.join(directory, item)
        if os.path.isdir(full_path):
            tree += "|   " * indent_level + "+-- " + item + "\n"
            tree += traverse_directory(indent_level + 1, full_path)
        else:
            tree += "|   " * indent_level + "|-- " + item + "\n"
    return tree

if __name__ == "__main__":
    directory_tree = create_directory_tree()
    print(directory_tree)
