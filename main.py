import sys
from stats import word_count, sorted_character_count
if len(sys.argv) <2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

path = sys.argv[1]
print("============ BOOKBOT ============")
print(f"Analyzing book found at {path}...")
print("----------- Word Count ----------")
word_count(path)
print("--------- Character Count -------")
characters = sorted_character_count(path)
for item in characters:
		print(f"{item['char']}: {item['num']}")
print("============= END ===============")
