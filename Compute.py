import json
import numpy
from Write import TfFormat
import os
import math

from collections import Counter

TfFormat = 'WordsTF/doc_{}.json'
Tf_IdfFormat = 'WordsTF_IDF/doc_{}.json'


class Retrieval:
    def RetrieveWordsTFs(docNum):
        f = open(TfFormat.format(docNum), mode="r", encoding="utf8")
        tmpDict = json.load(f)
        return tmpDict
    
    def RetrieveUniqueWords(docNum):
        tmpList = Retrieval.RetrieveWordsTFs(docNum).keys()
        return list(tmpList)
    
    def RetrieveDocTFs(docNum):
        tmpList = Retrieval.RetrieveWordsTFs(docNum).values()
        return list(tmpList)
    

    


class Tf_Idf:

    def TermIdf(term, cDict):
        c= 1
        c+= cDict[term]
        return math.log(50001 / c)




    def WriteDocTfIdf(docNum, cDict):
        tmpArr = numpy.array(Retrieval.RetrieveUniqueWords(docNum))
        tmpArr2 = numpy.array(Retrieval.RetrieveDocTFs(docNum))
        l = len(tmpArr)
        tmpDict = {}
        for i in range(l):
            idf = Tf_Idf.TermIdf(tmpArr[i], cDict)
            tf = tmpArr2[i]
            tmpDict[tmpArr[i]] = (tf , idf , tf*idf)
        
        f = open(Tf_IdfFormat.format(docNum), mode="w", encoding="utf8")
        json.dump(tmpDict, f)
        f.close()




    def WriteDocsStats():
        if os.path.exists("WordsTF_IDF/"):
            return -1
        
        
        os.mkdir("WordsTF_IDF/")
        tmpList = []
        d=0
        while d<50001:
            tmpList+= Retrieval.RetrieveUniqueWords(d)
            d+=1
        cDict = Counter(tmpList)
        f=open("UniqueWords.json", mode="w", encoding="utf8")
        json.dump(cDict, f)
        f.close()
        for i in range(50001):
            Tf_Idf.WriteDocTfIdf(i, cDict)
        return 1



