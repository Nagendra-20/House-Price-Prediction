from flask import Flask, request, jsonify
import pickle
import numpy as np

# Load the saved model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the House Price Prediction API!"


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)
        print("Received data:", data)
        
        features = np.array(data['features']).reshape(1, -1)
        prediction = model.predict(features)
        
        print("Prediction:", prediction)
        return jsonify({'prediction': float(prediction[0])})
    
    except Exception as e:
        print("Error:", str(e))
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
