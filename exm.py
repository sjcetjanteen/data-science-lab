import matplotlib.pyplot as plt
import pandas as pd
from sklearn import metrics,tree
from sklearn.model_selection import train_test_split
data = pd.read_csv("car.csv",names=["big" ,'med', 'small', 'low', 'vhigh', 'unacc'])
print(data.head())
data.info()
data['class'],class_names=pd.factorize(data['class'])
print(class_names)
print(data['class'].unique())
data['big'] = pd.factorize(data['big'])
data['med'] = pd.factorize(data['med'])
data['small'] = pd.factorize(data['small'])
data['low'] = pd.factorize(data['low'])
data['vhigh'] = pd.factorize(data['vhigh'])
data['unacc'] = pd.factorize(data['unacc'])
x = data.iloc[:,:-1]
y=data.iloc[:,:1]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=0)
dtree=tree.DecisionTreeClassifier(criterion='entropy',max_depth=3,random_state=0)
dtree.fit(x_train,y_train)
y_pred=dtree.predict(x_test)

