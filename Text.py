import numpy

dataForm = "data/document_{}.txt"



class Text:

    def Tokenizer(txt):
        txt = txt.lower()
        return numpy.array(txt.split())

    def ReadDoc(docNum):
        f = open(dataForm.format(docNum), mode="r", encoding="utf8")
        tmp = f.read().lower()
        return tmp
    

    def SortedDocWords(docNum):
        tmp = Text.Tokenizer(Text.ReadDoc(docNum))
        tmp.sort()
        return tmp
    


class Unique:


    def UniqueWordsOfArrayWithTf(arr1):
        length = len(arr1)
        tmpDict={}
        j=0
        while j < length:
            c = 1
            while (j+1<length) and (arr1[j] == arr1[j+1]):
                c+=1
                j+=1
            tmpDict[arr1[j]] = c/length
            j+=1
        return tmpDict


    def UniqueWordsTFs(docNum):
        tmp = Text.SortedDocWords(docNum)
        return Unique.UniqueWordsOfArrayWithTf(tmp)