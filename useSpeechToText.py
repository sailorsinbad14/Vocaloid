import io
import os


# Imports the Google Cloud client library
from google.cloud import speech_v1p1beta1 as speech
# from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types


# print('Credendtials from environ: {}'.format(
#     os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')))
# Instantiates a client
client = speech.SpeechClient()
#conver to wav
from pydub import AudioSegment
AudioSegment.converter = r"C:\Program Files\ffmpeg\bin\ffmpeg.exe"
# AudioSegment.converter = r"C:\Program Files (x86)\avconv\usr\bin\avconv.exe"
# sound = AudioSegment.from_wav(r"C:\Users\lbm4\PycharmProjects\Vocaloid\resources\commercial_mono.wav")

# sound2 = AudioSegment.from_mp3(r"C:\Users\lbm4\PycharmProjects\Vocaloid\resources\twinkles.mp3")

sound3 = AudioSegment.from_mp3(r"C:\Users\lbm4\PycharmProjects\Vocaloid\resources\japan.mp3")
# print (sound3.frame_rate)
# print(sound3.channels)
sound3.export(r"C:\Users\lbm4\PycharmProjects\Vocaloid\resources\japan.flac", format="flac")
# from  scipy.io import wavfile
# rate, data = wavfile.read(r"C:\Users\lbm4\PycharmProjects\Vocaloid\resources\feifan.wav")
# data0 = data [: , 0].tobytes()
# The name of the audio file to transcribe
file_name = os.path.join(
    os.path.dirname(__file__),
    'resources',
    'japan.flac')
first_lang = 'en-US'
second_lang = 'ja-JP'
third_lang = 'zh'
# Loads the audio into memory
with io.open(file_name, 'rb') as audio_file:
    content = audio_file.read()
    audio = speech.types.RecognitionAudio(content=content)

config = speech.types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
    sample_rate_hertz=sound3.frame_rate,
    audio_channel_count=sound3.channels,
    language_code=first_lang,
    alternative_language_codes=[second_lang, third_lang],
    enable_word_time_offsets=True

)


operation = client.long_running_recognize(config, audio)


# Detects speech in the audio file;
print (file_name,)
response = client.recognize(config, audio)
#print(response)

for result in response.results:
    alternative = result.alternatives[0]

    print('Transcript: {}'.format(result.alternatives [0].transcript))

    for word_info in alternative.words:
        word = word_info.word
        start_time = word_info.start_time
        end_time = word_info.end_time
        print('Word: {}, start_time: {}, end_time: {}'.format(
            word,
            start_time.seconds + start_time.nanos * 1e-9,
                end_time.seconds + end_time.nanos * 1e-9))

from langdetect import detect
lang = detect(result.alternatives [0].transcript)
if(lang == 'ja'):
    print("This is Japanese!")
elif(lang =='zh'):
    print("This is Simplified Chinese!")
elif(lang == 'en-US'):
    print("This is English!")
else:
    print("Cannot recognize this language...")


