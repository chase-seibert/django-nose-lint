import urllib2
from unittest import TestCase
from django.template import Context, Template
from django.test.client import Client


class DjangoNoseLintTestCase(TestCase):

    def test_socket(self):
        with self.assertRaises(DeprecationWarning):
            f = urllib2.urlopen('http://www.python.org/')
            f.read(100)

    def test_template(self):
        with self.assertRaises(DeprecationWarning):
            t = Template("My name is {{ my_name }}.")
            c = Context({"my_name": "Adrian"})
            t.render(c)

    def test_django_test_client(self):
        with self.assertRaises(DeprecationWarning):
            c = Client()
            c.post('/login/', {'username': 'john', 'password': 'smith'})
