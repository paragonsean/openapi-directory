# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.sentiment import Sentiment
from openapi_server.models.topic import Topic
from openapi_server.models.topic_sentiment import TopicSentiment
from openapi_server import util


class TopicSentimentOutput(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, language: str=None, sentiments: List[Sentiment]=None, text: str=None, topic_sentiments: List[TopicSentiment]=None, topics: List[Topic]=None):
        """TopicSentimentOutput - a model defined in OpenAPI

        :param id: The id of this TopicSentimentOutput.
        :param language: The language of this TopicSentimentOutput.
        :param sentiments: The sentiments of this TopicSentimentOutput.
        :param text: The text of this TopicSentimentOutput.
        :param topic_sentiments: The topic_sentiments of this TopicSentimentOutput.
        :param topics: The topics of this TopicSentimentOutput.
        """
        self.openapi_types = {
            'id': str,
            'language': str,
            'sentiments': List[Sentiment],
            'text': str,
            'topic_sentiments': List[TopicSentiment],
            'topics': List[Topic]
        }

        self.attribute_map = {
            'id': 'id',
            'language': 'language',
            'sentiments': 'sentiments',
            'text': 'text',
            'topic_sentiments': 'topicSentiments',
            'topics': 'topics'
        }

        self._id = id
        self._language = language
        self._sentiments = sentiments
        self._text = text
        self._topic_sentiments = topic_sentiments
        self._topics = topics

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TopicSentimentOutput':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The TopicSentimentOutput of this TopicSentimentOutput.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this TopicSentimentOutput.


        :return: The id of this TopicSentimentOutput.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TopicSentimentOutput.


        :param id: The id of this TopicSentimentOutput.
        :type id: str
        """

        self._id = id

    @property
    def language(self):
        """Gets the language of this TopicSentimentOutput.


        :return: The language of this TopicSentimentOutput.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this TopicSentimentOutput.


        :param language: The language of this TopicSentimentOutput.
        :type language: str
        """

        self._language = language

    @property
    def sentiments(self):
        """Gets the sentiments of this TopicSentimentOutput.


        :return: The sentiments of this TopicSentimentOutput.
        :rtype: List[Sentiment]
        """
        return self._sentiments

    @sentiments.setter
    def sentiments(self, sentiments):
        """Sets the sentiments of this TopicSentimentOutput.


        :param sentiments: The sentiments of this TopicSentimentOutput.
        :type sentiments: List[Sentiment]
        """

        self._sentiments = sentiments

    @property
    def text(self):
        """Gets the text of this TopicSentimentOutput.


        :return: The text of this TopicSentimentOutput.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this TopicSentimentOutput.


        :param text: The text of this TopicSentimentOutput.
        :type text: str
        """

        self._text = text

    @property
    def topic_sentiments(self):
        """Gets the topic_sentiments of this TopicSentimentOutput.


        :return: The topic_sentiments of this TopicSentimentOutput.
        :rtype: List[TopicSentiment]
        """
        return self._topic_sentiments

    @topic_sentiments.setter
    def topic_sentiments(self, topic_sentiments):
        """Sets the topic_sentiments of this TopicSentimentOutput.


        :param topic_sentiments: The topic_sentiments of this TopicSentimentOutput.
        :type topic_sentiments: List[TopicSentiment]
        """

        self._topic_sentiments = topic_sentiments

    @property
    def topics(self):
        """Gets the topics of this TopicSentimentOutput.


        :return: The topics of this TopicSentimentOutput.
        :rtype: List[Topic]
        """
        return self._topics

    @topics.setter
    def topics(self, topics):
        """Sets the topics of this TopicSentimentOutput.


        :param topics: The topics of this TopicSentimentOutput.
        :type topics: List[Topic]
        """

        self._topics = topics
