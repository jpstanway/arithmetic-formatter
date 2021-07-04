
def getError(type):
    errors = {
        "problems": "Error: Too many problems.",
        "numbers": "Error: Numbers cannot be more than four digits.",
        "operators": "Error: Operator must be '+' or '-'.",
    }
    return errors[type]


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

    if (len(problems) > 5):
        return getError("problems")

    for problem in problems:
        item = problem.split(" ")
        op = item[1]
        numA = item[0]
        numB = item[2]
        lenA = len(numA)
        lenB = len(numB)

        if (lenA > 4 or lenB > 4):
            return getError("numbers")
        elif (op != "+" and op != "-"):
            return getError("operators")

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

    line1 = line1.rstrip() + "\n"
    line2 = line2.rstrip() + "\n"
    line3 = line3.rstrip() + "\n"
    line4 = line4.rstrip()

    arranged_problems += line1 + line2 + line3

    if (showAnswer):
        arranged_problems += line4

    return arranged_problems
