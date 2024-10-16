# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ClientInitialAccessCreatePresentation(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, count: int=None, expiration: int=None):
        """ClientInitialAccessCreatePresentation - a model defined in OpenAPI

        :param count: The count of this ClientInitialAccessCreatePresentation.
        :param expiration: The expiration of this ClientInitialAccessCreatePresentation.
        """
        self.openapi_types = {
            'count': int,
            'expiration': int
        }

        self.attribute_map = {
            'count': 'count',
            'expiration': 'expiration'
        }

        self._count = count
        self._expiration = expiration

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ClientInitialAccessCreatePresentation':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ClientInitialAccessCreatePresentation of this ClientInitialAccessCreatePresentation.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def count(self):
        """Gets the count of this ClientInitialAccessCreatePresentation.


        :return: The count of this ClientInitialAccessCreatePresentation.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ClientInitialAccessCreatePresentation.


        :param count: The count of this ClientInitialAccessCreatePresentation.
        :type count: int
        """

        self._count = count

    @property
    def expiration(self):
        """Gets the expiration of this ClientInitialAccessCreatePresentation.


        :return: The expiration of this ClientInitialAccessCreatePresentation.
        :rtype: int
        """
        return self._expiration

    @expiration.setter
    def expiration(self, expiration):
        """Sets the expiration of this ClientInitialAccessCreatePresentation.


        :param expiration: The expiration of this ClientInitialAccessCreatePresentation.
        :type expiration: int
        """

        self._expiration = expiration
