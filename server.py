from flask import Flask, jsonify
from useSpeechToText import useSpeechToText

app = Flask(__name__, static_folder='website/')
# ffmpegAddress = r"C:\Program Files\ffmpeg\bin\ffmpeg.exe"
path = r"transcribe/audio/numb_.flac"
path2 = r"transcribe/audio/numb__.flac"
path3 = r"transcribe/audio/numb___.flac"


ffmpegAddress = r"C:\Program Files\ffmpeg\bin\ffmpeg.exe"

# def Merge(dict1, dict2,):
#     res = {**dict1, **dict2,}
#     return res
@app.route("/")
def root():
    return app.send_static_file('index.html')

@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)

@app.route("/test")
def testing():
    same, display, language = useSpeechToText(path)
    print (same)
    same2, display2, language2 = useSpeechToText(path2)
    print (same2)
    same3, display3, language3 = useSpeechToText(path3)
    print(same3)
    sames = dict(list(same.items()) + list(same2.items()) + list(same3.items()))
    displays =display + display2 + display3

    language = "en-US"
    return_dict = {}
    # return_dict["timestamps"] = Merge(same,same2,same3)
    # return_dict["display"] = Merge(display,display2,display3)
    # return_dict["language"] = language
    return_dict["timestamps"] = sames
    return_dict["display"] = displays
    return_dict["language"] = language

    return jsonify(return_dict)

if __name__ == '__main__' :
    app.run(debug=True)
