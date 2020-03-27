from flask import Flask, jsonify, request

db = []  # global section

app = Flask(__name__)


def add_patient_to_db(name, id, age):
    new_patient = {"name": name, "id": id, "age": age}
    db.append(new_patient)
    return True


def init_database():  # test entries, not mandatory
    add_patient_to_db("Ann Ables", 101, 35)
    add_patient_to_db("Bob Boyles", 102, 40)
    # Add code to start the logging


@app.route("/new_patient", mathods=["POST"])
def post_new_patient():
    """
    Receive the posting json
    Verify the json contains the correct keys and data  # write this first!
    If data is bad, reject request with bad status to client
    If data is good, add patient to database, and return good status to client
    """
    in_dict = request.get_json()
    check_result = verify_new_patient_info(in_dict)
    if check_result is not True:
        return check_result, 400
    add_patient_to_db(in_dict["name"], in_dict["id"], in_dict["age"])
    return "Patient added", 200


def verify_new_patient_info(in_dict):
    expected_keys = ("name", "id", "age")
    expected_types = (str, int, int)
    for idx, key in enumerate(expected_keys):
        if key not in in_dict.keys():  # not in
            return "{} key not found".format(key)
        if type(in_dict[key] is not expected_types[idx]):  # is not
            return "{} value not correct type".format(key)
    return True


if __name__ == '__main__':
    init_database()
    app.run()