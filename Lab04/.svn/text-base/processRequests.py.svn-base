def processRequests():

    # TODO: Remove the "pass" before you add any code to this block.
    users_access = getAccessControlByLogin()

    fp = open("ServerRequests.txt", "r")
    allLines = fp.readlines()

    list_accesses = []

    for line in allLines:
        user_tuple = tuple()
        user_access = line.split(" : ")
        user = user_access[0].strip()
        access = user_access[1].strip().split("/")


        if access[3] in users_access[user]:
            list_accesses.append((user, user_access[1].rstrip('\n'), access[3], access[4], True))
        else:
            list_accesses.append((user, user_access[1].rstrip('\n'), access[3], access[4], False))

    fp.close()

    return list_accesses


def getAccessControlByLogin():

    # TODO: Remove the "pass" before you add any code to this block.
    fp = open("AccessControl.txt", "r")

    allLines = fp.readlines()

    users_access = dict()

    for line in allLines[2:]:
        user = line.split(" : ")
        user[0] = user[0].strip()
        user[1] = user[1].rstrip("\n")

        if user[0] not in users_access:
            users_access[user[0]] = {user[1]}

        else:
            users_access[user[0]].add(user[1])

    fp.close()
    return users_access

def Login_Names():

    fp = open("Logins.txt", "r")

    allLines = fp.readlines()

    users = dict()

    for line in allLines[2:]:
        user = line.split("|")
        user[0] = user[0].strip()
        user[1] = user[1].strip()

        if user[1] not in users:
            users[user[1]] = user[0]

    fp.close()

    return users

def getAccessControlByController():

    # TODO: Remove the "pass" before you add any code to this block.

    users = Login_Names()

    fp = open("AccessControl.txt", "r")

    allLines = fp.readlines()

    users_access = dict()

    for line in allLines[2:]:
        user = line.split(" : ")
        user[0] = user[0].strip()
        user[1] = user[1].rstrip("\n")

        if user[1] not in users_access:
            users_access[user[1]] = {user[0]}

        else:
            users_access[user[1]].add(user[0])

    fp.close()

    users_list = users_access.keys()

    for val in users_list:
        new_set = list(users_access[val])

        for index in range(0,len(new_set)):
            new_set[index] = users[new_set[index]]

        users_access[val] = set(new_set)

    return users_access


def getActionsOfController():

    # TODO: Remove the "pass" before you add any code to this block.
    fp = open("ServerRequests.txt", "r")

    allLines = fp.readlines()

    users_access = dict()

    for line in allLines[2:]:
        user = line.split(" : ")
        user[1] = user[1].rstrip("\n")

        paths = user[1].split("/")

        if paths[3] not in users_access:
            users_access[paths[3]] = {paths[4]}

        else:
            users_access[paths[3]].add(paths[4])

    fp.close()

    return users_access

def isAccessAllowedFor(userID, url):

    # TODO: Remove the "pass" before you add any code to this block.
    users_access = getAccessControlByLogin()

    access = url.split("/")[3]

    if userID not in users_access:
        return False
    else:
        return access in users_access[userID]

def getRequestsBy(userID):

    # TODO: Remove the "pass" before you add any code to this block.
    process_Requests = processRequests()

    links_accessed = []

    for val in process_Requests:
        if(userID == val[0]):
            links_accessed.append((val[1], val[4]))

    return links_accessed

def aggregateUserRequests():

    # TODO: Remove the "pass" before you add any code to this block.
    users = Login_Names()

    user_Requests = processRequests()

    userReq = dict()

    for val in user_Requests:

        if users[val[0]] not in userReq:
            if(val[4]):
                userReq[users[val[0]]] = [1,0]
            else:
                userReq[users[val[0]]] = [0,1]

        else:
            if(val[4]):
                userReq[users[val[0]]][0] += 1
            else:
                userReq[users[val[0]]][1] += 1

    user_names = userReq.keys()

    for name in user_names:
        userReq[name] = tuple(userReq[name])

    return userReq

def aggregateControllerRequests():

    # TODO: Remove the "pass" before you add any code to this block.
    user_Requests = processRequests()

    userReq = dict()

    for val in user_Requests:

        if val[2] not in userReq:
            if(val[4]):
                userReq[val[2]] = [1,0]
            else:
                userReq[val[2]] = [0,1]

        else:
            if(val[4]):
                userReq[val[2]][0] += 1
            else:
                userReq[val[2]][1] += 1

    user_names = userReq.keys()

    for name in user_names:
        userReq[name] = tuple(userReq[name])

    return userReq

def main():

    print(getAccessControlByLogin()["sward"])

    print(getAccessControlByController()["Reports"])

    print(getActionsOfController()["Internal"])

    print(processRequests())

    print(isAccessAllowedFor("jkelly", "https://www.purdue.com/Proceedings/Page14"))
    print(isAccessAllowedFor("grichardson", "https://www.purdue.com/Internal/Page03"))
    print(isAccessAllowedFor("gorantla", "https://www.purdue.com/Internal/Page03"))

    print(getRequestsBy("hwilson"))

    print(aggregateUserRequests()["Miller, Aaron"])

    print(aggregateControllerRequests()["Comments"])

if __name__ == "__main__":

    # TODO: Remove the "pass" before you add any code to this block.
    main()
