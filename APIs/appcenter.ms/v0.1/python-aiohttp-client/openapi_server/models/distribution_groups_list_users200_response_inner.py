# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class DistributionGroupsListUsers200ResponseInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, avatar_url: str=None, can_change_password: bool=None, display_name: str=None, email: str=None, id: str=None, invite_pending: bool=None, name: str=None):
        """DistributionGroupsListUsers200ResponseInner - a model defined in OpenAPI

        :param avatar_url: The avatar_url of this DistributionGroupsListUsers200ResponseInner.
        :param can_change_password: The can_change_password of this DistributionGroupsListUsers200ResponseInner.
        :param display_name: The display_name of this DistributionGroupsListUsers200ResponseInner.
        :param email: The email of this DistributionGroupsListUsers200ResponseInner.
        :param id: The id of this DistributionGroupsListUsers200ResponseInner.
        :param invite_pending: The invite_pending of this DistributionGroupsListUsers200ResponseInner.
        :param name: The name of this DistributionGroupsListUsers200ResponseInner.
        """
        self.openapi_types = {
            'avatar_url': str,
            'can_change_password': bool,
            'display_name': str,
            'email': str,
            'id': str,
            'invite_pending': bool,
            'name': str
        }

        self.attribute_map = {
            'avatar_url': 'avatar_url',
            'can_change_password': 'can_change_password',
            'display_name': 'display_name',
            'email': 'email',
            'id': 'id',
            'invite_pending': 'invite_pending',
            'name': 'name'
        }

        self._avatar_url = avatar_url
        self._can_change_password = can_change_password
        self._display_name = display_name
        self._email = email
        self._id = id
        self._invite_pending = invite_pending
        self._name = name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'DistributionGroupsListUsers200ResponseInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The distributionGroups_listUsers_200_response_inner of this DistributionGroupsListUsers200ResponseInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def avatar_url(self):
        """Gets the avatar_url of this DistributionGroupsListUsers200ResponseInner.

        The avatar URL of the user

        :return: The avatar_url of this DistributionGroupsListUsers200ResponseInner.
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        """Sets the avatar_url of this DistributionGroupsListUsers200ResponseInner.

        The avatar URL of the user

        :param avatar_url: The avatar_url of this DistributionGroupsListUsers200ResponseInner.
        :type avatar_url: str
        """

        self._avatar_url = avatar_url

    @property
    def can_change_password(self):
        """Gets the can_change_password of this DistributionGroupsListUsers200ResponseInner.

        User is required to send an old password in order to change the password.

        :return: The can_change_password of this DistributionGroupsListUsers200ResponseInner.
        :rtype: bool
        """
        return self._can_change_password

    @can_change_password.setter
    def can_change_password(self, can_change_password):
        """Sets the can_change_password of this DistributionGroupsListUsers200ResponseInner.

        User is required to send an old password in order to change the password.

        :param can_change_password: The can_change_password of this DistributionGroupsListUsers200ResponseInner.
        :type can_change_password: bool
        """

        self._can_change_password = can_change_password

    @property
    def display_name(self):
        """Gets the display_name of this DistributionGroupsListUsers200ResponseInner.

        The full name of the user. Might for example be first and last name

        :return: The display_name of this DistributionGroupsListUsers200ResponseInner.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this DistributionGroupsListUsers200ResponseInner.

        The full name of the user. Might for example be first and last name

        :param display_name: The display_name of this DistributionGroupsListUsers200ResponseInner.
        :type display_name: str
        """

        self._display_name = display_name

    @property
    def email(self):
        """Gets the email of this DistributionGroupsListUsers200ResponseInner.

        The email address of the user

        :return: The email of this DistributionGroupsListUsers200ResponseInner.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this DistributionGroupsListUsers200ResponseInner.

        The email address of the user

        :param email: The email of this DistributionGroupsListUsers200ResponseInner.
        :type email: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")

        self._email = email

    @property
    def id(self):
        """Gets the id of this DistributionGroupsListUsers200ResponseInner.

        The unique id (UUID) of the user

        :return: The id of this DistributionGroupsListUsers200ResponseInner.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DistributionGroupsListUsers200ResponseInner.

        The unique id (UUID) of the user

        :param id: The id of this DistributionGroupsListUsers200ResponseInner.
        :type id: str
        """

        self._id = id

    @property
    def invite_pending(self):
        """Gets the invite_pending of this DistributionGroupsListUsers200ResponseInner.

        Whether the has accepted the invite. Available when an invite is pending, and the value will be \"true\".

        :return: The invite_pending of this DistributionGroupsListUsers200ResponseInner.
        :rtype: bool
        """
        return self._invite_pending

    @invite_pending.setter
    def invite_pending(self, invite_pending):
        """Sets the invite_pending of this DistributionGroupsListUsers200ResponseInner.

        Whether the has accepted the invite. Available when an invite is pending, and the value will be \"true\".

        :param invite_pending: The invite_pending of this DistributionGroupsListUsers200ResponseInner.
        :type invite_pending: bool
        """

        self._invite_pending = invite_pending

    @property
    def name(self):
        """Gets the name of this DistributionGroupsListUsers200ResponseInner.

        The unique name that is used to identify the user.

        :return: The name of this DistributionGroupsListUsers200ResponseInner.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DistributionGroupsListUsers200ResponseInner.

        The unique name that is used to identify the user.

        :param name: The name of this DistributionGroupsListUsers200ResponseInner.
        :type name: str
        """

        self._name = name
