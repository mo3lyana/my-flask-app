from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Flask App with CI/CD</h1>
    <p>Deployed automatically using GitHub Actions!</p>
    <ul>
        <li><a href="/health">Health Check</a></li>
        <li><a href="/api/info">API Info</a></li>
    </ul>
    """

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'service': 'Flask App',
        'version': '1.0.0'
    })

@app.route('/api/info')
def info():
    return jsonify({
        'name': 'Flask CI/CD Demo',
        'author': 'Your Name',
        'features': ['Auto Build', 'Auto Deploy', 'Docker']
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
