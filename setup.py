from distutils.core import setup


setup(
    name='aamnotifs',
    version='0.1.1',
    author='Andrei Marcu',
    author_email='andrei@marcu.net',
    packages=['aamnotifs'],
    url='http://github.com/adewinter/aamnotifs',
    license='LICENSE.txt',
    description='Simple notifications implementation with RabbitMQ using pika.',
    install_requires=[
        "pika",
    ],
)
