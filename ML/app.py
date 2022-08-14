import pickle 
import pandas as pd
import pathlib
data_dir = pathlib.Path("MOCK.csv")
data1=pd.read_csv(data_dir)
data1['Average'] = data1.mean(axis=1)
print(data1)
model = pickle.load(open('model.pkl','rb'))
if(model.predict(data1) == 0):
    print("You didn't work enough hours")
else:
    print("You worked enough hours")