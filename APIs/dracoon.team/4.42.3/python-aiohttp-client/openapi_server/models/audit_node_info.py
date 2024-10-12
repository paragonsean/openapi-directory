# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class AuditNodeInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, count_children: int=None, node_id: int=None, node_is_encrypted: bool=None, node_name: str=None, node_parent_id: int=None, node_parent_path: str=None):
        """AuditNodeInfo - a model defined in OpenAPI

        :param count_children: The count_children of this AuditNodeInfo.
        :param node_id: The node_id of this AuditNodeInfo.
        :param node_is_encrypted: The node_is_encrypted of this AuditNodeInfo.
        :param node_name: The node_name of this AuditNodeInfo.
        :param node_parent_id: The node_parent_id of this AuditNodeInfo.
        :param node_parent_path: The node_parent_path of this AuditNodeInfo.
        """
        self.openapi_types = {
            'count_children': int,
            'node_id': int,
            'node_is_encrypted': bool,
            'node_name': str,
            'node_parent_id': int,
            'node_parent_path': str
        }

        self.attribute_map = {
            'count_children': 'countChildren',
            'node_id': 'nodeId',
            'node_is_encrypted': 'nodeIsEncrypted',
            'node_name': 'nodeName',
            'node_parent_id': 'nodeParentId',
            'node_parent_path': 'nodeParentPath'
        }

        self._count_children = count_children
        self._node_id = node_id
        self._node_is_encrypted = node_is_encrypted
        self._node_name = node_name
        self._node_parent_id = node_parent_id
        self._node_parent_path = node_parent_path

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AuditNodeInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The AuditNodeInfo of this AuditNodeInfo.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def count_children(self):
        """Gets the count_children of this AuditNodeInfo.

        Number of direct children  (no recursion; for rooms only)

        :return: The count_children of this AuditNodeInfo.
        :rtype: int
        """
        return self._count_children

    @count_children.setter
    def count_children(self, count_children):
        """Sets the count_children of this AuditNodeInfo.

        Number of direct children  (no recursion; for rooms only)

        :param count_children: The count_children of this AuditNodeInfo.
        :type count_children: int
        """

        self._count_children = count_children

    @property
    def node_id(self):
        """Gets the node_id of this AuditNodeInfo.

        Node ID

        :return: The node_id of this AuditNodeInfo.
        :rtype: int
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this AuditNodeInfo.

        Node ID

        :param node_id: The node_id of this AuditNodeInfo.
        :type node_id: int
        """
        if node_id is None:
            raise ValueError("Invalid value for `node_id`, must not be `None`")

        self._node_id = node_id

    @property
    def node_is_encrypted(self):
        """Gets the node_is_encrypted of this AuditNodeInfo.

        Encryption state

        :return: The node_is_encrypted of this AuditNodeInfo.
        :rtype: bool
        """
        return self._node_is_encrypted

    @node_is_encrypted.setter
    def node_is_encrypted(self, node_is_encrypted):
        """Sets the node_is_encrypted of this AuditNodeInfo.

        Encryption state

        :param node_is_encrypted: The node_is_encrypted of this AuditNodeInfo.
        :type node_is_encrypted: bool
        """

        self._node_is_encrypted = node_is_encrypted

    @property
    def node_name(self):
        """Gets the node_name of this AuditNodeInfo.

        Node name

        :return: The node_name of this AuditNodeInfo.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        """Sets the node_name of this AuditNodeInfo.

        Node name

        :param node_name: The node_name of this AuditNodeInfo.
        :type node_name: str
        """
        if node_name is None:
            raise ValueError("Invalid value for `node_name`, must not be `None`")

        self._node_name = node_name

    @property
    def node_parent_id(self):
        """Gets the node_parent_id of this AuditNodeInfo.

        Parent room ID

        :return: The node_parent_id of this AuditNodeInfo.
        :rtype: int
        """
        return self._node_parent_id

    @node_parent_id.setter
    def node_parent_id(self, node_parent_id):
        """Sets the node_parent_id of this AuditNodeInfo.

        Parent room ID

        :param node_parent_id: The node_parent_id of this AuditNodeInfo.
        :type node_parent_id: int
        """

        self._node_parent_id = node_parent_id

    @property
    def node_parent_path(self):
        """Gets the node_parent_path of this AuditNodeInfo.

        Parent node path  `/` if node is a root node (room)

        :return: The node_parent_path of this AuditNodeInfo.
        :rtype: str
        """
        return self._node_parent_path

    @node_parent_path.setter
    def node_parent_path(self, node_parent_path):
        """Sets the node_parent_path of this AuditNodeInfo.

        Parent node path  `/` if node is a root node (room)

        :param node_parent_path: The node_parent_path of this AuditNodeInfo.
        :type node_parent_path: str
        """
        if node_parent_path is None:
            raise ValueError("Invalid value for `node_parent_path`, must not be `None`")

        self._node_parent_path = node_parent_path
