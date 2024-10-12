# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.version_types_with_id_version_types_version_type_inner import VersionTypesWithIdVersionTypesVersionTypeInner
from openapi_server import util


class VersionTypesWithIdVersionTypes(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, version_type: List[VersionTypesWithIdVersionTypesVersionTypeInner]=None):
        """VersionTypesWithIdVersionTypes - a model defined in OpenAPI

        :param version_type: The version_type of this VersionTypesWithIdVersionTypes.
        """
        self.openapi_types = {
            'version_type': List[VersionTypesWithIdVersionTypesVersionTypeInner]
        }

        self.attribute_map = {
            'version_type': 'version_type'
        }

        self._version_type = version_type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'VersionTypesWithIdVersionTypes':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The version_types_with_id_version_types of this VersionTypesWithIdVersionTypes.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def version_type(self):
        """Gets the version_type of this VersionTypesWithIdVersionTypes.


        :return: The version_type of this VersionTypesWithIdVersionTypes.
        :rtype: List[VersionTypesWithIdVersionTypesVersionTypeInner]
        """
        return self._version_type

    @version_type.setter
    def version_type(self, version_type):
        """Sets the version_type of this VersionTypesWithIdVersionTypes.


        :param version_type: The version_type of this VersionTypesWithIdVersionTypes.
        :type version_type: List[VersionTypesWithIdVersionTypesVersionTypeInner]
        """
        if version_type is None:
            raise ValueError("Invalid value for `version_type`, must not be `None`")
        if version_type is not None and len(version_type) < 1:
            raise ValueError("Invalid value for `version_type`, number of items must be greater than or equal to `1`")

        self._version_type = version_type
