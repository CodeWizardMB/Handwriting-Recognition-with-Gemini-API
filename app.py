from flask import Flask, request, jsonify, send_from_directory
import os
import requests

app = Flask(__name__)

# Configuration for Gemini API
api_key = os.getenv('GENAI_API_KEY')  # Use environment variable for API key

if not api_key:
    raise ValueError("API Key is missing! Please set GENAI_API_KEY environment variable.")

genai_api_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handles file upload and processes it for handwritten text recognition."""
    if 'file' not in request.files:
        return jsonify({"error": "No file part"})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"})

    # Save the file to the server
    file_path = os.path.join('uploads', file.filename)
    try:
        os.makedirs('uploads', exist_ok=True)
        file.save(file_path)
    except Exception as e:
        return jsonify({"error": f"Error saving file: {e}"})

    # Process the file with the Gemini API
    recognized_text = send_to_gemini(file_path)
    if "Error" in recognized_text:
        return jsonify({"error": recognized_text})

    return jsonify({"file_path": file_path, "recognized_text": recognized_text})

def send_to_gemini(file_path):
    """Sends the file to the Gemini API for handwritten text recognition."""
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/octet-stream',
    }
    try:
        with open(file_path, 'rb') as file:
            response = requests.post(genai_api_url, headers=headers, data=file)
        if response.status_code == 200:
            response_json = response.json()
            return response_json.get('recognized_text', 'No text found')
        else:
            return f"Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    app.run(debug=True)
