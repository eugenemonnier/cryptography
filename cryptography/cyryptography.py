import nltk
nltk.download('words')
from nltk.corpus import words

def encrypt(string, key):
  word_list = words.words()
  char_list = [chr(x) for x in range(ord('a'), ord('z') + 1)]
  encrypt_string = str()

  def encrypt_char(num):
    char_shift = (num + key) % len(char_list)
    return char_list[char_shift] 
  
  for char in string:
    if char.lower() in char_list:
      num = char_list.index(char.lower())
      print(num)
    encrypt_string += str(encrypt_char(num))
  print()
  return encrypt_string

encrypted = encrypt('Stuff', 10)
print(encrypted)

def decrypt (string, key):
  return encrypt(string, -key)

print(decrypt(encrypted, 10))