from CosineSimilarity import SimilarityRate
from Query import QueryVector
from DocAndLine import DocumentVector
from DocAndLine import LineVector
from Text import Text


def MostRelevantDocs(query, docNums):
    tmp = {}
    arr1 = QueryVector(query)
    for i in docNums:
        arr2 = DocumentVector(i, query)
        tmp[i] = SimilarityRate(arr1, arr2)

    tmp = sorted(tmp.items(), key=lambda x:x[1], reverse=True)
    result = []
    for i in tmp:
        result.append(i[0])
    return result




def LinesSimilarity(query, docNum):
    document = Text.ReadDoc(docNum)
    tmpList = document.split("\n")
    similarities = []
    for i in range(len(tmpList)):
        v1 = LineVector(tmpList[i] , query)
        v2 = QueryVector(query)
        similarities.append((i , SimilarityRate(v1, v2)))
    return similarities



def MostRelevantLines(query, docNum):
    tmp = LinesSimilarity(query, docNum)
    tmp.sort(key=lambda x:x[1], reverse=True)
    result = []
    for i in tmp:
        result.append(i[0])
    return result