import os
from glob import glob
from setuptools import setup

package_name = 'holmes_nav'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*.launch.py'))),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*.xml'))),
        (os.path.join('share', package_name, 'models','hh2'), glob(os.path.join('models', 'hh2', '*.config'))),
        (os.path.join('share', package_name, 'models','hh2'), glob(os.path.join('models', 'hh2', '*.sdf'))),
        (os.path.join('share', package_name, 'models','hh2', 'meshes'), glob(os.path.join('models', 'hh2','meshes', '*.stl'))),
        (os.path.join('share', package_name, 'worlds','hh2'), glob(os.path.join('worlds', 'hh2', '*.model'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='pat',
    maintainer_email='png@hawaii.edu',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'hh2_node = holmes_nav.hh2_node:main'
        ],
    },
)
