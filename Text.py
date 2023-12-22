import numpy
import difflib


dataForm = "data/document_{}.txt"



class Text:

    def AreAlmostSame(t1, t2):
        if difflib.SequenceMatcher(None, t1, t2).ratio() > 0.85:
            return True
        return False
    
    def ComesEarlier(t1,t2):
        i = 0
        l1 = len(t1)
        l2 = len(t2)
        while i<l1 and i<l2 and ord(t1[i]) == ord(t2[i]):
            i+=1
        if i == l1:
            return True
        elif i == l2:
            return False
        else:
            return ord(t1[i]) < ord(t2[i])

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
    

    def SearchInSortedArray(term, arr, s, e):
        if e-s+1 == 0 :
            if arr[0] == term:
                return s
            else: 
                return -1
        else:
            mid = int((e+s)/2)
            if term == arr[mid]:
                return mid
            elif Text.ComesEarlier(term, arr[mid]):
                return Text.SearchInSortedArray(term, arr, s, mid-1)
            else:
                return Text.SearchInSortedArray(term, arr, mid+1, e)
    


class Unique:

    def UniqueWordsOfArray(arr1):
        length = len(arr1)
        tmpList=[]
        j=0
        while j < length :
            while (j+1 < length) and (arr1[j]==arr1[j+1]):
                j+=1
            tmpList.append(arr1[j])
            j+=1
        return numpy.array(tmpList)
            

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