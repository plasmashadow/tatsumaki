from tatsumaki.connection import connect
from tatsumaki.fields import ReferenceType, StringType, ListType
from tatsumaki.base import Document
from schematics.models import Model
try:
    from pymongo.dbref import DBRef
except ImportError:
    from bson.dbref import DBRef
from tornado.testing import gen_test
from tornado.testing import AsyncTestCase


class TestFields(AsyncTestCase):

    def setUp(self):
        super(TestFields, self).setUp()
        connect('mongodb://localhost:27017/test')

    @gen_test
    def test_reference_property(self):

        class Location(Document):
            lat = StringType()
            lon = StringType()

        class Person(Document):
            loc = ReferenceType(Location)

        loc = Location(id="123")
        yield loc.save()
        p = Person(id="23")
        p.loc = loc
        yield p.save()
        self.assertIsNotNone(p.to_primitive())

    @gen_test
    def test_reference_list_property(self):

        class Location(Document):
            lat = StringType()
            lon = StringType()

        class NewPerson(Document):
            lists = ListType(ReferenceType(Location))

        loc1 = Location(id="123")
        yield loc1.save()
        loc2 = Location(id="124")
        yield loc2.save()

        p = NewPerson(id="35")
        p.lists = [loc1, loc2]
        yield p.save()

        self.assertIsNotNone(p.to_primitive())

    @gen_test
    def test_refrence_query(self):
        class Location(Document):
            lat = StringType()
            lon = StringType()

        class NewPerson(Document):
            lists = ListType(ReferenceType(Location))

        results = yield NewPerson.find({}, length=100)
        self.assertIsNotNone(results)
        result = results[0]
        self.assertIsInstance(result.lists[0], DBRef)
