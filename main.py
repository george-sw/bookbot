def main():
  book_text = get_book_text("./books/frankenstein.txt")
  book_word_count = get_book_word_count(book_text)
  book_character_counts = get_book_character_counts(book_text)
  book_character_list = get_book_character_list(book_character_counts)

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

def get_book_character_list(character_dict):
  book_character_list = []
  for character in character_dict:
    if (character.isalpha()):
      book_character_list.append({"character": character, "count": character_dict[character]})
  return book_character_list

def get_count(character_dict):
  return character_dict["count"]

if (__name__ == "__main__"):
  main()