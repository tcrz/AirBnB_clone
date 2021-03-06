#!/usr/bin/python3
"""
Unittest for Place Class
"""
import contextlib
from models.place import Place
import unittest
from datetime import datetime
from io import StringIO
import pep8


class TestPlaceClass(unittest.TestCase):
    def test_classtype(self):
        """tests class type"""
        place = Place()
        self.assertIsInstance(place, Place)

    def test_attr(self):
        """test attributes"""
        place = Place()
        uuid_val = place.id
        self.assertEqual(place.id, uuid_val)
        self.assertIsInstance(place.id, str)
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])
        created_time = place.created_at
        updated_time = place.updated_at
        self.assertEqual(created_time, place.created_at)
        self.assertEqual(updated_time, place.updated_at)

    def test_attr_kwargs(self):
        """tests instance init with kwargs"""
        place = Place()
        place.name = "New Model"
        place.my_number = 201
        place_json = place.to_dict()
        my_new_model = Place(**place_json)
        self.assertFalse(place is my_new_model)
        self.assertEqual(my_new_model.name, "New Model")
        self.assertEqual(my_new_model.my_number, 201)
        # unfinished

    def test_save_method(self):
        """test save method"""
        place = Place()
        place.name = "prototype"
        place.number = 1
        place.save()
        update_time = place.updated_at
        self.assertEqual(update_time, place.updated_at)
        with self.assertRaises(TypeError):
            place.save(None)

    def test_str_method(self):
        """test str method"""
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            place = Place()
            obj_print = place.__str__()
            print(place)
        output = temp_stdout.getvalue().strip()
        # print(output)
        self.assertEqual(output, obj_print)

    def test_to_dict(self):
        """test to_dict method"""
        place = Place()
        self.assertTrue(type(place.to_dict()) is dict)
        objdict = place.to_dict()
        self.assertEqual(objdict, place.to_dict())


if __name__ == '__main__':
    unittest.main()
