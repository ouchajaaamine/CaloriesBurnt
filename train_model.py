import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import joblib
import os

print("Loading datasets...")
# Load datasets
exercise_df = pd.read_csv("exercise.csv")
calories_df = pd.read_csv("calories.csv")

# Merge datasets on User_ID
print("Merging datasets...")
df = pd.merge(exercise_df, calories_df, on='User_ID')

# Prepare features and target
print("Preparing data...")
X = df[['Age', 'Gender', 'Height', 'Weight', 'Duration', 'Heart_Rate', 'Body_Temp']]
X['Gender'] = X['Gender'].map({'male': 1, 'female': 0})
y = df['Calories']

# Create and train the model
print("Training the model...")
model = LinearRegression()
model.fit(X, y)

# Create models directory if it doesn't exist
if not os.path.exists('models'):
    os.makedirs('models')

# Save the trained model
print("Saving the model...")
joblib.dump(model, 'models/calories_model.pkl')

# Save any additional data that might be needed for predictions
print("Saving additional data...")
feature_names = ['Age', 'Gender', 'Height', 'Weight', 'Duration', 'Heart_Rate', 'Body_Temp']
joblib.dump(feature_names, 'models/feature_names.pkl')

print("Model training completed and saved successfully!")
print("You can now run the server without retraining the model each time.") 