string = "Hello World"
reversed_string = ""
i = len(string) - 1
while i >= 0:
  reversed_string += string[i]
  i -= 1
print(reversed_string)