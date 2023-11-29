# Mushroom Classification Project

## Overview

This project focuses on the classification of mushrooms into edible and poisonous categories based on various features. The classification model is built using the Flask web framework and a Random Forest Classifier.

## Project Structure

The project is organized as follows:

- **Mushroom_classifier:**
  - **data:**
    - `new_data.csv`: Dataset containing preprocessed and imputed mushroom data.
  - **inputs_preprocessing:**
    - `preprocessing.py`: Module for preprocessing input data.
  - **models:**
    - `trained_model.pickle`: Pickle file containing the trained Random Forest model.
  - **notebooks:**
    - `MushroomClassifier.ipynb`: Jupyter Notebook containing the model training code.
  - **static:**
    - `style.css`: CSS file for styling of html.
  - **templates:**
    - `index.html`: HTML file for user input form.
    - `result.html`: HTML file to display the prediction result.
- `.gitignore`: File specifying files and directories to be ignored by version control.
- `app.py`: Flask application file.
- `README.md`: Project documentation.
- `requirements.txt`: File specifying Python dependencies.

## How to Run

1. Install dependencies using `pip install -r requirements.txt`.
2. Run the Flask application: `python app.py`.
3. Access the application in your web browser at `http://localhost:5000`.

## Usage

1. Visit the home page at `http://localhost:5000`.
2. Fill in the mushroom features in the form.
3. Click "Predict" to get the classification result.

## Model Training

The model was trained using the Jupyter Notebook `MushroomClassifier.ipynb`. The best parameters for the Random Forest Classifier were determined using Grid Search.

## Credits

- Dataset Source: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/mushroom)
- Flask: [Flask Documentation](https://flask.palletsprojects.com/)
- Scikit-learn: [Scikit-learn Documentation](https://scikit-learn.org/stable/)
- Autoimpute: [Autoimpute Documentation](https://pypi.org/project/autoimpute/)
