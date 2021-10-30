"""
VM preparation:
mkdir flask
mkdir venv
mkdir application
python3 -m venv ./venv
# if needed sudo apt install python3.8-venv
# for Windows: source ./Script/activate
# for Ubuntu: source my-project-env/bin/activate
python application.py
you can check if site is available here
http://138.195.138.220:5000/
"""

"""
improvement steps
port 80
domain name
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>!!! FALC is great !!!</h1>"
if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)
