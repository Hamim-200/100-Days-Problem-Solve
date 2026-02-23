# Python Decoder

"""
A Python decoder usually means a program or process that converts encoded data back into its original (human-readable or usable) form using Python.
“Decoding” can apply to text, files, images, audio, Base64, JSON, URL data, etc.

Why Decoding is Needed ??
We decode data in Python when:
✔ Reading files
✔ Getting API responses
✔ Converting Base64 data
✔ Working with JSON
✔ Handling URL data
✔ Processing encrypted/encoded messages

"""

# Decoding = transforming encoded/converted data ➜ original format.

# Step 1: encoded byte data
byte_data = b'Hello' # → stored as bytes

# Step 2: decode using UTF-8
text = byte_data.decode('utf-8') # → converts bytes → string

# Step 3: print result
print(text) # → readable text


# JSON Decoder in Python
import json

# Step 1: JSON encoded string
data = '{"name": "Hamim", "age": 22}'

# Step 2: decode JSON → Python dictionary
obj = json.loads(data)

# Step 3: use the data
print(obj["name"])