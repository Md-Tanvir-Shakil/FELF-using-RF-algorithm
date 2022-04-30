# I will use the pandas library for data analysis and manipulation.
import pandas as pd
#  I need some functions from numpy for adding support for large, multi-dimensional arrays and matrices.
import numpy as np
# visual representation of the data description
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import RobustScaler
# change the path according to your data 
# this data is for dependent variable (training data for furure )
E = pd.read_excel('Building.xlsx')
E['Time'] = pd.to_datetime(E['Time'], format='%Y-%m-%d %H:%M')
E2 = pd.DataFrame(E,columns=['Time', 'Demand(KW)'])
E2 = E2.set_index("Time")
# change the path according to your data 
# this data is for independent variable (training data for furure )
Path= "WeatherData.xlsx"
k= pd.read_excel(Path)
k['Time'] = pd.to_datetime(k['Time'], format='%m/%d/%Y %H:%M')
# change the data frame according to your needs .
k2= pd.DataFrame(k,columns=['Time', 'Temp', 'RH', 'Q', 'FF', 'P','month','HH'])
k2 = k2.set_index("Time")
df = pd.concat([k2, E2], axis=1) #axis =1 for considering the columns
sc1= StandardScaler()
sc2= MinMaxScaler()
sc3= RobustScaler()
X1 = sc1.fit_transform(k2)
X2 = sc2.fit_transform(k2)
X3 = sc3.fit_transform(k2)
RFReg = RandomForestRegressor(max_depth=12, random_state=0)
X_train2, X_test2, y_train2, y_test2 = train_test_split(X3, E2, test_size=0.2, random_state=0, shuffle= "False")
y_train2 = y_train2.values.ravel()
y_test2 = y_test2.values.ravel()
RFReg.fit(X_train2, y_train2)
# change the path according to your data 
# this data is for predicting the future ( independent variable)
path= "Weather_Cost.xlsx"
weather_cost = pd.read_excel(path)
weather_cost['Time'] = pd.to_datetime(weather_cost['Time'], format='%Y-%m-%d %H:%M')
weather_cost = weather_cost.set_index("Time")
X5 = sc1.transform(weather_cost)
predicted = RFReg.predict(X5)
predicted= pd.DataFrame(predicted, columns=['kWh'])
predicted['Time']= weather_cost.index
predicted= predicted.set_index('Time')
print(predicted)
