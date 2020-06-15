

def startsWith(str1, str2):
    return str1.find(str2) == 0 or str1.strip().find(str2) == 0


def removeUntil(str1, str2):
    ind = str1.find(str2)
    if ind == -1:
        return str1
    return str1[ind + len(str2):]

def removeList(str1, l):
    for word in l:
        str1 = str1.replace(word,"")
    return str1

def removeComments(str1):
    if str1.find("//") != -1:
        return removeComments(str1[:str1.find("//")])
    if str1.find("/*") != -1:
        return removeComments(str1[:str1.find("/*")] + str1[str1.rfind("*/")+2:])
    return str1
