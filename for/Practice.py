#coding: UTF-8
#for
for char in "Hello":
    print(char)

for i in range(5):
    print(i)

#for-else
scores = [100,100,90,90,100]
for score in scores:
    if score <= 70:
        break
else:
    print("Pass")
