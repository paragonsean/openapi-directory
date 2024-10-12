# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class FileSourceInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, share_id: str=None):
        """FileSourceInfo - a model defined in OpenAPI

        :param share_id: The share_id of this FileSourceInfo.
        """
        self.openapi_types = {
            'share_id': str
        }

        self.attribute_map = {
            'share_id': 'shareId'
        }

        self._share_id = share_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'FileSourceInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The FileSourceInfo of this FileSourceInfo.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def share_id(self):
        """Gets the share_id of this FileSourceInfo.

        File share ID.

        :return: The share_id of this FileSourceInfo.
        :rtype: str
        """
        return self._share_id

    @share_id.setter
    def share_id(self, share_id):
        """Sets the share_id of this FileSourceInfo.

        File share ID.

        :param share_id: The share_id of this FileSourceInfo.
        :type share_id: str
        """
        if share_id is None:
            raise ValueError("Invalid value for `share_id`, must not be `None`")

        self._share_id = share_id
