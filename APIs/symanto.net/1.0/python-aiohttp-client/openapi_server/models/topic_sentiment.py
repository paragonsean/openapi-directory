# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.sentiment import Sentiment
from openapi_server.models.topic import Topic
from openapi_server import util


class TopicSentiment(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, sentence: str=None, sentiment: Sentiment=None, topic: Topic=None):
        """TopicSentiment - a model defined in OpenAPI

        :param sentence: The sentence of this TopicSentiment.
        :param sentiment: The sentiment of this TopicSentiment.
        :param topic: The topic of this TopicSentiment.
        """
        self.openapi_types = {
            'sentence': str,
            'sentiment': Sentiment,
            'topic': Topic
        }

        self.attribute_map = {
            'sentence': 'sentence',
            'sentiment': 'sentiment',
            'topic': 'topic'
        }

        self._sentence = sentence
        self._sentiment = sentiment
        self._topic = topic

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TopicSentiment':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The TopicSentiment of this TopicSentiment.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def sentence(self):
        """Gets the sentence of this TopicSentiment.


        :return: The sentence of this TopicSentiment.
        :rtype: str
        """
        return self._sentence

    @sentence.setter
    def sentence(self, sentence):
        """Sets the sentence of this TopicSentiment.


        :param sentence: The sentence of this TopicSentiment.
        :type sentence: str
        """

        self._sentence = sentence

    @property
    def sentiment(self):
        """Gets the sentiment of this TopicSentiment.


        :return: The sentiment of this TopicSentiment.
        :rtype: Sentiment
        """
        return self._sentiment

    @sentiment.setter
    def sentiment(self, sentiment):
        """Sets the sentiment of this TopicSentiment.


        :param sentiment: The sentiment of this TopicSentiment.
        :type sentiment: Sentiment
        """

        self._sentiment = sentiment

    @property
    def topic(self):
        """Gets the topic of this TopicSentiment.


        :return: The topic of this TopicSentiment.
        :rtype: Topic
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this TopicSentiment.


        :param topic: The topic of this TopicSentiment.
        :type topic: Topic
        """

        self._topic = topic
