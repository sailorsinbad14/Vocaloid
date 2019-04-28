from getTimestamps import getTimestamps
from google.cloud import speech_v1p1beta1 as speech
from google.cloud.speech import enums
from google.cloud.speech import types
from pydub import AudioSegment
from langdetect import  detect
from useTextToSpeech import useTextToSpeech
from detectLanguage import detectLanguage
import io
import os

#numb_.flac
def useSpeechToText( path):
    client = speech.SpeechClient()

    # AudioSegment.converter = ffmpegAddress

    baseName= os.path.basename(path)
    # song = AudioSegment.from(path)
    # file_basename = baseName[0:len(baseName) - 4] + 'flac'
    file_name = os.path.join(
        os.path.dirname(__file__),
        'transcribe/audio',
        baseName)

    # song.export(file_name, format="flac")


    first_lang = 'en-US'
    Japanese = 'ja-JP'
    Chinese = 'zh'
    # Deutsch = 'de-DE'
    # Español = 'es'
    # Français = 'fr'
    # Italiano = 'it-IT'
    # Nederlands = 'nl-NL'
    # Português = 'pt'
    # Русский = 'ru-RU'
    # العربية = 'ar'
    # 한국어 = 'ko-KR'
    # Loads the audio into memory
    with io.open(file_name, 'rb') as audio_file:
        content = audio_file.read()
        audio = speech.types.RecognitionAudio(content=content)

    config = speech.types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
        # sample_rate_hertz=song.frame_rate,
        sample_rate_hertz=44100,
        audio_channel_count=2,
        language_code=first_lang,
       # alternative_language_codes=[Japanese, Chinese,Deutsch,Español,Français, Italiano, Nederlands, Português, Русский, العربية, 한국어],
        enable_word_time_offsets=True
    )

    # operation = client.long_running_recognize(config, audio)

    # Detects speech in the audio file;
    # print (audio, config)
    response = client.recognize(config, audio)

    output = 'Transcript: \n'
    for result in response.results:
        alternative = result.alternatives[0]
        output += ' {}'.format(result.alternatives[0].transcript)
    speaking = output

    same, display = getTimestamps(response)

    language = first_lang

    return same, display, language

def speak(text):
    try:
        useTextToSpeech(text, "en-US", 0.8)
        return "works"
    except:
        return "404 here but im lazy"
    # for word_info in alternative.words:
    #     word = word_info.word
    #     start_time = word_info.start_time
    #     end_time = word_info.end_time
    #     print('Word: {}, start_time: {}, end_time: {}'.format(
    #         word,
    #         start_time.seconds + start_time.nanos * 1e-9,
    #             end_time.seconds + end_time.nanos * 1e-9))

    #
    # def detectLanguage():
    #     from langdetect import detect
    #     lang = detect(result.alternatives [0].transcript)
    #     if(lang == 'ja'):
    #         print("This is Japanese!")
    #     elif(lang =='zh'):
    #         print("This is Simplified Chinese!")
    #     elif(lang == 'en-US'):
    #         print("This is English!")
    #     else:
    #         print("Cannot recognize this language...")
    #     return lang


    # from google.cloud import texttospeech_v1 as texttospeech
    #
    # # Instantiates a client
    # client = texttospeech.TextToSpeechClient()
    #
    # # Set the text input to be synthesized
    # synthesis_input = texttospeech.types.SynthesisInput(text=output)
    # # Build the voice request, select the language code ("en-US") and the ssml
    # # voice gender ("neutral")
    # voice = texttospeech.types.VoiceSelectionParams(
    #     language_code=lang,
    #     ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE,
    #     # name='ja-JP-Standard-A'
    #
    # )
    # # Select the type of audio file you want returned
    # audio_config = texttospeech.types.AudioConfig(
    #     audio_encoding=texttospeech.enums.AudioEncoding.MP3,
    #     speaking_rate=0.56
    # )
    #
    # # Perform the text-to-speech request on the text input with the selected
    # # voice parameters and audio file type
    # response = client.synthesize_speech(synthesis_input, voice, audio_config)
    #
    # # The response's audio_content is binary.
    # with open('output.mp3', 'wb') as out:
    #     # Write the response to the output file.
    #     out.write(response.audio_content)
    #     print('Audio content written to file "output.mp3"')
    #
    # from playsound import playsound
    # playsound(r'C:\Users\lbm4\PycharmProjects\Vocaloid\output.mp3')
    #
