import sys
import math

# The following variable(s) are the only lines of code that should be outside of a function.

accounts = [
    'Mark Thomas:    $11.99   $52.08   $81.15   $79.16   $16.23   $88.11   $21.20   $0.02   ',
    'Gregory Powell:      $97.42     $96.05     $71.82     $24.79     $14.42     $60.84     $35.46     ',
    'Kevin Wood:     $93.37    $16.73    $97.05    $14.57    $53.29    ',
    'Martin Watson:     $20.53    $90.58    $22.07    $1.28    $75.40    $48.98    $36.46    $42.65    $5.01  $52.62  ',
    'Frank Young:     $32.02    $51.20    $0.99    $51.85    $88.38    $67.26    $62.72    $47.36    $38.89    ',
    'Michelle Thompson:     $2.44    $100.72    $81.44    $48.07    $68.71    $23.11    $79.23    $71.02    ',
    'Anne Harris:     $30.10    $58.32    $6.22    $3.67    $30.02    $37.65    $6.17    $41.30    $51.15    ',
    'Kelly Cooper:      $73.74     $57.63     $91.94     $42.94     $59.26     $64.30     $13.59     $19.69     $4.11 ',
    'Benjamin Foster:      $4.22     $63.02     $73.07     $99.73     $24.00     $77.79     $20.30     ',
    'Marie Perry:    $32.90   $80.27   $70.18   $68.74   $14.11   $7.38   ',
    'Cynthia Simmons:      $91.64     $56.95     $40.73     $61.28     $53.88     $77.05     $6.88     $23.37     ']

def getRowSum(accList):


    sum_amounts = 0
    amount_list = []

    for val in accList:
        amounts = val.split(":")[1].strip().split(" ")
        for val_1 in amounts:
            if(val_1 != ''):
                sum_amounts += float(val_1.split('$')[1])

        amount_list.append(round(sum_amounts,2))
        sum_amounts = 0

    return amount_list


def getDoublePalindromes():

    integers_val = []

    for val in range(10, 1000001):
        val_str = str(val)
        val_bin = str(bin(val)).split('b')[1]

        stat_int = False
        stat_bin = False

        for val_1 in range(0,int(len(val_str)/2)):

            if(val_str[val_1] != val_str[len(val_str) - val_1 - 1]):
                stat_int = False
                break

            stat_int = True

        for val_2 in range(0, int(len(val_bin)/2)):

            if(val_bin[val_2] != val_bin[len(val_bin) - val_2 - 1]):
                stat_bin = False
                break

            stat_bin = True

        if(stat_bin and stat_int):
            integers_val.append(val)

    return integers_val

def scaleVector(s, vList):

    if(type(s) != int):
        if(type(s) != float):
            return None

    if(type(vList) != list or len(vList) == 0):
        return None

    for val in range(0, len(vList)):
        vList[val] = vList[val] * s

    return vList

def convertToBoolean(num):

    if(num < 0 or num > 255):
        return None

    val_bin = str(bin(num))
    val_bin = val_bin.split('b')[1]
    val_bin_str = "0"*(8-len(val_bin))
    val_bin_str += val_bin

    boolean_list = []

    for val in range(0, (8-len(val_bin))):
        boolean_list.append(False)

    for val in range(0, len(val_bin)):

        if(val_bin[val] == '1'):
            boolean_list.append(True)
        else:
            boolean_list.append(False)

    return boolean_list

def convertToInteger(boolList):

    if (type(boolList) != list or (len(boolList) == 0)):
        return None

    for val in boolList:
        if(type(val) != bool):
            return None

    str_bin = '0b'
    for val in boolList:
        if val == True:
            str_bin += '1'

        else:
            str_bin += '0'

    return int(str_bin,2)



def getWords(sentence, n):

    vals_set = set()
    vals_str = sentence.split(' ')

    for val in vals_str:
        if(len(val) == n):
            vals_set.add(val)

    return list(vals_set)

def isSubListOf(superList, subList):

    if(type(superList) != list or type(subList) != list):
        return None

    if(len(superList) < len(subList)):
        return None

    sub_bool = False

    for val in range(0,len(superList)):
        if(superList[val] == subList[0]):
            temp_val = val
            for val_2 in range(0, len(subList)):
                if subList[val_2] != superList[temp_val]:
                    sub_bool = False
                    break
                sub_bool = True
                temp_val += 1
            if(sub_bool == True):
                return True

    return sub_bool


def getElementsAt(l, i):

    return_list = []

    for list_val in l:
        try:
            return_list.append(list_val[i])

        except IndexError:
            return_list.append(0)

    return return_list

''' def main():

    print(getRowSum(accounts))
    print(getDoublePalindromes())
    print(scaleVector(3.14, []))
    print(scaleVector(3.14, [0,1,2,3]))
    print(convertToBoolean(135))
    print(convertToBoolean(9))
    print(convertToInteger([True, False, False, False, False, True, True, True]))

    print(getWords("the power of this engine matches that of the one we use last year", 4))
    print(getWords("the power of this engine matches that of the one we use last year", 2))
    print(getWords("the power of this engine matches that of the one we use last year", 1))
    print(getWords("", 1))

    print(isSubListOf([0,-3,2,2,8,1,4], [-3,2,2,8]))
    print(isSubListOf([0,-3,2,2,8,1,4], [8,2]))
    print(isSubListOf([0,-3,2,2,8,1,4], [0,-3,8]))
    print(isSubListOf([0,-3,8],[0,-3,2,2,8,1,4]))
    print(isSubListOf([0,-3,8],[-3,2,2,8,1,4]))

    list_vals = [[9, 1, 0, 3],[1, 3, 7],[11, 35, 96, -1, 85],[43, 17]]
    print(getElementsAt(list_vals, 4))

if __name__ == "__main__":
    # TODO: Remove the "pass" before you add any code to this block.
    main()
'''