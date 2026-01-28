# Comparing Two string for ANAGRAMS
# An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once

str1 ="Listen"
str2="Silent"

str1 = str1.replace(" ","").upper()
str2 = str2.replace(" ","").upper()

if sorted(str1) == sorted(str2):
    print("True")
else:
    print("False")
    
    
# Checking for PALINDROME Using Extended Slicing Technique
# A palindrome is a word, phrase, number, or sequence that reads the same backward as forward

str3 = "Madam".lower()
if str3 == str3[::-1]:
    print("true")
else:
    print("False")
    
    
