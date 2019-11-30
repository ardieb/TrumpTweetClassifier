import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier, GradientBoostingClassifier, AdaBoostClassifier
from sklearn.model_selection import RandomizedSearchCV
import datetime as dt
from collections import Counter
from pandas.tseries.holiday import USFederalHolidayCalendar

from sklearn.preprocessing import StandardScaler, MinMaxScaler
from src import Vectorize


def read_files (train_file):
  """
  Output:
  df_X : pandas data frame of training data
  Y    : numpy array of labels
  """
  df = pd.read_csv(train_file, index_col = 0)
  df_X = df[df.columns[0:17]]
  Y = np.array(df['label'])
  return df_X, Y


def main():
  df_X_train, Y_train = read_files('datasets/train.csv')
  xTr, xVal, yTr, yVal = train_test_split(df_X_train, Y_train, test_size = 0.2, stratify = Y_train)
  Test = Vectorize(xTr)
  Validate = Vectorize(xVal)
  xTr = Test(keep_labels = False)
  xVal = Validate(keep_labels = False)
  print(f'Got training data with shape: {xTr.shape}')
  print(f'Got validation data with shape: {xVal.shape}')
  clf = GradientBoostingClassifier()
  clf.fit(xTr, yTr)
  yTrPreds = clf.predict(xTr)
  yValPreds = clf.predict(xVal)
  print('Training error: ' + str(round(np.sum(yTrPreds != yTr) / yTr.shape[0] * 100, 2)) + '%')
  print('Validation error: ' + str(round(np.sum(yValPreds != yVal) / yVal.shape[0] * 100, 2)) + '%')
  return xTr, yTr, xVal, yVal


if __name__ == '__main__':
  main()



