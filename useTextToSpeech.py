

def useTextToSpeech(output, lang, speed):

    from google.cloud import texttospeech_v1 as texttospeech
    client = texttospeech.TextToSpeechClient()
    synthesis_input = texttospeech.types.SynthesisInput(text=output)
    voice = texttospeech.types.VoiceSelectionParams(
        language_code=lang,
        ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE,
    )
    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3,
        speaking_rate=speed
    )
    response = client.synthesize_speech(synthesis_input, voice, audio_config)
    with open('output.mp3', 'wb') as out:
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')
    from playsound import playsound
    import os

    playsound(os.path.abspath('output.mp3'))
    # playsound(r'C:\Users\lbm4\PycharmProjects\Vocaloid\output.mp3')



