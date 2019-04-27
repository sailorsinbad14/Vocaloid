import io
import os


# Imports the Google Cloud client library
from google.cloud import speech
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
sound = AudioSegment.from_wav(r"C:\Users\lbm4\PycharmProjects\Vocaloid\resources\commercial_mono.wav")

sound2 = AudioSegment.from_mp3(r"C:\Users\lbm4\PycharmProjects\Vocaloid\resources\hibiki.mp3")
print (sound.frame_rate)
print(sound.channels)
sound.export(r"C:\Users\lbm4\PycharmProjects\Vocaloid\resources\commercial_mono.flac", format="flac")
# from  scipy.io import wavfile
# rate, data = wavfile.read(r"C:\Users\lbm4\PycharmProjects\Vocaloid\resources\feifan.wav")
# data0 = data [: , 0].tobytes()
# The name of the audio file to transcribe
file_name = os.path.join(
    os.path.dirname(__file__),
    'resources',
    'commercial_mono.flac')

# Loads the audio into memory
with io.open(file_name, 'rb') as audio_file:
    content = audio_file.read()
    audio = types.RecognitionAudio(content=content)

config = types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
    sample_rate_hertz=8000,
    audio_channel_count=1,
    language_code='en-US',
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