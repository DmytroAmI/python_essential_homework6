string = "abcdef"

for char in string:
    print(char)

print()

my_iter = iter(string)
while True:
    try:
        print(next(my_iter))
    except StopIteration:
        break
