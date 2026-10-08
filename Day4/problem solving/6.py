#create a directory of 3 student name and id. then write this in a file

students = {
    "swapnil": 123,
    "riya": 456,
    "raj": 789
}

with open("students.txt", "w") as f:
    for name, id in students.items():
        f.write(f"{name}: {id}\n")

print("Done...")