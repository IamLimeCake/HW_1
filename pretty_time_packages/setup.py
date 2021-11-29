from setuptools import setup

setup(
    name='pretty_time_package',
    version='0.1',
    description='description',
    url='http://github.com/name/package_name',
    author='Nikita',
    author_email='email@example.com',
    license='MIT',
    packages=['get_pretty_time_package'],
    entry_points={
        'console_scripts': [
            'get_time_pp=get_pretty_time_package.pretty_time:main'
        ]
    }
)