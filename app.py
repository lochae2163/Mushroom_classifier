from flask import Flask, render_template, request
import pickle
from inputs_preprocessing.preprocessing import Preprocessor

app = Flask(__name__)

# Load the trained model
with open("trained_model.pickle", "rb") as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        preprocessor = Preprocessor()
        user_inputs = []

        for feature in preprocessor.features:
            user_input = request.form.get(feature)
            user_inputs.append(user_input)

        preprocessor.processed_inputs = preprocessor._one_hot_encode(user_inputs)

        # Make predictions
        prediction = model.predict([preprocessor.processed_inputs])

        result = 'Edible' if prediction[0] == 1 else 'Poisonous'

        return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
