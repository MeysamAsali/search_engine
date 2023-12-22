from WritingTfStats import WriteAll
from ReadingData import ReadDocument
from TF_IDF import QueryIdf
from Search import SearchInDocs
from Search import SearchInLines
from Write import WriteAllDocsTFs
import json


searchingFormat = "Your query is \"{}\" \n candidate documents: {} \n doc id: {} \n line number: {} \n"

def Prompting():
    f = open('data.json', mode="r", encoding="utf8")
    loadList = json.load(f)
    f.close()
    while True:
        i = (input("Enter a number between 0 and 50000: "))
        if i.lower() == "exit":
            break
        try:
            i= int(i)
            query = loadList[i]["query"]
            docNums = loadList[i]["candidate_documents_id"]
            print(searchingFormat.format(query, docNums, loadList[i]["document_id"], loadList[i]["is_selected"]))
            print("-------------------------------------------------")


            WriteAll.StatsOfAllDocs(docNums, query)
            QueryIdf.WriteQuery(query, docNums)
            r1=SearchInDocs.ListOfMostRelevantDocs(query, docNums)
            WriteAll.StatsOfAllLines(r1[0])
            print("Relevant results in order: ")
            print(r1)
            tmp = []
            for i in range(len(ReadDocument(r1[0]).split('\n'))):
                tmp.append(i)
            print()
            print("Relevant line: ")
            print(SearchInLines.SearchLines(query, tmp))
            print()         
        except:
            print("wrong input")
            print()


WriteAllDocsTFs()

Prompting()