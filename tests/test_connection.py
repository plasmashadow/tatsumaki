from motor import MotorClient
import tatsumaki
import unittest
import mock
from tatsumaki.connection import Connection, connect, close

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
        self.assertIsInstance(Connection.get_connection(), Connection)

    def test_disconnect(self):
        close()
        self.assertIsNone(Connection.get_connection())

    def test_mongoclient(self):
        connect('mongodb://localhost:27017/test')
        conn = Connection.get_connection()
        self.assertIsInstance(conn._connection, MotorClient)
