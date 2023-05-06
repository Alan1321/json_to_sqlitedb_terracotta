import sys
from sqlite import sqlite
from validate import validate
from utils import info

KEY_NAMES = ('type', 'date', 'band')
PATH = 'path'
DRIVER_NAME = None
JSON_FILE_PATH = None
OPTION = None

if len(sys.argv) != 4:
    info()
    sys.exit()

OPTION = sys.argv[1]
DRIVER_NAME = sys.argv[2]
JSON_FILE_PATH = sys.argv[3]

validate(OPTION, DRIVER_NAME, JSON_FILE_PATH, KEY_NAMES, PATH)
print("Validation Complete")

sqlite(OPTION, DRIVER_NAME, JSON_FILE_PATH, KEY_NAMES, PATH)
print(f"{DRIVER_NAME} operation {OPTION} complete.")