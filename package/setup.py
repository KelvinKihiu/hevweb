from setuptools import setup, find_packages
from hevweb import __version__

setup(
    name='hevweb',
    version=__version__,
    description='Hevok Web Framework',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['Tempita>=0.5.2', 'watchdog>=0.8.3', 'WebOb>=1.7.4', 'Jinja2>=2.10', 'docopt', 'paste'],
    author='Kelvin Kihiu',
    author_email='klvnkihiu@gmail.com',
    keywords=['hevweb python'],
    url='https://github.com/',
    entry_points={
        'console_scripts': [
            'hevweb=hevweb.hevweb_cli:main',
        ],
    }
)