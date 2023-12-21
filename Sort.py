from Vectors import Vectorize
from CosineSimilarity import CosineSimilarity


class Similarity:
    def DocSimilarity(thisDoc, query, docNums):
        tmp = Vectorize.QueryVector(query, docNums)
        arr = Vectorize.DocumentVector(tmp, docNums, thisDoc)
        return CosineSimilarity(tmp[1], arr)

    def LineSimilarity(lineNum, query, docNums):
        tmp = Vectorize.QueryVector(query, docNums)
        arr = Vectorize.LineVector(tmp, docNums, lineNum)
        return CosineSimilarity(tmp[1], arr)






class Sort:
        
    def MergeDocs(list1, list2, docNums, query):
        result=[]
        i=0
        j=0
        while i<len(list1) and j< len(list2):
            if Similarity.DocSimilarity(list1[i], query, docNums) < Similarity.DocSimilarity(list2[j], query, docNums):
                result.append(list1[i])
                i+=1
            else:
                result.append(list2[j])
                j+=1
        while i<len(list1):
            result.append(list1[i])
            i+=1
        while j<len(list2):
            result.append(list2[j])
            j+=1
        return result

    def SortDocs(myList, left, right, docNums, query):
        result=myList[left:right+1].copy()
        if left<right:
            mid=int((left + right)/2)
            a = Sort.SortDocs(myList, left, mid, docNums, query)
            b = Sort.SortDocs(myList, mid+1, right, docNums, query)
            result = Sort.MergeDocs(a,b, docNums, query)
        return result
    




    def MergeLines(list1, list2, lineNums, query):
        result=[]
        i=0
        j=0
        while i<len(list1) and j< len(list2):
            if Similarity.LineSimilarity(list1[i], query, lineNums) < Similarity.LineSimilarity(list2[j], query, lineNums):
                result.append(list1[i])
                i+=1
            else:
                result.append(list2[j])
                j+=1
        while i<len(list1):
            result.append(list1[i])
            i+=1
        while j<len(list2):
            result.append(list2[j])
            j+=1
        return result

    def SortLines(myList, left, right, lineNums, query):
        result=myList[left:right+1].copy()
        if left<right:
            mid=int((left + right)/2)
            a = Sort.SortLines(myList, left, mid, lineNums, query)
            b = Sort.SortLines(myList, mid+1, right, lineNums, query)
            result = Sort.MergeLines(a,b, lineNums, query)
        return result