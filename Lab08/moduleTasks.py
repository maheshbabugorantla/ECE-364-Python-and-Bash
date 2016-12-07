import re
from string import ascii_letters
from string import digits

def isIdValid(pin):

    if(re.match("^\w+$",pin)):
        return True
    else:
        return False

def parseAssignment(assignment):

    pins = re.match("^.\w+\(\w+\)$",assignment)
    if(pins is None):
        raise ValueError(assignment)
    else:
        pinNames = re.split("\(|\)",assignment)
        return(pinNames[0].split(".")[1],pinNames[1])

def parseLine(line):

    isValid = re.match("^\w+\s+\w+\s*\((?P<assignment>.*)\)$",line.strip())


    pins_val = []
    if isValid is not None:
        pins = isValid.group("assignment").split(",")
        comp_name = line.strip().split(" ")[0]

        instance_name = line.strip().split(" ")[1]

        if(instance_name.endswith("(")):
            instance_name = instance_name.rstrip("(")

        pins_val.append(comp_name)
        pins_val.append(instance_name)

        pins_val1 = []
        for pin in pins:
            pins_val1.append(parseAssignment(pin))

        pins_val.append(tuple(pins_val1))

    else:
        raise ValueError(line)

    return tuple(pins_val)

def main():

    print(isIdValid("123a-"))
    print(isIdValid("asdf_jkl"))
    print(isIdValid("wer_1234"))
    print(isIdValid("A_sdf_ghj_QWER"))

    print(" ")

    print(parseAssignment(".PORT_NAME(asdf_jkl)"))
    print(parseAssignment(".PORT_NAME1(asdf_jkl1234)"))
    print(parseAssignment(".PORT_NAME2(asdf_jkl45qwerty)"))
    #print(parseAssignment(".PORT_NAME(asdf_jkl-123_)"))
    print(" ")

    with open("verilog_test.v","r") as fp:

        for line in fp.readlines():
            print(parseLine(line.strip()))

'''    parseAssignment(".PORT_NAME#$%(asdf_jkl!@#)")
    parseAssignment(".PORT_NAME(asdf_jkl-123_)")
    parseAssignment(".PORT_NAME((asdf_jkl()")
    parseAssignment(".PORT_NAME((asdf_jkl))")
    parseAssignment(".PORT_NAME()asdf_jkl()")
    parseAssignment(".PORT_NAME)asdf_jkl")
    parseAssignment(".PORT_NAME)asdf_jkl(")
'''
    
if __name__=='__main__':
    main()