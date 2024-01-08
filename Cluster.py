from sklearn.cluster import KMeans
import DimensionReduction

def Cluster(reducedDocs, numberOfClusters):
    kmeans = KMeans(n_clusters = numberOfClusters)

    result = kmeans.fit_predict(reducedDocs)
    return result