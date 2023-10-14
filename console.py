#!/usr/bin/python3

import models
from models.base_model import BaseModel
# from models.base_model import BaseModel

# if __name__ == "__main__":
bm = BaseModel(name="Bini", age=20, created_at="2017-09-28T21:03:54.052298")
print("-----------")
bm.save()
# b = BaseModel()
# print("-----------")
