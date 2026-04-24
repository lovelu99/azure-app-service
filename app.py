from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Python App Running on Azure App Service</h1>
    <p>Status: Healthy</p>
    """

@app.route("/api/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "azure-app-service-python",
        "port": os.environ.get("PORT", "8000")
    })

@app.route("/api/products")
def products():
    return jsonify([
        {"id": 1, "name": "Laptop", "price": 1200},
        {"id": 2, "name": "Mouse", "price": 25},
        {"id": 3, "name": "Keyboard", "price": 75}
    ])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
    