#!/usr/bin/python3
"""
Unittest for Place Class
"""

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import unittest
# import pep8



class TestBaseClass(unittest.TestCase):
     """FileStorage Test class"""
    # def test_for_style(self):
    #     """style test"""
    #     style = pep8.StyleGuide(quiet=True)
    #     chk = style.check_files(['models/engine/file_storage.py'])
    #     self.assertEqual(chk.total_errors, 0, "fix pep8")

     def test_docstring(self):
        """checks for docstring"""
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_instances(self):
        """checks save and reload"""
        obj = BaseModel()
        models.storage.save()
        self.assertEqual(os.path.exists('file.json'), True)
    # def setUp(self):
    #     self.model = BaseModel()
    #     self.new_model = BaseModel()
    #     self.store = FileStorage()

    # def test_for_style(self):
    #     """style test"""
    #     pep_style = pep8.StyleGuide(quiet=True)
    #     error_check = pep_style.check_files(['models/engine/file_storage.py'])
    #     # self.assertTrue(error_check is pep_style.check_files(['models/engine/file_storage.py']))
    #     # self.assertEqual(error_check, 0)

    # def test_all(self):
    #     """test 'all' method attributes"""
    #     objs = self.store.all()
    #     self.assertEqual(objs, self.store.all())

    # def test_new(self):
    #     """test 'new' method"""
    #     self.store.new(self.new_model)
    #     objs = self.store.all()
    #     self.assertEqual(objs, self.store.all())

    # def test_save(self):
    #     """test save method"""
    #     self.store.save()

    # def test_reload(self):
    #     """test reload method"""
    #     self.store.reload()
    #     objs = self.store.all()
    #     self.assertEqual(objs, self.store.all())


if __name__ == '__main__':
    unittest.main()
