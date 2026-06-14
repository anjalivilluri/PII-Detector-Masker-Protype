from flask import (
    Flask,
    render_template,
    request,
    send_file
)

import os
import json

from processors.web_processor import (
    process_uploaded_csv
)

app = Flask(__name__)

generated_file = None

UPLOAD_FOLDER = "uploads"

os.makedirs("uploads", exist_ok=True)
os.makedirs("outputs", exist_ok=True)
os.makedirs("data", exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def home():

    return render_template(
        "index.html"
    )


@app.route(
    "/upload",
    methods=["POST"]
)
def upload():

    global generated_file

    file = request.files["file"]

    file_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    file.save(file_path)

    report, generated_file = process_uploaded_csv(file_path)

    # ---------------------
    # READ SCAN HISTORY
    # ---------------------

    history = []

    history_path = "data/scan_history.json"

    if os.path.exists(history_path):
        with open(history_path, "r") as file:
            history = json.load(file)
    else:
        history = []

    return render_template(
        "result.html",
        report=report,
        history=history[-5:]
    )


@app.route("/download")
def download():

    global generated_file

    return send_file(
        generated_file,
        as_attachment=True
    )


if __name__ == "__main__":

    app.run(
        debug=True
    )