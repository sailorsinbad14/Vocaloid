import transcribe

import librosa
import numpy as np
import sys

def get_default(path, offset=0):
    default_note, sr = librosa.load(path)
    default_note = default_note[offset*sr:int((offset+0.5)*sr)]
    _, root_index = transcribe.get_expanded_note(default_note, sr)
    return default_note, root_index, sr

def transpose(path, notes_dict, default_note, root_index, sr):
    transposed_notes = []
    scale_notes = transcribe.noteStrings
    num = 7
    count = 0
    last_note = 48

    for k,v in notes_dict.items():
        current_note = default_note
        if (v[0] == "no_note"):
            transposed_notes.append(np.zeros(current_note.shape))
            continue

        note = v[1]
        steps = note - root_index

        new_note = librosa.effects.pitch_shift(current_note, sr, steps)
        transposed_notes.append(new_note)
        count += 1
        last_note = note

    same = np.asarray(transposed_notes).reshape(-1, )
    librosa.output.write_wav(path, same, sr)

def full_transcribe(input, output, default_sound='c4.wav', notes_per_second=10):
    notes_dict = transcribe.transcribe('audio/cscale.wav', notes_per_second)
    default_note, root_index, sr = get_default('c4.wav')
    transpose('asdf.wav', notes_dict, default_note, root_index, sr)

full_transcribe('audio/cscale.wav', 'asdf.wav', 'c4.wav')
