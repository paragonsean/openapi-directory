# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.chore import Chore
from openapi_server import util


class Chorelist(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, chore: List[Chore]=None, success: int=None):
        """Chorelist - a model defined in OpenAPI

        :param chore: The chore of this Chorelist.
        :param success: The success of this Chorelist.
        """
        self.openapi_types = {
            'chore': List[Chore],
            'success': int
        }

        self.attribute_map = {
            'chore': 'chore',
            'success': 'success'
        }

        self._chore = chore
        self._success = success

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Chorelist':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The chorelist of this Chorelist.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def chore(self):
        """Gets the chore of this Chorelist.


        :return: The chore of this Chorelist.
        :rtype: List[Chore]
        """
        return self._chore

    @chore.setter
    def chore(self, chore):
        """Sets the chore of this Chorelist.


        :param chore: The chore of this Chorelist.
        :type chore: List[Chore]
        """

        self._chore = chore

    @property
    def success(self):
        """Gets the success of this Chorelist.


        :return: The success of this Chorelist.
        :rtype: int
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this Chorelist.


        :param success: The success of this Chorelist.
        :type success: int
        """

        self._success = success
