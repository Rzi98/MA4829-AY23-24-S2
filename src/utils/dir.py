import os

def print_directory_tree(root_dir, indent='', ignore_dirs=None):
    if ignore_dirs is None:
        ignore_dirs = set(['__pycache__', '.vscode', '.env', '.git', '.gitignore'])

    items = sorted(os.listdir(root_dir), key=lambda s: s.lower())
    
    for i, item in enumerate(items):
        item_path = os.path.join(root_dir, item)
        is_last_item = (i == len(items) - 1)

        if os.path.isdir(item_path):
            if item not in ignore_dirs:
                print(indent + ('└── ' if is_last_item else '├── ') + item)
                print_directory_tree(item_path, indent + ('    ' if is_last_item else '│   '), ignore_dirs)
        else:
            print(indent + ('└── ' if is_last_item else '├── ') + item)


if __name__ == "__main__":
    os.system('cls')
    os.chdir('../../')
    root = os.getcwd()
    print(root)
    print_directory_tree(root)
