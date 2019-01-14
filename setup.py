import os
from setuptools import setup


with open(os.path.join(os.path.dirname(__file__), 'VERSION')) as f:
    VERSION = f.read()

tests_require = [
    'Django>=2.1', 'WebTest==2.0.24', 'django-webtest==1.8.0', 'mock==1.0.1']

setup(
    name='sample_project',
    version=VERSION,
    description='Sample project.',
    long_description='\n'.join((
        open('README.rst').read(),
        open('CHANGES.rst').read(),
    )),
    author='Erik van Widenfelt',
    author_email='ew2789@gmail.com',
    maintainer='Erik van Widenfelt',
    url='https://github.com/erikvw/sample-project',
    packages=[
        'sample_project',
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Django",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Framework :: Django",
        "Framework :: Django :: 2.1",
        "Programming Language :: Python",
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        "License :: OSI Approved :: BSD License",
    ],
    python_requires=">=3.6",
    tests_require=tests_require,
    include_package_data=True,
    test_suite='runtests.main',
)
