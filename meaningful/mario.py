height = int(input("Height: "))

for i in range(1, height + 1):
    spaces = " " * (height - i)     
    tags = "#" * i
    gap = "  "                    

    print(spaces + tags + gap + tags)