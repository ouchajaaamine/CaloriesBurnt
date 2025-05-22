# FitBurner: Calories Burned Prediction

![FitBurner](https://i.imgur.com/jQjUYJJ.png)

## 📋 Overview

FitBurner is a web application that uses machine learning to predict calories burned during exercise based on personal metrics. This application allows users to get accurate predictions by entering their demographic information and exercise parameters.

## ✨ Features

- **Personalized Calorie Prediction**: Get tailored calorie burn estimates based on your specific metrics
- **Dark/Light Mode**: Comfortable viewing experience in any environment
- **Responsive Design**: Optimized for both desktop and mobile devices
- **Interactive Charts**: Visual representation of calorie burning patterns across different demographics
- **Statistical Analysis**: Explore trends and patterns in exercise efficiency
- **Personalized Tips**: Get actionable recommendations to optimize your exercise routine
- **AJAX Form Submissions**: Calculate calories without page refreshes for a smoother user experience

## 🛠️ Technologies Used

- **Frontend**: HTML, CSS, JavaScript, Chart.js
- **Backend**: Python, Flask
- **Machine Learning**: Scikit-learn, Pandas, NumPy
- **Data Analysis**: Python data science stack

## 📊 Data Analysis

The application analyzes several key factors that influence calorie burning:
- Gender differences in metabolic rates
- Age-related changes in calorie burning efficiency
- Optimal exercise duration for maximum calorie burn
- Heart rate zones for efficient fat burning

## 🚀 Installation & Setup

1. **Clone the repository**
   ```
   git clone https://github.com/yourusername/fitburner.git
   cd fitburner
   ```

2. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```
   python server.py
   ```

4. **Access the application**
   Open your browser and navigate to `http://localhost:5000`

## 📱 How to Use

1. Navigate to the Calorie Predictor page
2. Enter your personal information (age, gender, height, weight)
3. Provide exercise parameters (duration, heart rate, body temperature)
4. Click "Calculate Calories" to get your personalized prediction
5. View detailed statistics in the Statistics page

## 🗂️ Project Structure

```
.
├── server.py                 # Flask backend server
├── wsgi.py                   # WSGI entry point for deployment
├── requirements.txt          # Project dependencies
├── templates/                # HTML templates
│   ├── index.html            # Home page
│   ├── calorie.html          # Calorie prediction page
│   ├── stats.html            # Statistics page
│   └── about.html            # About page
├── static/                   # Static assets
│   ├── css/                  # Stylesheets
│   │   └── style.css         # Main stylesheet
│   ├── js/                   # JavaScript files
│   │   ├── darkmode.js       # Dark mode toggle functionality
│   │   ├── charts.js         # Chart visualizations
│   │   └── mobile-nav.js     # Mobile navigation functionality
├── exercise.csv              # Exercise dataset
└── calories.csv              # Calories dataset
```

## 👨‍💻 Author

**Amine Ouchajaa**

- [GitHub](https://github.com/ouchajaaamine)
- [LinkedIn](https://www.linkedin.com/in/amine-ouchajaa/)
- [Twitter](https://x.com/AOuchajaa)
- [Facebook](https://www.facebook.com/ouchajaaamine)
- [Instagram](https://www.instagram.com/amine.uja/)

## 🚀 Deployment

For deployment instructions on PythonAnywhere, please refer to [README_DEPLOY.md](README_DEPLOY.md).

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgements

Special thanks to all contributors who have helped in developing and refining this project.

---

© 2025 FitBurner | Powered by AMINE OUCHAJAA
