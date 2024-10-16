# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class CrashesGetCrashAttachmentLocation200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, uri: str=None):
        """CrashesGetCrashAttachmentLocation200Response - a model defined in OpenAPI

        :param uri: The uri of this CrashesGetCrashAttachmentLocation200Response.
        """
        self.openapi_types = {
            'uri': str
        }

        self.attribute_map = {
            'uri': 'uri'
        }

        self._uri = uri

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CrashesGetCrashAttachmentLocation200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The crashes_getCrashAttachmentLocation_200_response of this CrashesGetCrashAttachmentLocation200Response.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def uri(self):
        """Gets the uri of this CrashesGetCrashAttachmentLocation200Response.


        :return: The uri of this CrashesGetCrashAttachmentLocation200Response.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this CrashesGetCrashAttachmentLocation200Response.


        :param uri: The uri of this CrashesGetCrashAttachmentLocation200Response.
        :type uri: str
        """
        if uri is None:
            raise ValueError("Invalid value for `uri`, must not be `None`")

        self._uri = uri
