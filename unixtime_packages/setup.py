from setuptools import setup

setup(
    name='unixtime_package',
    version='0.1',
    description='description',
    url='http://github.com/name/package_name',
    author='Nikita',
    author_email='email@example.com',
    license='MIT',
    packages=['get_unixtime_package'],
    install_requires=[
        'requests==2.26.0',
    ],
    entry_points={
        'console_scripts': [
            'get_time=get_unixtime_package.unixtime:main',
        ]
    }
)