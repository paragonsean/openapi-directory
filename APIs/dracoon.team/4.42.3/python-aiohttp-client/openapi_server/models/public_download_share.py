# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.file_key import FileKey
from openapi_server.models.private_key_container import PrivateKeyContainer
from openapi_server import util


class PublicDownloadShare(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, created_at: datetime=None, creator_name: str=None, creator_username: str=None, expire_at: datetime=None, file_key: FileKey=None, file_name: str=None, has_download_limit: bool=None, is_encrypted: bool=None, is_protected: bool=None, limit_reached: bool=None, media_type: str=None, name: str=None, notes: str=None, private_key_container: PrivateKeyContainer=None, size: int=None):
        """PublicDownloadShare - a model defined in OpenAPI

        :param created_at: The created_at of this PublicDownloadShare.
        :param creator_name: The creator_name of this PublicDownloadShare.
        :param creator_username: The creator_username of this PublicDownloadShare.
        :param expire_at: The expire_at of this PublicDownloadShare.
        :param file_key: The file_key of this PublicDownloadShare.
        :param file_name: The file_name of this PublicDownloadShare.
        :param has_download_limit: The has_download_limit of this PublicDownloadShare.
        :param is_encrypted: The is_encrypted of this PublicDownloadShare.
        :param is_protected: The is_protected of this PublicDownloadShare.
        :param limit_reached: The limit_reached of this PublicDownloadShare.
        :param media_type: The media_type of this PublicDownloadShare.
        :param name: The name of this PublicDownloadShare.
        :param notes: The notes of this PublicDownloadShare.
        :param private_key_container: The private_key_container of this PublicDownloadShare.
        :param size: The size of this PublicDownloadShare.
        """
        self.openapi_types = {
            'created_at': datetime,
            'creator_name': str,
            'creator_username': str,
            'expire_at': datetime,
            'file_key': FileKey,
            'file_name': str,
            'has_download_limit': bool,
            'is_encrypted': bool,
            'is_protected': bool,
            'limit_reached': bool,
            'media_type': str,
            'name': str,
            'notes': str,
            'private_key_container': PrivateKeyContainer,
            'size': int
        }

        self.attribute_map = {
            'created_at': 'createdAt',
            'creator_name': 'creatorName',
            'creator_username': 'creatorUsername',
            'expire_at': 'expireAt',
            'file_key': 'fileKey',
            'file_name': 'fileName',
            'has_download_limit': 'hasDownloadLimit',
            'is_encrypted': 'isEncrypted',
            'is_protected': 'isProtected',
            'limit_reached': 'limitReached',
            'media_type': 'mediaType',
            'name': 'name',
            'notes': 'notes',
            'private_key_container': 'privateKeyContainer',
            'size': 'size'
        }

        self._created_at = created_at
        self._creator_name = creator_name
        self._creator_username = creator_username
        self._expire_at = expire_at
        self._file_key = file_key
        self._file_name = file_name
        self._has_download_limit = has_download_limit
        self._is_encrypted = is_encrypted
        self._is_protected = is_protected
        self._limit_reached = limit_reached
        self._media_type = media_type
        self._name = name
        self._notes = notes
        self._private_key_container = private_key_container
        self._size = size

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PublicDownloadShare':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PublicDownloadShare of this PublicDownloadShare.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def created_at(self):
        """Gets the created_at of this PublicDownloadShare.

        Creation date

        :return: The created_at of this PublicDownloadShare.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this PublicDownloadShare.

        Creation date

        :param created_at: The created_at of this PublicDownloadShare.
        :type created_at: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")

        self._created_at = created_at

    @property
    def creator_name(self):
        """Gets the creator_name of this PublicDownloadShare.

        Creator name

        :return: The creator_name of this PublicDownloadShare.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        """Sets the creator_name of this PublicDownloadShare.

        Creator name

        :param creator_name: The creator_name of this PublicDownloadShare.
        :type creator_name: str
        """
        if creator_name is None:
            raise ValueError("Invalid value for `creator_name`, must not be `None`")

        self._creator_name = creator_name

    @property
    def creator_username(self):
        """Gets the creator_username of this PublicDownloadShare.

        Creator username

        :return: The creator_username of this PublicDownloadShare.
        :rtype: str
        """
        return self._creator_username

    @creator_username.setter
    def creator_username(self, creator_username):
        """Sets the creator_username of this PublicDownloadShare.

        Creator username

        :param creator_username: The creator_username of this PublicDownloadShare.
        :type creator_username: str
        """

        self._creator_username = creator_username

    @property
    def expire_at(self):
        """Gets the expire_at of this PublicDownloadShare.

        Expiration date

        :return: The expire_at of this PublicDownloadShare.
        :rtype: datetime
        """
        return self._expire_at

    @expire_at.setter
    def expire_at(self, expire_at):
        """Sets the expire_at of this PublicDownloadShare.

        Expiration date

        :param expire_at: The expire_at of this PublicDownloadShare.
        :type expire_at: datetime
        """

        self._expire_at = expire_at

    @property
    def file_key(self):
        """Gets the file_key of this PublicDownloadShare.


        :return: The file_key of this PublicDownloadShare.
        :rtype: FileKey
        """
        return self._file_key

    @file_key.setter
    def file_key(self, file_key):
        """Sets the file_key of this PublicDownloadShare.


        :param file_key: The file_key of this PublicDownloadShare.
        :type file_key: FileKey
        """

        self._file_key = file_key

    @property
    def file_name(self):
        """Gets the file_name of this PublicDownloadShare.

        File name

        :return: The file_name of this PublicDownloadShare.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this PublicDownloadShare.

        File name

        :param file_name: The file_name of this PublicDownloadShare.
        :type file_name: str
        """
        if file_name is None:
            raise ValueError("Invalid value for `file_name`, must not be `None`")

        self._file_name = file_name

    @property
    def has_download_limit(self):
        """Gets the has_download_limit of this PublicDownloadShare.

        &#128640; Since v4.11.0  Determines whether Download Share has a limit for amount of downloads

        :return: The has_download_limit of this PublicDownloadShare.
        :rtype: bool
        """
        return self._has_download_limit

    @has_download_limit.setter
    def has_download_limit(self, has_download_limit):
        """Sets the has_download_limit of this PublicDownloadShare.

        &#128640; Since v4.11.0  Determines whether Download Share has a limit for amount of downloads

        :param has_download_limit: The has_download_limit of this PublicDownloadShare.
        :type has_download_limit: bool
        """
        if has_download_limit is None:
            raise ValueError("Invalid value for `has_download_limit`, must not be `None`")

        self._has_download_limit = has_download_limit

    @property
    def is_encrypted(self):
        """Gets the is_encrypted of this PublicDownloadShare.

        Encryption state

        :return: The is_encrypted of this PublicDownloadShare.
        :rtype: bool
        """
        return self._is_encrypted

    @is_encrypted.setter
    def is_encrypted(self, is_encrypted):
        """Sets the is_encrypted of this PublicDownloadShare.

        Encryption state

        :param is_encrypted: The is_encrypted of this PublicDownloadShare.
        :type is_encrypted: bool
        """

        self._is_encrypted = is_encrypted

    @property
    def is_protected(self):
        """Gets the is_protected of this PublicDownloadShare.

        Is share protected by password

        :return: The is_protected of this PublicDownloadShare.
        :rtype: bool
        """
        return self._is_protected

    @is_protected.setter
    def is_protected(self, is_protected):
        """Sets the is_protected of this PublicDownloadShare.

        Is share protected by password

        :param is_protected: The is_protected of this PublicDownloadShare.
        :type is_protected: bool
        """
        if is_protected is None:
            raise ValueError("Invalid value for `is_protected`, must not be `None`")

        self._is_protected = is_protected

    @property
    def limit_reached(self):
        """Gets the limit_reached of this PublicDownloadShare.

        Downloads limit reached

        :return: The limit_reached of this PublicDownloadShare.
        :rtype: bool
        """
        return self._limit_reached

    @limit_reached.setter
    def limit_reached(self, limit_reached):
        """Sets the limit_reached of this PublicDownloadShare.

        Downloads limit reached

        :param limit_reached: The limit_reached of this PublicDownloadShare.
        :type limit_reached: bool
        """
        if limit_reached is None:
            raise ValueError("Invalid value for `limit_reached`, must not be `None`")

        self._limit_reached = limit_reached

    @property
    def media_type(self):
        """Gets the media_type of this PublicDownloadShare.

        &#128640; Since v4.11.0  * `application/zip` (for folders and rooms)  * actual file media type (for files only)

        :return: The media_type of this PublicDownloadShare.
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """Sets the media_type of this PublicDownloadShare.

        &#128640; Since v4.11.0  * `application/zip` (for folders and rooms)  * actual file media type (for files only)

        :param media_type: The media_type of this PublicDownloadShare.
        :type media_type: str
        """
        if media_type is None:
            raise ValueError("Invalid value for `media_type`, must not be `None`")

        self._media_type = media_type

    @property
    def name(self):
        """Gets the name of this PublicDownloadShare.

        Share display name (alias name)

        :return: The name of this PublicDownloadShare.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PublicDownloadShare.

        Share display name (alias name)

        :param name: The name of this PublicDownloadShare.
        :type name: str
        """

        self._name = name

    @property
    def notes(self):
        """Gets the notes of this PublicDownloadShare.

        User notes

        :return: The notes of this PublicDownloadShare.
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this PublicDownloadShare.

        User notes

        :param notes: The notes of this PublicDownloadShare.
        :type notes: str
        """

        self._notes = notes

    @property
    def private_key_container(self):
        """Gets the private_key_container of this PublicDownloadShare.


        :return: The private_key_container of this PublicDownloadShare.
        :rtype: PrivateKeyContainer
        """
        return self._private_key_container

    @private_key_container.setter
    def private_key_container(self, private_key_container):
        """Sets the private_key_container of this PublicDownloadShare.


        :param private_key_container: The private_key_container of this PublicDownloadShare.
        :type private_key_container: PrivateKeyContainer
        """

        self._private_key_container = private_key_container

    @property
    def size(self):
        """Gets the size of this PublicDownloadShare.

        File size or container size not compressed (in bytes)

        :return: The size of this PublicDownloadShare.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this PublicDownloadShare.

        File size or container size not compressed (in bytes)

        :param size: The size of this PublicDownloadShare.
        :type size: int
        """
        if size is None:
            raise ValueError("Invalid value for `size`, must not be `None`")

        self._size = size
