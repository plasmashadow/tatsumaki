# -*- coding: utf-8 -*-
from schematics.models import Model
from tornado.gen import coroutine, Return
from tatsumaki.connection import Connection
from tatsumaki.exc import TatsumakiException


class Document(Model):

    _id_field = '_id'

    def __init__(self, *args, **kwargs):
        self._classname = self.__class__.__name__
        self._id_to_set = kwargs.get("id", None)
        if self._id_to_set:
            kwargs.pop("id")
        super(Document, self).__init__(*args, **kwargs)

    @coroutine
    def save(self):
        self.validate()
        data_to_save = self.to_dict()
        if self._id_to_set:
            data_to_save[self._id_field] = self._id_to_set
        yield Connection.get_collection(self._classname).save(data_to_save)
        self.id = data_to_save[self._id_field]
        raise Return(self.id)

    @coroutine
    def delete(self):
        data_to_remove = self.to_dict()
        if not self.id:
            raise TatsumakiException("No %s field found" % (self._id_field))
        coll = Connection.get_collection(self._classname)
        yield coll.remove({"_id": self.id})
        raise Return(self.id)

    def validate(self):
        super(Document, self).validate()

    def to_dict(self):
        return self._data
