from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='theme_searcher',
   version='1.0',
   description='basic theme search engine and api',
   license="MIT",
   long_description=long_description,
   author='Igor Stulikov',
   author_email='igor.s.stulikov@gmail.com',
   url="",
   packages=['theme_searcher'],
   install_requires=['sanic==19.9.0'],
   test_suite="tests"
)