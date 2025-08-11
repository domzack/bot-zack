# bot-zack

Scripts para automação de configuração de repositórios GitHub e aliases do Git.

## Arquivos

### gh_repo_config.py

Automatiza a criação de um novo repositório GitHub e inicialização do projeto local.

**Funcionalidades:**
- Pergunta o nome/path da pasta para criar/acessar.
- Se a pasta existir, permite acessar ou alterar o nome.
- Solicita usuário, nome do repositório e tipo (public/private).
- Confirma antes de criar o repositório.
- Executa `git init`, cria o repositório remoto com `gh repo create`, renomeia o branch para `main`.
- Cria um arquivo `README.md` padrão se não existir.
- Adiciona todos os arquivos, faz commit inicial e envia para o GitHub.

**Como usar:**
```bash
python3 gh_repo_config.py
```
Siga as instruções interativas no terminal.

---

### git_alias_config.py

Automatiza a configuração de um alias global do Git chamado `pop` e permite configurar o email global do usuário.

**Funcionalidades:**
- Remove o alias global `pop` se existir.
- Cria um novo alias global `pop` que executa: `git add . && git commit -a -m "$1" && git push && git status`.
- Configura o email global do usuário Git (`user.email`).
- Exibe o conteúdo do arquivo global de configuração do Git (`~/.gitconfig`) para confirmação.

**Como usar:**
```bash
python3 git_alias_config.py
```
O script configura o alias e o email automaticamente.

---

## Requisitos

- Python 3
- Git instalado e configurado
- GitHub CLI (`gh`) instalado e autenticado

---

## Observações

- O email configurado deve ser válido para associar os commits ao seu perfil do GitHub.
- O alias `pop` facilita o processo de adicionar, commitar e enviar alterações rapidamente.