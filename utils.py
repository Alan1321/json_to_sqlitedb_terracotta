import json

def syntax():
    string = ">>> Syntax: python3 main.py <option::-->-new/-append> <driver_name> <path_to_json_file>"
    return string

def json_format():
    string = '>>> JSON argument needed in the format: \n[{\n\t"type":"",\n\t"date":"",\n\t"band":"",\n\t"path":""\n}]'
    return string

def version():
    terracotta_version = "Terracotta Version: 0.7.5"
    python_version = "Python Version: 3.7"
    string = f"Dependencies:\n{terracotta_version}\n{python_version}\n"
    return string

def info():
    print("\nERROR")
    print(syntax())
    print(json_format())
    print(version())
    print("\n")


def read_json(file_path):
    file = open(file_path)
    data = json.load(file)
    file.close()
    return data