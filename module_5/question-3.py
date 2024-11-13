def countVocals(sentence):
  editedSentence = sentence.replace(" ", "").lower()
  vocals = "aiueo"
  onlyVocals = ""

  for letter in editedSentence:
    if vocals.find(letter) == -1:
      continue

    onlyVocals += letter

  totalVocals = len(onlyVocals)
  print(f"Jumlah vokal dalam '{sentence}' adalah {totalVocals}")

sentence = input("Masukkan kalimat: ")
countVocals(sentence)