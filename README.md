Django Nose lint is a [Nose](https://nose.readthedocs.org/en/latest/) plugin that can automatically fail tests that attempt to do a handful of things that can slow down the test suite. You can use options to configure which actions to fail on.

# Failures

- ESOK = Used a TCP socket
- ECLI = Used the Django Test Client
- ETEM = Tried to render a Django template
- ESLO = Test took over 1 second (takes --maxms argument)

- EALL = All of the above

# Install

`pip install django-nose-lint`

# Run it

```bash
./manage.py test --lint=EALL --maxms=300
```

# Output

```bash
Creating test database for alias 'default'...
.E
======================================================================
ERROR: test_one (tests.MyTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/cseibert/projects/django-nose-lint-test/virtualenv/lib/python2.7/site-packages/nose/case.py", line 133, in run
    self.runTest(result)
  File "/Users/cseibert/projects/django-nose-lint-test/virtualenv/lib/python2.7/site-packages/nose/case.py", line 151, in runTest
    test(result)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/unittest/case.py", line 376, in __call__
    return self.run(*args, **kwds)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/unittest/case.py", line 355, in run
    result.stopTest(self)
  File "/Users/cseibert/projects/django-nose-lint-test/virtualenv/lib/python2.7/site-packages/nose/proxy.py", line 180, in stopTest
    self.plugins.stopTest(self.test)
  File "/Users/cseibert/projects/django-nose-lint-test/virtualenv/lib/python2.7/site-packages/nose/plugins/manager.py", line 99, in __call__
    return self.call(*arg, **kw)
  File "/Users/cseibert/projects/django-nose-lint-test/virtualenv/lib/python2.7/site-packages/nose/plugins/manager.py", line 167, in simple
    result = meth(*arg, **kw)
  File "/Users/cseibert/projects/django-nose-lint-test/virtualenv/lib/python2.7/site-packages/noselint/__init__.py", line 76, in stopTest
    raise DeprecationWarning('DjangoNoseLint Error: ESLO - test took %s ms' % delta_ms)
DeprecationWarning: DjangoNoseLint Error: ESLO - test took 1101 ms

----------------------------------------------------------------------
Ran 1 test in 1.104s

FAILED (errors=1)
```

# More info

I have posted a quickstart guide on [my blog](http://chase-seibert.github.com/blog/2012/12/07/django-nose-lint.html).
