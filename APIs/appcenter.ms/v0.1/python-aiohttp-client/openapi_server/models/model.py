# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Model(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, count: int=None, model_name: str=None, previous_count: int=None):
        """Model - a model defined in OpenAPI

        :param count: The count of this Model.
        :param model_name: The model_name of this Model.
        :param previous_count: The previous_count of this Model.
        """
        self.openapi_types = {
            'count': int,
            'model_name': str,
            'previous_count': int
        }

        self.attribute_map = {
            'count': 'count',
            'model_name': 'model_name',
            'previous_count': 'previous_count'
        }

        self._count = count
        self._model_name = model_name
        self._previous_count = previous_count

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Model':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Model of this Model.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def count(self):
        """Gets the count of this Model.

        Count current of model.

        :return: The count of this Model.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this Model.

        Count current of model.

        :param count: The count of this Model.
        :type count: int
        """

        self._count = count

    @property
    def model_name(self):
        """Gets the model_name of this Model.

        Model's name.

        :return: The model_name of this Model.
        :rtype: str
        """
        return self._model_name

    @model_name.setter
    def model_name(self, model_name):
        """Sets the model_name of this Model.

        Model's name.

        :param model_name: The model_name of this Model.
        :type model_name: str
        """

        self._model_name = model_name

    @property
    def previous_count(self):
        """Gets the previous_count of this Model.

        Count of previous model.

        :return: The previous_count of this Model.
        :rtype: int
        """
        return self._previous_count

    @previous_count.setter
    def previous_count(self, previous_count):
        """Sets the previous_count of this Model.

        Count of previous model.

        :param previous_count: The previous_count of this Model.
        :type previous_count: int
        """

        self._previous_count = previous_count
