# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.node_permissions import NodePermissions
from openapi_server.models.user_info import UserInfo
from openapi_server import util


class RoomData(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, children: List[RoomData]=None, cnt_download_shares: int=None, cnt_upload_shares: int=None, created_at: datetime=None, created_by: UserInfo=None, has_recycle_bin: bool=None, id: int=None, is_encrypted: bool=None, is_favorite: bool=None, is_granted: bool=None, name: str=None, parent_id: int=None, permissions: NodePermissions=None, quota: int=None, recycle_bin_retention_period: int=None, size: int=None, type: str=None, updated_at: datetime=None, updated_by: UserInfo=None):
        """RoomData - a model defined in OpenAPI

        :param children: The children of this RoomData.
        :param cnt_download_shares: The cnt_download_shares of this RoomData.
        :param cnt_upload_shares: The cnt_upload_shares of this RoomData.
        :param created_at: The created_at of this RoomData.
        :param created_by: The created_by of this RoomData.
        :param has_recycle_bin: The has_recycle_bin of this RoomData.
        :param id: The id of this RoomData.
        :param is_encrypted: The is_encrypted of this RoomData.
        :param is_favorite: The is_favorite of this RoomData.
        :param is_granted: The is_granted of this RoomData.
        :param name: The name of this RoomData.
        :param parent_id: The parent_id of this RoomData.
        :param permissions: The permissions of this RoomData.
        :param quota: The quota of this RoomData.
        :param recycle_bin_retention_period: The recycle_bin_retention_period of this RoomData.
        :param size: The size of this RoomData.
        :param type: The type of this RoomData.
        :param updated_at: The updated_at of this RoomData.
        :param updated_by: The updated_by of this RoomData.
        """
        self.openapi_types = {
            'children': List[RoomData],
            'cnt_download_shares': int,
            'cnt_upload_shares': int,
            'created_at': datetime,
            'created_by': UserInfo,
            'has_recycle_bin': bool,
            'id': int,
            'is_encrypted': bool,
            'is_favorite': bool,
            'is_granted': bool,
            'name': str,
            'parent_id': int,
            'permissions': NodePermissions,
            'quota': int,
            'recycle_bin_retention_period': int,
            'size': int,
            'type': str,
            'updated_at': datetime,
            'updated_by': UserInfo
        }

        self.attribute_map = {
            'children': 'children',
            'cnt_download_shares': 'cntDownloadShares',
            'cnt_upload_shares': 'cntUploadShares',
            'created_at': 'createdAt',
            'created_by': 'createdBy',
            'has_recycle_bin': 'hasRecycleBin',
            'id': 'id',
            'is_encrypted': 'isEncrypted',
            'is_favorite': 'isFavorite',
            'is_granted': 'isGranted',
            'name': 'name',
            'parent_id': 'parentId',
            'permissions': 'permissions',
            'quota': 'quota',
            'recycle_bin_retention_period': 'recycleBinRetentionPeriod',
            'size': 'size',
            'type': 'type',
            'updated_at': 'updatedAt',
            'updated_by': 'updatedBy'
        }

        self._children = children
        self._cnt_download_shares = cnt_download_shares
        self._cnt_upload_shares = cnt_upload_shares
        self._created_at = created_at
        self._created_by = created_by
        self._has_recycle_bin = has_recycle_bin
        self._id = id
        self._is_encrypted = is_encrypted
        self._is_favorite = is_favorite
        self._is_granted = is_granted
        self._name = name
        self._parent_id = parent_id
        self._permissions = permissions
        self._quota = quota
        self._recycle_bin_retention_period = recycle_bin_retention_period
        self._size = size
        self._type = type
        self._updated_at = updated_at
        self._updated_by = updated_by

    @classmethod
    def from_dict(cls, dikt: dict) -> 'RoomData':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The RoomData of this RoomData.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def children(self):
        """Gets the children of this RoomData.

        &#128679; Deprecated since v4.10.0  List of rooms, where this room is a parent (if exist)

        :return: The children of this RoomData.
        :rtype: List[RoomData]
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this RoomData.

        &#128679; Deprecated since v4.10.0  List of rooms, where this room is a parent (if exist)

        :param children: The children of this RoomData.
        :type children: List[RoomData]
        """

        self._children = children

    @property
    def cnt_download_shares(self):
        """Gets the cnt_download_shares of this RoomData.

        Returns the number of Download Shares of this node.

        :return: The cnt_download_shares of this RoomData.
        :rtype: int
        """
        return self._cnt_download_shares

    @cnt_download_shares.setter
    def cnt_download_shares(self, cnt_download_shares):
        """Sets the cnt_download_shares of this RoomData.

        Returns the number of Download Shares of this node.

        :param cnt_download_shares: The cnt_download_shares of this RoomData.
        :type cnt_download_shares: int
        """

        self._cnt_download_shares = cnt_download_shares

    @property
    def cnt_upload_shares(self):
        """Gets the cnt_upload_shares of this RoomData.

        Returns the number of Upload Shares of this node.

        :return: The cnt_upload_shares of this RoomData.
        :rtype: int
        """
        return self._cnt_upload_shares

    @cnt_upload_shares.setter
    def cnt_upload_shares(self, cnt_upload_shares):
        """Sets the cnt_upload_shares of this RoomData.

        Returns the number of Upload Shares of this node.

        :param cnt_upload_shares: The cnt_upload_shares of this RoomData.
        :type cnt_upload_shares: int
        """

        self._cnt_upload_shares = cnt_upload_shares

    @property
    def created_at(self):
        """Gets the created_at of this RoomData.

        Expiration date

        :return: The created_at of this RoomData.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this RoomData.

        Expiration date

        :param created_at: The created_at of this RoomData.
        :type created_at: datetime
        """

        self._created_at = created_at

    @property
    def created_by(self):
        """Gets the created_by of this RoomData.


        :return: The created_by of this RoomData.
        :rtype: UserInfo
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this RoomData.


        :param created_by: The created_by of this RoomData.
        :type created_by: UserInfo
        """

        self._created_by = created_by

    @property
    def has_recycle_bin(self):
        """Gets the has_recycle_bin of this RoomData.

        &#128679; Deprecated since v4.10.0  Is recycle bin active (for rooms only)  Recycle bin is always on (disabling is not possible).

        :return: The has_recycle_bin of this RoomData.
        :rtype: bool
        """
        return self._has_recycle_bin

    @has_recycle_bin.setter
    def has_recycle_bin(self, has_recycle_bin):
        """Sets the has_recycle_bin of this RoomData.

        &#128679; Deprecated since v4.10.0  Is recycle bin active (for rooms only)  Recycle bin is always on (disabling is not possible).

        :param has_recycle_bin: The has_recycle_bin of this RoomData.
        :type has_recycle_bin: bool
        """
        if has_recycle_bin is None:
            raise ValueError("Invalid value for `has_recycle_bin`, must not be `None`")

        self._has_recycle_bin = has_recycle_bin

    @property
    def id(self):
        """Gets the id of this RoomData.

        Room ID

        :return: The id of this RoomData.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RoomData.

        Room ID

        :param id: The id of this RoomData.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def is_encrypted(self):
        """Gets the is_encrypted of this RoomData.

        Encryption state

        :return: The is_encrypted of this RoomData.
        :rtype: bool
        """
        return self._is_encrypted

    @is_encrypted.setter
    def is_encrypted(self, is_encrypted):
        """Sets the is_encrypted of this RoomData.

        Encryption state

        :param is_encrypted: The is_encrypted of this RoomData.
        :type is_encrypted: bool
        """
        if is_encrypted is None:
            raise ValueError("Invalid value for `is_encrypted`, must not be `None`")

        self._is_encrypted = is_encrypted

    @property
    def is_favorite(self):
        """Gets the is_favorite of this RoomData.

        Node is marked as favorite (for rooms / folders only)

        :return: The is_favorite of this RoomData.
        :rtype: bool
        """
        return self._is_favorite

    @is_favorite.setter
    def is_favorite(self, is_favorite):
        """Sets the is_favorite of this RoomData.

        Node is marked as favorite (for rooms / folders only)

        :param is_favorite: The is_favorite of this RoomData.
        :type is_favorite: bool
        """

        self._is_favorite = is_favorite

    @property
    def is_granted(self):
        """Gets the is_granted of this RoomData.

        Is user granted room permissions

        :return: The is_granted of this RoomData.
        :rtype: bool
        """
        return self._is_granted

    @is_granted.setter
    def is_granted(self, is_granted):
        """Sets the is_granted of this RoomData.

        Is user granted room permissions

        :param is_granted: The is_granted of this RoomData.
        :type is_granted: bool
        """
        if is_granted is None:
            raise ValueError("Invalid value for `is_granted`, must not be `None`")

        self._is_granted = is_granted

    @property
    def name(self):
        """Gets the name of this RoomData.

        Name

        :return: The name of this RoomData.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RoomData.

        Name

        :param name: The name of this RoomData.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def parent_id(self):
        """Gets the parent_id of this RoomData.

        Parent node ID (room or folder)

        :return: The parent_id of this RoomData.
        :rtype: int
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this RoomData.

        Parent node ID (room or folder)

        :param parent_id: The parent_id of this RoomData.
        :type parent_id: int
        """

        self._parent_id = parent_id

    @property
    def permissions(self):
        """Gets the permissions of this RoomData.


        :return: The permissions of this RoomData.
        :rtype: NodePermissions
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this RoomData.


        :param permissions: The permissions of this RoomData.
        :type permissions: NodePermissions
        """

        self._permissions = permissions

    @property
    def quota(self):
        """Gets the quota of this RoomData.

        Quota in byte

        :return: The quota of this RoomData.
        :rtype: int
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        """Sets the quota of this RoomData.

        Quota in byte

        :param quota: The quota of this RoomData.
        :type quota: int
        """

        self._quota = quota

    @property
    def recycle_bin_retention_period(self):
        """Gets the recycle_bin_retention_period of this RoomData.

        Retention period for deleted nodes in days

        :return: The recycle_bin_retention_period of this RoomData.
        :rtype: int
        """
        return self._recycle_bin_retention_period

    @recycle_bin_retention_period.setter
    def recycle_bin_retention_period(self, recycle_bin_retention_period):
        """Sets the recycle_bin_retention_period of this RoomData.

        Retention period for deleted nodes in days

        :param recycle_bin_retention_period: The recycle_bin_retention_period of this RoomData.
        :type recycle_bin_retention_period: int
        """
        if recycle_bin_retention_period is None:
            raise ValueError("Invalid value for `recycle_bin_retention_period`, must not be `None`")
        if recycle_bin_retention_period is not None and recycle_bin_retention_period > 9999:
            raise ValueError("Invalid value for `recycle_bin_retention_period`, must be a value less than or equal to `9999`")
        if recycle_bin_retention_period is not None and recycle_bin_retention_period < 0:
            raise ValueError("Invalid value for `recycle_bin_retention_period`, must be a value greater than or equal to `0`")

        self._recycle_bin_retention_period = recycle_bin_retention_period

    @property
    def size(self):
        """Gets the size of this RoomData.

        Room size

        :return: The size of this RoomData.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this RoomData.

        Room size

        :param size: The size of this RoomData.
        :type size: int
        """

        self._size = size

    @property
    def type(self):
        """Gets the type of this RoomData.

        Node type

        :return: The type of this RoomData.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RoomData.

        Node type

        :param type: The type of this RoomData.
        :type type: str
        """
        allowed_values = ["room"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def updated_at(self):
        """Gets the updated_at of this RoomData.

        Modification date

        :return: The updated_at of this RoomData.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this RoomData.

        Modification date

        :param updated_at: The updated_at of this RoomData.
        :type updated_at: datetime
        """

        self._updated_at = updated_at

    @property
    def updated_by(self):
        """Gets the updated_by of this RoomData.


        :return: The updated_by of this RoomData.
        :rtype: UserInfo
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this RoomData.


        :param updated_by: The updated_by of this RoomData.
        :type updated_by: UserInfo
        """

        self._updated_by = updated_by
