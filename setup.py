import os
from setuptools import setup, find_packages


def read(f_name):
    return open(os.path.join(os.path.dirname(__file__), f_name)).read()


setup(
    name='sway-save-outputs',
    version='0.1',
    description='script to save current sway outputs configuration to a text file',
    packages=find_packages(),
    include_package_data=True,
    package_data={},
    url='https://github.com/nwg-piotr/sway-save-outputs',
    license='MIT',
    author='Piotr Miller',
    author_email='nwg.piotr@gmail.com',
    python_requires='>=3.5.0',
    install_requires=[],
    entry_points={
        'gui_scripts': [
            'sway-save-outputs = sway_save_outputs.main:main'
        ]
    }
)
