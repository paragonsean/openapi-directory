# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class PurgeParameters(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, content_paths: List[str]=None):
        """PurgeParameters - a model defined in OpenAPI

        :param content_paths: The content_paths of this PurgeParameters.
        """
        self.openapi_types = {
            'content_paths': List[str]
        }

        self.attribute_map = {
            'content_paths': 'contentPaths'
        }

        self._content_paths = content_paths

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PurgeParameters':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PurgeParameters of this PurgeParameters.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def content_paths(self):
        """Gets the content_paths of this PurgeParameters.

        The path to the content to be purged. Can describe a file path or a wild card directory.

        :return: The content_paths of this PurgeParameters.
        :rtype: List[str]
        """
        return self._content_paths

    @content_paths.setter
    def content_paths(self, content_paths):
        """Sets the content_paths of this PurgeParameters.

        The path to the content to be purged. Can describe a file path or a wild card directory.

        :param content_paths: The content_paths of this PurgeParameters.
        :type content_paths: List[str]
        """
        if content_paths is None:
            raise ValueError("Invalid value for `content_paths`, must not be `None`")

        self._content_paths = content_paths
