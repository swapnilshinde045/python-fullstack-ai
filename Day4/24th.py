names = input("Enter names separated by space: ").split()

with open("names.txt","a") as f:
    for n in names:
        f.write(n + "\n")

print("Data written")

        