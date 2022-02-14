import os
from pathlib import Path
import ex1

print(f'String imported from ex1.py: {ex1.ex1_string}')
print(f'file path: {os.path.dirname(__file__)}')
print(f'file path: {Path(__file__).parents[0]}')

ex1.yolo(2)

import sys
print(sys.path)

from config import config_dict
print(config_dict['key1'])

print('done')
