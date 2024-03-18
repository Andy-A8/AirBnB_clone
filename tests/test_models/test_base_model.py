#!/usr/bin/python3
"""Defines unittests for models/base_model.py."""


import unittest
import models
from datetime import datetime
from models.base_model import BaseModel
from time import sleep
import os
import uuid


class TestBaseModel_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""

    def test_no_args_instantiates(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_unique_ids(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        conv_uuid_one = uuid.UUID(bm1.id)
        conv_uuid_two = uuid.UUID(bm2.id)
        self.assertNotEqual(conv_uuid_one, conv_uuid_two)

    def test_two_models_different_created_at(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertLess(bm1.created_at, bm2.created_at)

    def test_two_models_different_updated_at(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertLess(bm1.updated_at, bm2.updated_at)

    def test_str_representation(self):
        dt = datetime.now()
        dt_repr = repr(dt)
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = dt
        self.assertIn("[BaseModel] (123456)", bm.__str__())
        self.assertIn("'id': '123456'", bm.__str__())
        self.assertIn("'created_at': " + dt_repr, bm.__str__())
        self.assertIn("'updated_at': " + dt_repr, bm.__str__())


if __name__ == "__main__":
    unittest.main()
