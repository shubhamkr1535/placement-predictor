from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import os

app = Flask(__name__)

# Load the model
model_path = 'model.pkl'


try:
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from the form
        data = request.get_json()
        iq = float(data['iq'])
        cgpa = float(data['cgpa'])
        
        # Validate inputs
        if iq <= 0 or cgpa <= 0:
            return jsonify({'error': 'Please enter positive values for IQ and CGPA'}), 400
        
        if cgpa > 10:
            return jsonify({'error': 'CGPA should be between 0 and 10'}), 400
        
        # Prepare input for model
        features = np.array([[iq, cgpa]])
        
        # Make prediction
        if model is None:
            return jsonify({'error': 'Model not loaded properly'}), 500
            
        prediction = model.predict(features)
        
        # Return result
        if prediction[0] == 1:
            result = "You will get placed"
        else:
            result = "You will not get placed"
        
        return jsonify({'prediction': result})
    
    except ValueError:
        return jsonify({'error': 'Please enter valid numbers'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
