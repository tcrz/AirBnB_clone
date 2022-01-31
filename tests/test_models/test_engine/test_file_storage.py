#!/usr/bin/python3
"""
Unittest for Place Class
"""

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import unittest


class TestBaseClass(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel()
        self.new_model = BaseModel()
        self.store = FileStorage()

    def test_all(self):
        """test 'all' method attributes"""
        objs = self.store.all()
        self.assertEqual(objs, self.store.all())

    def test_new(self):
        """test 'new' method"""
        self.store.new(self.new_model)
        objs = self.store.all()
        self.assertEqual(objs, self.store.all())

    def test_save(self):
        """test save method"""
        self.store.save()

    def test_reload(self):
        """test reload method"""
        self.store.reload()
        objs = self.store.all()
        self.assertEqual(objs, self.store.all())


if __name__ == '__main__':
    unittest.main()
