import json
import numpy
from Write import TfFormat
from Text import Text
import os
import shutil
import math
import random

TfFormat = 'WordsTF/doc_{}.json'
Tf_IdfFormat = 'WordsTF_IDF/doc_{}.json'


class Retrieval:
    def RetrieveWordsTFs(docNum):
        f = open(TfFormat.format(docNum), mode="r", encoding="utf8")
        tmpDict = json.load(f)
        return tmpDict
    
    def RetrieveUniqueWords(docNum):
        tmpList = Retrieval.RetrieveWordsTFs(docNum).keys()
        return numpy.array(list(tmpList))
    
    def RetrieveDocTFs(docNum):
        tmpList = Retrieval.RetrieveWordsTFs(docNum).values()
        return numpy.array(list(tmpList))
    
    


class Tf_Idf:


    def TermIdf(term):
        c=1
        d=0
        while d<25:
            i = random.randint(0, 50000)
            tmp = Retrieval.RetrieveWordsTFs(i)
            if term in tmp:
                c+=1
            d+=1
        return math.log(25 / c)

    def WriteDocTfIdf(docNum):
        tmpArr = Retrieval.RetrieveUniqueWords(docNum)
        tmpArr2 = Retrieval.RetrieveDocTFs(docNum)
        l = len(tmpArr)
        tmpDict = {}
        for i in range(l):
            idf = Tf_Idf.TermIdf(tmpArr[i])
            tf = tmpArr2[i]
            tmpDict[tmpArr[i]] = (tf , idf , tf*idf)
        
        f = open(Tf_IdfFormat.format(docNum), mode="w", encoding="utf8")
        json.dump(tmpDict, f)
        f.close()




    def WriteDocsStats():
        if os.path.exists("WordsTF_IDF/"):
            return -1
        os.mkdir("WordsTF_IDF/")

        # CopyFiles(TfFormat, 'CopyFiles/' )

        for i in range(50001):
            Tf_Idf.WriteDocTfIdf(i)
        return 1


