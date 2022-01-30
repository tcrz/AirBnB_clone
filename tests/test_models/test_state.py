#!/usr/bin/python3
"""
Unittest for State Class
"""
import contextlib
from models.state import State
import unittest
from datetime import datetime
from io import StringIO
import pep8


class TestBaseClass(unittest.TestCase):
    def test_classtype(self):
        """tests class type"""
        state = State()
        self.assertIsInstance(state, State)

    def test_for_style(self):
        """style test"""
        pep_style = pep8.StyleGuide(quiet=True)
        error_check = pep_style.check_files(['models/state.py'])
        self.assertEqual(error_check, 0)

    def test_attr(self):
        """test attributes"""
        state = State()
        uuid_val = state.id
        self.assertEqual(state.id, uuid_val)
        self.assertIsInstance(state.id, str)
        created_time = state.created_at
        updated_time = state.updated_at
        self.assertEqual(created_time, state.created_at)
        self.assertEqual(updated_time, state.updated_at)

    def test_attr_kwargs(self):
        """tests instance init with kwargs"""
        state = State()
        state.name = "New Model"
        state.my_number = 201
        state_json = state.to_dict()
        my_new_model = State(**state_json)
        self.assertFalse(state is my_new_model)
        self.assertEqual(my_new_model.name, "New Model")
        self.assertEqual(my_new_model.my_number, 201)
        # unfinished

    def test_save_method(self):
        """test save method"""
        state = State()
        state.name = "prototype"
        state.number = 1
        state.save()
        update_time = state.updated_at
        self.assertEqual(update_time, state.updated_at)
        with self.assertRaises(TypeError):
            state.save(None)

    def test_str_method(self):
        """test str method"""
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            state = State()
            obj_print = state.__str__()
            print(state)
        output = temp_stdout.getvalue().strip()
        # print(output)
        self.assertEqual(output, obj_print)

    def test_to_dict(self):
        """test to_dict method"""
        state = State()
        self.assertTrue(type(state.to_dict()) is dict)
        objdict = state.to_dict()
        self.assertEqual(objdict, state.to_dict())


if __name__ == '__main__':
    unittest.main()
