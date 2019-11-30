from src.derive_features import *
from src.text_analysis import *
from src.consts import *


def add_feature(df, feature, source, target = None, verbose = True):
  """
  Adds a new feature to the dataframe df derived from the source columns in sources and puts the
  resulting series into the target columns in targets

  :param verbose: Whether to print results
  :param df: The dataframe to augment
  :param feature: The feature extraction function\
  :param source: The source columns to apply the function to
  :param target: The target columns to add
  :return: A new dataframe
  """
  if verbose: print(
    f'Deriving features using {feature} function, sources {source}, targets {target}...')
  derived = df[source].apply(feature)
  if verbose: print(f'Done. Got {derived}')
  unpacked = pd.DataFrame({target: derived}) if target else derived.apply(pd.Series)
  return pd.concat([df, unpacked], axis = 1)


def augment(df):
  """
  Augments the dataframe df with additional features using derived characteristics

  :param df: The dataframe to augment
  :return: An augmented dataframe
  """
  df = add_feature(df, avg_sentence_length, 'text', 'avg_sentence_length')
  df = add_feature(df, avg_word_length, 'text', 'avg_word_length')
  df = add_feature(df, character_count, 'text', 'characer_count')
  df = add_feature(df, is_quoted_retweet, 'text', 'is_quoted_retweet')
  df = add_feature(df, count_all_caps, 'text', 'number_all_caps')
  df = add_feature(df, count_random_caps, 'text', 'random_caps')
  df = add_feature(df, is_mention, 'text', 'is_mention')
  df = add_feature(df, ends_with_link, 'text', 'ends_with_link')
  df = add_feature(df, ends_with_hashtag, 'text', 'ends_with_hashtag')
  df = add_feature(df, count_punctuation, 'text')
  df = add_feature(df, period_of_day, 'created', 'period_of_day')
  df = add_feature(df, day_of_week, 'created', 'weekday')
  df = add_feature(df, starts_with_I, 'text', 'starts_with_I')
  df = add_feature(df, count_keywords, 'text')
  df = add_feature(df, get_vader_scores, 'text')
  df = add_feature(df, text_emotion, 'text')
  return df
