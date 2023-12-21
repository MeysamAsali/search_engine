from ClassesAndFuncs import Address
from ClassesAndFuncs import SortedUniqueWordsOfText
import ReadingData
import math
import json




# -----------------------------------------------------------
# idf:
    

class QueryIdf:
    def ComputeTermIDF(term, docNums):
        count = 0
        for i in range(len(docNums)):
            if ReadingData.Check.IsInDocument(term.lower(), docNums[i]):
                count+=1
        return (math.log(len(docNums)+1) - math.log(count + 1))


    def ComputeQueryTfAndIdf(query, docNums):
        tmpList = SortedUniqueWordsOfText(query)
        result={}
        for i in range(len(tmpList)):
            result[tmpList[i]] = (QueryIdf.ComputeTermIDF(tmpList[i], docNums),Tf.ComputeTermTFinLine(tmpList[i], query))
        return result


    def WriteQuery(query, docNums):
        tmp = QueryIdf.ComputeQueryTfAndIdf(query, docNums)
        f = open(Address.queryAddress, mode="w", encoding="utf8")
        json.dump(tmp, f)
        f.close()




# ------------------------------------------------------------------
# Computing Tf in doc and line:
        

class Tf:
    def ComputeTermTFinDocument(term, docNum):
        tmpList = ReadingData.WordsOfDocument(docNum)
        count = 0
        for i in range(len(tmpList)):
            if ReadingData.Check.AreAlmostSame(term.lower(), tmpList[i]):
                count+=1
        return (count/len(tmpList))



    def ComputeTermTFinLine(term, paragraph):
        tmpList = paragraph.lower().split()
        count = 0
        for i in range(len(tmpList)):
            if ReadingData.Check.AreAlmostSame(term.lower(), tmpList[i]):
                count+=1
        return (count/len(tmpList))

# ----------------------------------------------------------
# Retrieve Tf and Idf:
    

class Retrieval:
    def RetrieveTFinDoc(term, docNum):
        result = 0
        f = open(Address.JsonAddress.format(docNum), mode="r", encoding="utf8")
        tmpDict = json.load(f)
        f.close()
        try:
            result = tmpDict[term]
        except KeyError:
            pass
        return result



    def RetrieveTFinLine(term, lineNum):
        result = 0
        f =open(Address.LineAddress.format(lineNum), mode="r", encoding="utf8")
        tmpDict = json.load(f)
        f.close()
        try:
            result = tmpDict[term]
        except KeyError:
            pass
        return result



    def RetrieveQueryIdf(term, docNums):
        result = math.log(len(docNums)+1)
        f = open(Address.queryAddress, mode="r", encoding="utf8")
        tmpDict = json.load(f)
        f.close()
        try:
            result = tmpDict[term][0]
        except KeyError:
            pass
        return result
    


    def RetrieveQueryTf(term):
        result = 0
        f = open(Address.queryAddress, mode="r", encoding="utf8")
        tmpDict = json.load(f)
        f.close()
        try:
            result = tmpDict[term][1]
        except KeyError:
            pass
        return result

# ------------------------------------------------------------
# Compute Tf-Idf:



class Term_Tf_Idf:
    def TF_IDF_in_corpus(term, docNums, thisDoc):
        return Retrieval.RetrieveQueryIdf(term.lower(), docNums) * Retrieval.RetrieveTFinDoc(term.lower(), thisDoc)



    def TF_IDF_in_document(term, docNums, lineNum):
        return Retrieval.RetrieveQueryIdf(term.lower(), docNums) * Retrieval.RetrieveTFinLine(term.lower(), lineNum)



    def TF_IDF_in_query(term, docNums):
        return Retrieval.RetrieveQueryIdf(term.lower(), docNums) * Retrieval.RetrieveQueryTf(term)
