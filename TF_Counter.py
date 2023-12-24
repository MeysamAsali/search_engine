import json
import numpy as np


tf_lst = []


for i in range(50001):
    with open(f'WordsTF\doc_{i}.json', 'r') as json_file:
            
        tf_txt = json.load(json_file)
        tf_sorted_txt = sorted(tf_txt.items(), key=lambda x:x[1], reverse=True)
        tf_lst.append(tf_sorted_txt[:10])


my_array = np.array(tf_lst)
print(my_array[20064])