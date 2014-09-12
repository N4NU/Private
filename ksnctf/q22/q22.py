cipher = ""
big = " "
small = ""
for row in open("square.txt", "r"):
    cipher += row[:-1]
for cha in cipher:
    if ord(cha) <= 90:
        big += cha
    else:
        small += cha
    if big[-1] != " " and ord(cha) > 90:
        big += " "
    if small[-1] != " " and ord(cha) < 90:
        small += " "
print big
print small
