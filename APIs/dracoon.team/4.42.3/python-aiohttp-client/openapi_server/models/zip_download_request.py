# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ZipDownloadRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, node_ids: List[int]=None):
        """ZipDownloadRequest - a model defined in OpenAPI

        :param node_ids: The node_ids of this ZipDownloadRequest.
        """
        self.openapi_types = {
            'node_ids': List[int]
        }

        self.attribute_map = {
            'node_ids': 'nodeIds'
        }

        self._node_ids = node_ids

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ZipDownloadRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ZipDownloadRequest of this ZipDownloadRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def node_ids(self):
        """Gets the node_ids of this ZipDownloadRequest.

        List of node IDs

        :return: The node_ids of this ZipDownloadRequest.
        :rtype: List[int]
        """
        return self._node_ids

    @node_ids.setter
    def node_ids(self, node_ids):
        """Sets the node_ids of this ZipDownloadRequest.

        List of node IDs

        :param node_ids: The node_ids of this ZipDownloadRequest.
        :type node_ids: List[int]
        """
        if node_ids is None:
            raise ValueError("Invalid value for `node_ids`, must not be `None`")

        self._node_ids = node_ids
