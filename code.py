import random

def display(room):
    print(room)

room = []
print("enter entries")

#print("All the rooom are dirty")
R=3
C=3
for i in range(R):          # A for loop for row entries
    a =[]
    for j in range(C):      # A for loop for column entries
         a.append(int(input()))
    room.append(a)
display(room)

x =0
y= 0



print("Before cleaning the room I detect all of these random dirts")
display(room)
x =0
y= 0
z=0
while x < 3:
    while y < 3:
        if room[x][y] == 1:
            print("Vaccum in this location now,",x, y)
            room[x][y] = 0
            print("cleaned", x, y)
            z+=1
        y+=1
    x+=1
    y=0
print("cost = ",z)
display(room)
