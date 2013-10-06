from distutils.core import setup

setup(
    name = 'i3minator',
    version = '0.0.1',
    author = 'Enrico Carlesso',
    author_email = 'enricocarlesso@gmail.com',
    packages = ['i3minator'],
    scripts = ['bin/i3minator'],
    url = '',
    license = 'LICENSE.txt',
    description = 'i3 project manager similar to tmuxinator',
    long_description = open("README.txt").read(),
    install_requires = ['i3-py >= 0.6.4']
)
