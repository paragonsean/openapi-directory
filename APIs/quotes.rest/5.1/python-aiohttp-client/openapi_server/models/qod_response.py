# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.qod_response_contents import QODResponseContents
from openapi_server import util


class QODResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, contents: QODResponseContents=None, success: str=None):
        """QODResponse - a model defined in OpenAPI

        :param contents: The contents of this QODResponse.
        :param success: The success of this QODResponse.
        """
        self.openapi_types = {
            'contents': QODResponseContents,
            'success': str
        }

        self.attribute_map = {
            'contents': 'contents',
            'success': 'success'
        }

        self._contents = contents
        self._success = success

    @classmethod
    def from_dict(cls, dikt: dict) -> 'QODResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The QODResponse of this QODResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def contents(self):
        """Gets the contents of this QODResponse.


        :return: The contents of this QODResponse.
        :rtype: QODResponseContents
        """
        return self._contents

    @contents.setter
    def contents(self, contents):
        """Sets the contents of this QODResponse.


        :param contents: The contents of this QODResponse.
        :type contents: QODResponseContents
        """

        self._contents = contents

    @property
    def success(self):
        """Gets the success of this QODResponse.

        Metadata about this successful call

        :return: The success of this QODResponse.
        :rtype: str
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this QODResponse.

        Metadata about this successful call

        :param success: The success of this QODResponse.
        :type success: str
        """

        self._success = success
