from flask import Flask, render_template, request
import pickle
from inputs_preprocessing.preprocessing import Preprocessor

app = Flask(__name__)

# Load the trained model
try:
    with open("models/trained_model.pickle", "rb") as file:
        model = pickle.load(file)
except Exception as e:
    print(f"Error loading the model: {e}")
    model = None

# A function to process inputs and make predictions
def predict_result(user_inputs):
    if model is not None:
        preprocessor = Preprocessor()
        preprocessor.processed_inputs = preprocessor._one_hot_encode(user_inputs)

        # Make predictions
        prediction = model.predict([preprocessor.processed_inputs])

        result = 'Edible' if prediction[0] == 1 else 'Poisonous'
        return result
    else:
        return "Error: Model not available"


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        user_inputs = [request.form.get(feature) for feature in Preprocessor.features]

        # Check if all inputs are provided
        if None in user_inputs:
            return render_template('result.html', result="Error: Incomplete input")

        result = predict_result(user_inputs)

        return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
