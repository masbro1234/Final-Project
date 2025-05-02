from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = 'be7d2482c42e883759f9d99f4166350d'
HEADERS = {
    'x-apisports-key': API_KEY
}
BASE_URL = 'https://v3.football.api-sports.io'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    search_type = request.form['search_type']

    if search_type == 'team':
        endpoint = f'{BASE_URL}/teams'
        params = {'search': query}
    elif search_type == 'player':
        endpoint = f'{BASE_URL}/players'
        params = {'search': query, 'season': 2023}
    else:
        return render_template('result.html', not_found=True, query=query)

    response = requests.get(endpoint, headers=HEADERS, params=params)

    if response.status_code != 200:
        return f"Error fetching data: {response.status_code}"

    data = response.json().get('response', [])
    if not data:
        return render_template('result.html', not_found=True, query=query)

    return render_template('result.html', not_found=False, data=data, search_type=search_type)

if __name__ == '__main__':
    app.run(debug=True)
