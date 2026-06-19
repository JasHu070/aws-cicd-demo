from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>AWS CI/CD Demo Project</h1>
    <p>Automated deployment using GitHub Actions and AWS</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
