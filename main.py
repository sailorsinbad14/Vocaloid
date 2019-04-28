from useSpeechToText import useSpeechToText

ffmpegAddress = r"C:\Program Files\ffmpeg\bin\ffmpeg.exe"
# path = r'C:\Users\lbm4\PycharmProjects\Vocaloid\resources\japan.mp3'
path = "transcribe/audio/numb_.flac"
path2 = "transcribe/audio/numb__.flac"
path3 = "transcribe/audio/numb___.flac"
same, display, language =useSpeechToText( path)
same2, display2, language2 =useSpeechToText( path2)
same3, display3, language3 =useSpeechToText(path3)
print(same, display, language)
print(same2, display2, language2)
print(same3, display3, language3)

def duration ():
    from mutagen.flac import FLAC
    audio = FLAC (path)
    audio2 = FLAC (path2)
    audio3 = FLAC (path3)

    return audio.info.length + audio2.info.length + audio3.info.length

print(duration())