def isPalindrome(word):
  word = word.lower()
  result = False

  if word == word[::-1]:
    result = True

  print(f"Hasil palindrome dari '{word}' adalah {result}")

word = input("Masukkan kata: ")
isPalindrome(word)