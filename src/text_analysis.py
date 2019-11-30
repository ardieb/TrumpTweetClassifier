import pandas as pd
from nltk import word_tokenize, pos_tag, download
from nltk.tag import StanfordNERTagger
from nltk.stem.snowball import SnowballStemmer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import os
download('punkt')


def pos_tagging(text):
  """
  Creates a sequence of POS tags given the input text

  :param text: The text to analyze (str) (tweet)
  :return: A sequence of numbers representing the tokenized sequence
  """
  pos = pos_tag(word_tokenize(text))
  return " ".join(item[1] for item in pos)


def ner_tagging(text):
    """
    Takes a tweetokenized string of words and uses the Stanford NER Tagger to
    replace names, places, and organizations with a standard token. The text must be tokenized by
    TweetTokenizer before being processed

    :param text: The text to analyze (str) (tweet)
    :return: tagged_tweet (str)
    """
    st = StanfordNERTagger('stanford-ner/classifiers/english.all.3class.'
                           'distsim.crf.ser.gz', 'stanford-ner/stanford-ner.'
                           'jar', encoding='utf-8')
    ner = st.tag(word_tokenize(text))
    string = ""
    for item in ner:
        if item[1] == 'O':
            if item[0] == '<' or item[0] == '@':
                string += item[0]
            elif item[0] == '>':
                    string = string[:-1] + item[0] + ' '
            else:
                string += item[0] + ' '
        else:
            string += item[1] + ' '
    tweet = ''
    for word in string.split():
        if word.isupper():
            tweet += word + ' '
        else:
            tweet += word.lower() + ' '
    return tweet


def text_emotion(text):
  """
  Determines the ten NRC emotion values

  :param text: The text to perform emote analysis on
  :return: dictionary of scores for the ten NRC standard emotions
  """
  filepath = os.path.abspath("./NRC-emotion-lexicon.txt")
  lex_df = pd.read_csv(filepath,
                          names = ["word", "emotion", "association"],
                          sep = '\t')
  lex_words = lex_df.pivot(index = 'word',
                                 columns = 'emotion',
                                 values = 'association').reset_index()
  emotions = lex_words.columns.drop('word')
  values = {emotion: 0 for emotion in emotions}

  stemmer = SnowballStemmer("english")
  document = word_tokenize(text)
  for word in document:
    word = stemmer.stem(word.lower())
    score = lex_words[lex_words.word == word]
    if not score.empty:
      for emotion in list(emotions):
        values[emotion] += score[emotion]
  return values


def get_vader_scores(text):
    """
    Takes a string of text and outputs four values for Vader's negative,
    neutral, positive, and compound (normalized) sentiment scores

    :param text: The text to analyze (str)
    :return: a dictionary of vader scores
    """
    analyser = SentimentIntensityAnalyzer()
    scores = analyser.polarity_scores(text)
    scores['compound'] += 1
    return scores
