import json
import Query
import numpy
from Text import Text
from Text import Unique
import math

docAddress = 'WordsTF_IDF/doc_{}.json'

def DocumentVector(docNum, query):
    f = open(docAddress.format(docNum), mode="r", encoding="utf8")
    tmp = json.load(f)
    f.close()
    queryWords = Query.QueryTFs(query)
    result = []
    for i in queryWords:
        try:
            w = tmp[i][2]
        except:
            w = 0
        result.append(w)
    return numpy.array(result)

# ----------------------------------------------------




def LineTf(str):
    tmp = Text.Tokenizer(str)
    tmp.sort()
    return Unique.UniqueWordsOfArrayWithTf(tmp)




def LineTfIdf(str):
    f = open('UniqueWords.json', mode="r", encoding="utf8")
    cDict = json.load(f)
    f.close()
    tmp = LineTf(str)
    result = {}
    for i in tmp:
        try:
            e = math.log(50001 / (cDict[i]+1))
        except:
            e = 0
        result[i] = [ tmp[i], e, tmp[i] * e]
    
    return result



def LineVector(str, query):
    tmp = LineTfIdf(str)
    queryWords = Query.QueryTFs(query)
    result = []
    for i in queryWords:
        try:
            w = tmp[i][2]
        except:
            w = 0
        result.append(w)
    return numpy.array(result)



