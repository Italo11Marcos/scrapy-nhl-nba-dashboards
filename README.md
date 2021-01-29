<h1>Flask Pytrends</h1>

<p align="center">
  <img src="https://img.shields.io/static/v1?label=python&message=3.9.0&color=3776AB&style=for-the-badge&logo=PYTHON"/>
  <img src="https://img.shields.io/static/v1?label=Heroku&message=deploy&color=430098&style=for-the-badge&logo=heroku"/>
  <img src="http://img.shields.io/static/v1?label=Flask&message=1.1.x&color=000000&style=for-the-badge&logo=Flask"/>
  <img src="http://img.shields.io/static/v1?label=License&message=MIT&color=green&style=for-the-badge"/>
  <img src="http://img.shields.io/static/v1?label=STATUS&message=CONCLUIDO&color=green&style=for-the-badge"/>
</p>

### :checkered_flag: Tópicos 

:pushpin: [Descrição do projeto](#descrição-do-projeto)

:pushpin: [Funcionalidades](#funcionalidades)

:pushpin: [Deploy da Aplicação](#deploy-da-aplicação)

:pushpin: [Pré-requisitos](#pré-requisitos)

:pushpin: [Como rodar a aplicação](#como-rodar-a-aplicação)

## Descrição do Projeto
<p align="justify">
  Flask app que extrai os dados dessa [página](https://www.espn.com.br/nhl/scoreboard) e informa a diferença de gols dos jogos do dia anterior.
  
  Desenvolvi essa aplicação para poder assistir os highlights das partidas mais disputadas e sem saber o resultado do mesmo.
  
  Exemplo de saída:

```
Red Wings x Avalanche teve uma diferença no placar de 3 gols

Panthers x Wild teve uma diferença no placar de 1 gols
```
</p>

## Funcionalidades
:white_check_mark: Scrapy de dados da página da [espn](https://www.espn.com.br/nhl/scoreboard).

## Link Deploy
* [Heroku](https://scrapy-nhl-scoreboards-espn-im.herokuapp.com/)

## Pré Requisitos
* Python 3.x
* Flask 1.1.x
* beautifulsoup4==4.8.2
* urllib3==1.25.7

## Como rodar a aplicação
    1. Clone o projeto

    git clone https://github.com/Italo11Marcos/scrapy-nhl-dashboards-nhl.git

    2. Crie um virtualenv
    
    virtualenv venv --python=3.x.x

    3. Ative o seu virtualenv. 

    source venv/bin/activate

    4. Instale dependências

    pip3 -r install requirements.txt

    5. Execute o projeto

    python3 flask_app.py

## Considerações

Bibliotecas utilizadas
* [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
* [urllib3](https://pypi.org/project/urllib3/)

## Erros conhecidos

Haverá erro toda vez que for o primeiro dia do mês, mas será corrigido o mais breve possível.

