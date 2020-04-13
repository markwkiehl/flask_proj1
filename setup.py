#setup.py

from setuptools import setup

#name & packages must point to the inner folder name for the application
setup(
    version='0.1',
    name='proj_flask',
    packages=['proj_flask'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
    description='describe thie project',
    url='http://github.com/proj/folder',
    author='Mechatronic Solutions LLC',
    author_email='mechtronsol@gmail.com',
    license='MIT',
    zip_safe=False
)
