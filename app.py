from flask import Flask, render_template, send_from_directory

import os
import random

app = Flask(__name__)

allbirds = [file[:-4] for file in os.listdir("static/img") if file.endswith(".jpg")]

@app.route("/")
def index():
    random.shuffle(allbirds)
    birds = allbirds[0:3]
    shownbird = random.choice(birds)
    return render_template("index.html", shownbird=shownbird, birds=birds)

# in stand alone mode, pass through static files
@app.route('/<path:path>', methods = ['POST', 'GET'])
def send(path):
    return send_from_directory("static", path, max_age = 60 * 60)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5001)))
