<img src="https://help.twitter.com/content/dam/help-twitter/brand/logo.png" align="right" width="200"/>

# Unfollow Twitter
Aplicação que realiza o unfollow em usuário do twitter que não te segue

## Funcionalidade:
- Realiza o unfollow de usuários no twitter seguindo os passos descritos abaixo. <br>
1 - Faz login na api do Twitter usando as credenciais de acesso do usuário.<br>
2 - Encontrar todos os seguidores e pessoas que o usuário segue.<br>
3 - Cria dpos dicionário, um com com todos os seguidores e outro com os não seguidores.<br>
4 - Faz uma comparação entre os dois dicionário e retorna os ids diferentes (ids diferente são usuário que não se encontram nos dois dicionário, logo não são seguidores).<br>
5- Realiza o unfollow usando os ids recuperados no passo 4.<br>

## Requisitos

1) Ter o pip instalado <br>
2) Ter o npm instaldo <br>
3) Ter o Severless Framework instaldo <br>

## Instalação

1) Faça o clone do projeto<br>
- ```$ git clone https://github.com/Wilson3g/unfollow-twitter.git```<br>

2) Crie e ative uma virtual env usando python3<br>
- ```$ python3 -m venv nome_da_sua_env```<br>
- ```$ . nome_da_sua_env/bin/activate```<br>

3) Instale os pacotes necessários para rodar o projeto<br>
- ```$ pip install -r requirements```<br>

4) No arquivo twitter.py adicione as suas credenciais do twitter
- ```consumer key```, ```consumer secret```, ```access token```, ```access token secret``` <br>

5) Execute<br>
- ```$ npm init```<br>

6) ```$ npm install serverless-python-requirements```<br>

7) Para rodar o projeto localmente execute<br>
- ```$ serverless invoke local -f main```<br>

## Deploy

1) execute ```$ sls deploy -v```
