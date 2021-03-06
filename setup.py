from distutils.core import setup

setup(
    name='coinmetrics',
    version='0.0.1',
    packages=['coinmetrics',],
    license='MIT',
    description = 'Python wrapper around the coinmetrics.io API.',
    long_description=open('README.md').read(),
    author = 'Christoforou Manolis',
    author_email = 'emchristoforou@gmail.com',
    install_requires=['requests', 'pytest', 'responses'],
    url = 'https://github.com/man-c/coinmetrics',
    )
