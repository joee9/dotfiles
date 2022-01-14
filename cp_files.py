# Joe Nyhan, 14 January 2022
# Script to copy various config files to this directory

# TODO: make so that user places paths in a local file so that each unique machine can update this file


from os import system as sh
from sys import argv

def main():

    assert len(argv) == 2 and argv[1] in ["to", "from"]

    homepath = '/home/joee9/documents/dotfiles'

    paths = [
        {'sys_path': "/mnt/c/Users/Joe/AppData/Roaming/Code/User/settings.json",'save_path': f'{homepath}/vscode/settings.json'} # vscode settings file
    ]

    for info in paths:
        if argv[1] == "from": # copy from files
            source = info['sys_path']
            dest = info['save_path']
        elif argv[1] == "to": # copy to files, i.e. update files
            dest = info['sys_path']
            source = info['save_path']

        sh(f'cp {source} {dest}')

if __name__ == '__main__':
    main()