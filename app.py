from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)

temperature_data = pd.read_csv('Datasets/final_temp_2050.csv')

heatwave_data = pd.read_csv('Datasets/heatwave_score.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_data/<year>')
def get_data(year):
    year_data = temperature_data[temperature_data['year'] == int(year)]
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

@app.route('/get_india_data')
def get_india_data():
    try:
        india_states = []
        for _, row in heatwave_data.iterrows():
            india_states.append({
                'state': row['State'],
                'lat': row['lat'],  
                'lon': row['lon'],  
                'category': row['Category'],
                'air_pollution': row['Air Pollution Index'],
                'carbon_emissions': row['Carbon Emission Impact Score'],
                'healthcare': row['Wellness and Healthcare Index'],
                'groundwater': row['Groundwater Sustainability Score'],
                'population': row['Population Density Index'],
                'rainfall': row['Rainfall Sufficiency Index'],
                'temperature': row['Temperature Variation Score'],
                'heatwave': row['Heatwave Susceptiblity Score']
            })
        return jsonify(india_states)
    except Exception as e:
        print(f"Error in /get_india_data: {e}")
        return jsonify({"error": "Data processing failed"}), 500


if __name__ == '__main__':
    app.run(debug=True)
