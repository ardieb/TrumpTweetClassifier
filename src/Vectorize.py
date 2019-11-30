from src.pipeline import augment
import numpy as np
import pandas as pd


class Vectorize:
  """
  Given a dataset of Trump's tweeting history, this class will create and maintain
  an array of vectors that represent this data, as well as the labels for each data point
  """
  def __init__(self, df):
    self._df = df
    self._augmented = None
    self._vecs = None
    self._labels = None

  def __call__(self, df = None, keep_labels = True):
    if df:
      self._df = df
      self._augmented = augment(self._df)
    if not self._augmented:
      self._augmented = augment(self._df)
    if keep_labels:
      self._labels = np.array(self._df['label'])
    mat = self._augmented[self._augmented.columns.difference([
      'text',
      'replyToSN',
      'created',
      'id.1',
      'replyToUID',
      'statusSource',
      'screenName',
      'label'])].copy()
    mat = mat.apply(pd.to_numeric, errors='ignore').fillna(0)
    mat.transpose()
    self._vecs = np.nan_to_num(np.array(mat.to_numpy(dtype=np.float)))
    return self._vecs[0], np.array(self._labels) if keep_labels else self._vecs[0]


