import sys
from sqlite import sqlite
from validate import validate
from utils import info

KEY_NAMES = ('type', 'date', 'band')
PATH = 'path'
DRIVER_NAME = None
JSON_FILE_PATH = []
OPTION = None

if len(sys.argv) < 4:
    info()
    sys.exit()

OPTION = sys.argv[1]
DRIVER_NAME = sys.argv[2]
for i in range(len(sys.argv) - 3):
    JSON_FILE_PATH.append(sys.argv[i+3])

print(JSON_FILE_PATH)
validate(OPTION, DRIVER_NAME, JSON_FILE_PATH, KEY_NAMES, PATH)
print("Validation Complete")

sqlite(OPTION, DRIVER_NAME, JSON_FILE_PATH, KEY_NAMES, PATH)
print(f"{DRIVER_NAME} operation {OPTION} complete.")

['main.py' ,'raster.sqlite','a.json' ,'b.json' ,'c.json']