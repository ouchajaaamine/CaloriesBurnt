# Deploying FitBurner to PythonAnywhere

This guide will help you deploy the FitBurner application on PythonAnywhere.

## Prerequisites

- A [PythonAnywhere](https://www.pythonanywhere.com) account (free tier works fine)
- All project files uploaded to PythonAnywhere

## Step 1: Upload Your Files

1. Log in to your PythonAnywhere account
2. Go to the "Files" tab
3. Either create a new directory (e.g., `fitburner`) or use your home directory
4. Upload all the project files:
   - `server.py` (main application)
   - `wsgi.py` (for PythonAnywhere configuration)
   - `requirements.txt` (dependencies)
   - `exercise.csv` and `calories.csv` (data files)
   - `static/` folder (CSS, JS, images)
   - `templates/` folder (HTML templates)

## Step 2: Set Up a Virtual Environment

1. Go to the "Consoles" tab
2. Start a new Bash console
3. Navigate to your project directory:
   ```bash
   cd ~/fitburner  # or whatever directory you used
   ```
4. Create a virtual environment:
   ```bash
   mkvirtualenv --python=python3.9 fitburner-venv
   ```
5. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Step 3: Configure a Web App

1. Go to the "Web" tab
2. Click "Add a new web app"
3. Choose "Manual configuration"
4. Select Python version (Python 3.9 recommended)
5. Enter your project path (e.g., `/home/yourusername/fitburner`)

## Step 4: Configure WSGI File

1. In the Web tab, look for the link to the WSGI configuration file and click it
2. Delete all the sample code
3. Add the following code:
   ```python
   import sys
   path = '/home/yourusername/fitburner'  # Update with your actual path
   if path not in sys.path:
       sys.path.append(path)
   
   from wsgi import application
   ```
4. Save the file

## Step 5: Configure Static Files

1. In the Web tab, scroll down to "Static files"
2. Add a new mapping:
   - URL: `/static/`
   - Directory: `/home/yourusername/fitburner/static`
   
## Step 6: Reload Your Web App

1. Click the green "Reload" button in the Web tab
2. Your application should now be deployed and accessible at `yourusername.pythonanywhere.com`

## Troubleshooting

- Check the error logs in the Web tab if your app doesn't work
- Make sure all file paths are correct
- Verify that all required files are uploaded
- Confirm that all dependencies are installed

## Notes

- PythonAnywhere free tier has limitations on CPU usage and outgoing network requests
- Database connections may require additional configuration
- For custom domains, you'll need a paid PythonAnywhere account 