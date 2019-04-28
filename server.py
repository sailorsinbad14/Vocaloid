from flask import Flask, jsonify
from useSpeechToText import useSpeechToText

app = Flask(__name__)
ffmpegAddress = r"C:\Program Files\ffmpeg\bin\ffmpeg.exe"
path = r'resources/twinkles.mp3'

@app.route("/")
def testing():
    same, display, language = useSpeechToText(ffmpegAddress,path)
    return_dict = {}
    return_dict["timestamps"] = same
    return_dict["display"] = display
    return_dict["language"] = language

    return jsonify(return_dict)

if __name__ == '__main__' :
    app.run(debug=True)
