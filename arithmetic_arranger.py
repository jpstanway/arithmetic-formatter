def gap(size):
    gap = " "
    return gap * size


def arithmetic_arranger(problems, showAnswer=False):
    global spacing
    global underline
    global ans
    arranged_problems = ""
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""

    for x in problems:
        item = x.split(" ")
        op = item[1]
        numA = item[0]
        numB = item[2]
        lenA = len(numA)
        lenB = len(numB)

        if (lenA > lenB):
            spacing = lenA - lenB
            underline = lenA + 2
            line1 += gap(2) + numA + gap(4)
            line2 += op + gap(1) + (spacing *
                                    gap(1)) + numB + gap(4)
            line3 += "-" * underline + gap(4)
        else:
            spacing = lenB - lenA
            underline = lenB + 2
            line1 += gap(2) + spacing * gap(1) + numA + gap(4)
            line2 += op + gap(1) + numB + gap(4)
            line3 += "-" * underline + gap(4)

        if (op == "+"):
            ans = str(int(numA) + int(numB))
        else:
            ans = str(int(numA) - int(numB))

        line4 += gap(underline - len(ans)) + ans + gap(4)

    line1 += "\n"
    line2 += "\n"
    line3 += "\n"
    line4 += "\n"

    arranged_problems += line1 + line2 + line3

    if (showAnswer):
        arranged_problems += line4

    return arranged_problems
