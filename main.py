def main():
  book_text = get_book_text("./books/frankenstein.txt")
  book_word_count = get_book_word_count(book_text)
  book_character_counts = get_book_character_counts(book_text)
  print(book_character_counts)

def get_book_text(file_path):
  with open(file_path) as file:
    return file.read()

def get_book_word_count(book_text):
  return len(book_text.split())

def get_book_character_counts(book_text):
  book_word_list = book_text.split()
  book_character_dict = {}
  for word in book_word_list:
    lower_case_word = word.lower()
    for character in lower_case_word:
      if (character not in book_character_dict):
        book_character_dict[character] = 1
      else:
        book_character_dict[character] += 1
  return book_character_dict

if (__name__ == "__main__"):
  main()