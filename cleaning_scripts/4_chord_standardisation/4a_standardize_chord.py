# this file contains a funciton that, given a chord, will standardize it by
#removing brackets
# replacing + with aug
# replacing - with min
# replacing o with m7b5
# in cases where the last letter is m, lowercase the m
# in cases where the last letter is -, change to m
# change M to maj
# change maj to Maj
import re

horrible_chords = ["D(sus4)", "C+", "CM7", "E#(b5)/B", "Dm(maj7)", "Db7-9", "Bm7-5", "B+", "Am(7)", "Do", "C+9", "C-", "G7+5", "Baug", "Gsus", "Gsus2", "Gsusadd9"]

def standardize_chord(chord):
    # remove brackets
    chord = chord.replace("(", "")
    chord = chord.replace(")", "")
    #if + is the final character, replace with aug
    if chord[-1] == "+":
        chord = chord.replace("+", "#5")

    # replace aug with #5
    chord = chord.replace("aug", "#5")
    
    # if - is the final character, replace with m
    if chord[-1] == "-":
        chord = chord.replace("-", "m")
    
    # if o is the final character, replace with m7b5
    if chord[-1] == "o":
        chord = chord.replace("o", "m7b5")

    # replace M7 with Maj7
    chord = chord.replace("M7", "Maj7")

    # replace M9 with Maj9
    chord = chord.replace("M9", "Maj9")
    
    #replace-5 with b5
    chord = chord.replace("-5", "b5")

    # replace -9 with b9
    chord = chord.replace("-9", "b9")

    #replace +5 with #5
    chord = chord.replace("+5", "#5")

    #replace +9 with #9
    chord = chord.replace("+9", "#9")

    #capitalize instances of maj
    chord = chord.replace("maj", "Maj")

    #if the characters sus are followed by anything but a 2, replace sus with sus4
    # without overwriting the character following sus
    chord = re.sub(r'sus[^2]', "sus4", chord)

    return chord


# call standardize_chord on each chord in horrible_chords
standardized_chords = [standardize_chord(chord) for chord in horrible_chords]
print(horrible_chords)
print(standardized_chords)


