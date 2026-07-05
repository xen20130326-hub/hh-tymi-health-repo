from flask import Flask, jsonify
from flask_cors import CORS
from routes.patients import patients_bp
from db.custom_db import init_db
import os

app = Flask(__name__)
CORS(app)

# Initialize database on startup
init_db()

# Register Blueprints
app.register_blueprint(patients_bp, url_prefix='/api')

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "service": "TYMI Health Backend"}), 200

if __name__ == '__main__':
    # Use environment variable for port if available, default to 5000
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
