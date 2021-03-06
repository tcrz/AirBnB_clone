#!/usr/bin/python3
"""
Unittest for Place Class
"""
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import models
import unittest


class TestFileStorageClass(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel()
        self.new_model = BaseModel()
        self.store = FileStorage()

    def test_attrs(self):
        self.assertEqual(self.store._FileStorage__file_path, "file.json")
        self.assertIsInstance(self.store._FileStorage__objects, dict)

    def test_all(self):
        """test 'all' method attributes"""
        objs = self.store.all()
        self.assertIsInstance(self.store.all(), dict)
        self.assertCountEqual(objs, self.store.all())

    def test_new(self):
        """test 'new' method"""
        self.store.new(self.new_model)
        objs = self.store.all()
        self.assertEqual(objs, self.store.all())

    def test_save(self):
        """test save method"""
        obj = BaseModel()
        models.storage.save()
        self.assertEqual(os.path.exists('file.json'), True)
        self.store.save()
        self.assertEqual(os.path.exists('file.json'), True)

    def test_reload(self):
        """test reload method"""
        self.store.reload()
        objs = self.store.all()
        self.assertEqual(objs, self.store.all())


if __name__ == '__main__':
    unittest.main()
