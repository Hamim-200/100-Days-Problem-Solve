# count special characters in a string (! , . @ # $ etc)

text = "Hi! I am Hamim, 25 years old.@#"

special_count = 0

for ch in text:
    if not ch.isalnum() and not ch.isspace():
        special_count += 1

print(special_count)