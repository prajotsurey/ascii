chars = []
for i in range(32,127):
    chars.append(chr(i))

print(" ".join(chars))
file = open("chars.txt", "w")
file.write(str(chars))
file.close