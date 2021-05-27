def arithmetic_arranger(problems):
    global width
    global diff
    global a
    global b
    arranged_problems = []

    for x in problems:
        items = x.split(" ")
        op = items[1] + " "

        if len(items[0]) > len(items[2]):
            a = "  " + items[0]
            width = len(a)
            diff = " " * (width - len(items[2]))
            b = op + diff + items[2]
        else:
            b = op + "  " + items[2]
            width = len(b)
            diff = " " * (width - len(items[0]))
            a = "  " + diff + items[0]

        arranged_problems.append([a, b, "-" * (width + 2)])
    print(arranged_problems)
    return arranged_problems
