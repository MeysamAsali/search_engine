import json
from Write import WriteAllDocsTFs
from Compute import Tf_Idf
from Prompting import Prompting
from Search import MostRelevantDocs

WriteAllDocsTFs()
Tf_Idf.WriteDocsStats()
# Prompting()


f = open('data.json', mode = 'r', encoding = 'utf8')
load_list = json.load(f)
f.close

counter = 0

for i in range(1000):
    query = load_list[i]["query"]
    doc_nums = load_list[i]["candidate_documents_id"]
    rty = []

    for j in range(1000):
        rty.append(j)
    
    r1 = MostRelevantDocs(query, rty)
    if load_list[i]["document_id"] in r1[0:10]:
        counter += 1

print(counter/1000)