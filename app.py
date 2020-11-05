from flask import Flask
from flask import render_template
from flask import request
from playlist_length import playlistlength

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    data = request.args.get('link')
    try:
        time = playlistlength(data)
    except:
        time = False
    return render_template('index.html', time=time)
