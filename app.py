from flask import Flask
from flask import render_template
from flask import request
from playlist_length import playlistlength

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    data = request.form.get('link', None)
    time = playlistlength(data)
    if time is False and data is None:
        time = True
    # print("Data: ", data, "Time", time)  # debugging
    return render_template('index.html', time=time, data=data)
