def arithmetic_arranger(problems):
    global spacing
    arranged_problems = ""
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""

    for x in problems:
        item = x.split(" ")
        ans = int(item[0]) + int(item[2])

        if (len(item[0]) > len(item[2])):
            spacing = len(item[0]) - len(item[2])
            line1 += "  " + item[0] + " " * 4
            line2 += item[1] + " " + (spacing * " ") + item[2] + " " * 4
            line3 += len(item[0]) + 2 * "-" + " " * 4
        else:
            spacing = len(item[2]) - len(item[0])
            line1 += (spacing * " ") + item[0] + " " * 4
            line2 += item[1] + " " + item[2] + " " * 4
            line3 += len(item[2]) + 2 * "-" + " " * 4

        line4 += "  " + str(ans) + " " * 4

    line1 += "\n"
    line2 += "\n"
    line3 += "\n"
    line4 += "\n"

    arranged_problems += line1 + line2 + line3 + line4

    # global width
    # global diff
    # global a
    # global b
    # arranged_problems = []

    # for x in problems:
    #     items = x.split(" ")
    #     op = items[1] + " "
    #     c = int(items[0]) + int(items[2])

    #     if len(items[0]) > len(items[2]):
    #         a = "  " + items[0] + "\n"
    #         width = len(a)
    #         diff = " " * (width - len(items[2]))
    #         b = op + diff + items[2] + "\n"
    #     else:
    #         b = op + "  " + items[2] + "\n"
    #         width = len(b)
    #         diff = " " * (width - len(items[0]))
    #         a = "  " + diff + items[0] + "\n"

    #     final = a + b + "-" * (width + 2) + "\n" + diff + " " + str(c)

    #     arranged_problems.append(final)

    # for y in arranged_problems:
    #     print(y)

    return arranged_problems
