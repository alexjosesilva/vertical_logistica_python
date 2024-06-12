from flask import Flask, request, jsonify
from models import process_file

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file:
        result = process_file(file)
        # Decodificar valores relevantes para garantir que possam ser serializados
        for user in result:
            user['name'] = user['name'].decode('utf-8')
            ##for order in user['orders']:
            ## order['date'] = order['date'].decode('utf-8')
        return jsonify(result), 200

if __name__ == '__main__':
    app.run(debug=True)
