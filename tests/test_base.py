#!/usr/bin/python3
"""
Unittest for BaseModel Class
"""
from models.base_model import BaseModel
import unittest


class TestBaseClass(unittest.TestCase):
    def test_classtype(self):
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)

#    def test_baseclass_attr(self):
#        my_model = BaseModel()

#    def test_str_method(self):
#        temp_stdout = StringIO()
#        with contextlib.redirect_stdout(temp_stdout):
#            my_model = BaseModel()
#            print(my_model)
#        output = temp_stdout.getvalue().strip()
#        assert output, '[BaseModel] (c98e786a-9a2d-409e-bb94-1721cbaca19a) {'id': 'c98e786a-9a2d-409e-bb94-1721cbaca19a', 'created_at': datetime.datetime(2022, 1, 25, 9, 14, 2, 409891), 'updated_at': datetime.datetime(2022, 1, 25, 9, 14, 2, 409899), 'name': 'My First Model', 'my_number': 89}'
#        self.assertEqual(output, '[BaseModel] (c98e786a-9a2d-409e-bb94-1721cbaca19a) {'id': 'c98e786a-9a2d-409e-bb94-1721cbaca19a', 'created_at': datetime.datetime(2022, 1, 25, 9, 14, 2, 409891), 'updated_at': datetime.datetime(2022, 1, 25, 9, 14, 2, 409899), 'name': 'My First Model', 'my_number': 89}')



if __name__ == '__main__':
    unittest.main()
