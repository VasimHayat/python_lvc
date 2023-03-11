# loop item in range 
for i in range(10):
    print(i)
    if( i%2 == 0):
        print("Even")
    elif( i%2!= 0 ):
        print("Odd")

print("While Loop...")
# While Loop
index:int = 10;
while( index >= 1):
    print(index)
    index-=1

def subtract(a, b):
    if a is None or b is None:
        return None
    return a - b

print(subtract(10,None))
print(subtract(10,3))
