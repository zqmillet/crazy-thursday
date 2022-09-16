"""
this is the setup of this package.
"""

from setuptools import setup
from setuptools import find_packages

from crazy_thursday import VERSION

with open('crazy_thursday/requirements.txt', 'r', encoding='utf8') as file:
    install_requires = list(map(lambda x: x.strip(), file.readlines()))

with open('README.md', 'r', encoding='utf8') as file:
    long_description = file.read()

setup(
    name='crazy-thursday',
    version='.'.join(map(str, VERSION)),
    author='kinopico',
    author_email='zqmillet@qq.com',
    url='https://github.com/zqmillet/sphinx-console',
    description='an extension for sphinx to display console in sphinx documents',
    packages=find_packages(),
    install_requires=install_requires,
    long_description=long_description,
    long_description_content_type='text/markdown',
    package_data={
        'crazy_thursday': ['*'],
    },
    entry_points = {
        'console_scripts': [
            'crazy-thursday=crazy_thursday.__main__:main',
            'kfc=crazy_thursday.__main__:main',
        ],
    }
)
