from flask import Flask, request, render_template, send_file
from io import BytesIO
from pytube import YouTube

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        link = request.form['link']
        video = YouTube(link)
        stream = video.streams.get_highest_resolution()
        file = BytesIO()
        stream.stream_to_buffer(file)
        file.seek(0)
        return send_file(file, as_attachment=True, mimetype='video/mp4', download_name=f"{video.title}.mp4")
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
