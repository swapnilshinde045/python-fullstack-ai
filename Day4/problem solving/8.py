#read a text file and print the number of  lines, words.

with open("notes.txt","r") as f:
    lines = f.readlines()
    words = []
    for line in lines:
        words.extend(line.split())

print("Lines:", len(lines))
print("Words:", len(words))
