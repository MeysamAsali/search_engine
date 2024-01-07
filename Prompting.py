from Search import MostRelevantDocs
from Search import MostRelevantLines
import json


searchingFormat = "Your query is \"{}\" \n candidate documents: {} \n doc id: {} \n line number: {} \n"


def Prompting():
    f = open('data.json', mode="r", encoding="utf8")
    loadList = json.load(f)
    f.close()
    while True:
        i = (input("Enter a number please: "))
        print()
        if i.lower() == "exit":
            break
        try:
            i= int(i)
            query = loadList[i]["query"]
            docNums = loadList[i]["candidate_documents_id"]
            print(searchingFormat.format(query, docNums, loadList[i]["document_id"], loadList[i]["is_selected"]))
            print("-------------------------------------------------")

            r1 = MostRelevantDocs(query, docNums)

            print("Relevant results in order: ")
            print(r1)
            print()

            r2 = MostRelevantLines(query, r1[0])
            print("Related lines: " + str(r2))



        except:
            print("wrong input")
            print()