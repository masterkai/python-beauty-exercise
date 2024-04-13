result_str = ""

for row in range(1, 6):
    for column in range(1, 5):
        if (row == 1 or row == 3 or row == 5):
            result_str = result_str + "*"
        elif column == 1:
            result_str = result_str + "*"
    result_str = result_str + "\n"

print(result_str)
