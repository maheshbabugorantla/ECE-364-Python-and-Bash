def isValidOutput(fileName):

    # TODO: Remove the "pass" before you add any code to this block.

    fp = open(fileName,"r")

    row_column = []

    for val in fp:
        row_column.append(list(val.rstrip('\n')))

    fp.close()

    index = 0

    for row in row_column:
        row = list(map(int,row))
        row_column[index] = row
        index += 1

    rows = len(row_column)

    temp_rows = rows

    sum_val_1 = 0
    sum_val = sum(range(1,10))


    row_1 = 0
    row_3 = 0

    while row_1 < rows:
        for row_2 in range(row_1,row_1 + 3):
            for column_1 in range(row_3, row_3 + 3):
                print(row_2,column_1)
            row_3 += 3
        row_3 = 0
        row_1 += 3

    return True

def isColumnPuzzle(fileName):

    # TODO: Remove the "pass" before you add any code to this block.
    pass

def solvePuzzle(sourceFileName, targetFileName):

    # TODO: Remove the "pass" before you add any code to this block.
    pass

def getCallersOf(phoneNumber):

    # TODO: Remove the "pass" before you add any code to this block.
    fp = open("ActivityList.txt")

    lines = fp.readlines()

    dict_numbers = {}

    for line in lines[2:]:
        vals = line.strip().split("        ")

        if(vals[1].strip() not in dict_numbers):
            dict_numbers[vals[1].strip()] = set(vals[0].strip())

        else:
            dict_numbers[vals[1].strip()].add(vals[0].strip())


    fp2 = open("People.txt", "r")



    fp.close()
    fp2.close()

def getCallActivity():

    # TODO: Remove the "pass" before you add any code to this block.
    pass

def main():
    #print(isValidOutput("valid.sud"))
    getCallersOf("123-456-7890")

if __name__ == "__main__":

    # TODO: Remove the "pass" before you add any code to this block.
    main()
