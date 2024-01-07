from sklearn.decomposition import PCA
from Compute import Retrieval
from collections import Counter
import json


TfIdfFormat = "WordsTF_IDF/doc_{}.json"


def DocsVectors(documents):
    tmp = []
    for i in documents:
        tmp+=(Retrieval.RetrieveUniqueWords(i))

    cDict = Counter(tmp)
    l = len(cDict)

    result = []


    for i in documents:
        f= open(TfIdfFormat.format(i), mode="r", encoding="utf8")
        TfIdfDoc = json.load(f)
        f.close()


        tmpList = []
        for var in cDict:
            try:
                tmpList.append(TfIdfDoc[var][2])
            except:
                tmpList.append(0)
        
        result.append(tmpList.copy())

    return result


def ReduceDimensions(documents):
    tmp = DocsVectors(documents)
    PCAinstance = PCA(n_components=2)
    result = PCAinstance.fit_transform(tmp)
    return result


def WriteReducedDocs(documents):
    rd1 = ReduceDimensions(documents)
    rd2=[]
    for v in rd1:
        rd2.append(list(v))
    y = open('tmp.json', mode="w", encoding="utf8")
    json.dump(rd2, y)
    y.close()