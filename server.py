from flask import Flask, jsonify
from useSpeechToText import useSpeechToText

app = Flask(__name__)
# ffmpegAddress = r"C:\Program Files\ffmpeg\bin\ffmpeg.exe"
path = r"transcribe/audio/numb_.flac"
path2 = r"transcribe/audio/numb__.flac"
path3 = r"transcribe/audio/numb___.flac"

# def Merge(dict1, dict2,):
#     res = {**dict1, **dict2,}
#     return res
@app.route("/")
def testing():
    same, display, language = useSpeechToText(path)
    same2, display2, language2 = useSpeechToText(path2)
    same3, display3, language3 = useSpeechToText(path3)
    sames =same3.update(same2.update(same))
    displays = display3.update(display2.update(display))
    language = "en-US"
    return_dict = {}
    # return_dict["timestamps"] = Merge(same,same2,same3)
    # return_dict["display"] = Merge(display,display2,display3)
    # return_dict["language"] = language
    return_dict["timestamps"] = sames
    return_dict["display"] = displays

    return jsonify(return_dict)

if __name__ == '__main__' :
    app.run(debug=True)
