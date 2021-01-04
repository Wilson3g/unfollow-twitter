<img src="https://help.twitter.com/content/dam/help-twitter/brand/logo.png" align="right" width="200"/>

# Unfollow Twitter
Aplicação que realiza o unfollow em usuário do twitter que não te seguem

## Funcionalidade:
- Realizar o unfollow de usuários no twitter seguindo os passos descritos abaixo.
1 - Faz login na api do Twitter usando as credenciais de acesso do usuário.
2 - Encontrar todos os seguidores e pessoas que o usuário segue.
3 - Cria dpos dicionário, um com com todos os seguidores e outro com os não seguidores.
4 - Faz uma comparação entre os dois dicionário e retorna os ids diferentes (ids diferente são usuário que não se encontram nos dois dicionário, logo não são seguidores).
5- Realiza o unfollow usando os ids recuperados no passo 4.

## Instalação

1) Faça o clone do projeto
1.2 - git clone nome_do_repositório

2) Crie e ative uma virtual env usando python3
2.1 - python3 -m venv nome_da_sua_env
2.2 - . nome_da_sua_env/bin/activate

3) Instale os pacotes necessários para rodar o projeto
3.1 - pip install -r requirements

4) No arquivo twitter.py adicione as suas credenciais do twitter

5) Execute o projeto com python main.py

