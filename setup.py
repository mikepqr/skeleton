try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Skeleton Project',
    'author': 'Michael Williams',
    'url': 'http://github.com/williamsmj',
    'download_url': 'Where to download it.',
    'author_email': 'mike@pentangle.net',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
