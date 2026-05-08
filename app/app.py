from flask import Flask, request, render_template_string
import joblib
import pandas as pd
import os

app = Flask(__name__)

# Get the absolute path to the models directory
models_dir = os.path.join(os.path.dirname(__file__), '..', 'models')

# Load the model and feature columns
model = joblib.load(os.path.join(models_dir, 'cricket_model.pkl'))
feature_columns = joblib.load(os.path.join(models_dir, 'feature_columns.pkl'))

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        team1 = request.form['team1']
        team2 = request.form['team2']
        venue = request.form['venue']
        toss_winner = request.form['toss_winner']
        toss_decision = request.form['toss_decision']

        # Create input DataFrame
        input_data = pd.DataFrame(columns=feature_columns)
        input_data.loc[0] = 0  # Initialize with zeros

        # Set the values
        input_data[f'team1_{team1}'] = 1
        input_data[f'team2_{team2}'] = 1
        input_data[f'venue_{venue}'] = 1
        input_data[f'toss_winner_{toss_winner}'] = 1
        input_data[f'toss_decision_{toss_decision}'] = 1

        # Predict
        prediction = model.predict(input_data)[0]
        winner = team1 if prediction == 1 else team2

        return render_template_string('''
        <h1>Prediction Result</h1>
        <p>The predicted winner is: {{ winner }}</p>
        <a href="/">Predict Again</a>
        ''', winner=winner)

    return render_template_string('''
    <h1>Cricket Match Winner Predictor</h1>
    <form method="post">
        Team 1: <select name="team1">
            <option>India</option>
            <option>Australia</option>
            <option>England</option>
            <option>Pakistan</option>
            <option>South Africa</option>
            <option>New Zealand</option>
            <option>Sri Lanka</option>
            <option>West Indies</option>
            <option>Bangladesh</option>
            <option>Afghanistan</option>
        </select><br>
        Team 2: <select name="team2">
            <option>India</option>
            <option>Australia</option>
            <option>England</option>
            <option>Pakistan</option>
            <option>South Africa</option>
            <option>New Zealand</option>
            <option>Sri Lanka</option>
            <option>West Indies</option>
            <option>Bangladesh</option>
            <option>Afghanistan</option>
        </select><br>
        Venue: <select name="venue">
            <option>Melbourne</option>
            <option>Lords</option>
            <option>Wellington</option>
            <option>Colombo</option>
            <option>Dhaka</option>
            <option>Ahmedabad</option>
            <option>Perth</option>
            <option>Cape Town</option>
            <option>Chittagong</option>
            <option>Kingston</option>
            <option>Eden Gardens</option>
            <option>Johannesburg</option>
            <option>Lahore</option>
            <option>Manchester</option>
            <option>Bridgetown</option>
            <option>Sydney</option>
            <option>Centurion</option>
            <option>Auckland</option>
        </select><br>
        Toss Winner: <select name="toss_winner">
            <option>India</option>
            <option>Australia</option>
            <option>England</option>
            <option>Pakistan</option>
            <option>South Africa</option>
            <option>New Zealand</option>
            <option>Sri Lanka</option>
            <option>West Indies</option>
            <option>Bangladesh</option>
            <option>Afghanistan</option>
        </select><br>
        Toss Decision: <select name="toss_decision">
            <option>bat</option>
            <option>bowl</option>
        </select><br>
        <input type="submit" value="Predict">
    </form>
    ''')

if __name__ == '__main__':
    app.run(debug=True)