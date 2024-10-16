# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class BuildsUpdateRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, status: str=None):
        """BuildsUpdateRequest - a model defined in OpenAPI

        :param status: The status of this BuildsUpdateRequest.
        """
        self.openapi_types = {
            'status': str
        }

        self.attribute_map = {
            'status': 'status'
        }

        self._status = status

    @classmethod
    def from_dict(cls, dikt: dict) -> 'BuildsUpdateRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The builds_update_request of this BuildsUpdateRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def status(self):
        """Gets the status of this BuildsUpdateRequest.

        The build status; used to cancel builds

        :return: The status of this BuildsUpdateRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BuildsUpdateRequest.

        The build status; used to cancel builds

        :param status: The status of this BuildsUpdateRequest.
        :type status: str
        """
        allowed_values = ["cancelling"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status
