# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class UserProfileResponsev2(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, admin_role: str=None, avatar_url: str=None, can_change_password: bool=None, created_at: str=None, display_name: str=None, email: str=None, feature_flags: List[str]=None, id: str=None, name: str=None, next_nps_survey_date: str=None, origin: str=None, session_hash: str=None, settings: object=None):
        """UserProfileResponsev2 - a model defined in OpenAPI

        :param admin_role: The admin_role of this UserProfileResponsev2.
        :param avatar_url: The avatar_url of this UserProfileResponsev2.
        :param can_change_password: The can_change_password of this UserProfileResponsev2.
        :param created_at: The created_at of this UserProfileResponsev2.
        :param display_name: The display_name of this UserProfileResponsev2.
        :param email: The email of this UserProfileResponsev2.
        :param feature_flags: The feature_flags of this UserProfileResponsev2.
        :param id: The id of this UserProfileResponsev2.
        :param name: The name of this UserProfileResponsev2.
        :param next_nps_survey_date: The next_nps_survey_date of this UserProfileResponsev2.
        :param origin: The origin of this UserProfileResponsev2.
        :param session_hash: The session_hash of this UserProfileResponsev2.
        :param settings: The settings of this UserProfileResponsev2.
        """
        self.openapi_types = {
            'admin_role': str,
            'avatar_url': str,
            'can_change_password': bool,
            'created_at': str,
            'display_name': str,
            'email': str,
            'feature_flags': List[str],
            'id': str,
            'name': str,
            'next_nps_survey_date': str,
            'origin': str,
            'session_hash': str,
            'settings': object
        }

        self.attribute_map = {
            'admin_role': 'admin_role',
            'avatar_url': 'avatar_url',
            'can_change_password': 'can_change_password',
            'created_at': 'created_at',
            'display_name': 'display_name',
            'email': 'email',
            'feature_flags': 'feature_flags',
            'id': 'id',
            'name': 'name',
            'next_nps_survey_date': 'next_nps_survey_date',
            'origin': 'origin',
            'session_hash': 'session_hash',
            'settings': 'settings'
        }

        self._admin_role = admin_role
        self._avatar_url = avatar_url
        self._can_change_password = can_change_password
        self._created_at = created_at
        self._display_name = display_name
        self._email = email
        self._feature_flags = feature_flags
        self._id = id
        self._name = name
        self._next_nps_survey_date = next_nps_survey_date
        self._origin = origin
        self._session_hash = session_hash
        self._settings = settings

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UserProfileResponsev2':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The UserProfileResponsev2 of this UserProfileResponsev2.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def admin_role(self):
        """Gets the admin_role of this UserProfileResponsev2.

        The new admin_role

        :return: The admin_role of this UserProfileResponsev2.
        :rtype: str
        """
        return self._admin_role

    @admin_role.setter
    def admin_role(self, admin_role):
        """Sets the admin_role of this UserProfileResponsev2.

        The new admin_role

        :param admin_role: The admin_role of this UserProfileResponsev2.
        :type admin_role: str
        """
        allowed_values = ["superAdmin", "admin", "devOps", "customerSupport", "notAdmin"]  # noqa: E501
        if admin_role not in allowed_values:
            raise ValueError(
                "Invalid value for `admin_role` ({0}), must be one of {1}"
                .format(admin_role, allowed_values)
            )

        self._admin_role = admin_role

    @property
    def avatar_url(self):
        """Gets the avatar_url of this UserProfileResponsev2.

        The avatar URL of the user

        :return: The avatar_url of this UserProfileResponsev2.
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        """Sets the avatar_url of this UserProfileResponsev2.

        The avatar URL of the user

        :param avatar_url: The avatar_url of this UserProfileResponsev2.
        :type avatar_url: str
        """

        self._avatar_url = avatar_url

    @property
    def can_change_password(self):
        """Gets the can_change_password of this UserProfileResponsev2.

        User is required to send an old password in order to change the password.

        :return: The can_change_password of this UserProfileResponsev2.
        :rtype: bool
        """
        return self._can_change_password

    @can_change_password.setter
    def can_change_password(self, can_change_password):
        """Sets the can_change_password of this UserProfileResponsev2.

        User is required to send an old password in order to change the password.

        :param can_change_password: The can_change_password of this UserProfileResponsev2.
        :type can_change_password: bool
        """

        self._can_change_password = can_change_password

    @property
    def created_at(self):
        """Gets the created_at of this UserProfileResponsev2.

        The created date of the user

        :return: The created_at of this UserProfileResponsev2.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this UserProfileResponsev2.

        The created date of the user

        :param created_at: The created_at of this UserProfileResponsev2.
        :type created_at: str
        """

        self._created_at = created_at

    @property
    def display_name(self):
        """Gets the display_name of this UserProfileResponsev2.

        The full name of the user. Might for example be first and last name

        :return: The display_name of this UserProfileResponsev2.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this UserProfileResponsev2.

        The full name of the user. Might for example be first and last name

        :param display_name: The display_name of this UserProfileResponsev2.
        :type display_name: str
        """
        if display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")

        self._display_name = display_name

    @property
    def email(self):
        """Gets the email of this UserProfileResponsev2.

        The email address of the user

        :return: The email of this UserProfileResponsev2.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserProfileResponsev2.

        The email address of the user

        :param email: The email of this UserProfileResponsev2.
        :type email: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")

        self._email = email

    @property
    def feature_flags(self):
        """Gets the feature_flags of this UserProfileResponsev2.

        The feature flags that are enabled for this user

        :return: The feature_flags of this UserProfileResponsev2.
        :rtype: List[str]
        """
        return self._feature_flags

    @feature_flags.setter
    def feature_flags(self, feature_flags):
        """Sets the feature_flags of this UserProfileResponsev2.

        The feature flags that are enabled for this user

        :param feature_flags: The feature_flags of this UserProfileResponsev2.
        :type feature_flags: List[str]
        """

        self._feature_flags = feature_flags

    @property
    def id(self):
        """Gets the id of this UserProfileResponsev2.

        The unique id (UUID) of the user

        :return: The id of this UserProfileResponsev2.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserProfileResponsev2.

        The unique id (UUID) of the user

        :param id: The id of this UserProfileResponsev2.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def name(self):
        """Gets the name of this UserProfileResponsev2.

        The unique name that is used to identify the user.

        :return: The name of this UserProfileResponsev2.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserProfileResponsev2.

        The unique name that is used to identify the user.

        :param name: The name of this UserProfileResponsev2.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def next_nps_survey_date(self):
        """Gets the next_nps_survey_date of this UserProfileResponsev2.

        The date in the future when the user should be checked again for NPS eligibility

        :return: The next_nps_survey_date of this UserProfileResponsev2.
        :rtype: str
        """
        return self._next_nps_survey_date

    @next_nps_survey_date.setter
    def next_nps_survey_date(self, next_nps_survey_date):
        """Sets the next_nps_survey_date of this UserProfileResponsev2.

        The date in the future when the user should be checked again for NPS eligibility

        :param next_nps_survey_date: The next_nps_survey_date of this UserProfileResponsev2.
        :type next_nps_survey_date: str
        """

        self._next_nps_survey_date = next_nps_survey_date

    @property
    def origin(self):
        """Gets the origin of this UserProfileResponsev2.

        The creation origin of this user

        :return: The origin of this UserProfileResponsev2.
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """Sets the origin of this UserProfileResponsev2.

        The creation origin of this user

        :param origin: The origin of this UserProfileResponsev2.
        :type origin: str
        """
        allowed_values = ["appcenter", "hockeyapp", "codepush"]  # noqa: E501
        if origin not in allowed_values:
            raise ValueError(
                "Invalid value for `origin` ({0}), must be one of {1}"
                .format(origin, allowed_values)
            )

        self._origin = origin

    @property
    def session_hash(self):
        """Gets the session_hash of this UserProfileResponsev2.

        The session hash of the user

        :return: The session_hash of this UserProfileResponsev2.
        :rtype: str
        """
        return self._session_hash

    @session_hash.setter
    def session_hash(self, session_hash):
        """Sets the session_hash of this UserProfileResponsev2.

        The session hash of the user

        :param session_hash: The session_hash of this UserProfileResponsev2.
        :type session_hash: str
        """

        self._session_hash = session_hash

    @property
    def settings(self):
        """Gets the settings of this UserProfileResponsev2.

        The user's settings

        :return: The settings of this UserProfileResponsev2.
        :rtype: object
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this UserProfileResponsev2.

        The user's settings

        :param settings: The settings of this UserProfileResponsev2.
        :type settings: object
        """

        self._settings = settings
