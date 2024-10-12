# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Healthcheck400Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, status: str=None):
        """Healthcheck400Response - a model defined in OpenAPI

        :param status: The status of this Healthcheck400Response.
        """
        self.openapi_types = {
            'status': str
        }

        self.attribute_map = {
            'status': 'status'
        }

        self._status = status

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Healthcheck400Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The healthcheck_400_response of this Healthcheck400Response.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def status(self):
        """Gets the status of this Healthcheck400Response.

        The status of this API (`up` or `down`).

        :return: The status of this Healthcheck400Response.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Healthcheck400Response.

        The status of this API (`up` or `down`).

        :param status: The status of this Healthcheck400Response.
        :type status: str
        """

        self._status = status
