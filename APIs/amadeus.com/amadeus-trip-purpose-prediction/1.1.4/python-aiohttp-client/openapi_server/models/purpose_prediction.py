# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.prediction_result_type import PredictionResultType
from openapi_server import util


class PurposePrediction(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, probability: str=None, result: PredictionResultType=None, sub_type: str=None, type: str=None):
        """PurposePrediction - a model defined in OpenAPI

        :param id: The id of this PurposePrediction.
        :param probability: The probability of this PurposePrediction.
        :param result: The result of this PurposePrediction.
        :param sub_type: The sub_type of this PurposePrediction.
        :param type: The type of this PurposePrediction.
        """
        self.openapi_types = {
            'id': str,
            'probability': str,
            'result': PredictionResultType,
            'sub_type': str,
            'type': str
        }

        self.attribute_map = {
            'id': 'id',
            'probability': 'probability',
            'result': 'result',
            'sub_type': 'subType',
            'type': 'type'
        }

        self._id = id
        self._probability = probability
        self._result = result
        self._sub_type = sub_type
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PurposePrediction':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Purpose_Prediction of this PurposePrediction.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this PurposePrediction.

        item identifier

        :return: The id of this PurposePrediction.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PurposePrediction.

        item identifier

        :param id: The id of this PurposePrediction.
        :type id: str
        """

        self._id = id

    @property
    def probability(self):
        """Gets the probability of this PurposePrediction.

        probability of the forecast (between 0 and 1)

        :return: The probability of this PurposePrediction.
        :rtype: str
        """
        return self._probability

    @probability.setter
    def probability(self, probability):
        """Sets the probability of this PurposePrediction.

        probability of the forecast (between 0 and 1)

        :param probability: The probability of this PurposePrediction.
        :type probability: str
        """

        self._probability = probability

    @property
    def result(self):
        """Gets the result of this PurposePrediction.


        :return: The result of this PurposePrediction.
        :rtype: PredictionResultType
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this PurposePrediction.


        :param result: The result of this PurposePrediction.
        :type result: PredictionResultType
        """

        self._result = result

    @property
    def sub_type(self):
        """Gets the sub_type of this PurposePrediction.


        :return: The sub_type of this PurposePrediction.
        :rtype: str
        """
        return self._sub_type

    @sub_type.setter
    def sub_type(self, sub_type):
        """Sets the sub_type of this PurposePrediction.


        :param sub_type: The sub_type of this PurposePrediction.
        :type sub_type: str
        """

        self._sub_type = sub_type

    @property
    def type(self):
        """Gets the type of this PurposePrediction.

        the resource name (`prediction`)

        :return: The type of this PurposePrediction.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PurposePrediction.

        the resource name (`prediction`)

        :param type: The type of this PurposePrediction.
        :type type: str
        """

        self._type = type
