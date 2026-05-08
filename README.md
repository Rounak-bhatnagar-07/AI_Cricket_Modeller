# AI Cricket Modeller

A machine learning project for predicting cricket match outcomes using Flask web interface.

## Project Structure

```
AI_Cricket_Modeller/
│
├── data/                          # Data files
│   └── cricket_matches.csv       # Sample cricket match data
│
├── notebooks/                     # Jupyter notebooks
│   └── cricket_model.ipynb       # Model training and analysis
│
├── models/                        # Trained models
│   ├── cricket_model.pkl         # Random Forest classifier model
│   └── feature_columns.pkl       # Feature column names
│
├── app/                          # Flask web application
│   └── app.py                    # Main Flask app with prediction API
│
├── main.py                       # Entry point for web app
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

## Features

1. **Data Analysis**: Jupyter notebook for exploring cricket match data
2. **Machine Learning Model**: Random Forest classifier for predicting match winners
3. **Web Interface**: Flask-based web app for making predictions
4. **Model Persistence**: Save and load trained models using joblib

## Installation

1. Create a virtual environment:
```bash
python -m venv .venv
```

2. Activate the virtual environment:
   - **Windows**: `.venv\Scripts\activate.ps1`
   - **Mac/Linux**: `source .venv/bin/activate`

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Web Application

```bash
python main.py
```

The web app will be available at `http://127.0.0.1:5000`

### Using the Jupyter Notebook

Open the notebook:
```bash
jupyter notebook notebooks/cricket_model.ipynb
```

This notebook allows you to:
- Load and explore cricket match data
- Train the Random Forest model
- Evaluate model accuracy
- Save the trained model

## Data Format

The CSV file should have the following columns:
- `team1`: First team name
- `team2`: Second team name
- `venue`: Match venue
- `toss_winner`: Team that won the toss
- `toss_decision`: Decision after toss (bat/bowl)
- `winner`: Match winner (0 or 1 for team1/team2)

## Supported Teams

- India
- Australia
- England
- Pakistan
- South Africa
- New Zealand
- Sri Lanka
- West Indies
- Bangladesh
- Afghanistan

## Prediction

Use the web interface to predict match outcomes by selecting:
- Team 1
- Team 2
- Venue
- Toss Winner
- Toss Decision (bat/bowl)

The model will predict which team is likely to win.

## Technologies Used

- **Python**: Programming language
- **Pandas**: Data manipulation
- **NumPy**: Numerical computing
- **Scikit-learn**: Machine learning
- **Flask**: Web framework
- **Joblib**: Model serialization
- **Matplotlib & Seaborn**: Data visualization

## Current Model Performance

- Accuracy: 50% (on test set with limited data)
- Model Type: Random Forest Classifier
- Note: With more comprehensive cricket data, accuracy can be significantly improved

## Future Improvements

1. Include more match statistics (runs scored, wickets, etc.)
2. Add player performance metrics
3. Incorporate historical win patterns
4. Use time-series data for trends
5. Implement multiple ML algorithms (XGBoost, Neural Networks)
6. Deploy as a cloud-based API
7. Add visualization dashboards

## License

MIT

## Author

AI Cricket Modeller Project
