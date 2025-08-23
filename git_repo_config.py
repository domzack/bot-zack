import subprocess
import os

def perguntar(msg, opcoes=None):
    while True:
        resp = input(msg).strip()
        if not opcoes or resp in opcoes:
            return resp

def main():
    # Pergunta o path/nome da pasta
    while True:
        pasta = input('Informe o nome/path da pasta para criar/acessar: ').strip()
        if os.path.exists(pasta):
            print(f'A pasta "{pasta}" já existe.')
            escolha = perguntar('Deseja acessar a pasta existente (s) ou alterar o nome (n)? [s/n]: ', ['s', 'n'])
            if escolha == 's':
                break
            else:
                continue
        else:
            os.makedirs(pasta)
            print(f'Pasta "{pasta}" criada.')
            break

    os.chdir(pasta)
    print(f'Acessando pasta: {os.getcwd()}')

    usuario = input('Usuário do GitHub: ').strip()
    repositorio = input('Nome do repositório: ').strip()
    tipo = perguntar('Tipo do repositório? [public/private]: ', ['public', 'private'])

    confirmar = perguntar(f'Confirma criar o repositório {usuario}/{repositorio} ({tipo})? [s/n]: ', ['s', 'n'])
    if confirmar != 's':
        print('Operação cancelada.')
        return

    comandos = [
        'git init',
        f'gh repo create {usuario}/{repositorio} --{tipo} --source=. --remote=origin',
        'git branch -M main',
    ]

    # Executa comandos iniciais
    for comando in comandos:
        print(f'Executando: {comando}')
        try:
            subprocess.run(comando, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f'Erro ao executar: {comando}\n{e}')
            return

    # Cria README.md se não existir
    if not os.path.exists('README.md'):
        with open('README.md', 'w') as f:
            f.write(f'# {repositorio}\n\nRepositório criado automaticamente.\n')
        print('Arquivo README.md criado.')

    # Adiciona, commita e envia
    try:
        subprocess.run('git add .', shell=True, check=True)
        subprocess.run('git commit -m "primeiro commit"', shell=True, check=True)
        subprocess.run('git push -u origin main', shell=True, check=True)
        print('Repositório criado e enviado com sucesso!')
    except subprocess.CalledProcessError as e:
        print(f'Erro ao enviar arquivos: {e}')

if __name__ == '__main__':
    main()