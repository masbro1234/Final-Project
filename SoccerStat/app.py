from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = 'be7d2482c42e883759f9d99f4166350d' 
HEADERS = {'x-apisports-key': API_KEY}
BASE_URL = 'https://v3.football.api-sports.io'
LEAGUE_ID = 39  # Premier League

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    search_type = request.form['search_type']
    season = request.form['season']

    if search_type == 'team':
        team_resp = requests.get(f"{BASE_URL}/teams", headers=HEADERS, params={"search": query})
        teams = team_resp.json().get('response', [])
        if not teams:
            return render_template('result.html', not_found=True, query=query)

        team = teams[0]
        team_id = team['team']['id']
        logo = team['team']['logo']
        name = team['team']['name']

        stats_resp = requests.get(f"{BASE_URL}/teams/statistics", headers=HEADERS, params={
            "team": team_id,
            "season": season,
            "league": LEAGUE_ID
        })
        stats = stats_resp.json().get('response', {})

        wins = stats.get('fixtures', {}).get('wins', {}).get('total', 'N/A')
        draws = stats.get('fixtures', {}).get('draws', {}).get('total', 'N/A')
        losses = stats.get('fixtures', {}).get('loses', {}).get('total', 'N/A')
        goals_for = stats.get('goals', {}).get('for', {}).get('total', {}).get('total', 'N/A')
        goals_against = stats.get('goals', {}).get('against', {}).get('total', {}).get('total', 'N/A')

        return render_template('result.html', not_found=False, search_type='team',
                               name=name, logo=logo, wins=wins, draws=draws, losses=losses,
                               goals_for=goals_for, goals_against=goals_against)

    elif search_type == 'player':
        player_resp = requests.get(f"{BASE_URL}/players", headers=HEADERS, params={
            "search": query,
            "season": season,
            "league": LEAGUE_ID
        })
        players = player_resp.json().get('response', [])
        if not players:
            return render_template('result.html', not_found=True, query=query)

        player = players[0]['player']
        stats = players[0]['statistics'][0]

        return render_template('result.html', not_found=False, search_type='player',
                               name=player['name'], photo=player['photo'], team=stats['team']['name'],
                               goals=stats['goals']['total'], assists=stats['goals']['assists'])

    return render_template('result.html', not_found=True, query=query)

if __name__ == '__main__':
    app.run(debug=True)
