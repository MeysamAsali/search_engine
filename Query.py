from Text import Text
from Text import Unique
import json
import math
import numpy


def QueryTFs(query):
    tmp = Text.Tokenizer(query)
    tmp.sort()
    return Unique.UniqueWordsOfArrayWithTf(tmp)


def QueryTfIdf(query):
    f = open('UniqueWords.json', mode="r", encoding="utf8")
    cDict = json.load(f)
    f.close()
    tmp = QueryTFs(query)
    result = {}
    for i in tmp:
        try:
            e = math.log(50001/(cDict[i.lower()] + 1))
        except:
            e = 0
        result[i] = [ tmp[i] , e , tmp[i]*e ]
    return result


def QueryVector(query):
    tmp = QueryTfIdf(query)
    result = []
    for i in tmp:
        result.append(tmp[i][2])
    return numpy.array(result)