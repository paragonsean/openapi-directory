# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class PartnerInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, location: str=None, replication_role: str=None):
        """PartnerInfo - a model defined in OpenAPI

        :param id: The id of this PartnerInfo.
        :param location: The location of this PartnerInfo.
        :param replication_role: The replication_role of this PartnerInfo.
        """
        self.openapi_types = {
            'id': str,
            'location': str,
            'replication_role': str
        }

        self.attribute_map = {
            'id': 'id',
            'location': 'location',
            'replication_role': 'replicationRole'
        }

        self._id = id
        self._location = location
        self._replication_role = replication_role

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PartnerInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PartnerInfo of this PartnerInfo.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this PartnerInfo.

        Resource identifier of the partner server.

        :return: The id of this PartnerInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PartnerInfo.

        Resource identifier of the partner server.

        :param id: The id of this PartnerInfo.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def location(self):
        """Gets the location of this PartnerInfo.

        Geo location of the partner server.

        :return: The location of this PartnerInfo.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this PartnerInfo.

        Geo location of the partner server.

        :param location: The location of this PartnerInfo.
        :type location: str
        """

        self._location = location

    @property
    def replication_role(self):
        """Gets the replication_role of this PartnerInfo.

        Replication role of the partner server.

        :return: The replication_role of this PartnerInfo.
        :rtype: str
        """
        return self._replication_role

    @replication_role.setter
    def replication_role(self, replication_role):
        """Sets the replication_role of this PartnerInfo.

        Replication role of the partner server.

        :param replication_role: The replication_role of this PartnerInfo.
        :type replication_role: str
        """
        allowed_values = ["Primary", "Secondary"]  # noqa: E501
        if replication_role not in allowed_values:
            raise ValueError(
                "Invalid value for `replication_role` ({0}), must be one of {1}"
                .format(replication_role, allowed_values)
            )

        self._replication_role = replication_role
