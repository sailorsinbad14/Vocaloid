def useSpeechToText(ffmpegAddress, path):
    import io
    import os

    # Imports the Google Cloud client library
    from google.cloud import speech_v1p1beta1 as speech
    # from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types
    # ffmpegAddress = r"C:\Program Files\ffmpeg\bin\ffmpeg.exe"
    # path = r'C:\Users\lbm4\PycharmProjects\Vocaloid\resources\japan.mp3'
    # print('Credendtials from environ: {}'.format(
    #     os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')))
    # Instantiates a client


    client = speech.SpeechClient()
    # conver to wav
    from pydub import AudioSegment

    # AudioSegment.converter = ffmpegAddress


    print ("hello")
    baseName= os.path.basename(path)
    print(baseName)
    song = AudioSegment.from_mp3(path)
    file_basename = baseName[0:len(baseName) - 3] + 'flac'
    print(file_basename)
    file_name = os.path.join(
        os.path.dirname(__file__),
        'resources',
        file_basename)
    print(file_name)

    song.export(file_name, format="flac")

    # print(file_name)

    first_lang = 'en-US'
    second_lang = 'ja-JP'
    third_lang = 'zh'
    # Loads the audio into memory
    with io.open(file_name, 'rb') as audio_file:
        content = audio_file.read()
        audio = speech.types.RecognitionAudio(content=content)

    config = speech.types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=song.frame_rate,
        audio_channel_count=song.channels,
        language_code=first_lang,
        alternative_language_codes=[second_lang, third_lang],
        enable_word_time_offsets=True
    )

    # operation = client.long_running_recognize(config, audio)

    # Detects speech in the audio file;
    # print (audio, config)
    response = client.recognize(config, audio)
    print(response)
    output = 'Transcript: \n'
    for result in response.results:
        alternative = result.alternatives[0]
        output += ' {}'.format(result.alternatives[0].transcript)

        # print('Transcript: {}'.format(result.alternatives[0].transcript))
    speaking = output
    from getTimestamps import getTimestamps

    # print(getTimestamps(response))

    output +=  '<br>' + getTimestamps(response)+'<br>'
    # print(output)
    from langdetect import  detect

    lang = detect(result.alternatives[0].transcript)

    from detectLanguage import detectLanguage

    output += detectLanguage(lang)+'<br>'

    return output

def speak(speaking):
    from useTextToSpeech import useTextToSpeech
    # lang = detect(result.alternatives[0].transcript)

    useTextToSpeech(speaking, "en-US-Standard-B", 0.8)
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
