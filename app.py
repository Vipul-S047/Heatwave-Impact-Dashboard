from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)

data = pd.read_csv('temp_till_2100.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_data/<year>')
def get_data(year):
    year_data = data[data['year'] == int(year)]
    locations = []
    for _, row in year_data.iterrows():
        locations.append({
            'lat': row['lat'],
            'lon': row['lon'],
            'temp': row['temp'],
            'city': row['city'],
            'country': row['country']
        })
    return jsonify(locations)

if __name__ == '__main__':
    app.run(debug=True)
