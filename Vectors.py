import numpy
import math
from TF_IDF import Term_Tf_Idf
from ClassesAndFuncs import SortedUniqueWordsOfText


def VectorLength(vector):
    tmp = 0
    for i in range(len(vector)):
        tmp += vector[i]*vector[i]
    return math.sqrt(tmp)



class Vectorize:
    def QueryVector(query, docNums):
        tmpList = SortedUniqueWordsOfText(query)
        result = tmpList.copy()
        result = numpy.array(result)
        tmpList = numpy.array([0.0]*len(tmpList))
        for i in range(len(tmpList)):
            tmpList[i] = Term_Tf_Idf.TF_IDF_in_query(result[i], docNums)
        return (result, tmpList)



    def DocumentVector(queryVec, docNums, thisDoc):
        docVec = numpy.array([0.0]*len(queryVec[0]))
        for i in range(len(queryVec[0])):
            docVec[i] = Term_Tf_Idf.TF_IDF_in_corpus(queryVec[0][i] , docNums, thisDoc)
        return docVec
    


    def LineVector(queryVec, docNums, thisLine):
        docVec = numpy.array([0.0] * len(queryVec[0]))
        for i in range(len(queryVec[0])):
            docVec[i] = Term_Tf_Idf.TF_IDF_in_document(queryVec[0][i], docNums, thisLine)
        return docVec