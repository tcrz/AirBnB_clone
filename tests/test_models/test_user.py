#!/usr/bin/python3
"""
Unittest for User Class
"""
import contextlib
from models.user import User
import unittest
from datetime import datetime
from io import StringIO
import pep8


class TestBaseClass(unittest.TestCase):
    def test_classtype(self):
        """tests class type"""
        my_user = User()
        self.assertIsInstance(my_user, User)

    def test_for_style(self):
        """style test"""
        pep_style = pep8.StyleGuide(quiet=True)
        error_check = pep_style.check_files(['models/user.py'])
        self.assertEqual(error_check, 0)

    def test_attr(self):
        """test attributes"""
        my_user = User()
        uuid_val = my_user.id
        self.assertEqual(my_user.id, uuid_val)
        self.assertIsInstance(my_user.id, str)
        created_time = my_user.created_at
        updated_time = my_user.updated_at
        self.assertEqual(created_time, my_user.created_at)
        self.assertEqual(updated_time, my_user.updated_at)

    def test_attr_kwargs(self):
        """tests instance init with kwargs"""
        my_user = User()
        my_user.name = "New Model"
        my_user.my_number = 201
        my_user_json = my_user.to_dict()
        my_new_model = User(**my_user_json)
        self.assertFalse(my_user is my_new_model)
        self.assertEqual(my_new_model.name, "New Model")
        self.assertEqual(my_new_model.my_number, 201)
        # unfinished

    def test_save_method(self):
        """test save method"""
        my_user = User()
        my_user.name = "prototype"
        my_user.number = 1
        my_user.save()
        update_time = my_user.updated_at
        self.assertEqual(update_time, my_user.updated_at)
        with self.assertRaises(TypeError):
            my_user.save(None)

    def test_str_method(self):
        """test str method"""
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            my_user = User()
            obj_print = my_user.__str__()
            print(my_user)
        output = temp_stdout.getvalue().strip()
        # print(output)
        self.assertEqual(output, obj_print)

    def test_to_dict(self):
        """test to_dict method"""
        my_user = User()
        self.assertTrue(type(my_user.to_dict()) is dict)
        objdict = my_user.to_dict()
        self.assertEqual(objdict, my_user.to_dict())


if __name__ == '__main__':
    unittest.main()
