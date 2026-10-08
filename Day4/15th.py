word_list=["ai","flutter","ml","react"]

count={}

for w in word_list:
    count[w]=count.get(w,0)+1

print(count)