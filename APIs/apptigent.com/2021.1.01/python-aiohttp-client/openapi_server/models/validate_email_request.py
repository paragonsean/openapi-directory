# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ValidateEmailRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, source: str=None):
        """ValidateEmailRequest - a model defined in OpenAPI

        :param source: The source of this ValidateEmailRequest.
        """
        self.openapi_types = {
            'source': str
        }

        self.attribute_map = {
            'source': 'source'
        }

        self._source = source

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ValidateEmailRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ValidateEmail_request of this ValidateEmailRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def source(self):
        """Gets the source of this ValidateEmailRequest.

        String variable or text value

        :return: The source of this ValidateEmailRequest.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this ValidateEmailRequest.

        String variable or text value

        :param source: The source of this ValidateEmailRequest.
        :type source: str
        """
        if source is None:
            raise ValueError("Invalid value for `source`, must not be `None`")

        self._source = source
