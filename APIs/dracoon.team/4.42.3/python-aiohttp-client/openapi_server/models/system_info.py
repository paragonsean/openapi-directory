# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.auth_method import AuthMethod
from openapi_server import util


class SystemInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, auth_methods: List[AuthMethod]=None, hide_login_input_fields: bool=None, language_default: str=None, s3_enforce_direct_upload: bool=None, s3_hosts: List[str]=None, use_s3_storage: bool=None):
        """SystemInfo - a model defined in OpenAPI

        :param auth_methods: The auth_methods of this SystemInfo.
        :param hide_login_input_fields: The hide_login_input_fields of this SystemInfo.
        :param language_default: The language_default of this SystemInfo.
        :param s3_enforce_direct_upload: The s3_enforce_direct_upload of this SystemInfo.
        :param s3_hosts: The s3_hosts of this SystemInfo.
        :param use_s3_storage: The use_s3_storage of this SystemInfo.
        """
        self.openapi_types = {
            'auth_methods': List[AuthMethod],
            'hide_login_input_fields': bool,
            'language_default': str,
            's3_enforce_direct_upload': bool,
            's3_hosts': List[str],
            'use_s3_storage': bool
        }

        self.attribute_map = {
            'auth_methods': 'authMethods',
            'hide_login_input_fields': 'hideLoginInputFields',
            'language_default': 'languageDefault',
            's3_enforce_direct_upload': 's3EnforceDirectUpload',
            's3_hosts': 's3Hosts',
            'use_s3_storage': 'useS3Storage'
        }

        self._auth_methods = auth_methods
        self._hide_login_input_fields = hide_login_input_fields
        self._language_default = language_default
        self._s3_enforce_direct_upload = s3_enforce_direct_upload
        self._s3_hosts = s3_hosts
        self._use_s3_storage = use_s3_storage

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SystemInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The SystemInfo of this SystemInfo.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def auth_methods(self):
        """Gets the auth_methods of this SystemInfo.

        &#128679; Deprecated since v4.13.0  Authentication methods:  * `sql`  * `active_directory`  * `radius`  * `openid`  use `authData` instead

        :return: The auth_methods of this SystemInfo.
        :rtype: List[AuthMethod]
        """
        return self._auth_methods

    @auth_methods.setter
    def auth_methods(self, auth_methods):
        """Sets the auth_methods of this SystemInfo.

        &#128679; Deprecated since v4.13.0  Authentication methods:  * `sql`  * `active_directory`  * `radius`  * `openid`  use `authData` instead

        :param auth_methods: The auth_methods of this SystemInfo.
        :type auth_methods: List[AuthMethod]
        """
        if auth_methods is None:
            raise ValueError("Invalid value for `auth_methods`, must not be `None`")

        self._auth_methods = auth_methods

    @property
    def hide_login_input_fields(self):
        """Gets the hide_login_input_fields of this SystemInfo.

        &#128679; Deprecated since v4.42.0  Defines if login fields should be hidden

        :return: The hide_login_input_fields of this SystemInfo.
        :rtype: bool
        """
        return self._hide_login_input_fields

    @hide_login_input_fields.setter
    def hide_login_input_fields(self, hide_login_input_fields):
        """Sets the hide_login_input_fields of this SystemInfo.

        &#128679; Deprecated since v4.42.0  Defines if login fields should be hidden

        :param hide_login_input_fields: The hide_login_input_fields of this SystemInfo.
        :type hide_login_input_fields: bool
        """
        if hide_login_input_fields is None:
            raise ValueError("Invalid value for `hide_login_input_fields`, must not be `None`")

        self._hide_login_input_fields = hide_login_input_fields

    @property
    def language_default(self):
        """Gets the language_default of this SystemInfo.

        System default language  cf. [RFC 5646](https://tools.ietf.org/html/rfc5646)

        :return: The language_default of this SystemInfo.
        :rtype: str
        """
        return self._language_default

    @language_default.setter
    def language_default(self, language_default):
        """Sets the language_default of this SystemInfo.

        System default language  cf. [RFC 5646](https://tools.ietf.org/html/rfc5646)

        :param language_default: The language_default of this SystemInfo.
        :type language_default: str
        """
        if language_default is None:
            raise ValueError("Invalid value for `language_default`, must not be `None`")

        self._language_default = language_default

    @property
    def s3_enforce_direct_upload(self):
        """Gets the s3_enforce_direct_upload of this SystemInfo.

        &#128640; Since v4.15.0  Determines whether S3 direct upload is enforced or not

        :return: The s3_enforce_direct_upload of this SystemInfo.
        :rtype: bool
        """
        return self._s3_enforce_direct_upload

    @s3_enforce_direct_upload.setter
    def s3_enforce_direct_upload(self, s3_enforce_direct_upload):
        """Sets the s3_enforce_direct_upload of this SystemInfo.

        &#128640; Since v4.15.0  Determines whether S3 direct upload is enforced or not

        :param s3_enforce_direct_upload: The s3_enforce_direct_upload of this SystemInfo.
        :type s3_enforce_direct_upload: bool
        """
        if s3_enforce_direct_upload is None:
            raise ValueError("Invalid value for `s3_enforce_direct_upload`, must not be `None`")

        self._s3_enforce_direct_upload = s3_enforce_direct_upload

    @property
    def s3_hosts(self):
        """Gets the s3_hosts of this SystemInfo.

        &#128640; Since v4.14.0  List of S3 Hosts for CSP header

        :return: The s3_hosts of this SystemInfo.
        :rtype: List[str]
        """
        return self._s3_hosts

    @s3_hosts.setter
    def s3_hosts(self, s3_hosts):
        """Sets the s3_hosts of this SystemInfo.

        &#128640; Since v4.14.0  List of S3 Hosts for CSP header

        :param s3_hosts: The s3_hosts of this SystemInfo.
        :type s3_hosts: List[str]
        """
        if s3_hosts is None:
            raise ValueError("Invalid value for `s3_hosts`, must not be `None`")

        self._s3_hosts = s3_hosts

    @property
    def use_s3_storage(self):
        """Gets the use_s3_storage of this SystemInfo.

        &#128640; Since v4.21.0  Defines if S3 is used as storage backend

        :return: The use_s3_storage of this SystemInfo.
        :rtype: bool
        """
        return self._use_s3_storage

    @use_s3_storage.setter
    def use_s3_storage(self, use_s3_storage):
        """Sets the use_s3_storage of this SystemInfo.

        &#128640; Since v4.21.0  Defines if S3 is used as storage backend

        :param use_s3_storage: The use_s3_storage of this SystemInfo.
        :type use_s3_storage: bool
        """
        if use_s3_storage is None:
            raise ValueError("Invalid value for `use_s3_storage`, must not be `None`")

        self._use_s3_storage = use_s3_storage
