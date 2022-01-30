#!/usr/bin/python3
"""
Unittest for Review Class
"""
import contextlib
from models.review import Review
import unittest
from datetime import datetime
from io import StringIO
import pep8


class TestBaseClass(unittest.TestCase):
    def test_classtype(self):
        """tests class type"""
        review = Review()
        self.assertIsInstance(review, Review)

    def test_for_style(self):
        """style test"""
        pep_style = pep8.StyleGuide(quiet=True)
        error_check = pep_style.check_files(['models/state.py'])
        self.assertEqual(error_check.total_errors, 0)

    def test_attr(self):
        """test attributes"""
        review = Review()
        uuid_val = review.id
        self.assertEqual(review.id, uuid_val)
        self.assertIsInstance(review.id, str)
        created_time = review.created_at
        updated_time = review.updated_at
        self.assertEqual(created_time, review.created_at)
        self.assertEqual(updated_time, review.updated_at)

    def test_attr_kwargs(self):
        """tests instance init with kwargs"""
        review = Review()
        review.name = "New Model"
        review.my_number = 201
        review_json = review.to_dict()
        my_new_model = Review(**review_json)
        self.assertFalse(review is my_new_model)
        self.assertEqual(my_new_model.name, "New Model")
        self.assertEqual(my_new_model.my_number, 201)
        # unfinished

    def test_save_method(self):
        """test save method"""
        review = Review()
        review.name = "prototype"
        review.number = 1
        review.save()
        update_time = review.updated_at
        self.assertEqual(update_time, review.updated_at)
        with self.assertRaises(TypeError):
            review.save(None)

    def test_str_method(self):
        """test str method"""
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            review = Review()
            obj_print = review.__str__()
            print(review)
        output = temp_stdout.getvalue().strip()
        # print(output)
        self.assertEqual(output, obj_print)

    def test_to_dict(self):
        """test to_dict method"""
        review = Review()
        self.assertTrue(type(review.to_dict()) is dict)
        objdict = review.to_dict()
        self.assertEqual(objdict, review.to_dict())


if __name__ == '__main__':
    unittest.main()
