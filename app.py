# app.py

from flask import *
import json, csv

app = Flask(__name__)

with open('data.csv', 'r') as csv_file:
    users = csv.DictReader(csv_file)   
    # Convert CSV data to a list of dictionaries
    users_list = list(users)


@app.route('/v1', methods=['GET'])
def home_page():
    data_set = {'Page': 'Home', 'Message':'This is a HOME PAGE'}
    json_dump = json.dumps(data_set)
    return json_dump

@app.route('/v1/users', methods=['GET'])
def get_users():
    return users_list

@app.route('/v1/users/<name>', methods=['POST'])
def update_users(name):
    update_value = {}
    # find max id number and increment
    max_id = 0
    for user in users_list:
        current_id = int(user['id'])
        if current_id > max_id:
            max_id = current_id
    
    update_id = max_id + 1
    update_value = {'id': str(update_id), 'name': name}
    users_list.append(update_value)
    return update_value
     
@app.route('/v1/users/<lookup_id>', methods=['GET'])
def get_user_by_id(lookup_id):
    return_value = {}
    for user in users_list:
        if user['id'] == lookup_id:
            return_value = user
    return return_value
           

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)