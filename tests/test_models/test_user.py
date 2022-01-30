#!/usr/bin/python3
"""test for User"""
import unittest
from models.user import User
from models.base_model import BaseModel
from datetime import datetime
import pep8


class Test(unittest.TestCase):
    def test_for_style(self):
        """style test"""
        style = pep8.StyleGuide(quiet=True)
        chk = style.check_files(['models/user.py'])
        self.assertEqual(chk.total_errors, 0, "fix pep8")

    def test_docstring(self):
        """checks for docstring"""
        self.assertIsNotNone(User.__doc__)

    def test_attributes_type(self):
        """check that class"""
        my_model = BaseModel()
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
