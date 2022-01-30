#!/usr/bin/python3
"""
Unittest for City Class
"""
import contextlib
from models.city import City
import unittest
from datetime import datetime
from io import StringIO
import pep8


class TestBaseClass(unittest.TestCase):
    def test_classtype(self):
        """tests class type"""
        city = City()
        self.assertIsInstance(city, City)

    def test_for_style(self):
        """style test"""
        pep_style = pep8.StyleGuide(quiet=True)
        error_check = pep_style.check_files(['models/city.py'])
        self.assertEqual(error_check.total_errors, 0)

    def test_attr(self):
        """test attributes"""
        city = City()
        uuid_val = city.id
        self.assertEqual(city.id, uuid_val)
        self.assertIsInstance(city.id, str)
        created_time = city.created_at
        updated_time = city.updated_at
        self.assertEqual(created_time, city.created_at)
        self.assertEqual(updated_time, city.updated_at)

    def test_attr_kwargs(self):
        """tests instance init with kwargs"""
        city = City()
        city.name = "New Model"
        city.my_number = 201
        city_json = city.to_dict()
        my_new_model = City(**city_json)
        self.assertFalse(city is my_new_model)
        self.assertEqual(my_new_model.name, "New Model")
        self.assertEqual(my_new_model.my_number, 201)
        # unfinished

    def test_save_method(self):
        """test save method"""
        city = City()
        city.name = "prototype"
        city.number = 1
        city.save()
        update_time = city.updated_at
        self.assertEqual(update_time, city.updated_at)
        with self.assertRaises(TypeError):
            city.save(None)

    def test_str_method(self):
        """test str method"""
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            city = City()
            obj_print = city.__str__()
            print(city)
        output = temp_stdout.getvalue().strip()
        # print(output)
        self.assertEqual(output, obj_print)

    def test_to_dict(self):
        """test to_dict method"""
        city = City()
        self.assertTrue(type(city.to_dict()) is dict)
        objdict = city.to_dict()
        self.assertEqual(objdict, city.to_dict())


if __name__ == '__main__':
    unittest.main()
