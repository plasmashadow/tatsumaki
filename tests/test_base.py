# -*- coding: utf-8 -*-

from .context import tatsumaki
from motor import MotorClient
from tatsumaki.base import Document
from tatsumaki.connection import connect, Connection
# Importing testing libraries for async tests
from tornado.testing import gen_test
from tornado.testing import AsyncTestCase


class DocumentTest(AsyncTestCase):
    """Test the Behaviour of document class"""

    def setUp(self):
        super(DocumentTest, self).setUp()
        connect('mongodb://localhost:27017/test')
        client = MotorClient("mongodb://localhost:27017/test")

        class Hello(Document):
            name = tatsumaki.StringType()
        self.Modal = Hello
        self.db = client['test']['Hello']

    @gen_test
    def test_save(self):
        new_mod = self.Modal(id=2)
        new_mod.name = "grey"
        saved = yield new_mod.save()
        ided = yield self.db.find_one({"_id": 2})
        self.assertIsNotNone(ided)
        self.assertEqual(saved, ided["_id"])

    @gen_test
    def test_remove(self):
        new_mod = self.Modal(id=2)
        yield new_mod.save()
        yield new_mod.delete()
        ided = yield self.db.find_one({"_id": 2})
        self.assertIsNone(ided)

    @gen_test
    def test_find(self):
        results = yield self.Modal.find({}, length=100)
        self.assertIsNotNone(results)
        result = results[0]
        self.assertIsInstance(result, self.Modal)

    def tearDown(self):
        super(DocumentTest, self).tearDown()

if __name__ == '__main__':
    unittest.main()
