from flask import Flask, request, jsonify


app = flask(__name__)


@app.route("/", methods = ["GET"])
def server_status():
    return "Server On"


@app.route("/info", methods = ["GET"])
def info_route():
    return "This server was written for BME 547"
    

@app.route("/HDL_analysis", methods = ["POST"])
def HDL_route_handler():
    """
    
    in_data = {"name": <patient_name>,
               "HDL_value": <HDL_results> }
    """
    from blood_calculator import HDL_analysis
    in_data = request.get_json()
    print("Received HDL value of {}".format(in_data["HDL_values"]))
    diagnosis = HDL_analysis(in_data["HDL_value"])
    return diagnosis
    
    
@app.route("/add", methods = ["POST"])
def add_numbers():
    in_data = requests.get_json()
    answer = in_data["a"] + in_data["b"]
    if answer < 0:
        return "The answer was less than zero. BAD", 400
    return jsonify(answer)
    
    
@app.route("add_two/<a>/<b>", methods = ["GET"])
def add_two_handler(a, b):
    answer = int(a) + int(b)
    return jsonify(answer)

if __name__ == "__main__":
    app.run()
