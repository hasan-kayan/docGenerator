import os

def generate_directory_schema(directory_path):
    # Ensure the directory path exists
    if not os.path.isdir(directory_path):
        print(f"Error: {directory_path} is not a valid directory.")
        return

    # Print the directory path
    print(f"Directory: {directory_path}")

    # Recursively traverse the directory
    _generate_directory_schema_recursive(directory_path, 0)


def _generate_directory_schema_recursive(directory_path, depth):
    # Get the list of files and folders in the current directory
    items = os.listdir(directory_path)

    # Iterate over each item
    for item in items:
        # Construct the full path of the item
        item_path = os.path.join(directory_path, item)

        # Determine indentation based on the depth
        indentation = "    " * depth

        # Print the item with appropriate indentation
        print(f"{indentation}{item}")

        # Recursively call the function if the item is a directory
        if os.path.isdir(item_path):
            _generate_directory_schema_recursive(item_path, depth + 1)


if __name__ == "__main__":
    import sys

    # Check if the command-line argument is provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)

    # Get the directory path from the command-line argument
    directory_path = sys.argv[1]

    # Generate and print the directory schema
    generate_directory_schema(directory_path)
