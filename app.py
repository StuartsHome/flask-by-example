import os
import requests 
import operator
import re
import nltk
# import requests library to send external HTTP GET requqests to grab the URL
from flask import Flask, render_template, request
# Flask request object to handle GET and POST requests within the Flask app.
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from stop_words import stops
from collections import Counter
from bs4 import BeautifulSoup
from rq import Queue    
from rq.job import Job
from worker import conn


load_dotenv()                   # Load gathers the value from dotenv file.
                                # The key/values are now present as system environment
                                # variable and they can be conveniently accessed
                                # via os.getenv()
                                # Use from_object when configs contain classes
#os.environ["APP_SETTINGS"]
#print("OS Environ before", os.environ["APP_SETTINGS"])
#os.getenv("APP_SETTINGS")
#print("get", os.getenv("APP_SETTINGS"))
#config.DevelopmentConfig

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True     # Was set to False, but following tutorial states False
db = SQLAlchemy(app)
q = Queue(connection=conn)

from models import *

#app.config.from_object(os.environ["APP_SETTINGS"])ç
print("OS environ after", os.environ['APP_SETTINGS'])

@app.route('/', methods = ['GET', 'POST'])
def index():
    errors = []
    results = {}
    if request.method == "POST":
        # get URL user has entered
        try:
            url = request.form['url']
            r = requests.get(url)
            print(r.text)
        except:
            errors.append(
                "Unable to get URL. Please make sure it's valid and try again"
            )
        if r:
            # text processing
            raw = BeautifulSoup(r.text, 'html.parser').get_text()
            nltk.data.path.append('./nltk_data/') # set the path
            tokens = nltk.word_tokenize(raw)
            text = nltk.Text(tokens)
            # remove punctuation, count raw words
            nonPunct = re.compile('.*[A-Za-z].*')
            raw_words = [w for w in text if nonPunct.match(w)]
            raw_word_count = Counter(raw_words)
            # stop words
            no_stop_words = [w for w in raw_words if w.lower() not in stops]
            no_stop_words_count = Counter(no_stop_words)
            results = sorted(
                no_stop_words_count.items(),
                key=operator.itemgetter(1),
                reverse=True
            )[:10]
            try:
                result = Result(
                    url = url,
                    result_all = raw_word_count,
                    result_no_stop_words=no_stop_words_count
                )
                db.session.add(result)
                db.sessions.commit()
            except:
                errors.append("Unable to add item to database.")
    return render_template('index.html', errors = errors, results=results)

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run()
    print(os.environ['APP_SETTINGS'])