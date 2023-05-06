import terracotta as tc
import json

class sqlite():
    def __init__(self, driver_name,json_file_path):
        self.driver_name = driver_name
        self.json_file_path = json_file_path
        self.key_names = ('type', 'date', 'band')
        self.json_data = None
        self.start()

    def start(self):
        self.read_json()
        self.create_db()

    def read_json(self):
        file = open(self.json_file_path)
        self.json_data = json.load(file)
        file.close()
        print(self.json_data)

    def create_db(self):
        driver = tc.get_driver(self.driver_name)
        driver.create(self.key_names)

        for data in self.json_data:
            keys, raster_file = self.separate_key_filename(data)
            driver.insert(keys, raster_file)

    def separate_key_filename(self, data):
        keys = (data[self.key_names[0]],data[self.key_names[1]],data[self.key_names[2]])
        raster_file = data['path']
        return keys, raster_file
