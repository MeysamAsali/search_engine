import difflib
from ClassesAndFuncs import Address


# ---------------------------------------------------------
# Reading from data:

def ReadDocument(docNum):
    f = open(Address.dataAddress.format(docNum), encoding="utf8")
    res = f.read().lower()
    f.close()
    return res



def WordsOfDocument(docNum):
    return ReadDocument(docNum).split()



def UniqueWordsOfList(tmpList):
    tmpList.sort()
    j=len(tmpList) - 2
    while j>=0 :
        if tmpList[j] == tmpList[j+1]:
            tmpList.remove(tmpList[j+1])
        j-=1
    return tmpList



def FindUniqueWords(docNum):
    tmpList = WordsOfDocument(docNum)
    tmpList = UniqueWordsOfList(tmpList)
    return tmpList



# ---------------------------------------------------------------
# Checking:



class Check:
    def AreAlmostSame(str1 , str2):
        return (difflib.SequenceMatcher(None, str1.lower(), str2.lower()).ratio() > 0.85)

    def IsInDocument(term, docNum):
        tmpList = FindUniqueWords(docNum)
        for i in range(len(tmpList)):
            if Check.AreAlmostSame(term, tmpList[i]):
                return True
        return False

