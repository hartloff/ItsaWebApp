from flask import Flask, send_file

app = Flask(__name__, static_url_path="/static")


@app.route('/')
def index():
    return send_file("static/index.html")


app.run("0.0.0.0", 7999)
