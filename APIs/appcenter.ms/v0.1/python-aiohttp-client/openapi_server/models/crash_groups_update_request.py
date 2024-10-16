# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class CrashGroupsUpdateRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, annotation: str=None, status: str=None):
        """CrashGroupsUpdateRequest - a model defined in OpenAPI

        :param annotation: The annotation of this CrashGroupsUpdateRequest.
        :param status: The status of this CrashGroupsUpdateRequest.
        """
        self.openapi_types = {
            'annotation': str,
            'status': str
        }

        self.attribute_map = {
            'annotation': 'annotation',
            'status': 'status'
        }

        self._annotation = annotation
        self._status = status

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CrashGroupsUpdateRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The crashGroups_update_request of this CrashGroupsUpdateRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def annotation(self):
        """Gets the annotation of this CrashGroupsUpdateRequest.


        :return: The annotation of this CrashGroupsUpdateRequest.
        :rtype: str
        """
        return self._annotation

    @annotation.setter
    def annotation(self, annotation):
        """Sets the annotation of this CrashGroupsUpdateRequest.


        :param annotation: The annotation of this CrashGroupsUpdateRequest.
        :type annotation: str
        """

        self._annotation = annotation

    @property
    def status(self):
        """Gets the status of this CrashGroupsUpdateRequest.


        :return: The status of this CrashGroupsUpdateRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CrashGroupsUpdateRequest.


        :param status: The status of this CrashGroupsUpdateRequest.
        :type status: str
        """
        allowed_values = ["open", "closed", "ignored"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status
