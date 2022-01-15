from flask import Flask, render_template, request, redirect, session, flash, url_for
import requests
from bs4 import BeautifulSoup
import datetime as dt

#render template: passando o nome do modelo e a variáveis ele vai renderizar o template
#request: faz as requisições da nosa aplicação
#redirect: redireciona pra outras páginas
#session: armazena informações do usuário
#flash:mensagem de alerta exibida na tela
#url_for: vai para aonde o redirect indica

app = Flask(__name__)
app.secret_key = 'flask'
#chave secreta da sessão



#configuração da rota index.
@app.route('/', methods=['get', 'post'])
def index():
    
    teamA_NBA = []; teamH_NBA = []; scores_NBA = []
    teamA_NHL = []; teamH_NHL = []; scores_NHL = []

    def webScrappingNHL(url):

        req = requests.get(url)
        
        if req.status_code == 200:
            print('Iniciando...')
        else:
            print('Site não encontrado =/')
        
        soup = BeautifulSoup(req.content, 'html.parser')

        for i in soup.find_all('div', attrs={'class':'ScoreboardScoreCell pa4 nhl ScoreboardScoreCell--post ScoreboardScoreCell--tabletPlus'}):
            teamAway = i.find_all('div', attrs={'class':'ScoreCell__TeamName ScoreCell__TeamName--shortDisplayName truncate db'})[0].text
            scoreAway = i.find_all('div', attrs={'class':'ScoreCell__Score h4 clr-gray-01 fw-heavy tar ScoreCell_Score--scoreboard pl2'})[0].text
            teamHome = i.find_all('div', attrs={'class':'ScoreCell__TeamName ScoreCell__TeamName--shortDisplayName truncate db'})[1].text
            scoreHome = i.find_all('div', attrs={'class':'ScoreCell__Score h4 clr-gray-01 fw-heavy tar ScoreCell_Score--scoreboard pl2'})[1].text
            
            if scoreAway != '' or scoreHome != '':
                diference = abs( int(scoreAway) - int(scoreHome) )

            teamA_NHL.append(teamAway); teamH_NHL.append(teamHome); scores_NHL.append(diference)

            #print('{} x {} teve a diferença de {} no resultado final. '.format( teamAway, teamHome, diference ))


    def webScrappingNBA(url):

        req = requests.get(url)
        
        if req.status_code == 200:
            print('Iniciando...')
        else:
            print('Site não encontrado =/')
        
        soup = BeautifulSoup(req.content, 'html.parser')

        for i in soup.find_all('div', attrs={'class':'ScoreboardScoreCell pa4 nba ScoreboardScoreCell--post ScoreboardScoreCell--tabletPlus'}):
            teamAway = i.find_all('div', attrs={'class':'ScoreCell__TeamName ScoreCell__TeamName--shortDisplayName truncate db'})[0].text
            scoreAway = i.find_all('div', attrs={'class':'ScoreCell__Score h4 clr-gray-01 fw-heavy tar ScoreCell_Score--scoreboard pl2'})[0].text
            teamHome = i.find_all('div', attrs={'class':'ScoreCell__TeamName ScoreCell__TeamName--shortDisplayName truncate db'})[1].text
            scoreHome = i.find_all('div', attrs={'class':'ScoreCell__Score h4 clr-gray-01 fw-heavy tar ScoreCell_Score--scoreboard pl2'})[1].text
            
            if scoreAway != '' or scoreHome != '':
                diference = abs( int(scoreAway) - int(scoreHome) )

            teamA_NBA.append(teamAway); teamH_NBA.append(teamHome); scores_NBA.append(diference)

            #print('{} x {} teve a diferença de {} no resultado final. '.format( teamAway, teamHome, diference ))


    def pegaData():

        data = dt.datetime.now()

        ano = data.strftime("%Y") #str(data.year)

        mes = data.strftime("%m")  #str(data.month)

        dia = data.strftime("%d") #str(data.day)
        diaAnterior = int(dia)-1
        dia = str(diaAnterior)
        #dia = "0"+dia #adiciona um 0 a esquerda

        datetime = ano+mes+dia

        return int(datetime)

    def main():

        data = pegaData()

        print(data)

        urlNHL = 'https://www.espn.com/nhl/scoreboard/_/date/{}'.format(data)
        urlNBA = 'https://www.espn.com/nba/scoreboard/_/date/{}'.format(data)

        webScrappingNBA(urlNBA)
        webScrappingNHL(urlNHL)

    main()

    tamNBA = len(teamA_NBA)
    tamNHL = len(teamA_NHL)

    return render_template('index.html', teamA_NHL=teamA_NHL, 
                                         teamH_NHL=teamH_NHL, 
                                         scores_NHL=scores_NHL, 
                                         tamNHL=tamNHL,
                                         teamA_NBA=teamA_NBA, 
                                         teamH_NBA=teamH_NBA, 
                                         scores_NBA=scores_NBA, 
                                         tamNBA=tamNBA)

if __name__ == "__main__":
    app.run(debug=True)
    
    







