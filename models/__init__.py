#!/usr/bin/python3
""" __init__ magic method for creating python package."""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
