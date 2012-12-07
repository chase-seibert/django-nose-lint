import os
import socket
from nose.plugins import Plugin
from django.conf import settings
try:
    settings.configure(DEBUG=True, TEMPLATE_DEBUG=True, TEMPLATE_DIRS=('/home/web-apps/myapp', '/home/web-apps/base'), ROOT_URLCONF='urls.py')
except RuntimeError:
    pass
from django.test.client import Client
from django.template import Template


DEFAULT_MAX_MS = 1000


class DjangoNoseLint(Plugin):

    name = 'noselint'
    env_opt = 'NOSE_DJANGOLINT'
    options = None
    max_time_ms = None
    times = {}

    def options(self, parser, env=os.environ):
        parser.add_option(
            '--lint',
            dest='error_codes', default=env.get(self.env_opt, ''),
            help='DjangoNoseLint errors codes')
        parser.add_option(
            '--maxms',
            dest='max_time_ms', default=env.get(self.env_opt, ''),
            help='DjangoNoseLint max test time in milliseconds')

    def configure(self, options, conf):
        self.conf = conf
        self.options = options

        error_codes = getattr(options, 'error_codes', '')
        self.enabled = error_codes != ''
        if self.enabled:
            for code in error_codes.split(','):
                try:
                    getattr(self, code)()
                except AttributeError:
                    print 'Invalid DjangoNoseLint --lint argument: %s' % code
                    exit(1)

    def ESOK(self):
        socket.getaddrinfo = raise_ESOK

    def ETEM(self):
        Template.render = classmethod(raise_ETEM)

    def ECLI(self):
        Client.__init__ = classmethod(raise_ECLI)

    def ESLO(self):
        self.max_time_ms = int(getattr(self.options, 'max_time_ms') or DEFAULT_MAX_MS)

    def EALL(self):
        for attr in dir(self):
            if attr.startswith('E') and attr != 'EALL':
                getattr(self, attr)()

    def startTest(self, test):
        from datetime import datetime
        self.times[test] = datetime.now()

    def stopTest(self, test):
        if test not in self.times or not self.max_time_ms:
            return
        from datetime import datetime
        delta = datetime.now() - self.times[test]
        delta_ms = delta.seconds * 1000 + delta.microseconds / 1000
        if delta_ms > self.max_time_ms:
            raise DeprecationWarning('DjangoNoseLint Error: ESLO - test took %s ms' % delta_ms)


def raise_ESOK(*args, **kwargs):
    raise DeprecationWarning('DjangoNoseLint Error: ESOK - cannot open socket connections in tests')


def raise_ETEM(*args, **kwargs):
    raise DeprecationWarning('DjangoNoseLint Error: ETEM - cannot render Django templates in tests.')


def raise_ECLI(*args, **kwargs):
    raise DeprecationWarning('DjangoNoseLint Error: ECLI - cannot use the Django test client in tests.')
