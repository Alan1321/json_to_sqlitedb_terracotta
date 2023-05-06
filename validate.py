from utils import read_json, syntax, json_format
import sys

class validate():
    def __init__(self, option, db_name, json_file_path, key_names, path):
        self.db_name = db_name
        self.json_file_path = json_file_path
        self.option = option
        self.key_names = key_names
        self.path = path
        self.start()

    def start(self):
        self.validate_db_name()
        self.validate_json_file()

    def validate_option(self):
        if option != "-new" or option != "-append":
            print(f"\n\nFAILED validate.py LINE 19 -- Invalid Option. Pick --> -new\-append \n")
            print(syntax())
            sys.exit()

    def validate_db_name(self):
        if self.db_name[-7:len(self.db_name)] != ".sqlite":
            print("\n\nFAILED validate.py LINE 25 -- Invalid db_name. Make sure the db name ends with .sqlite. Example --> raster.sqlite, hello.sqlite\n")
            sys.exit()

    def validate_json_file(self):
        for file in self.json_file_path:
            data = read_json(file)
            try:
                for d in data:
                    arg1 = d[self.key_names[0]]
                    arg2 = d[self.key_names[1]]
                    arg3 = d[self.key_names[2]]
            except:
                print("\n\nFAILED validate.py LINE 36 -- Make sure of all the json data format.")
                print(json_format())
                sys.exit()
