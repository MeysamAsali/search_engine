from math import sqrt

def VectorLength(vector):
    tmp = 0
    for i in range(len(vector)):
        tmp += vector[i]*vector[i]
    return sqrt(tmp)



def SimilarityRate(array1, array2):
    tmp = 0
    for i in range(len(array1)):
        tmp += array1[i]*array2[i]
    v1 = VectorLength(array1)
    v2 = VectorLength(array2)
    if v1==0 or v2==0:
        return 0
    return tmp/(v1 * v2)