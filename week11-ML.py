import pandas as pd
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import re
from sklearn import tree
import pydotplus   # you may also need to install the package graphviz - you may need to install the executable package from here: https://graphviz.org/download/
from sklearn.tree import DecisionTreeClassifier
import matplotlib.image as pltimg

scale = StandardScaler()

pd.set_option('display.max_columns', None)
nbaFrame = pd.read_csv('Seasons_Stats.csv')  # import csv spreadsheet data into pandas frame
print(nbaFrame.loc[:8])  # check to see if it worked by showing the first several rows
print("column names are: ", nbaFrame.columns) #what are the column names
print("column types are: ", nbaFrame.dtypes) #what are the column types

print("ingested data shape is:", nbaFrame.shape)
nbaFrame.dropna('columns', 'all', inplace=True) # remove any columns with all missing data
print("after dropping empty columns data shape is:", nbaFrame.shape)

nbaFrame.dropna('rows', inplace=True)  # remove any rows with missing data
print("after dropping rows with missing row values nbaFrame data shape is:", nbaFrame.shape)

def get_data(df, score, column):
    """Return rows of Dataframe where 'column' has value greater than 'score'."""
    new_df = df.loc[df[column] > score]
    return new_df

nbaTest = get_data(nbaFrame, 50, 'FTA')

nbaTest = get_data(nbaTest, 2016.0, 'Year')

nbaTest['AllStar'] = 0  #add a default negative value to the new AllStar column

allstars = ['Kyrie Irving', 'DeMar DeRozan', 'LeBron James', 'Jimmy Butler', 'Giannis Antetokounmpo', 'Isaiah Thomas', 'John Wall', 'Kevin Love', 'Carmelo Anthony', 'Kyle Lowry', 'Paul George', 'Kemba Walker', 'Paul Millsap', 'Stephen Curry', 'James Harden', 'Kevin Durant', 'Kawhi Leonard', 'Anthony Davis', 'Russell Westbrook', 'Klay Thompson', 'Draymond Green', 'DeMarcus Cousins', 'Marc Gasol', 'DeAndre Jordan', 'Gordon Hayward']

nbaTest.loc[nbaTest.Player.isin(allstars), 'AllStar'] = 1

print(nbaTest.loc[:8])

print("after dropping rows with missing row values and culling all years but 2017 nbaTest data shape is:", nbaTest.shape)

X = nbaTest[['eFG%', 'FT%']]
y = nbaTest['3P%']

scaledNBA = scale.fit_transform(X)

regr = linear_model.LinearRegression()
regr.fit(scaledNBA, y)

scaled = scale.transform([[0.51, 1841]])

predictedFTpercentage = regr.predict([scaled[0]])

print(predictedFTpercentage)

plt.scatter(X['FT%'], y)
plt.show()

totalx = int(len(X['FT%']) * 0.8)
totaly = int(len(y) * 0.8)

train_xPTS = X['FT%'][:totalx]
train_yFTper = y[:totaly]

test_xPTS = X['FT%'][totalx:]
test_yFTper = y[totaly:]

plt.scatter(train_xPTS, train_yFTper)
plt.show()

plt.scatter(test_xPTS, test_yFTper)
plt.show()

mymodel = np.poly1d(np.polyfit(train_xPTS, train_yFTper, 4))

myline = np.linspace(0, 1, 50)

plt.scatter(train_xPTS, train_yFTper)
plt.plot(myline, mymodel(myline), 'g')
plt.show()

r2 = r2_score(train_yFTper, mymodel(train_xPTS))

print(r2)

r2d2 = r2_score(test_yFTper, mymodel(test_xPTS))

print(r2d2)

print(mymodel(0.9))

posMapping = {'PG': 1, 'PG-SG': 1, 'SG-PG': 2, 'G': 2, 'G-F': 2, 'SG': 2, 'SG-F': 2, 'SG-SF': 2, 'SF': 3, 'SF-SG': 3, 'F-SG': 3, 'F': 3, 'SF-PF': 3, 'F-G': 3, 'F-PF': 3, 'PF-SF': 4, 'PF-C': 4, 'PF': 4, 'F-C': 4, 'C-F': 5, 'C-PF': 5, 'C': 5}
nbaTest['Pos'] = nbaTest['Pos'].map(posMapping)

print(nbaTest.tail(20))

features = ['Age', 'Pos', 'PER', 'WS']

xx = nbaTest[features]
yy = nbaTest['AllStar']

dtree = DecisionTreeClassifier()
dtree = dtree.fit(xx, yy)
data = tree.export_graphviz(dtree, out_file=None, feature_names=features)
graph = pydotplus.graph_from_dot_data(data)
graph.write_png('mydecisiontree.png')

img=pltimg.imread('mydecisiontree.png')
imgplot = plt.imshow(img)
plt.show()

if dtree.predict([[28, 2, 31, 9]])[0] > 0:
    print("you're an AllStar, get your game on, get paid")
else:
    print("enjoy your vacation during All Star weekend!")
