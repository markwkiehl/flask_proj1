# __init__.py

# For help, see:	https://timothybramlett.com/How_to_create_a_Python_Package_with___init__py.html
#					https://python-packaging.readthedocs.io/en/latest/minimal.html

from flask import Flask
# The app variable is an instance of class Flask, making it 
# a member of the app package. 
# The __name__ variable will resolve to the correct package.
app = Flask(__name__)

# All view functions (those with route() decorator on top) must be imported
# in this __init__.py file. 
#import proj_flask.web_app
