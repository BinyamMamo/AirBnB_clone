#!/usr/bin/python3

import inspect
from models.base_model import BaseModel

print(inspect.getmembers(BaseModel, predicate=inspect.isfunction))