import re
from datetime import datetime

from src.consts import *


def avg_sentence_length(text):
  """
  Averages the number of words in a sentence of `text`

  :param text: The text to analyze (str)
  :return: average_words (float)
  """
  sentences = [s.strip() for s in re.split(r'[\.\?!]', text) if s]
  return sum(len(sentence.split()) for sentence in sentences) / len(sentences)


def avg_word_length(text):
  """
  Averages the word length in `text`

  :param text: The text to analyze (str)
  :return: average_word_len (float)
  """
  words = re.sub(r'[\.\?!]', '', text).split()
  return sum(len(word) for word in words) / len(words)


def character_count(text):
  """
  Returns the number of alpha numeric characters in `text`

  :param text: The text to analyze (str)
  :return: character_count (int)
  """
  return len(re.sub(r'^[A-Za-z0-9_]', '', text))


def is_quoted_retweet(text):
  """
  Determines if the text begins with a quoted retweet

  :param text: The text to analyze (str)
  :return: true | false
  """
  return int(text[:2] == '"@')


def count_all_caps(text):
  """
  Determines the number of all caps words in `text`

  :param text: The text to analyze (str)
  :return: num_all_caps (int)
  """
  return len(re.findall('\s([A-Z][A-Z]+)', text))


def count_random_caps(text):
  """
  Determines the number of randomly capitalized words in `text`

  :param text: The text to analyze (str)
  :return: num_random_caps (int)
  """
  return len(re.findall(r"(?<!\.\s)(?<!\!\s)(?<!\?\s)\b[A-Z][a-z]*[^'][^I]\b", text))


def is_mention(text):
  """
  Determines whether the tweet is a mention i.e. `text` begins with <USER>

  :param text: The text to analyze (str)
  :return: true | false
  """
  return int(text[0] == '@')


def count_punctuation(text):
  """
  Determines the counts of different types of punctuation in `text`
  Punctuation can be one of comma, lparen, rparen, exclamation, period, semicolon, colon, question

  :param text: The text to analyze (str)
  :return: The counts for the different types of punctuation
  """
  counts = dict()
  for mark in punctuation:
    counts[mark] = len(re.findall(mark, text))
  return counts


def period_of_day(s):
  """
  Determines the period of the day given the string s, which represents a datetime object

  :param s: The datetime string to read (str)
  :return: period (int) - one of
    0 (early morning),
    1 (morning),
    2 (midday),
    3 (afternoon),
    4 (evening),
    5 (night),
    6 (midnight)
  """
  dt = datetime.strptime(s, datetime_fmt)
  if dt.hour <= 3: return 6
  elif dt.hour <= 6: return 0
  elif dt.hour <= 11: return 1
  elif dt.hour <= 14: return 2
  elif dt.hour <= 17: return 3
  elif dt.hour <= 20: return 4
  else: return 5


def day_of_week(s):
  """
  Determines the day of the week given the string s, which represents a datetime object

  :param s: The datetime string to read
  :return: day (int) - indexed at 0 for monday
  """
  dt = datetime.strptime(s, datetime_fmt)
  return dt.weekday()


def starts_with_I(text):
  """
  Determines whether the text starts with the letter 'I'

  :param text: The text to analyze
  :return: 1 if the text starts with an 'I', 0 otherwise
  """
  return int(re.search(r'.*([A-Z]{1}|[a-z]{1}).*', text).group(0).lower() == 'i')


def count_keywords(text):
  """
  Determines the counts for each nickname in text

  :param text: The text to analyze
  :return: counts of the keywords as a dict
  """
  t = text.lower()
  counts = {}
  for keyword in keywords:
    counts[keyword] = len(re.findall(keyword, t))
  return counts


def ends_with_link(text):
  """
  Determines whether the text ends with a link

  :param text: The text to analyze
  :return: 0 - 1 if there is not or is a link as the last word
  """
  return int(text.split(' ')[-1][:4] == 'http')


def ends_with_hashtag(text):
  """
  Determines whether the text ends with a hashtag

  :param text: The text to analyze
  :return: 0 - 1 if there is not or is a hastag as the last word
  """
  return int(text.split(' ')[-1][0] == '#')






