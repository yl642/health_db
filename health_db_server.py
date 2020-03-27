from flask import Flask, jsonify, request

db = []  # global section

app = Flask(__name__)


def add_patient_to_db(name, id, age):
    new_patient = {"name": name, "id": id, "age": age, "test": []}
    db.append(new_patient)
    print("db is {}".format(db))
    return True


def init_database():  # test entries, not mandatory
    add_patient_to_db("Ann Ables", 101, 35)
    add_patient_to_db("Bob Boyles", 102, 40)
    # Add code to start the logging


@app.route("/new_patient", methods=["POST"])
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
        if type(in_dict[key]) is not expected_types[idx]:  # is not
            return "{} value not correct type".format(key)
    return True


@app.route("/add_test", methods=["POST"])
def post_add_test():
    """
    Receive the posting json
    Verify the json contains the correct keys and data  # write this first!
    Verify that the patient id exists in database
    If data is bad, reject request with bad status to client
    If data is good, add test results to indicated patient, and return good status to client
    """
    in_dict = request.get_json()
    check_result = verify_add_test_info(in_dict)
    if check_result is not True:
        return check_result, 400
    if is_patient_in_database(in_dict["id"]) is False:
        return "Patient {} is not found on server".format(in_dict["id"]), 400
    add_test = add_test_to_patient(in_dict)
    if add_test:
        return "Test added to patient id {}".format(in_dict["id"]), 200
    return "Unknown problem", 400



def verify_add_test_info(in_dict):
    expected_keys = ("id", "test_name", "test_result")
    expected_types = (int, str, int)
    for idx, key in enumerate(expected_keys):
        if key not in in_dict.keys():  # not in
            return "{} key not found".format(key)
        if type(in_dict[key]) is not expected_types[idx]:  # is not
            return "{} value not correct type".format(key)
    return True


def is_patient_in_database(id):
    for patient in db:
        if patient["id"] == id:
            return True
    return False


def add_test_to_patient(in_dict):
    for patient in db:
        if patient["id"] == in_dict["id"]:
            patient["test"].append((in_dict["test_name"], in_dict["test.result"]))
            print("db is {}". format(db))
            return True
    return False


if __name__ == '__main__':
    init_database()
    app.run()