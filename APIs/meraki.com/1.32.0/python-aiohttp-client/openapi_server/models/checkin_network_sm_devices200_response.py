# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class CheckinNetworkSmDevices200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, ids: List[str]=None):
        """CheckinNetworkSmDevices200Response - a model defined in OpenAPI

        :param ids: The ids of this CheckinNetworkSmDevices200Response.
        """
        self.openapi_types = {
            'ids': List[str]
        }

        self.attribute_map = {
            'ids': 'ids'
        }

        self._ids = ids

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CheckinNetworkSmDevices200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The checkinNetworkSmDevices_200_response of this CheckinNetworkSmDevices200Response.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ids(self):
        """Gets the ids of this CheckinNetworkSmDevices200Response.

        The Meraki Ids of the set of devices.

        :return: The ids of this CheckinNetworkSmDevices200Response.
        :rtype: List[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """Sets the ids of this CheckinNetworkSmDevices200Response.

        The Meraki Ids of the set of devices.

        :param ids: The ids of this CheckinNetworkSmDevices200Response.
        :type ids: List[str]
        """

        self._ids = ids
