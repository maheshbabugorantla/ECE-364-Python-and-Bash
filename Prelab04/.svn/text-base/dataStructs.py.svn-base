
def uniqueletters(s):

    new_set = set(s)
    new_set = list(new_set)
    new_set.sort(reverse=True)
    new_str = ""
    for val in new_set:
        new_str += val

    return new_str

def scaleSet(aSet, num):

    a = {round(x*num, 2) for x in aSet}
    return a

def printNames(aSet):

    aSet = list(aSet)
    aSet.sort()

    for val in aSet:
        print(val)

    return

def getStateName(stateAbb):

    if(len(stateAbb) != 2):
        return None

    states = {"Indiana": "IN", "California": "CA", "Ohio": "OH", "Alabama": "AL", "New York": "NY"}
    return list(states.keys())[list(states.values()).index(stateAbb)]

def getZipCodes(stateName):

    d1 = {"Indiana": "IN", "California": "CA", "Ohio": "OH", "Alabama": "AL", "New York": "NY"}
    d2 = {47906: "IN", 47907:"IN", 10001: "NY", 10025: "NY", 90001: "CA", 90005:"CA", 90009: "CA"}

    state = d1[stateName]

    ZipCodes = set()

    for key, value in d2.items():
        if state == value:
            ZipCodes.add(key)

    return ZipCodes

def printSortedMap(s):

    l = list()

    for val in s.items():
        l.append(val)

    l = tuple(l)
    l = sorted(l, key = lambda x:x[0][1])

    for (last, first, mi), weight in l:
        o = "{1} {2} {0} has a weight of {3} lb.".format(last, first, mi, weight)
        print(o)

def switchNames(s):

    new_dict = {}

    keys = s.keys()

    for key in keys:
        lastName = key[0]
        firstName = key[1]

        name = firstName + " " + lastName
        new_dict[name] = s[key]

    return new_dict

def getPossibleMatches(record, n):

    Possible_Matches = set()

    for key in record.keys():

        if((n == record[key][0]) or (n == record[key][1]) or (n == record[key][2])):
            Possible_Matches.add(key)

    return Possible_Matches

def getPurchaseReport():

    item_costs = {}

    fp = open('purchases/Item List.txt' , 'r')

    all_lines = fp.readlines()

    for val in range(2,len(all_lines)):
        split_vals = all_lines[val].split()
        item_costs[split_vals[0]] = float(split_vals[1][1:])

    fp.close()

    return_dict = {}

    for val in range(0,10):
        filename = "purchase_00" + str(val) + ".txt"

        fp = open('purchases/'+filename, "r")
        all_lines = fp.readlines()

        total_cost = 0
        for line in all_lines[2:]:
            split_vals = line.split()
            total_cost += (int(split_vals[1]) * item_costs[split_vals[0]])

        return_dict[val] = total_cost

        fp.close()

    return return_dict

def getTotalSold():

    items_count = {}

    fp = open('purchases/Item List.txt' , 'r')

    all_lines = fp.readlines()

    for val in range(2,len(all_lines)):
        split_vals = all_lines[val].split()
        items_count[split_vals[0]] = 0

    fp.close()

    for val in range(0,10):
        filename = "purchase_00" + str(val) + ".txt"

        fp = open('purchases/'+filename, "r")
        all_lines = fp.readlines()

        for line in all_lines[2:]:
            split_vals = line.split()
            items_count[split_vals[0]] += int(split_vals[1])

        fp.close()

    return items_count

'''
def main():

    # 1st Function
    print("Unique Letters: " + str(uniqueletters("ABDBDARWET")))

    # 2nd Function
    print("Scaled Set: " +str(scaleSet({3.12, 5.0, 7.2, 15.24}, 2.1)))

    # 4th Function
    print("State Name of CA is " + getStateName("CA"))

    # 5th Function
    print(str(getZipCodes("California")))

    s = { ("Frank", "Xavier", "L"): 209.9, ("James", "Rodney", "M"): 199.0, ("George", "Johnson", "T"): 250.9 }

    # 6th Function
    printSortedMap(s)

    dictionary = {"Mahesh": (2, 27, 95),"Ajay": (7, 8, 99), "Venkatesh": (7, 3, 93), "Asheem": (12, 22, 93), "Sampath": (3, 4, 95) }
    # 8th Function
    print(str(getPossibleMatches(dictionary,95)))

    s = { ("Frank", "Xavier", "L"): 209.9, ("James", "Rodney", "M"): 199.0, ("George", "Johnson", "T"): 250.9 }

    # 7th Function
    print(str(switchNames(s)))

    # 9th Function
    map_s = { ("Frank", "Xavier", "L"): 209.9, ("James", "Rodney", "M"): 199.0, ("George", "Johnson", "T"): 250.9 }
    printSortedMap(map_s)

    print("Purchase Report: " + str(getPurchaseReport()))

    print("getTotalSold(): " + str(getTotalSold()))

if __name__=='__main__':
    main()
'''