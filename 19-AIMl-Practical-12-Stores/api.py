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
@app.route('/api/predict/Stores', methods=['POST'])
def api():
    if request.method == 'POST':
        data = request.get_json()
        print (data)
        model = get_model()
        if not model:
            return jsonify({'error': 'no model found'}), 500
        elif data.get('Store_Area') is None or data.get('Items_Available') is None or data.get('Daily_Customer_Count') is None:
            return jsonify({'error': 'missing data'}), 400
        else:
            prediction = model.predict([[data['Store_Area'], data['Items_Available'], data['Daily_Customer_Count']]])
            print (prediction[0])
            return jsonify({'prediction': prediction[0]}), 200

if __name__ == '__main__':
    app.run(debug=True)
    