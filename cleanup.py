from os import getcwd, scandir, rmdir
from shutil import move
# Used for a visual aide
# from pprint import pprint

root = getcwd()

def get_folders(path):
    folders = []
    if type(path) is str:
        with scandir(path) as contents:
            for child in contents:
                if not child.name.startswith('.') and child.is_dir():
                    folders.append(child.path)
        return folders
    if type(path) is list:
        for item in path:
            with scandir(item) as contents:
                for child in contents:
                    if not child.name.startswith('.') and child.is_dir():
                        folders.append(child.path)
        return folders
    return False

def get_files(path):
    files = []
    if type(path) is str:
        with scandir(path) as contents:
            for child in contents:
                if child.is_file():
                    files.append(child.path)
        return files
    if type(path) is list:
        for item in path:
            with scandir(item) as contents:
                for child in contents:
                    if child.is_file():
                        files.append(child.path)
        return files
    return False

def new_path(curpath):
    new = curpath.split('/')
    del new[-2]
    new = '/'.join(new)
    return new

def perform_cleanup(children, grandchildren, orphans):
    if not orphans['folders'] or not orphans['files']:
        for file in grandchildren['files']:
            move(file, new_path(file))

parents = {'folders': get_folders(root), 'files': get_files(root)}
children = {'folders': get_folders(parents['folders']), 'files': get_files(parents['folders'])}
grandchildren = {'folders': get_folders(children['folders']), 'files': get_files(children['folders'])}
orphans = {'folders': get_folders(grandchildren['folders']), 'files': get_files(grandchildren['folders'])}

# for file in grandchildren['files']:
#     new = file.split('/')
#     del new[-2]
#     new = '/'.join(new)
#     move(file, new)

# for folder in children['folders']:
#     rmdir(folder)