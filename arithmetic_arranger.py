def arithmetic_arranger(problems, answers=False):
    if len(problems) > 5: return 'Error: Too many problems.'

    line_1 = ''
    line_2 = ''
    line_3 = ''
    line_4 = ''
    for problem in problems:
        # retrieving the values
        num_1 = (problem.split()[0])
        num_2 = (problem.split()[2])
        op = (problem.split()[1])
        display_length = (max(len(problem.split()[0]), len(problem.split()[2])) + 2)

        # test that operands can convert to integers
        try:
            int(num_1) + int(num_2)
        except:
            return 'Error: Numbers must only contain digits.'

        # test operands not too long
        if len(num_1) > 4 or len(num_2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        # calulate answers and test operator
        if op == '+':
            answer = int(num_1) + int(num_2)
        elif op == '-':
            answer = int(num_1) - int(num_2)
        else:
            return "Error: Operator must be '+' or '-'."

        # append to the relevant lines
        line_1 += ' ' * (display_length - len(num_1)) + num_1 + ' ' * 4
        line_2 += op + ' ' * (display_length - len(num_2) - 1) + num_2 + ' ' * 4
        line_3 += '-' * display_length + ' ' * 4
        if answers == True:
            line_4 += ' ' * (display_length - len(str(answer))) + str(answer) + ' ' * 4

    arranged_problems = line_1.rstrip() + '\n' + line_2.rstrip() + '\n' + line_3.rstrip()
    if answers == True:
        arranged_problems += '\n' + line_4.rstrip()
    return arranged_problems