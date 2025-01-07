file = "smiley_emoji_mod.xpm"
try:
    fh = open(file, "r")
    line2 = fh.readline().strip()
    [cols, rows, numColors] = line2.split(" ")
    num2 = int(cols)
    num3 = int(rows)
    numColors = int(numColors)
    print(num2)
    print(num3)
    print(numColors)
    symbols = {}
    for i in range(numColors):
        line = fh.readline().strip()
        [sym, c, color] = line.split(" ")
        if sym == "~":
            sym = " "
        symbols[sym] = color
    print(symbols)
    r = fh.readline().strip()
except OSError as err:
    print("Not found", err)
fh.close()
