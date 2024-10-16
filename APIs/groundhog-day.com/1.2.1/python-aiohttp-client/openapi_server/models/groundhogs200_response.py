# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.groundhog import Groundhog
from openapi_server import util


class Groundhogs200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, groundhogs: List[Groundhog]=None):
        """Groundhogs200Response - a model defined in OpenAPI

        :param groundhogs: The groundhogs of this Groundhogs200Response.
        """
        self.openapi_types = {
            'groundhogs': List[Groundhog]
        }

        self.attribute_map = {
            'groundhogs': 'groundhogs'
        }

        self._groundhogs = groundhogs

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Groundhogs200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The groundhogs_200_response of this Groundhogs200Response.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def groundhogs(self):
        """Gets the groundhogs of this Groundhogs200Response.


        :return: The groundhogs of this Groundhogs200Response.
        :rtype: List[Groundhog]
        """
        return self._groundhogs

    @groundhogs.setter
    def groundhogs(self, groundhogs):
        """Sets the groundhogs of this Groundhogs200Response.


        :param groundhogs: The groundhogs of this Groundhogs200Response.
        :type groundhogs: List[Groundhog]
        """

        self._groundhogs = groundhogs
