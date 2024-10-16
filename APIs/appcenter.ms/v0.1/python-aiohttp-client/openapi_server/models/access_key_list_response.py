# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.access_key_list_response_access_keys_inner import AccessKeyListResponseAccessKeysInner
from openapi_server import util


class AccessKeyListResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, access_keys: List[AccessKeyListResponseAccessKeysInner]=None):
        """AccessKeyListResponse - a model defined in OpenAPI

        :param access_keys: The access_keys of this AccessKeyListResponse.
        """
        self.openapi_types = {
            'access_keys': List[AccessKeyListResponseAccessKeysInner]
        }

        self.attribute_map = {
            'access_keys': 'accessKeys'
        }

        self._access_keys = access_keys

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AccessKeyListResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The AccessKeyListResponse of this AccessKeyListResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def access_keys(self):
        """Gets the access_keys of this AccessKeyListResponse.

        Array containing the list of existing AccessKeys

        :return: The access_keys of this AccessKeyListResponse.
        :rtype: List[AccessKeyListResponseAccessKeysInner]
        """
        return self._access_keys

    @access_keys.setter
    def access_keys(self, access_keys):
        """Sets the access_keys of this AccessKeyListResponse.

        Array containing the list of existing AccessKeys

        :param access_keys: The access_keys of this AccessKeyListResponse.
        :type access_keys: List[AccessKeyListResponseAccessKeysInner]
        """

        self._access_keys = access_keys
