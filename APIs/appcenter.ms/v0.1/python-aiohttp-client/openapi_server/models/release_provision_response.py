# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ReleaseProvisionResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, status_url: str=None):
        """ReleaseProvisionResponse - a model defined in OpenAPI

        :param status_url: The status_url of this ReleaseProvisionResponse.
        """
        self.openapi_types = {
            'status_url': str
        }

        self.attribute_map = {
            'status_url': 'status_url'
        }

        self._status_url = status_url

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ReleaseProvisionResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ReleaseProvisionResponse of this ReleaseProvisionResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def status_url(self):
        """Gets the status_url of this ReleaseProvisionResponse.

        The url to check provisioning status.

        :return: The status_url of this ReleaseProvisionResponse.
        :rtype: str
        """
        return self._status_url

    @status_url.setter
    def status_url(self, status_url):
        """Sets the status_url of this ReleaseProvisionResponse.

        The url to check provisioning status.

        :param status_url: The status_url of this ReleaseProvisionResponse.
        :type status_url: str
        """

        self._status_url = status_url
