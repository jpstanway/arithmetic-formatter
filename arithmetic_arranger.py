def gap(size):
    gap = " "
    if (size == "md"):
        return gap * 2
    elif (size == "lg"):
        return gap * 4
    else:
        return gap


def arithmetic_arranger(problems, showAnswer=False):
    global spacing
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
            line1 += gap("md") + numA + gap("lg")
            line2 += op + gap("sm") + (spacing *
                                       gap("sm")) + numB + gap("lg")
            line3 += "-" * (lenA + 2) + gap("lg")
        else:
            spacing = lenB - lenA
            line1 += gap("md") + spacing * gap("sm") + numA + gap("lg")
            line2 += op + gap("sm") + numB + gap("lg")
            line3 += "-" * (lenB + 2) + gap("lg")

        if (op == "+"):
            ans = int(numA) + int(numB)
        else:
            ans = int(numA) - int(numB)

        line4 += gap("md") + str(ans) + gap("lg")

    line1 += "\n"
    line2 += "\n"
    line3 += "\n"
    line4 += "\n"

    arranged_problems += line1 + line2 + line3

    if (showAnswer):
        arranged_problems += line4

    return arranged_problems
