def number_penagram(s):
    dictionary_number = {}
    for number in "0123456789":
        dictionary_number[number] = 0 
    for number in s:
        if number in dictionary_number:
            dictionary_number[number] += 1 
    for number in dictionary_number:
        if dictionary_number[number] == 0 :
            return False

        return True
numbers = input("Enter a number from 0-9" )
if number_penagram(numbers):
    print("number_penagram")

else :
    print("not an penagram") 



