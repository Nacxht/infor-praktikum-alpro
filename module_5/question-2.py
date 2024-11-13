def countConsonants(sentence):
  editedSentence = sentence.replace(" ", "").lower()
  vocals = "aiueo"

  for vocal in vocals:
    editedSentence = editedSentence.replace(vocal, "")

  totalConsonant = len(editedSentence)

  print(f"Jumlah huruf konsonan dalam '{sentence}' adalah {totalConsonant}.")

sentence = input("Masukkan kalimat: ")
countConsonants(sentence)