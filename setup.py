try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Learn Algorithm The Hard Way',
    'author': 'Pragmatic Coder',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'alvi.akbar@realpythonengineer.com',
    'version': '0.1',
    'install_requires': ['unittest'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'lathw'
}

setup(**config)
