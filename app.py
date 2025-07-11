from flask import Flask, request, jsonify, render_template
import pickle


app = Flask(__name__)


with open('house_price_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:

        area = request.form['area'] if request.method == 'POST' else request.get_json()['area']


        predicted_price = model.predict([[float(area)]])[0]


        return jsonify({'predicted_price': predicted_price})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
