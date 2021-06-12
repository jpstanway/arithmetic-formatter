def arithmetic_arranger(problems):
    global spacing
    smGap = " " * 2
    lgGap = " " * 4
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
            line1 += smGap + item[0] + lgGap
            line2 += item[1] + " " + (spacing * " ") + item[2] + lgGap
            line3 += "-" * (len(item[0]) + 2) + lgGap
        else:
            spacing = len(item[2]) - len(item[0])
            line1 += smGap + spacing * " " + item[0] + lgGap
            line2 += item[1] + " " + item[2] + lgGap
            line3 += "-" * (len(item[2]) + 2) + lgGap

        line4 += smGap + str(ans) + lgGap

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
