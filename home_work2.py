# Home work 2 
def char_frequency(s):
    frequencies = {}
    for character in s:
        frequencies[character] = frequencies.get(character, 0) + 1

    print(frequencies)
char_frequency("string")   
