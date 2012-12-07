from distutils.core import setup

setup(
    name='django-nose-lint',
    version='0.1',
    author='Chase Seibert',
    author_email='chase.seibert@gmail.com',
    packages=['noselint'],
    install_requires='nose',
    entry_points={
        'nose.plugins.0.10': [
            'noselint = noselint:DjangoNoseLint'
        ]
    },
    url='https://github.com/chase-seibert/django-nose-lint',
    license='LICENSE.txt',
    description='Fails test that are slow, make network calls, use the django test client, etc.',
    long_description='''Django Nose lint is a Nose plugin that can automatically fail tests that attempt to do a handful of things that can slow down the test suite. You can use options to configure which actions to fail on.''',
)
