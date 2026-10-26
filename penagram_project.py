#Penagram

def penagram(s):
    dictionary_letter= {}
    for charecter in "abcdefghijklmnopqrstuvwxyz":
        dictionary_letter[charecter]=0
    for charecter in s.lower():
        if charecter in dictionary_letter:
            dictionary_letter[charecter]+=1 
    for charecter in dictionary_letter:
        if dictionary_letter[charecter]==0:
            return False
    return True
letters = input("Enter a string")
if penagram(letters):
    print("penagram")

        

