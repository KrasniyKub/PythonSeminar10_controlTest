import random
import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

def one_hot(data_frame):
    data_frame = data_frame.values
    columns = set()
    
    for i in range(data_frame.shape[1]):
        for _ in range(data_frame.shape[0]):
            columns.add(data_frame[_,i])
    
    data_one_hot = pd.DataFrame()
    columns = list(columns)
    lst = ['0'] * data_frame.shape[0]

    for n in range(data_frame.shape[1]):
        for i in range(len(columns)):
            for _ in range(data_frame.shape[0]):
                if columns[i] == data_frame[_,n]:
                    lst[_] = '1' 
            data_one_hot[columns[i]] = lst
            lst = ['0'] * data_frame.shape[0]

    return data_one_hot

res = one_hot(data)

print(res)