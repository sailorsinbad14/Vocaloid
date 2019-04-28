from flask import Flask, jsonify
from useSpeechToText import useSpeechToText

app = Flask(__name__, static_folder='website/')
ffmpegAddress = r"C:\Program Files\ffmpeg\bin\ffmpeg.exe"
path = "transcribe/audio/jb.wav"

@app.route("/")
def root():
    return app.send_static_file('index.html')

@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)

@app.route("/test")
def testing():
    app.logger.debug(request.files['file'].filename)
    timestamps, display, language = useSpeechToText()

    timestamps

    return_dict = {}
    return_dict["timestamps"] = timestamps
    return_dict["display"] = display
    return_dict["language"] = language

    return jsonify(return_dict)

if __name__ == '__main__' :
    app.run(debug=True)
