# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.availability_mixin_availability_inner_version_types import AvailabilityMixinAvailabilityInnerVersionTypes
from openapi_server import util


class AvailabilityMixinAvailabilityInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, status: str=None, version_types: AvailabilityMixinAvailabilityInnerVersionTypes=None):
        """AvailabilityMixinAvailabilityInner - a model defined in OpenAPI

        :param status: The status of this AvailabilityMixinAvailabilityInner.
        :param version_types: The version_types of this AvailabilityMixinAvailabilityInner.
        """
        self.openapi_types = {
            'status': str,
            'version_types': AvailabilityMixinAvailabilityInnerVersionTypes
        }

        self.attribute_map = {
            'status': 'status',
            'version_types': 'version_types'
        }

        self._status = status
        self._version_types = version_types

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AvailabilityMixinAvailabilityInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The availability_mixin_availability_inner of this AvailabilityMixinAvailabilityInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def status(self):
        """Gets the status of this AvailabilityMixinAvailabilityInner.


        :return: The status of this AvailabilityMixinAvailabilityInner.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AvailabilityMixinAvailabilityInner.


        :param status: The status of this AvailabilityMixinAvailabilityInner.
        :type status: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")

        self._status = status

    @property
    def version_types(self):
        """Gets the version_types of this AvailabilityMixinAvailabilityInner.


        :return: The version_types of this AvailabilityMixinAvailabilityInner.
        :rtype: AvailabilityMixinAvailabilityInnerVersionTypes
        """
        return self._version_types

    @version_types.setter
    def version_types(self, version_types):
        """Sets the version_types of this AvailabilityMixinAvailabilityInner.


        :param version_types: The version_types of this AvailabilityMixinAvailabilityInner.
        :type version_types: AvailabilityMixinAvailabilityInnerVersionTypes
        """
        if version_types is None:
            raise ValueError("Invalid value for `version_types`, must not be `None`")

        self._version_types = version_types
