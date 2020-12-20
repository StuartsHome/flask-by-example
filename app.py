import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()                   # Load gathers the value from dotenv file.
                                # The key/values are now present as system environment
                                # variable and they can be conveniently accessed
                                # via os.getenv()
                                # Use from_object when configs contain classes
print("OS Environ before", os.environ["APP_SETTINGS"])
print(os.getenv("APP_SETTINGS"))
#print("get", os.getenv("APP_SETTINGS"))
#config.DevelopmentConfig

app = Flask(__name__)
app.config.from_object(os.environ["APP_SETTINGS"])

#app.config.from_object(os.environ["APP_SETTINGS"])
#print("OS environ after", os.environ['APP_SETTINGS'])

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run(debug = True)