import subprocess
import os
import sys

def is_windows():
    return os.name == 'nt'

def remover_alias_pop():
    print('Removendo alias global "pop" (se existir)...')
    subprocess.run('git config --global --unset alias.pop', shell=True)

def criar_alias_pop():
    print('Criando novo alias global "pop"...')
    if is_windows():
        # No Windows, o comando precisa ser adaptado para batch
        comando = (
            'git config --global alias.pop '
            '"!git add . && git commit -a -m \"%1\" && git push && git status"'
        )
    else:
        # Unix-like (Linux/Mac)
        comando = (
            "git config --global alias.pop "
            "'! pop() { git add . && git commit -a -m \"$1\" && git push && git status ; } ; pop'"
        )
    subprocess.run(comando, shell=True, check=True)

def configurar_email():
    email = 'domzack1@gmail.com'
    subprocess.run(f'git config --global user.email "{email}"', shell=True, check=True)
    print(f'Email global alterado para: {email}')

if __name__ == '__main__':
    remover_alias_pop()
    criar_alias_pop()
    configurar_email()
    # Exibe o conteúdo do arquivo de configuração global do git
    gitconfig_path = os.path.expanduser('~/.gitconfig')
    print('\nConteúdo do arquivo ~/.gitconfig:')
    if os.path.exists(gitconfig_path):
        with open(gitconfig_path, 'r') as f:
            print(f.read())
    else:
        print('Arquivo ~/.gitconfig não encontrado.')