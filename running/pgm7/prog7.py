# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 17:46:38 2018

@author: Devaraja
"""
import numpy as np
import pandas as pd
import csv
from pgmpy.estimators import MaximumLikelihoodEstimator 
from pgmpy.models import BayesianModel
from pgmpy.inference import VariableElimination 
lines = list(csv.reader(open('data7_names.csv', 'r'))); 
attributes = lines[0]
heartDisease = pd.read_csv('data7_heart.csv', names = attributes)
heartDisease = heartDisease.replace('?', np.nan)
print('Few examples from the dataset are given below')
print(heartDisease.head())
print('\nAttributes and datatypes')
print(heartDisease.dtypes)
model = BayesianModel([('age', 'trestbps'),('age', 'fbs'),('sex', 'trestbps'),('exang', 'trestbps'), ('trestbps','heartdisease'),('fbs','heartdisease'), ('heartdisease','restecg'),('heartdisease','thalach'),('heartdisease','chol')])
print('\nLearning CPDs using Maximum Likelihood Estimators...')
model.fit(heartDisease, estimator=MaximumLikelihoodEstimator)
print('\nInferencing with Bayesian Network:')
HeartDisease_infer = VariableElimination(model)
print('\n1.Probability of HeartDisease given Age=20')
q = HeartDisease_infer.query(variables=['heartdisease'], evidence={'age': 5}) 
print(q['heartdisease'])
print('\n2. Probability of HeartDisease given chol (Cholestoral) =100')
q = HeartDisease_infer.query(variables=['heartdisease'], evidence={'chol': 50})
print(q['heartdisease'])
