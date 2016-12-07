class Entry:

    key = tuple()
    value = "" # String Value

    def __init__(self, k1, k2, v):

        if not isinstance(k1,int):
            raise TypeError("Make sure that k1 is of type 'int'")

        if not isinstance(k2,int):
            raise TypeError("Make sure that k2 is of type 'int'")

        if not isinstance(v,str):
            raise TypeError("Make sure that v is of type 'str' ")

        self.key = (k1,k2)
        self.value = v


    def __str__(self):
        return ("(" + str(self.key[0]) + ", " + str(self.key[1]) + "): " + "\"" + self.value + "\"")

    def __hash__(self):
        return hash(self.key)

    def __eq__(self, other):
        return (self.key == other.key)

class Lookup:

    _container = set()
    _name = ""

    def __init__(self, name):

        if(len(name) == 0):
            raise ValueError("Make sure that 'name' cannot be an empty string")

        self._name = name
        self._container = set()

    def __str__(self):

        entries = str(len(self._container))

        if(len(entries) == 1):
            entries = '0' + str(entries)

        return("[\"" + self._name + "\": " + entries + " Entries")


    def add(self, entry):

        # Checking if it is present
        for val in self._container:
            if(hash(val) == hash(entry)):
                raise KeyError("Cannot add Entry with the same key")

        self._container.add(entry)

    def update(self, entry):

        flag = 1
        for item in self._container:
            if(hash(entry) == hash(item)):
                item.value = entry.value
                flag = 0
                break

        if(flag):
            raise KeyError(str(entry.key) + " not present in the dictionary")

    def addOrUpdate(self, entry):

        try:
            self.update(entry)

        except KeyError:
                self.add(entry)

    def remove(self, entry):

        if entry not in self._container:
            raise KeyError(str(entry.key) + " not in the dictionary hence cannot remove")

        self._container.remove(entry)

    def count(self):
        return len(self._container)

    def __getitem__(self, item):

        if isinstance(item,tuple):

            for val in self._container:
                if(hash(val) == hash(item)):
                    return val.value

            raise KeyError(str(item) + " not present in the LookUp Table")

        elif isinstance(item,int):

            strSet = list()

            for val in self._container:

                if(val.key[0] == item):
                    strSet.append(val.value)
                elif(val.key[1] == item):
                    strSet.append(val.value)

            if(len(strSet) == 0):
                raise KeyError("No item present with the given key")

            strSet.sort()
            return strSet

        else:
            raise IndexError("Invalid Index for the LookUp")

    def __setitem__(self, key, value):

        entry = Entry(key[0],key[1],value)

        for val in self._container:

            if(hash(entry) == hash(val)):
                self.update(entry) # updating the Existing Entry
                return

        self.add(entry) # Adding a new entry because it is not present in the container

def main():

    lut = Lookup("lut")

    entry = Entry(0,1,"It is today")
    entry1 = Entry(1,2,"Tomorrow is better")
    entry2 = Entry(2,3,"The future is bright")

    print(str(entry))
    print(str(entry1))
    print(str(entry2))

    lut.add(entry)
    lut.add(entry1)
    lut.add(entry2)

    print(lut[(1,2)])
    print(lut[2])
    #print(lut[(3,2)])
    #print(lut[4])
    lut[(0,1)] = "Hello World."
    lut[(3,5)] = "Again!"

    print(lut[(0,1)])
    print(lut[(1,2)])
    print(lut[(2,3)])
    print(lut[(3,5)])

if __name__ == '__main__':
    main()
