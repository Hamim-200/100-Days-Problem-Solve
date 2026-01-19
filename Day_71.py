# Counting Vowels in a given word

vowel = ['a','e','i','o','u']
word =  "Hello World"
count = 0

for character in word:
    if character in vowel:
        count = count + 1 #count+=1

print(f"Total vowels in the word '{word}' = {count}")


# Counting Consonent in a given word

vowel = ['a','e','i','o','u']
word =  "Hello World"
consonent_count = 0

for character in word:
    if character not in vowel:
        consonent_count += 1
        
print(f"The Total Consonent in the '{word}' are = {consonent_count}")


#counting any specific word in sentence 

word =  "helloworld"
search = 'l'
specific_count = 0

for i in word:
    if i == search:
        specific_count +=1

print(f"The Total Number of the Character '{search}' in '{word}' are = {specific_count}")
