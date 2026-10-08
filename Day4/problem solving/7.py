#write 5 names to a file, then read and print them with line numbers

with open("names.txt", "w") as f:
    f.write("swapnil\n")
    f.write("riya\n")
    f.write("raj\n")
    f.write("smita\n")
    f.write("swapnali\n")

with open("names.txt", "r") as f:
    for i, line in enumerate(f, 1):
        print(i, line.strip())
