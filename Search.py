from Sort import Sort

class SearchInDocs:

    def ListOfMostRelevantDocs(query, docNums):
        result = docNums.copy()
        tmp = Sort.SortDocs(result, 0, len(result)-1, docNums, query)
        tmp.reverse()
        return tmp


    def SearchDocs(query, docNums):
        tmpList = SearchInDocs.ListOfMostRelevantDocs(query, docNums)
        return tmpList[0]
    




class SearchInLines:

    def ListOfMostRelevantLines(query, lineNums):
        result = lineNums.copy()
        tmp = Sort.SortLines(result, 0 , len(result)-1, lineNums, query)
        tmp.reverse()
        return tmp
    

    def SearchLines(query, lineNums):
        tmpList = SearchInLines.ListOfMostRelevantLines(query, lineNums)
        return tmpList[0]