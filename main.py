def sort_on(dict):
    return dict["value"]
book_path = "books/frankenstein.txt"
with open(file=f"./{book_path}") as file:
    file_contents = file.read()
    
wordcount = len(file_contents.split())

letter_count = {}

for line in file_contents:
    if line.lower() in letter_count.keys():
        letter_count[line.lower()] += 1
    else:
        letter_count[line.lower()] = 1
file.close()

letter_count = [{"name":key, "value": value} for _, (key, value) in enumerate(letter_count.items()) if key.isalpha()]


letter_count.sort(key=sort_on, reverse=True)

print(f"--- Begin report of {book_path} ---")
print(f"{wordcount} words found in the document")
print("\n")
for index, val in enumerate(letter_count):
    print(f"The '{val["name"]}' character was found {val["value"]} times")

print("--- End report ---")
