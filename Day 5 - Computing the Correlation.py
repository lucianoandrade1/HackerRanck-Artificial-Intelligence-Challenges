#Hackerrank Day 5: Computing the Correlation challenge
#Author: Luciano Andrade

#You are given the scores of N students in three different subjects - Mathematics,*Physics* and Chemistry; all of which have 
#been graded on a scale of 0 to 100. Your task is to compute the Pearson product-moment correlation coefficient between the 
#scores of different pairs of subjects (Mathematics and Physics, Physics and Chemistry, Mathematics and Chemistry) based on 
#this data. This data is based on the records of the CBSE K-12 Examination - a national school leaving examination in India, 
#for the year 2013.

#Input Format

#The first row contains an integer N.
#This is followed by N rows containing three tab-space ('\t') separated integers, M P C corresponding to a candidate's scores 
#in Mathematics, Physics and Chemistry respectively.

#Each row corresponds to the scores attained by a unique candidate in these three subjects.

#Input Constraints

#1 <= N <= 5 x 105
#0 <= M, P, C <= 100

#Output Format

#The output should contain three lines, with correlation coefficients computed and rounded off correct to exactly 2 decimal 
#places.
#The first line should contain the correlation coefficient between Mathematics and Physics scores.
#The second line should contain the correlation coefficient between Physics and Chemistry scores.
#The third line should contain the correlation coefficient between Chemistry and Mathematics scores.

#So, your output should look like this (these values are only for explanatory purposes):

#0.12
#0.13
#0.95

#Test Cases

#There is one sample test case with scores obtained in Mathematics, Physics and Chemistry by 20 students. The hidden test case 
#contains the scores obtained by all the candidates who appeared for the examination and took all three tests (Mathematics, 
#Physics and Chemistry).

import numpy as np
import scipy.stats
import pandas as pd

data = {'Mathematics':  [73, 48, 95, 95, 33, 47, 98, 91, 95, 93, 70, 85, 33, 47, 95, 84, 43, 95, 54, 72],
        'Physics': [72, 67, 92, 95, 59, 58, 95, 94, 84, 83, 70, 79, 67, 73, 87, 86, 63, 92, 80, 76],
        'Chemistry': [76, 76, 95, 96, 79, 74, 97, 97, 90, 90, 78, 91, 76, 90, 95, 95, 75, 100, 87, 90]}

acorr, _ = scipy.stats.pearsonr(data['Mathematics'], data['Physics'])    # Pearson's r

bcorr, _ = scipy.stats.pearsonr(data['Physics'], data['Chemistry'])    # Pearson's r

ccorr, _ = scipy.stats.pearsonr(data['Chemistry'], data['Mathematics'])    # Pearson's r


print('%.2f' % acorr)
print('%.2f' % bcorr)
print('%.2f' % ccorr)
