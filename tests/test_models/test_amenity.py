#!/usr/bin/python3
"""
Unittest for Amenity Class
"""
import contextlib
from models.amenity import Amenity
import unittest
from datetime import datetime
from io import StringIO
import pep8


class TestBaseClass(unittest.TestCase):
    def test_classtype(self):
        """tests class type"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_for_style(self):
        """style test"""
        pep_style = pep8.StyleGuide(quiet=True)
        error_check = pep_style.check_files(['models/amenity.py'])
        self.assertTrue(error_check is pep_style.check_files(['models/engine/file_storage.py']))

    def test_attr(self):
        """test attributes"""
        amenity = Amenity()
        uuid_val = amenity.id
        self.assertEqual(amenity.id, uuid_val)
        self.assertIsInstance(amenity.id, str)
        created_time = amenity.created_at
        updated_time = amenity.updated_at
        self.assertEqual(created_time, amenity.created_at)
        self.assertEqual(updated_time, amenity.updated_at)

    def test_attr_kwargs(self):
        """tests instance init with kwargs"""
        amenity = Amenity()
        amenity.name = "New Model"
        amenity.my_number = 201
        amenity_json = amenity.to_dict()
        my_new_model = Amenity(**amenity_json)
        self.assertFalse(amenity is my_new_model)
        self.assertEqual(my_new_model.name, "New Model")
        self.assertEqual(my_new_model.my_number, 201)
        # unfinished

    def test_save_method(self):
        """test save method"""
        amenity = Amenity()
        amenity.name = "prototype"
        amenity.number = 1
        amenity.save()
        update_time = amenity.updated_at
        self.assertEqual(update_time, amenity.updated_at)
        with self.assertRaises(TypeError):
            amenity.save(None)

    def test_str_method(self):
        """test str method"""
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            amenity = Amenity()
            obj_print = amenity.__str__()
            print(amenity)
        output = temp_stdout.getvalue().strip()
        # print(output)
        self.assertEqual(output, obj_print)

    def test_to_dict(self):
        """test to_dict method"""
        amenity = Amenity()
        self.assertTrue(type(amenity.to_dict()) is dict)
        objdict = amenity.to_dict()
        self.assertEqual(objdict, amenity.to_dict())


if __name__ == '__main__':
    unittest.main()
