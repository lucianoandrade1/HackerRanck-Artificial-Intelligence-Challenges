#Hackerrank Correlation and Regression Lines - A quick recap #3 challenge
#Author: Luciano Andrade

#Here are the test scores of 10 students in physics and history:

#Physics Scores  15  12  8   8   7   7   7   6   5   3
#History Scores  10  25  17  11  13  17  20  13  9   15

#When a student scores 10 in Physics, what is his probable score in History? Compute the answer correct to one decimal place.

#Output Format

#In the text box, enter the floating point/decimal value required. Do not leave any leading or trailing spaces.

import numpy as np
from sklearn.linear_model import LinearRegression

PhysicsScores = np.array([15,  12,  8,   8,   7,   7,   7,   6,   5,   3]).reshape((-1, 1))
HistoryScores = np.array([10,  25,  17,  11,  13,  17,  20,  13,  9,   15]).reshape((-1, 1))

reg = LinearRegression().fit(PhysicsScores, HistoryScores)

HScoreNew = reg.predict((np.array([10]).reshape((-1, 1))))

print('%.1f' % HScoreNew)
