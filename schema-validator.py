import json
from jsonschema import validate, exceptions

# Load the JSON Schema
with open("2.2 CivilCommon Json Schema.txt", "r") as schema_file:
    schema = json.load(schema_file)

# Load the JSON data to validate
with open("MDDC_Output_MDDC20230817.txt_523_010100215942019_201.json", "r") as data_file:
    data = json.load(data_file)

try:
    validate(data, schema)
    print("JSON data is valid against the schema.")
except exceptions.ValidationError as e:
    print("JSON data is not valid against the schema.")
    print(e)
