import terracotta as tc
from utils import read_json, syntax
import sys

class sqlite():
    def __init__(self,option, driver_name, json_file_path, key_names, path):
        self.driver_name = driver_name
        self.json_file_path = json_file_path
        self.option = option
        self.key_names = key_names
        self.path = path
        self.json_data = read_json(self.json_file_path)
        self.start()

    def start(self):
        if self.option == "-new":
            self.create_db()
        elif self.option == "-append":
            self.append_db()

    def create_db(self):
        driver = tc.get_driver(self.driver_name)
        try:
            driver.create(self.key_names)
        except:
            print("ERROR. Database with that name already exists. Use -append option if you want to append to it instead.")
            print(syntax())
            sys.exit()

        for data in self.json_data:
            keys, raster_file = self.separate_key_filename(data)
            driver.insert(keys, raster_file)

    def append_db(self):
        driver = tc.get_driver(self.driver_name)
        for data in self.json_data:
            keys, raster_file = self.separate_key_filename(data)
            driver.insert(keys, raster_file)

    def separate_key_filename(self, data):
        keys = (data[self.key_names[0]],data[self.key_names[1]],data[self.key_names[2]])
        raster_file = data[self.path]
        return keys, raster_file
