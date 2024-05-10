# -*- coding: utf-8 -*-
"""Ass_2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ibEqCs4xV1gJVqzxit4dzcyGihxSFP1B
"""

import pandas as pd
df=pd.read_csv("Heart.csv")

print(df.to_string())

#a) Find standard deviation, variance of every numerical attribute.
df = df.apply(pd.to_numeric, errors='coerce')
print(df.std())  #Standard Deviation

print(df.var())  #Variance

#b) Find covariance and perform Correlation analysis using Correlation coefficient.
print(df.cov())   #Covariance

print(df.corr())  #Corelation

#e) Perform the data discretization using equi frequency binning method on age attribute
bins = pd.cut(df['Age'], bins=5, labels=False)
df['Age'] = bins

print(df.head(5))

#c) How many independent features are present in the given dataset?
features = df.drop(columns=['AHD'])
# Get the number of independent features
independent_features = features.shape[1]
# .shape : returns a tuple representing its dimensions (number of rows, number of columns)
# features.shape[1] : retrieves the number of columns, which corresponds to the number of independent features.
print(independent_features)

#d)Can we identify unwanted features?
import pandas as pd
# Identify constant value columns
constant_cols = [col for col in df.columns if df[col].nunique() == 1]

# Identify duplicate columns
duplicate_cols = []
for i in range(len(df.columns)):
    col1 = df.columns[i]
    for col2 in df.columns[i+1:]:
        if df[col1].equals(df[col2]):
            duplicate_cols.append(col2)

# Combine all potentially unwanted columns
unwanted_cols = set(constant_cols + duplicate_cols)

print("Potentially unwanted columns:")
print(unwanted_cols)

#f) Normalize RestBP, chol, and MaxHR attributes (considering above dataset) using min-max normalization, Z-score normalization, and decimal scaling normalization.
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler
# Select attributes to normalize
attributes_to_normalize = ['RestBP', 'Chol', 'MaxHR']

# Min-Max normalization
min_max_scaler = MinMaxScaler()
ans=df[attributes_to_normalize] = min_max_scaler.fit_transform(df[attributes_to_normalize])
print(ans)

# Z-score normalization
z_score_scaler = StandardScaler()
ans=df[attributes_to_normalize] = z_score_scaler.fit_transform(df[attributes_to_normalize])
print(ans)

# Decimal scaling normalization
decimal_scaler = RobustScaler()
ans=df[attributes_to_normalize] = decimal_scaler.fit_transform(df[attributes_to_normalize])
print(ans)