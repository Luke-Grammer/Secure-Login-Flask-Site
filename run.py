# run.py
# Written by Luke Grammer (12/19/19)

# local imports
from app import create_app

# third-party imports
import os

config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
