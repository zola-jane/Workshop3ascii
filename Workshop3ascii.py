# display number and corresponding character
for i in range(10,  120,  11):
    print("{:<5d} ===== {:>5s}".format(i, chr(i)))