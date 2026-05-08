import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load dataset
matches = pd.read_csv("data/matches.csv")

print(matches.head())

# Convert text into numbers
le = LabelEncoder()

matches['team1'] = le.fit_transform(matches['team1'])
matches['team2'] = le.fit_transform(matches['team2'])
matches['venue'] = le.fit_transform(matches['venue'])
matches['toss_winner'] = le.fit_transform(matches['toss_winner'])
matches['toss_decision'] = le.fit_transform(matches['toss_decision'])

print(matches.head())