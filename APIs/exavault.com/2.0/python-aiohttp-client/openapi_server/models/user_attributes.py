# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.user_permissions import UserPermissions
from openapi_server import util


class UserAttributes(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, access_timestamp: str=None, account_name: str=None, created: datetime=None, email: str=None, expiration: str=None, first_login: bool=None, home_path: str=None, locked: bool=None, modified: datetime=None, nickname: str=None, onboarding: bool=None, permissions: UserPermissions=None, role: str=None, status: int=None, time_zone: str=None, username: str=None):
        """UserAttributes - a model defined in OpenAPI

        :param access_timestamp: The access_timestamp of this UserAttributes.
        :param account_name: The account_name of this UserAttributes.
        :param created: The created of this UserAttributes.
        :param email: The email of this UserAttributes.
        :param expiration: The expiration of this UserAttributes.
        :param first_login: The first_login of this UserAttributes.
        :param home_path: The home_path of this UserAttributes.
        :param locked: The locked of this UserAttributes.
        :param modified: The modified of this UserAttributes.
        :param nickname: The nickname of this UserAttributes.
        :param onboarding: The onboarding of this UserAttributes.
        :param permissions: The permissions of this UserAttributes.
        :param role: The role of this UserAttributes.
        :param status: The status of this UserAttributes.
        :param time_zone: The time_zone of this UserAttributes.
        :param username: The username of this UserAttributes.
        """
        self.openapi_types = {
            'access_timestamp': str,
            'account_name': str,
            'created': datetime,
            'email': str,
            'expiration': str,
            'first_login': bool,
            'home_path': str,
            'locked': bool,
            'modified': datetime,
            'nickname': str,
            'onboarding': bool,
            'permissions': UserPermissions,
            'role': str,
            'status': int,
            'time_zone': str,
            'username': str
        }

        self.attribute_map = {
            'access_timestamp': 'accessTimestamp',
            'account_name': 'accountName',
            'created': 'created',
            'email': 'email',
            'expiration': 'expiration',
            'first_login': 'firstLogin',
            'home_path': 'homePath',
            'locked': 'locked',
            'modified': 'modified',
            'nickname': 'nickname',
            'onboarding': 'onboarding',
            'permissions': 'permissions',
            'role': 'role',
            'status': 'status',
            'time_zone': 'timeZone',
            'username': 'username'
        }

        self._access_timestamp = access_timestamp
        self._account_name = account_name
        self._created = created
        self._email = email
        self._expiration = expiration
        self._first_login = first_login
        self._home_path = home_path
        self._locked = locked
        self._modified = modified
        self._nickname = nickname
        self._onboarding = onboarding
        self._permissions = permissions
        self._role = role
        self._status = status
        self._time_zone = time_zone
        self._username = username

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UserAttributes':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The UserAttributes of this UserAttributes.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def access_timestamp(self):
        """Gets the access_timestamp of this UserAttributes.

        Timestamp of most recent successful user login.

        :return: The access_timestamp of this UserAttributes.
        :rtype: str
        """
        return self._access_timestamp

    @access_timestamp.setter
    def access_timestamp(self, access_timestamp):
        """Sets the access_timestamp of this UserAttributes.

        Timestamp of most recent successful user login.

        :param access_timestamp: The access_timestamp of this UserAttributes.
        :type access_timestamp: str
        """

        self._access_timestamp = access_timestamp

    @property
    def account_name(self):
        """Gets the account_name of this UserAttributes.

        Name of the account this user belongs to.

        :return: The account_name of this UserAttributes.
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this UserAttributes.

        Name of the account this user belongs to.

        :param account_name: The account_name of this UserAttributes.
        :type account_name: str
        """
        if account_name is None:
            raise ValueError("Invalid value for `account_name`, must not be `None`")

        self._account_name = account_name

    @property
    def created(self):
        """Gets the created of this UserAttributes.

        Timestamp of user creation.

        :return: The created of this UserAttributes.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this UserAttributes.

        Timestamp of user creation.

        :param created: The created of this UserAttributes.
        :type created: datetime
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")

        self._created = created

    @property
    def email(self):
        """Gets the email of this UserAttributes.

        Email address of the user.

        :return: The email of this UserAttributes.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserAttributes.

        Email address of the user.

        :param email: The email of this UserAttributes.
        :type email: str
        """

        self._email = email

    @property
    def expiration(self):
        """Gets the expiration of this UserAttributes.

        Timestamp of user expiration.

        :return: The expiration of this UserAttributes.
        :rtype: str
        """
        return self._expiration

    @expiration.setter
    def expiration(self, expiration):
        """Sets the expiration of this UserAttributes.

        Timestamp of user expiration.

        :param expiration: The expiration of this UserAttributes.
        :type expiration: str
        """

        self._expiration = expiration

    @property
    def first_login(self):
        """Gets the first_login of this UserAttributes.

        `true` if the user has logged into the system.

        :return: The first_login of this UserAttributes.
        :rtype: bool
        """
        return self._first_login

    @first_login.setter
    def first_login(self, first_login):
        """Sets the first_login of this UserAttributes.

        `true` if the user has logged into the system.

        :param first_login: The first_login of this UserAttributes.
        :type first_login: bool
        """

        self._first_login = first_login

    @property
    def home_path(self):
        """Gets the home_path of this UserAttributes.

        Path to the user's home folder.

        :return: The home_path of this UserAttributes.
        :rtype: str
        """
        return self._home_path

    @home_path.setter
    def home_path(self, home_path):
        """Sets the home_path of this UserAttributes.

        Path to the user's home folder.

        :param home_path: The home_path of this UserAttributes.
        :type home_path: str
        """

        self._home_path = home_path

    @property
    def locked(self):
        """Gets the locked of this UserAttributes.

        `true` if the user is locked and cannot log in.

        :return: The locked of this UserAttributes.
        :rtype: bool
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """Sets the locked of this UserAttributes.

        `true` if the user is locked and cannot log in.

        :param locked: The locked of this UserAttributes.
        :type locked: bool
        """

        self._locked = locked

    @property
    def modified(self):
        """Gets the modified of this UserAttributes.

        Timestamp of user modification.

        :return: The modified of this UserAttributes.
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this UserAttributes.

        Timestamp of user modification.

        :param modified: The modified of this UserAttributes.
        :type modified: datetime
        """
        if modified is None:
            raise ValueError("Invalid value for `modified`, must not be `None`")

        self._modified = modified

    @property
    def nickname(self):
        """Gets the nickname of this UserAttributes.

        Nickname of the user.

        :return: The nickname of this UserAttributes.
        :rtype: str
        """
        return self._nickname

    @nickname.setter
    def nickname(self, nickname):
        """Sets the nickname of this UserAttributes.

        Nickname of the user.

        :param nickname: The nickname of this UserAttributes.
        :type nickname: str
        """
        if nickname is None:
            raise ValueError("Invalid value for `nickname`, must not be `None`")

        self._nickname = nickname

    @property
    def onboarding(self):
        """Gets the onboarding of this UserAttributes.

        Whether the onboarding help system is enabled for this user. `true` means that additional help popups are displayed in the web application for this user.

        :return: The onboarding of this UserAttributes.
        :rtype: bool
        """
        return self._onboarding

    @onboarding.setter
    def onboarding(self, onboarding):
        """Sets the onboarding of this UserAttributes.

        Whether the onboarding help system is enabled for this user. `true` means that additional help popups are displayed in the web application for this user.

        :param onboarding: The onboarding of this UserAttributes.
        :type onboarding: bool
        """
        if onboarding is None:
            raise ValueError("Invalid value for `onboarding`, must not be `None`")

        self._onboarding = onboarding

    @property
    def permissions(self):
        """Gets the permissions of this UserAttributes.


        :return: The permissions of this UserAttributes.
        :rtype: UserPermissions
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this UserAttributes.


        :param permissions: The permissions of this UserAttributes.
        :type permissions: UserPermissions
        """
        if permissions is None:
            raise ValueError("Invalid value for `permissions`, must not be `None`")

        self._permissions = permissions

    @property
    def role(self):
        """Gets the role of this UserAttributes.

        User's access level

        :return: The role of this UserAttributes.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this UserAttributes.

        User's access level

        :param role: The role of this UserAttributes.
        :type role: str
        """
        allowed_values = ["user", "admin", "master"]  # noqa: E501
        if role not in allowed_values:
            raise ValueError(
                "Invalid value for `role` ({0}), must be one of {1}"
                .format(role, allowed_values)
            )

        self._role = role

    @property
    def status(self):
        """Gets the status of this UserAttributes.

        Indicates user activity status. `0` means the user is locked and cannot log in. `1` means the user is active and can log in.

        :return: The status of this UserAttributes.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UserAttributes.

        Indicates user activity status. `0` means the user is locked and cannot log in. `1` means the user is active and can log in.

        :param status: The status of this UserAttributes.
        :type status: int
        """
        allowed_values = [0, 1]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def time_zone(self):
        """Gets the time_zone of this UserAttributes.

        User's timezone. See <a href='https://php.net/manual/en/timezones.php' target='blank'>this page</a> for allowed values.

        :return: The time_zone of this UserAttributes.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this UserAttributes.

        User's timezone. See <a href='https://php.net/manual/en/timezones.php' target='blank'>this page</a> for allowed values.

        :param time_zone: The time_zone of this UserAttributes.
        :type time_zone: str
        """
        if time_zone is None:
            raise ValueError("Invalid value for `time_zone`, must not be `None`")

        self._time_zone = time_zone

    @property
    def username(self):
        """Gets the username of this UserAttributes.

        Username of the user.

        :return: The username of this UserAttributes.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this UserAttributes.

        Username of the user.

        :param username: The username of this UserAttributes.
        :type username: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")

        self._username = username
