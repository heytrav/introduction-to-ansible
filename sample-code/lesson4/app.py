import os
import config
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)
app.config.from_object(config.Config)
db = SQLAlchemy(app)

# list of cat images

@app.route('/')
def index():
    result = db.engine.execute(
        'select image from images where id = %d ' % random.randint(0,9)
    )
    url = result.first()[0]
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
