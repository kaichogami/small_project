'''
Write the code here to transform the data.json file to the required format. Please store the new file under name 'output.json'
'''
import json

file_name = 'data.json'
with open(file_name) as f:
    data_raw = json.load(f)

data_raw[]

def convert_data_json(data_raw):
    new_data_dict = {}
    for x in data_raw:
        new_data_dict['restaurants'][0]['name'] = 'bbsr'
    new_data_dict.to_json()
    with open('output_json.json') as f:
        f.write(new_data_dict)

    return new_data_json