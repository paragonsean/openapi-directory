# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.crash_groups_list200_response_crash_groups_inner import CrashGroupsList200ResponseCrashGroupsInner
from openapi_server import util


class CrashGroupsList200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, continuation_token: str=None, crash_groups: List[CrashGroupsList200ResponseCrashGroupsInner]=None, limited_result_set: bool=None):
        """CrashGroupsList200Response - a model defined in OpenAPI

        :param continuation_token: The continuation_token of this CrashGroupsList200Response.
        :param crash_groups: The crash_groups of this CrashGroupsList200Response.
        :param limited_result_set: The limited_result_set of this CrashGroupsList200Response.
        """
        self.openapi_types = {
            'continuation_token': str,
            'crash_groups': List[CrashGroupsList200ResponseCrashGroupsInner],
            'limited_result_set': bool
        }

        self.attribute_map = {
            'continuation_token': 'continuation_token',
            'crash_groups': 'crash_groups',
            'limited_result_set': 'limited_result_set'
        }

        self._continuation_token = continuation_token
        self._crash_groups = crash_groups
        self._limited_result_set = limited_result_set

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CrashGroupsList200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The crashGroups_list_200_response of this CrashGroupsList200Response.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def continuation_token(self):
        """Gets the continuation_token of this CrashGroupsList200Response.

        Cassandra request continuation token. The token is used for pagination.

        :return: The continuation_token of this CrashGroupsList200Response.
        :rtype: str
        """
        return self._continuation_token

    @continuation_token.setter
    def continuation_token(self, continuation_token):
        """Sets the continuation_token of this CrashGroupsList200Response.

        Cassandra request continuation token. The token is used for pagination.

        :param continuation_token: The continuation_token of this CrashGroupsList200Response.
        :type continuation_token: str
        """

        self._continuation_token = continuation_token

    @property
    def crash_groups(self):
        """Gets the crash_groups of this CrashGroupsList200Response.


        :return: The crash_groups of this CrashGroupsList200Response.
        :rtype: List[CrashGroupsList200ResponseCrashGroupsInner]
        """
        return self._crash_groups

    @crash_groups.setter
    def crash_groups(self, crash_groups):
        """Sets the crash_groups of this CrashGroupsList200Response.


        :param crash_groups: The crash_groups of this CrashGroupsList200Response.
        :type crash_groups: List[CrashGroupsList200ResponseCrashGroupsInner]
        """
        if crash_groups is None:
            raise ValueError("Invalid value for `crash_groups`, must not be `None`")

        self._crash_groups = crash_groups

    @property
    def limited_result_set(self):
        """Gets the limited_result_set of this CrashGroupsList200Response.


        :return: The limited_result_set of this CrashGroupsList200Response.
        :rtype: bool
        """
        return self._limited_result_set

    @limited_result_set.setter
    def limited_result_set(self, limited_result_set):
        """Sets the limited_result_set of this CrashGroupsList200Response.


        :param limited_result_set: The limited_result_set of this CrashGroupsList200Response.
        :type limited_result_set: bool
        """
        if limited_result_set is None:
            raise ValueError("Invalid value for `limited_result_set`, must not be `None`")

        self._limited_result_set = limited_result_set
