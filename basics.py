# My first Python file
# James Mitchell

name = "James"
age = 36
height = 6.0

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}")
is_employed = True
is_veteran = True

print(f"Employed: {is_employed}")
print(f"Veteran: {is_veteran}")
if is_veteran == True and is_employed == True:
    print("Veteran and currently employed")
elif is_veteran == True and is_employed == False:
    print("Veteran seeking employment.")
else:
    print("Welcome.")
