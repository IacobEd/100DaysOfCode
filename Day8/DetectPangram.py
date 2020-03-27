#A pangram is a sentence that contains every single letter of the alphabet at least once. 
#For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant). 
#Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
def count(string):
  string = string.lower()
  for char in "abcdefghijklmnopqrstuvwxyz":
    if char not in string:
      return False
  return True
print(count("The quick brown fox jumps over the lazy dog"))
#Result : True
print(count("The quick brown fox jumps over the lazy cat"))
#Result : False
