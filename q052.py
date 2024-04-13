x = 0

while x < 4:

    if x % 4 == 0:

        print("party", x)

    elif x - 2 < 0:

        print("cake", x)

    elif x / 3 == 0:

        print("greeting", x)

    else:

        print("birthday", x)

    x = x + 1
