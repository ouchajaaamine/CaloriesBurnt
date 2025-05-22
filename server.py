from flask import *
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    # This function renders the index.html template when the root URL is accessed.
    return render_template('index.html')

@app.route('/r')
def predict():
    # This function renders the calorie.html template when the '/r' URL is accessed.
    # It opens the form for result prediction.
    return render_template('calorie.html')

@app.route('/cp', methods=['POST'])
def caloriesburntpredict():
    # This function is called when the form in calorie.html is submitted.
    # It receives the input from the user via the form.

    # Get input values from the form and convert them to appropriate data types
    Age = float(request.form.get("Age"))
    Gender = request.form.get("Gender")
    Height = float(request.form.get("Height"))
    Weight = float(request.form.get("Weight"))
    Duration = float(request.form.get("Duration"))
    Heart_Rate = float(request.form.get("Heart_Rate"))
    Body_Temp = float(request.form.get("Body_Temp"))
    
    # Convert Gender to numeric (0 for female, 1 for male)
    gender_numeric = 1 if Gender.lower() == 'male' else 0

    # Load the dataset files
    exercise_df = pd.read_csv("exercise.csv")
    calories_df = pd.read_csv("calories.csv")
    
    # Merge datasets on User_ID
    df = pd.merge(exercise_df, calories_df, on='User_ID')
    
    # Prepare features and target
    X = df[['Age', 'Gender', 'Height', 'Weight', 'Duration', 'Heart_Rate', 'Body_Temp']]
    X['Gender'] = X['Gender'].map({'male': 1, 'female': 0})
    y = df['Calories']
    
    # Create and train model
    model = LinearRegression()
    model.fit(X, y)
    
    # Make prediction with user inputs
    prediction = model.predict([[Age, gender_numeric, Height, Weight, Duration, Heart_Rate, Body_Temp]])
    
    # Round to 2 decimal places
    result = round(float(prediction[0]), 2)

    # Return prediction with additional stats
    avg_calories = round(float(df[df['Gender'] == Gender.lower()]['Calories'].mean()), 2)
    
    return render_template("calorie.html", 
                          data=result, 
                          age=Age,
                          gender=Gender,
                          height=Height,
                          weight=Weight,
                          duration=Duration,
                          heart_rate=Heart_Rate,
                          body_temp=Body_Temp,
                          avg_calories=avg_calories)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    # This block of code runs the Flask application when the script is executed.
    app.run(debug=True)
