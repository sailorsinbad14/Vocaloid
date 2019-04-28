from flask import Flask
app = Flask(__name__)
from useSpeechToText import useSpeechToText
# ffmpegAddress = r"C:\Program Files\ffmpeg\bin\ffmpeg.exe"
path = r'resources/twinkles.mp3'

@app.route("/")
def testing():
    same = useSpeechToText(ffmpegAddress,path)
    return same
    # print (same)

if __name__ == '__main__' :
    app.run(debug=True)
