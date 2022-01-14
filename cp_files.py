from os import system as sh

def main():
    homepath = '/home/joee9/documents/dotfiles'
    paths = [
        {'sys_path': "/mnt/c/Users/Joe/AppData/Roaming/Code/User/settings.json",'save_path': f'{homepath}/vscode/settings.json'}
    ]
    for info in paths:
        sys_path = info['sys_path']
        save_path = info['save_path']

        sh(f'cp {sys_path} {save_path}')

if __name__ == '__main__':
    main()