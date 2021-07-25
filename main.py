import requests
from bs4 import BeautifulSoup
import pandas

if __name__ == '__main__':
    print('EPL Standings')
    response = requests.get('https://www.premierleague.com/tables')
    soup = BeautifulSoup(response.content, 'lxml')
    table = soup.find('tbody')
    df = pandas.DataFrame(columns = ['Position', 'Team', 'Played', 'Won', 'Loss', 'GF', 'GA', 'GD', 'Points'])
    for row in table.find_all('tr'):
        if row['class'] != ['expandable']:
            # print(row['class'])
            obj = row.find_all('td')
            # print(obj)
            pos = obj[1].get_text().strip()
            team = obj[2].find(class_ = 'long').get_text()
            played = obj[3].get_text()
            won = obj[4].get_text()
            draw = obj[5].get_text()
            loss = obj[6].get_text()
            goals_for = obj[7].get_text()
            goals_against = obj[8].get_text()
            goals_diff = obj[9].get_text().strip()
            points = obj[10].get_text()
            # print(played)
            df = df.append({'Position': pos, 'Team': team, 'Played': played, 'Won': won, 'Draw': draw, 'Loss': loss,
                            'GF': goals_for, 'GA': goals_against, 'GD': goals_diff, 'Points': points},
                           ignore_index = True)
    print(df)