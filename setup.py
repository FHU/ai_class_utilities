from setuptools import setup

package_name = 'ai_class_utilities'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Ben Clark',
    maintainer_email='bclark@fhu.edu',
    description='Utilities for create 3 robots in AI for Robotics',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'goal_translator = ai_class_utilities.goal_translator:main'
        ],
    },
)
