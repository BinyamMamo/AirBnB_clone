#!/usr/bin/python3

from models.engine.file_storage import FileStorage

storage = FileStorage("fiely.json")
storage.reload()
