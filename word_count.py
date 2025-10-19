def get_book_text(path_to_file):
        with open(path_to_file) as f:
                file_contents = f.read()
                return(file_contents)

def word_count():
	text_of_frankenstein = get_book_text("books/frankenstein.txt")
	num_words = len(text_of_frankenstein.split())
	print(f"Found {num_words} total words")

word_count()
