def SortedUniqueWordsOfText(text):
    text = text.lower()
    tmpList = text.split()
    tmpList.sort()
    j=len(tmpList) - 2
    while j>=0 :
        if tmpList[j] == tmpList[j+1]:
            tmpList.remove(tmpList[j+1])
        j-=1
    return tmpList



class Address:
    uniqueWordsAddress = "DocsUniqueWords/document_{}.json"
    dataAddress = "data/document_{}.txt"
    JsonAddress = "TfInDocs/docStat_{}.json"
    LineAddress = "LineUniqueWords/Line_{}.json"
    queryAddress = "queryStats.json"
