from Text import Unique
import os
import json


TfFormat = 'WordsTF/doc_{}.json'

def WriteAllDocsTFs():
    if os.path.exists("WordsTF/"):
        return -1
    os.mkdir("WordsTF/")
    for i in range(1000):
        tmp = Unique.UniqueWordsTFs(i)
        f = open(TfFormat.format(i), mode="w", encoding="utf8")
        json.dump(tmp, f)
        f.close()
    return 1
