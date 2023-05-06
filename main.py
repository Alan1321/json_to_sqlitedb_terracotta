import sys
from sqlite import sqlite

#command line arguments
print(sys.argv)

#arguments to accept
#1.driver_name
#2. path to json file

print("#Syntax: python3 main.py <driver_name> <path_to_json_file>")
print('#JSON argument needed in the format: \n[{\n\t"type":"",\n\t"date":"",\n\t"band":"",\n\t"path":""\n}]')

sqlite('raster1.sqlite', 'test.json')