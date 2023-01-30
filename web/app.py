"""
Sewon Sohn's Flask API.
"""

from flask import Flask, abort, send_from_directory
import os
import configparser

app = Flask(__name__)

def parse_config(config_paths):
    config_path = None
    for f in config_paths:
        if os.path.isfile(f):
            config_path = f
            break

    if config_path is None:
        raise RuntimeError("Configuration file not found!")

    config = configparser.ConfigParser()
    config.read(config_path)
    return config

config = parse_config(["credentials.ini", "default.ini"])
portnum = config["SERVER"]["PORT"]


@app.route("/<file_name>")
def find_file(file_name):
    if ".." in file_name or "~" in file_name:
        abort(403)
    elif os.path.exists(f"pages/{file_name}"):
        return send_from_directory('pages/', f"{file_name}"), 200
    else:
        abort(404)

@app.errorhandler(403)
def forbidden(e):
    print("File is forbidden!")
    return send_from_directory('pages/', '403.html'), 403

@app.errorhandler(404)
def not_found(e):
    print("File not found!")
    return send_from_directory('pages/', '404.html'), 404

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=portnum)
