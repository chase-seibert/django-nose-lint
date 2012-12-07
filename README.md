Django Nose lint is a [Nose](https://nose.readthedocs.org/en/latest/) plugin that can automatically fail tests that attempt to do a handful of things that can slow down the test suite. You can use options to configure which actions to fail on.

# Failures

- ESOK = Used a TCP socket
- ECLI = Used the Django Test Client
- ETEM = Tried to render a Django template
- ESLO = Test took over 1 second (takes --maxms argument)

- EALL = All of the above

# Install and Configuration

`pip install django-nose-lint`

In `settings.py`, add the plugin:

```python
NOSE_PLUGINS = ('noselint.DjangoNoseLint', )
```

# Example

```bash
./manage.py test --lint=EALL --maxms=1000
```
