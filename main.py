def main():
  book_text = get_book_text("./books/frankenstein.txt")
  book_word_count = get_book_word_count(book_text)

def get_book_text(file_path):
  with open(file_path) as file:
    return file.read()

def get_book_word_count(book_text):
  return len(book_text.split())

if (__name__ == "__main__"):
  main()