# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.user_auth_data import UserAuthData
from openapi_server.models.user_auth_method import UserAuthMethod
from openapi_server import util


class FirstAdminUser(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, auth_data: UserAuthData=None, auth_methods: List[UserAuthMethod]=None, email: str=None, first_name: str=None, gender: str='n', language: str=None, last_name: str=None, login: str=None, needs_to_change_password: bool=None, needs_to_change_user_name: bool=False, notify_user: bool=None, password: str=None, phone: str=None, receiver_language: str=None, title: str=None, user_name: str=None):
        """FirstAdminUser - a model defined in OpenAPI

        :param auth_data: The auth_data of this FirstAdminUser.
        :param auth_methods: The auth_methods of this FirstAdminUser.
        :param email: The email of this FirstAdminUser.
        :param first_name: The first_name of this FirstAdminUser.
        :param gender: The gender of this FirstAdminUser.
        :param language: The language of this FirstAdminUser.
        :param last_name: The last_name of this FirstAdminUser.
        :param login: The login of this FirstAdminUser.
        :param needs_to_change_password: The needs_to_change_password of this FirstAdminUser.
        :param needs_to_change_user_name: The needs_to_change_user_name of this FirstAdminUser.
        :param notify_user: The notify_user of this FirstAdminUser.
        :param password: The password of this FirstAdminUser.
        :param phone: The phone of this FirstAdminUser.
        :param receiver_language: The receiver_language of this FirstAdminUser.
        :param title: The title of this FirstAdminUser.
        :param user_name: The user_name of this FirstAdminUser.
        """
        self.openapi_types = {
            'auth_data': UserAuthData,
            'auth_methods': List[UserAuthMethod],
            'email': str,
            'first_name': str,
            'gender': str,
            'language': str,
            'last_name': str,
            'login': str,
            'needs_to_change_password': bool,
            'needs_to_change_user_name': bool,
            'notify_user': bool,
            'password': str,
            'phone': str,
            'receiver_language': str,
            'title': str,
            'user_name': str
        }

        self.attribute_map = {
            'auth_data': 'authData',
            'auth_methods': 'authMethods',
            'email': 'email',
            'first_name': 'firstName',
            'gender': 'gender',
            'language': 'language',
            'last_name': 'lastName',
            'login': 'login',
            'needs_to_change_password': 'needsToChangePassword',
            'needs_to_change_user_name': 'needsToChangeUserName',
            'notify_user': 'notifyUser',
            'password': 'password',
            'phone': 'phone',
            'receiver_language': 'receiverLanguage',
            'title': 'title',
            'user_name': 'userName'
        }

        self._auth_data = auth_data
        self._auth_methods = auth_methods
        self._email = email
        self._first_name = first_name
        self._gender = gender
        self._language = language
        self._last_name = last_name
        self._login = login
        self._needs_to_change_password = needs_to_change_password
        self._needs_to_change_user_name = needs_to_change_user_name
        self._notify_user = notify_user
        self._password = password
        self._phone = phone
        self._receiver_language = receiver_language
        self._title = title
        self._user_name = user_name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'FirstAdminUser':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The FirstAdminUser of this FirstAdminUser.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def auth_data(self):
        """Gets the auth_data of this FirstAdminUser.


        :return: The auth_data of this FirstAdminUser.
        :rtype: UserAuthData
        """
        return self._auth_data

    @auth_data.setter
    def auth_data(self, auth_data):
        """Sets the auth_data of this FirstAdminUser.


        :param auth_data: The auth_data of this FirstAdminUser.
        :type auth_data: UserAuthData
        """

        self._auth_data = auth_data

    @property
    def auth_methods(self):
        """Gets the auth_methods of this FirstAdminUser.

        &#128679; Deprecated since v4.13.0  Authentication methods:  * `sql`  * `active_directory`  * `radius`  * `openid`  use `authData` instead

        :return: The auth_methods of this FirstAdminUser.
        :rtype: List[UserAuthMethod]
        """
        return self._auth_methods

    @auth_methods.setter
    def auth_methods(self, auth_methods):
        """Sets the auth_methods of this FirstAdminUser.

        &#128679; Deprecated since v4.13.0  Authentication methods:  * `sql`  * `active_directory`  * `radius`  * `openid`  use `authData` instead

        :param auth_methods: The auth_methods of this FirstAdminUser.
        :type auth_methods: List[UserAuthMethod]
        """

        self._auth_methods = auth_methods

    @property
    def email(self):
        """Gets the email of this FirstAdminUser.

        Email 

        :return: The email of this FirstAdminUser.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this FirstAdminUser.

        Email 

        :param email: The email of this FirstAdminUser.
        :type email: str
        """

        self._email = email

    @property
    def first_name(self):
        """Gets the first_name of this FirstAdminUser.

        User first name

        :return: The first_name of this FirstAdminUser.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this FirstAdminUser.

        User first name

        :param first_name: The first_name of this FirstAdminUser.
        :type first_name: str
        """
        if first_name is None:
            raise ValueError("Invalid value for `first_name`, must not be `None`")

        self._first_name = first_name

    @property
    def gender(self):
        """Gets the gender of this FirstAdminUser.

        &#128679; Deprecated since v4.12.0  Gender

        :return: The gender of this FirstAdminUser.
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this FirstAdminUser.

        &#128679; Deprecated since v4.12.0  Gender

        :param gender: The gender of this FirstAdminUser.
        :type gender: str
        """

        self._gender = gender

    @property
    def language(self):
        """Gets the language of this FirstAdminUser.

        &#128679; Deprecated since v4.7.0  Language ID or ISO 639-1 code

        :return: The language of this FirstAdminUser.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this FirstAdminUser.

        &#128679; Deprecated since v4.7.0  Language ID or ISO 639-1 code

        :param language: The language of this FirstAdminUser.
        :type language: str
        """

        self._language = language

    @property
    def last_name(self):
        """Gets the last_name of this FirstAdminUser.

        User last name

        :return: The last_name of this FirstAdminUser.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this FirstAdminUser.

        User last name

        :param last_name: The last_name of this FirstAdminUser.
        :type last_name: str
        """
        if last_name is None:
            raise ValueError("Invalid value for `last_name`, must not be `None`")

        self._last_name = last_name

    @property
    def login(self):
        """Gets the login of this FirstAdminUser.

        &#128679; Deprecated since v4.13.0  User login name

        :return: The login of this FirstAdminUser.
        :rtype: str
        """
        return self._login

    @login.setter
    def login(self, login):
        """Sets the login of this FirstAdminUser.

        &#128679; Deprecated since v4.13.0  User login name

        :param login: The login of this FirstAdminUser.
        :type login: str
        """

        self._login = login

    @property
    def needs_to_change_password(self):
        """Gets the needs_to_change_password of this FirstAdminUser.

        &#128679; Deprecated since v4.13.0  Determines whether user has to change his / her initial password.  use `authDate.mustChangePassword` instead

        :return: The needs_to_change_password of this FirstAdminUser.
        :rtype: bool
        """
        return self._needs_to_change_password

    @needs_to_change_password.setter
    def needs_to_change_password(self, needs_to_change_password):
        """Sets the needs_to_change_password of this FirstAdminUser.

        &#128679; Deprecated since v4.13.0  Determines whether user has to change his / her initial password.  use `authDate.mustChangePassword` instead

        :param needs_to_change_password: The needs_to_change_password of this FirstAdminUser.
        :type needs_to_change_password: bool
        """

        self._needs_to_change_password = needs_to_change_password

    @property
    def needs_to_change_user_name(self):
        """Gets the needs_to_change_user_name of this FirstAdminUser.

        &#128679; Deprecated since v4.13.0  If `true`, the user must change the `userName` at the first login.

        :return: The needs_to_change_user_name of this FirstAdminUser.
        :rtype: bool
        """
        return self._needs_to_change_user_name

    @needs_to_change_user_name.setter
    def needs_to_change_user_name(self, needs_to_change_user_name):
        """Sets the needs_to_change_user_name of this FirstAdminUser.

        &#128679; Deprecated since v4.13.0  If `true`, the user must change the `userName` at the first login.

        :param needs_to_change_user_name: The needs_to_change_user_name of this FirstAdminUser.
        :type needs_to_change_user_name: bool
        """

        self._needs_to_change_user_name = needs_to_change_user_name

    @property
    def notify_user(self):
        """Gets the notify_user of this FirstAdminUser.

        Notify user about his new account  * default: `true` for `basic` auth type  * default: `false` for `active_directory`, `openid` and `radius` auth types

        :return: The notify_user of this FirstAdminUser.
        :rtype: bool
        """
        return self._notify_user

    @notify_user.setter
    def notify_user(self, notify_user):
        """Sets the notify_user of this FirstAdminUser.

        Notify user about his new account  * default: `true` for `basic` auth type  * default: `false` for `active_directory`, `openid` and `radius` auth types

        :param notify_user: The notify_user of this FirstAdminUser.
        :type notify_user: bool
        """

        self._notify_user = notify_user

    @property
    def password(self):
        """Gets the password of this FirstAdminUser.

        &#128679; Deprecated since v4.13.0  An initial password may be preset  use `authData` instead

        :return: The password of this FirstAdminUser.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this FirstAdminUser.

        &#128679; Deprecated since v4.13.0  An initial password may be preset  use `authData` instead

        :param password: The password of this FirstAdminUser.
        :type password: str
        """

        self._password = password

    @property
    def phone(self):
        """Gets the phone of this FirstAdminUser.

        Phone number

        :return: The phone of this FirstAdminUser.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this FirstAdminUser.

        Phone number

        :param phone: The phone of this FirstAdminUser.
        :type phone: str
        """

        self._phone = phone

    @property
    def receiver_language(self):
        """Gets the receiver_language of this FirstAdminUser.

        IETF language tag

        :return: The receiver_language of this FirstAdminUser.
        :rtype: str
        """
        return self._receiver_language

    @receiver_language.setter
    def receiver_language(self, receiver_language):
        """Sets the receiver_language of this FirstAdminUser.

        IETF language tag

        :param receiver_language: The receiver_language of this FirstAdminUser.
        :type receiver_language: str
        """

        self._receiver_language = receiver_language

    @property
    def title(self):
        """Gets the title of this FirstAdminUser.

        &#128679; Deprecated since v4.18.0  Job title

        :return: The title of this FirstAdminUser.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this FirstAdminUser.

        &#128679; Deprecated since v4.18.0  Job title

        :param title: The title of this FirstAdminUser.
        :type title: str
        """

        self._title = title

    @property
    def user_name(self):
        """Gets the user_name of this FirstAdminUser.

        &#128640; Since v4.13.0  Username

        :return: The user_name of this FirstAdminUser.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this FirstAdminUser.

        &#128640; Since v4.13.0  Username

        :param user_name: The user_name of this FirstAdminUser.
        :type user_name: str
        """

        self._user_name = user_name
