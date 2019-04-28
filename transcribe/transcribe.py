import librosa
from pydub import AudioSegment
import math
import numpy, scipy, matplotlib.pyplot as plt, IPython.display as ipd

noteStrings = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"];

def frequencyFromNoteNumber(note):
    return 440 * 2**((note-69)/12)

def centsOffFromPitch(frequency, note):
    return math.floor(1200 * math.log(frequency / frequencyFromNoteNumber(note)) / math.log(2))

def noteFromPitch(freq):
    noteNum = 12*math.log(freq/440)/math.log(2)
    return round(noteNum) + 69

def ac_clip(clip, sr):
    r = librosa.autocorrelate(clip, max_size=5000)
    midi_hi = 80.0
    midi_lo = 6.0
    f_hi = librosa.midi_to_hz(midi_hi)
    f_lo = librosa.midi_to_hz(midi_lo)
    t_lo = sr/f_hi
    t_hi = sr/f_lo
    r[:int(t_lo)] = 0
    r[int(t_hi):] = 0
    return r

def get_note(sr, t_max):
    frequency = float(sr)/t_max
    note_index = noteFromPitch(frequency)
    note = noteStrings[note_index % 12]
    octave = note_index // 12
    full_note = note + str(octave)
    return full_note, note_index

def get_expanded_note(clip, sr):
    r = ac_clip(clip, sr)
    t_max = r.argmax()
    if (t_max == 0):
        full_note = "no_note"
        note_index = -1
    else:
        full_note, note_index = get_note(sr, t_max)
    return full_note, note_index

def transcribe(path, num):
    x, sr = librosa.load(path)
    span = int(sr/num)
    audio = [x[n:(n+span)] for n in range(0, len(x), span)]
    notes_dict = {}
    count = 0

    for clip in audio:
        full_note, note_index = get_expanded_note(clip, sr)
        # r = ac_clip(clip, sr)
        # t_max = r.argmax()
        # if (t_max == 0):
        #     full_note = "no_note"
        #     freq = -1
        # else:
        #     full_note, freq = get_note(sr, t_max)
        notes_dict[round(0.2*count)] = (full_note,note_index)
        count += 1
    return notes_dict
