# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class GetNetworkSmTrustedAccessConfigs200ResponseInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, access_end_at: datetime=None, access_start_at: datetime=None, id: str=None, name: str=None, scope: str=None, ssid_name: str=None, tags: List[str]=None, timebound_type: str=None):
        """GetNetworkSmTrustedAccessConfigs200ResponseInner - a model defined in OpenAPI

        :param access_end_at: The access_end_at of this GetNetworkSmTrustedAccessConfigs200ResponseInner.
        :param access_start_at: The access_start_at of this GetNetworkSmTrustedAccessConfigs200ResponseInner.
        :param id: The id of this GetNetworkSmTrustedAccessConfigs200ResponseInner.
        :param name: The name of this GetNetworkSmTrustedAccessConfigs200ResponseInner.
        :param scope: The scope of this GetNetworkSmTrustedAccessConfigs200ResponseInner.
        :param ssid_name: The ssid_name of this GetNetworkSmTrustedAccessConfigs200ResponseInner.
        :param tags: The tags of this GetNetworkSmTrustedAccessConfigs200ResponseInner.
        :param timebound_type: The timebound_type of this GetNetworkSmTrustedAccessConfigs200ResponseInner.
        """
        self.openapi_types = {
            'access_end_at': datetime,
            'access_start_at': datetime,
            'id': str,
            'name': str,
            'scope': str,
            'ssid_name': str,
            'tags': List[str],
            'timebound_type': str
        }

        self.attribute_map = {
            'access_end_at': 'accessEndAt',
            'access_start_at': 'accessStartAt',
            'id': 'id',
            'name': 'name',
            'scope': 'scope',
            'ssid_name': 'ssidName',
            'tags': 'tags',
            'timebound_type': 'timeboundType'
        }

        self._access_end_at = access_end_at
        self._access_start_at = access_start_at
        self._id = id
        self._name = name
        self._scope = scope
        self._ssid_name = ssid_name
        self._tags = tags
        self._timebound_type = timebound_type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetNetworkSmTrustedAccessConfigs200ResponseInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The getNetworkSmTrustedAccessConfigs_200_response_inner of this GetNetworkSmTrustedAccessConfigs200ResponseInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def access_end_at(self):
        """Gets the access_end_at of this GetNetworkSmTrustedAccessConfigs200ResponseInner.

        time that access ends

        :return: The access_end_at of this GetNetworkSmTrustedAccessConfigs200ResponseInner.
        :rtype: datetime
        """
        return self._access_end_at

    @access_end_at.setter
    def access_end_at(self, access_end_at):
        """Sets the access_end_at of this GetNetworkSmTrustedAccessConfigs200ResponseInner.

        time that access ends

        :param access_end_at: The access_end_at of this GetNetworkSmTrustedAccessConfigs200ResponseInner.
        :type access_end_at: datetime
        """

        self._access_end_at = access_end_at

    @property
    def access_start_at(self):
        """Gets the access_start_at of this GetNetworkSmTrustedAccessConfigs200ResponseInner.

        time that access starts

        :return: The access_start_at of this GetNetworkSmTrustedAccessConfigs200ResponseInner.
        :rtype: datetime
        """
        return self._access_start_at

    @access_start_at.setter
    def access_start_at(self, access_start_at):
        """Sets the access_start_at of this GetNetworkSmTrustedAccessConfigs200ResponseInner.

        time that access starts

        :param access_start_at: The access_start_at of this GetNetworkSmTrustedAccessConfigs200ResponseInner.
        :type access_start_at: datetime
        """

        self._access_start_at = access_start_at

    @property
    def id(self):
        """Gets the id of this GetNetworkSmTrustedAccessConfigs200ResponseInner.

        device ID

        :return: The id of this GetNetworkSmTrustedAccessConfigs200ResponseInner.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetNetworkSmTrustedAccessConfigs200ResponseInner.

        device ID

        :param id: The id of this GetNetworkSmTrustedAccessConfigs200ResponseInner.
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this GetNetworkSmTrustedAccessConfigs200ResponseInner.

        device name

        :return: The name of this GetNetworkSmTrustedAccessConfigs200ResponseInner.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetNetworkSmTrustedAccessConfigs200ResponseInner.

        device name

        :param name: The name of this GetNetworkSmTrustedAccessConfigs200ResponseInner.
        :type name: str
        """

        self._name = name

    @property
    def scope(self):
        """Gets the scope of this GetNetworkSmTrustedAccessConfigs200ResponseInner.

        scope

        :return: The scope of this GetNetworkSmTrustedAccessConfigs200ResponseInner.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this GetNetworkSmTrustedAccessConfigs200ResponseInner.

        scope

        :param scope: The scope of this GetNetworkSmTrustedAccessConfigs200ResponseInner.
        :type scope: str
        """

        self._scope = scope

    @property
    def ssid_name(self):
        """Gets the ssid_name of this GetNetworkSmTrustedAccessConfigs200ResponseInner.

        SSID name

        :return: The ssid_name of this GetNetworkSmTrustedAccessConfigs200ResponseInner.
        :rtype: str
        """
        return self._ssid_name

    @ssid_name.setter
    def ssid_name(self, ssid_name):
        """Sets the ssid_name of this GetNetworkSmTrustedAccessConfigs200ResponseInner.

        SSID name

        :param ssid_name: The ssid_name of this GetNetworkSmTrustedAccessConfigs200ResponseInner.
        :type ssid_name: str
        """

        self._ssid_name = ssid_name

    @property
    def tags(self):
        """Gets the tags of this GetNetworkSmTrustedAccessConfigs200ResponseInner.

        device tags

        :return: The tags of this GetNetworkSmTrustedAccessConfigs200ResponseInner.
        :rtype: List[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this GetNetworkSmTrustedAccessConfigs200ResponseInner.

        device tags

        :param tags: The tags of this GetNetworkSmTrustedAccessConfigs200ResponseInner.
        :type tags: List[str]
        """

        self._tags = tags

    @property
    def timebound_type(self):
        """Gets the timebound_type of this GetNetworkSmTrustedAccessConfigs200ResponseInner.

        type of access period, either a static range or a dynamic period

        :return: The timebound_type of this GetNetworkSmTrustedAccessConfigs200ResponseInner.
        :rtype: str
        """
        return self._timebound_type

    @timebound_type.setter
    def timebound_type(self, timebound_type):
        """Sets the timebound_type of this GetNetworkSmTrustedAccessConfigs200ResponseInner.

        type of access period, either a static range or a dynamic period

        :param timebound_type: The timebound_type of this GetNetworkSmTrustedAccessConfigs200ResponseInner.
        :type timebound_type: str
        """
        allowed_values = ["dynamic", "static"]  # noqa: E501
        if timebound_type not in allowed_values:
            raise ValueError(
                "Invalid value for `timebound_type` ({0}), must be one of {1}"
                .format(timebound_type, allowed_values)
            )

        self._timebound_type = timebound_type
