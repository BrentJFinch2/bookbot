def get_book_text(path_to_file):
        with open(path_to_file) as f:
                file_contents = f.read()
                return(file_contents)

def word_count(path):
        text_of_book = get_book_text(path)
        num_words = len(text_of_book.split())
        print(f"Found {num_words} total words")

def character_count(path):
	text_of_book = get_book_text(path)
	text_of_book = text_of_book.lower()
	characters_dict = {}
	for character in text_of_book:
		if character in characters_dict:
			characters_dict[character] += 1
		else:
			characters_dict[character] = 1
	return characters_dict

def sort_on(items):
	return items["num"]

def sorted_character_count(path):
	counts = character_count(path)
	sorted_count = []
	for ch, n in counts.items():
		if ch.isalpha():
			sorted_count.append({"char": ch, "num": n})
	sorted_count.sort(reverse=True, key=sort_on)
	return sorted_count
