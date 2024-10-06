from flask import Flask, request, send_file, jsonify
import os
import tempfile
import uuid

app = Flask(__name__)

TEMP_DIR = tempfile.gettempdir()

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/save-audio', methods=['POST'])
def save_audio():
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file'}), 400
    
    audio_file = request.files['audio']
    filename = f"{uuid.uuid4()}.mp3"
    filepath = os.path.join(TEMP_DIR, filename)
    
    audio_file.save(filepath)
    
    return jsonify({'filename': filename})

@app.route('/audio/<filename>')
def get_audio(filename):
    return send_file(os.path.join(TEMP_DIR, filename), mimetype='audio/mpeg')

if __name__ == '__main__':
    app.run(debug=True)