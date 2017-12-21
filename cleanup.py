from os import getcwd, scandir, rmdir, rename
from shutil import move

# Dictionary where keys = subdirs in root, value = subdirs in keys

def get_tree(path):
    tree = {}
    with scandir(path) as parents:
        for parent in parents:
            with scandir(parent) as children:
                tree[parent] = children

# def get_tree(path):
#     tree = []
#     with scandir(path) as contents:
#         for content in contents:
#             if not content.name.startswith('.') and content.is_dir():
#                 tree.append(content.path)
#     return tree

def get_leaf(path):
    leaf = []
    with scandir(path) as contents:
        for entry in contents:
            if not entry.name.startswith('.') and entry.is_file():
                leaf.append(entry.name)
    return leaf

ROOT_TREE = get_struct(getcwd())
CHILD_TREE = []

for entry in ROOT_TREE:
    CHILD_TREE.extend(get_struct(entry))

for subfolder in CHILD_TREE:
    files = get_struct(subfolder, kind='file')
    parent = subfolder.split('/')
    del parent[-1]
    parent = '/'.join(parent)
    for file in files:
        curLoc = subfolder + '/' + file
        newLoc = parent + '/' + file
        move(curLoc, newLoc)
    rmdir(subfolder)

