from setuptools import setup
import os
from glob import glob

package_name = 'sample_maps'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'sample_maps'), glob(os.path.join('sample_maps', '*.pgm'))),
        (os.path.join('share', package_name, 'sample_maps'), glob(os.path.join('sample_maps', '*.yaml'))),
        (os.path.join('share', package_name, 'sample_maps'), glob(os.path.join('sample_maps', '*.data'))),
        (os.path.join('share', package_name, 'sample_maps'), glob(os.path.join('sample_maps', '*.posegraph'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ranlab',
    maintainer_email='png@hawaii.edu',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
