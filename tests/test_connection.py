from motor import MotorClient, MotorDatabase, MotorCollection
import tatsumaki
import unittest
from tatsumaki.connection import Connection, connect, close
from tatsumaki.exc import TatsumakiException


class ConnectionTest(unittest.TestCase):
    """Unittest for connection class"""
    def setUp(self):
        connect('mongodb://localhost:27017/test')

    def tearDown(self):
        close()

    def test_connection_exists(self):
        self.assertIsNotNone(Connection.get_connection())


class ConnectionBehaviourTest(unittest.TestCase):
    """unittests for connection behaviour"""
    def test_connect(self):
        connect('mongodb://localhost:27017/test')
        self.assertIsNotNone(Connection.get_connection())

    def test_disconnect(self):
        close()
        with self.assertRaises(TatsumakiException):
            Connection.get_connection()

    def test_mongoclient(self):
        connect('mongodb://localhost:27017/test')
        conn = Connection.get_connection()
        self.assertIsInstance(conn, MotorClient)

    def test_get_collection(self):
        connect('mongodb://localhost:27017/test')
        coll = Connection.get_collection("users")
        self.assertIsInstance(coll, MotorCollection)

    def test_raising_collection_exception(self):
        close()
        with self.assertRaises(TatsumakiException):
            Connection.get_collection("users")
