from ReadingData import ReadDocument
from TF_IDF import Tf
from ClassesAndFuncs import Address
from ClassesAndFuncs import SortedUniqueWordsOfText
import shutil
import os
import json





class WriteSingle:
    
    def WriteDocStats(docNum, tmpList):
        result = {}
        for i in range(len(tmpList)):
            result[tmpList[i]] = Tf.ComputeTermTFinDocument(tmpList[i], docNum)
        f= open(Address.JsonAddress.format(docNum), mode="w", encoding="utf8")
        json.dump(result, f)
        f.close()



    def WriteLineStats(line, lineNum):
        result = {}
        tmpList = line.lower().split()
        tmpList.sort()
        j=len(tmpList) - 2
        while j>=0 :
            if tmpList[j] == tmpList[j+1]:
                tmpList.remove(tmpList[j+1])
            j-=1
        for i in range(len(tmpList)):
            result[tmpList[i]] = Tf.ComputeTermTFinLine(tmpList[i], line)
        f= open(Address.LineAddress.format(lineNum), mode="w", encoding="utf8")
        json.dump(result, f)
        f.close()


# -----------------------------------------------------------
# All docs or lines:
        

class WriteAll:


    def StatsOfAllLines(docNum):
        tmpStr = ReadDocument(docNum)
        tmpList = tmpStr.split("\n")
        if os.path.exists("LineUniqueWords/"):
            shutil.rmtree("LineUniqueWords/")
        os.mkdir("LineUniqueWords/")
        for i in range(len(tmpList)):
            WriteSingle.WriteLineStats(tmpList[i], i)
        return True


    def StatsOfAllDocs(docNums, query):
        tmpList = SortedUniqueWordsOfText(query)
        if os.path.exists("TfInDocs/"):
            shutil.rmtree("TfInDocs/")
        os.mkdir("TfInDocs/")
        for i in docNums:
            WriteSingle.WriteDocStats(i, tmpList)
        return True