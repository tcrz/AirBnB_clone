#!/usr/bin/python3
"""
Unittest for Place Class
"""

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import unittest
import pep8


class TestBaseClass(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel()
        self.new_model = BaseModel()
        self.store = FileStorage()

    def test_for_style(self):
        """style test"""
        pep_style = pep8.StyleGuide(quiet=True)
        error_check = pep_style.check_files(['models/engine/file_storage.py'])
        
        self.assertTrue(error_check is pep_style.check_files(['models/engine/file_storage.py']))

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
