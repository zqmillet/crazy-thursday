"""
this is the setup of this package.
"""

from setuptools import setup
from setuptools import find_packages

from crazy_thursday import VERSION

setup(
    name='crazy_thursday',
    version='.'.join(map(str, VERSION)),
    author='kinopico',
    author_email='zqmillet@qq.com',
    url='https://github.com/zqmillet/crazy-thursday',
    description='v me 50',
    packages=find_packages(),
    entry_points = {
        'console_scripts': [
            'crazy-thursday = crazy_thursday.__main__:main',
            'kfc = crazy_thursday.__main__:main',
        ],
    },
)
