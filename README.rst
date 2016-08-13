Tatsumaki
========================

AsyncORM for Mongodb made with Motor and Tornado.

**USAGE:**

.. code-block:: python

     from tatsumaki import Document
     from tatsumaki import connect
     from tatsumaki.fields import *
     from tornado.gen import coroutine

     class Person(Document):
         name = StringType()
         age = IntType()

     class Address(Document):
         personed = ReferenceType(Person)

     @coroutine
     def create_new_person():
         p = Person(id="11231")
         p.name = "hello"
         p.age = 24
         yield p.save()
         address = Address()
         address.personed = p
         yield address.save()


**LICENSE**
MIT
