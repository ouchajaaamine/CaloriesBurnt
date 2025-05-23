from flask import *
import pandas as pd
import numpy as np
import joblib
import os
import re

app = Flask(__name__, static_folder='static')

# Check if the model exists, if not inform the user to run train_model.py first
model_path = 'models/calories_model.pkl'
if not os.path.exists(model_path):
    print("ERROR: Pre-trained model not found!")
    print("Please run 'python train_model.py' before starting the server.")
    print("This will train the model once and save it for future use.")
else:
    print("Loading pre-trained model...")
    
# Load the pre-trained model (will only be accessed if it exists)
def load_model():
    try:
        return joblib.load(model_path)
    except Exception as e:
        print(f"Error loading model: {str(e)}")
        return None

# Load the model if it exists
model = load_model() if os.path.exists(model_path) else None

# Load datasets for statistics only (not for model training)
exercise_df = pd.read_csv("exercise.csv")
calories_df = pd.read_csv("calories.csv")
df = pd.merge(exercise_df, calories_df, on='User_ID')

@app.route('/')
def index():
    # This function displays the home page
    return render_template('index.html')

@app.route('/r')
def predict():
    # This function displays the prediction form
    return render_template('calorie.html')

@app.route('/about')
def about():
    # This function displays the about page
    return render_template('about.html')

@app.route('/stats')
def stats():
    # This function generates and displays statistics
    
    # Calculate averages by gender
    male_avg = round(df[df['Gender'] == 'male']['Calories'].mean(), 2)
    female_avg = round(df[df['Gender'] == 'female']['Calories'].mean(), 2)
    
    # Define age groups
    age_groups = {
        '<20': df[df['Age'] < 20],
        '20-30': df[(df['Age'] >= 20) & (df['Age'] < 30)],
        '30-40': df[(df['Age'] >= 30) & (df['Age'] < 40)],
        '40-50': df[(df['Age'] >= 40) & (df['Age'] < 50)],
        '50+': df[df['Age'] >= 50]
    }
    
    # Calculate statistics by age group
    age_stats = {}
    for group, data in age_groups.items():
        age_stats[group] = {
            'count': len(data),
            'avg_calories': round(data['Calories'].mean(), 2),
            'male_avg': round(data[data['Gender'] == 'male']['Calories'].mean(), 2),
            'female_avg': round(data[data['Gender'] == 'female']['Calories'].mean(), 2)
        }
    
    # Other general statistics
    total_records = len(df)
    avg_calories = round(df['Calories'].mean(), 2)
    max_calories = round(df['Calories'].max(), 2)
    min_calories = round(df['Calories'].min(), 2)
    
    # Average calories by exercise duration
    duration_groups = {
        '<10min': df[df['Duration'] < 10],
        '10-20min': df[(df['Duration'] >= 10) & (df['Duration'] < 20)],
        '20-30min': df[(df['Duration'] >= 20) & (df['Duration'] <= 30)]
    }
    
    duration_stats = {}
    for group, data in duration_groups.items():
        duration_stats[group] = {
            'count': len(data),
            'avg_calories': round(data['Calories'].mean(), 2)
        }
    
    return render_template(
        'stats.html',
        male_avg=male_avg,
        female_avg=female_avg,
        age_stats=age_stats,
        total_records=total_records,
        avg_calories=avg_calories,
        max_calories=max_calories,
        min_calories=min_calories,
        duration_stats=duration_stats
    )

@app.route('/cp', methods=['POST'])
def caloriesburntpredict():
    # This function is called when the form is submitted
    
    error_message = None
    
    try:
        # Check if model is loaded
        if model is None:
            error_message = "Model not loaded. Please run train_model.py first."
            return render_template("calorie.html", error=error_message)
            
        # Input validation
        age = request.form.get("Age")
        gender = request.form.get("Gender")
        height = request.form.get("Height")
        weight = request.form.get("Weight")
        duration = request.form.get("Duration")
        heart_rate = request.form.get("Heart_Rate")
        body_temp = request.form.get("Body_Temp")
        
        # Check that fields are not empty
        if not all([age, gender, height, weight, duration, heart_rate, body_temp]):
            error_message = "All fields are required."
            return render_template("calorie.html", error=error_message)
        
        # Type conversion
        try:
            age = float(age)
            height = float(height)
            weight = float(weight)
            duration = float(duration)
            heart_rate = float(heart_rate)
            body_temp = float(body_temp)
        except ValueError:
            error_message = "Numeric values are invalid."
            return render_template("calorie.html", error=error_message)
        
        # Value range validation
        if age < 10 or age > 100:
            error_message = "Age must be between 10 and 100 years."
        elif gender not in ['male', 'female']:
            error_message = "Gender must be 'male' or 'female'."
        elif height < 100 or height > 250:
            error_message = "Height must be between 100 and 250 cm."
        elif weight < 30 or weight > 200:
            error_message = "Weight must be between 30 and 200 kg."
        elif duration < 1 or duration > 180:
            error_message = "Duration must be between 1 and 180 minutes."
        elif heart_rate < 60 or heart_rate > 200:
            error_message = "Heart rate must be between 60 and 200 BPM."
        elif body_temp < 36 or body_temp > 42:
            error_message = "Body temperature must be between 36 and 42°C."
        
        if error_message:
            return render_template("calorie.html", error=error_message)
        
        # Gender conversion to numeric value (0 for female, 1 for male)
        gender_numeric = 1 if gender.lower() == 'male' else 0
        
        # Prediction with validated inputs
        prediction = model.predict([[age, gender_numeric, height, weight, duration, heart_rate, body_temp]])
        
        # Round to 2 decimal places
        result = round(float(prediction[0]), 2)
        
        # Calculate additional statistics for comparison
        avg_calories = round(float(df[df['Gender'] == gender.lower()]['Calories'].mean()), 2)
        
        return render_template("calorie.html", 
                            data=result, 
                            age=age,
                            gender=gender,
                            height=height,
                            weight=weight,
                            duration=duration,
                            heart_rate=heart_rate,
                            body_temp=body_temp,
                            avg_calories=avg_calories)
    
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return render_template("calorie.html", error=error_message)

if __name__ == '__main__':
    if model is None:
        print("WARNING: Running without trained model!")
        print("Please run 'python train_model.py' before starting the server.")
    # Run the Flask application
    app.run(debug=True)
