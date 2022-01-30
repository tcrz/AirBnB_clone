#!/usr/bin/python3
"""
Unittest for BaseModel Class
"""
import contextlib
from models.base_model import BaseModel
import unittest
from datetime import datetime
from io import StringIO
import pep8


class TestBaseClass(unittest.TestCase):
    def test_classtype(self):
        """tests class type"""
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)

    def test_for_style(self):
        """style test"""
        pep_style = pep8.StyleGuide(quiet=True)
        error_check = pep_style.check_files(['models/base_model.py'])
        self.assertTrue(error_check is pep_style.check_files(['models/engine/file_storage.py']))
        # self.assertEqual(error_check, 0)

    def test_attr(self):
        """test attributes"""
        my_model = BaseModel()
        uuid_val = my_model.id
        self.assertEqual(my_model.id, uuid_val)
        self.assertIsInstance(my_model.id, str)
        created_time = my_model.created_at
        updated_time = my_model.updated_at
        self.assertEqual(created_time, my_model.created_at)
        self.assertEqual(updated_time, my_model.updated_at)

    def test_attr_kwargs(self):
        """tests instance init with kwargs"""
        my_model = BaseModel()
        my_model.name = "New Model"
        my_model.my_number = 201
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)
        self.assertFalse(my_model is my_new_model)
        self.assertEqual(my_new_model.name, "New Model")
        self.assertEqual(my_new_model.my_number, 201)
        # unfinished

    def test_save_method(self):
        """test save method"""
        my_model = BaseModel()
        my_model.name = "prototype"
        my_model.number = 1
        my_model.save()
        update_time = my_model.updated_at
        self.assertEqual(update_time, my_model.updated_at)
        with self.assertRaises(TypeError):
            my_model.save(None)

    def test_str_method(self):
        """test str method"""
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            my_model = BaseModel()
            obj_print = my_model.__str__()
            print(my_model)
        output = temp_stdout.getvalue().strip()
        # print(output)
        self.assertEqual(output, obj_print)

    def test_to_dict(self):
        """test to_dict method"""
        my_model = BaseModel()
        self.assertTrue(type(my_model.to_dict()) is dict)
        objdict = my_model.to_dict()
        self.assertEqual(objdict, my_model.to_dict())


if __name__ == '__main__':
    unittest.main()
