from model import get_model
from flask import Flask, request, jsonify, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('./index.html')

@app.route('/images/<path:path>')
def send_images(path):
    return send_from_directory('images', path)
@app.route('/predict', methods=['POST'])
@app.route('/api/predict/insurance', methods=['POST'])
def api():
    if request.method == 'POST':
        data = request.get_json()
        print (data)
        model = get_model()
        if not model:
            return jsonify({'error': 'no model found'}), 500
        elif data.get('age') is None or data.get('sex') is None or data.get(
            'bmi') is None or data.get('children') is None or data.get('smoker') is None:
            return jsonify({'error': 'missing data'}), 400
        else:
            prediction = model.predict([[
                    data['age'], 
                    0 if data['sex']=="male" else 1,
                    data['bmi'],
                    data['children'],
                    1 if data['smoker']=="yes" else 0
            ]])
            print (prediction[0])
            return jsonify({'charges': prediction[0]}), 200

if __name__ == '__main__':
    app.run(debug=True)
    