from flask import Flask


app = flask(__name__)


@app.route("/", methods = ["GET"])
def server_status():
    return "Server On"


@app.route("/info", methods = ["GET"])
def info_route():
    return "This server was written for BME 547"
    

if __name__ == "__main__":
    app.run()
