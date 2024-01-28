import numpy
import nltk

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

dataForm = "data/document_{}.txt"


class Text:

    def Tokenizer(txt):
        txt = txt.lower()
        return nltk.tokenize.word_tokenize(txt)
    

    def lemmatizer(txt):
        txt_lst = Text.Tokenizer(txt)
        wnl = nltk.WordNetLemmatizer()
        for i in range(len(txt_lst)):
            txt_lst[i] = wnl.lemmatize(txt_lst[i])
        return txt_lst


    def ReadDoc(docNum):
        f = open(dataForm.format(docNum), mode="r", encoding="utf8")
        tmp = f.read().lower()
        return tmp
    

    def SortedDocWords(docNum):
        doc = Text.ReadDoc(docNum)
        tmp = Text.lemmatizer(doc)

        #delete stop words
        stop_words = set(nltk.corpus.stopwords.words('english'))
        for i in tmp:
            if i in stop_words:
                tmp.remove(i)

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