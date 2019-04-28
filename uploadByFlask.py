from flask import Flask
app = Flask(__name__)
from useSpeechToText import useSpeechToText
ffmpegAddress = r"C:\Program Files\ffmpeg\bin\ffmpeg.exe"
path = r'C:\Users\lbm4\PycharmProjects\Vocaloid\resources\twinkles.mp3'

@app.route("/")
def testing():
    return useSpeechToText(ffmpegAddress,path)

if __name__ == '__main__' :
    app.run(debug=True)