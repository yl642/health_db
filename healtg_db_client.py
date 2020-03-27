import requests


server_name = "http://127.0.0.1:5000"


def add_some_patients():
    new_p = {"name": "Claire Chou", "id": 103, "age": 45}
    r = requests.post(server_name+"/new_patient", json=new_p)
    if r.status_code != 200:
        print("Error: {} - {}".format(r.status_code, r.text))
    else:
        print("Success {}".format(r.text))


if __name__ == "__main__":
    add_some_patients()