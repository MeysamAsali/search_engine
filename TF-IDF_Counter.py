import json
import numpy as np

def calculate_tfidfs():

    tf_idf_lst = []


    for i in range(50001):
        with open(f'WordsTF_IDF\doc_{i}.json', 'r') as json_file:
                
            tf_idf_txt = json.load(json_file)
            tf_idf_sorted_txt = sorted(tf_idf_txt.items(), key=lambda x:x[3], reverse=True)
            tf_idf_lst.append(tf_idf_sorted_txt[:10])



    my_array = np.array(tf_idf_lst)

    return my_array