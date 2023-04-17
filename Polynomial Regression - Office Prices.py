#Hackerrank Polynomial Regression: Office Prices challenge
#Author: Luciano Andrade

#Charlie wants to purchase office-space. He does a detailed survey of the offices and corporate complexes in the area, and tries to quantify a lot of factors, such as the distance of the offices from residential and other commercial areas, schools and workplaces; the reputation of the construction companies and builders involved in constructing the apartments; the distance of the offices from highways, freeways and important roads; the facilities around the office space and so on.

#Each of these factors are quantified, normalized and mapped to values on a scale of 0 to 1. Charlie then makes a table. Each row in the table corresponds to Charlie's observations for a particular house. If Charlie has observed and noted F features, the row contains F values separated by a single space, followed by the office-space price in dollars/square-foot. If Charlie makes observations for H houses, his observation table has (F+1) columns and H rows, and a total of (F+1) * H entries.

#Charlie does several such surveys and provides you with the tabulated data. At the end of these tables are some rows which have just F columns (the price per square foot is missing). Your task is to predict these prices. F can be any integer number between 1 and 5, both inclusive.

#There is one important observation which Charlie has made.

#The prices per square foot, are (approximately) a polynomial function of the features in the observation table. This polynomial always has an order less than 4

#Input Format

#The first line contains two space separated integers, F and N. Over here, F is the number of observed features. N is the number of rows for which features as well as price per square-foot have been noted.

#This is followed by a table having F+1 columns and N rows with each row in a new line and each column separated by a single space. The last column is the price per square foot.

#The table is immediately followed by integer T followed by T rows containing F columns.

#Constraints

#1 <= F <= 5
#5 <= N <= 100
#1 <= T <= 100
#0 <= Price Per Square Foot <= 10^6 0 <= Factor Values <= 1

#Output Format

#T lines. Each line 'i' contains the predicted price for the 'i'th test case.

import sys
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

a, n = map(int,sys.stdin.readline().split())

tr =[]
for line in range(n):
    tr.append(sys.stdin.readline().split())

n = int(sys.stdin.readline(),10)

te =[]
for line in range(n):
    te.append(sys.stdin.readline().split())

dfInput = pd.DataFrame(tr).iloc[:,0:a]

dfOutput = pd.DataFrame(tr).iloc[:,a]

dfTest =  pd.DataFrame(te)

polynomial_features= PolynomialFeatures(degree=4)
dfInput_poly = polynomial_features.fit_transform(dfInput)

model = LinearRegression()
model.fit(dfInput_poly, dfOutput)

polynomial_features= PolynomialFeatures(degree=4)
dfTest_poly = polynomial_features.fit_transform(dfTest)

predictions = model.predict(dfTest_poly)

print("\n".join(["{:0.2f}".format(x) for x in predictions]))
