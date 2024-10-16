# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.distribution_groups_list_users200_response_inner import DistributionGroupsListUsers200ResponseInner
from openapi_server import util


class DistributionGroupDetailsResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, display_name: str=None, id: str=None, is_public: bool=None, name: str=None, origin: str=None, group_type: str=None, is_shared: bool=None, notified_user_count: float=None, total_apps_count: float=None, total_user_count: float=None, users: List[DistributionGroupsListUsers200ResponseInner]=None):
        """DistributionGroupDetailsResponse - a model defined in OpenAPI

        :param display_name: The display_name of this DistributionGroupDetailsResponse.
        :param id: The id of this DistributionGroupDetailsResponse.
        :param is_public: The is_public of this DistributionGroupDetailsResponse.
        :param name: The name of this DistributionGroupDetailsResponse.
        :param origin: The origin of this DistributionGroupDetailsResponse.
        :param group_type: The group_type of this DistributionGroupDetailsResponse.
        :param is_shared: The is_shared of this DistributionGroupDetailsResponse.
        :param notified_user_count: The notified_user_count of this DistributionGroupDetailsResponse.
        :param total_apps_count: The total_apps_count of this DistributionGroupDetailsResponse.
        :param total_user_count: The total_user_count of this DistributionGroupDetailsResponse.
        :param users: The users of this DistributionGroupDetailsResponse.
        """
        self.openapi_types = {
            'display_name': str,
            'id': str,
            'is_public': bool,
            'name': str,
            'origin': str,
            'group_type': str,
            'is_shared': bool,
            'notified_user_count': float,
            'total_apps_count': float,
            'total_user_count': float,
            'users': List[DistributionGroupsListUsers200ResponseInner]
        }

        self.attribute_map = {
            'display_name': 'display_name',
            'id': 'id',
            'is_public': 'is_public',
            'name': 'name',
            'origin': 'origin',
            'group_type': 'group_type',
            'is_shared': 'is_shared',
            'notified_user_count': 'notified_user_count',
            'total_apps_count': 'total_apps_count',
            'total_user_count': 'total_user_count',
            'users': 'users'
        }

        self._display_name = display_name
        self._id = id
        self._is_public = is_public
        self._name = name
        self._origin = origin
        self._group_type = group_type
        self._is_shared = is_shared
        self._notified_user_count = notified_user_count
        self._total_apps_count = total_apps_count
        self._total_user_count = total_user_count
        self._users = users

    @classmethod
    def from_dict(cls, dikt: dict) -> 'DistributionGroupDetailsResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The DistributionGroupDetailsResponse of this DistributionGroupDetailsResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def display_name(self):
        """Gets the display_name of this DistributionGroupDetailsResponse.

        The name of the distribution group

        :return: The display_name of this DistributionGroupDetailsResponse.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this DistributionGroupDetailsResponse.

        The name of the distribution group

        :param display_name: The display_name of this DistributionGroupDetailsResponse.
        :type display_name: str
        """

        self._display_name = display_name

    @property
    def id(self):
        """Gets the id of this DistributionGroupDetailsResponse.

        The unique ID of the distribution group

        :return: The id of this DistributionGroupDetailsResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DistributionGroupDetailsResponse.

        The unique ID of the distribution group

        :param id: The id of this DistributionGroupDetailsResponse.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def is_public(self):
        """Gets the is_public of this DistributionGroupDetailsResponse.

        Whether the distribution group is public

        :return: The is_public of this DistributionGroupDetailsResponse.
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """Sets the is_public of this DistributionGroupDetailsResponse.

        Whether the distribution group is public

        :param is_public: The is_public of this DistributionGroupDetailsResponse.
        :type is_public: bool
        """
        if is_public is None:
            raise ValueError("Invalid value for `is_public`, must not be `None`")

        self._is_public = is_public

    @property
    def name(self):
        """Gets the name of this DistributionGroupDetailsResponse.

        The name of the distribution group used in URLs

        :return: The name of this DistributionGroupDetailsResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DistributionGroupDetailsResponse.

        The name of the distribution group used in URLs

        :param name: The name of this DistributionGroupDetailsResponse.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def origin(self):
        """Gets the origin of this DistributionGroupDetailsResponse.

        The creation origin of this distribution group

        :return: The origin of this DistributionGroupDetailsResponse.
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """Sets the origin of this DistributionGroupDetailsResponse.

        The creation origin of this distribution group

        :param origin: The origin of this DistributionGroupDetailsResponse.
        :type origin: str
        """
        allowed_values = ["appcenter", "hockeyapp"]  # noqa: E501
        if origin not in allowed_values:
            raise ValueError(
                "Invalid value for `origin` ({0}), must be one of {1}"
                .format(origin, allowed_values)
            )

        self._origin = origin

    @property
    def group_type(self):
        """Gets the group_type of this DistributionGroupDetailsResponse.

        Type of group (Default, HockeyAppDefault or MicrosoftDogfooding)

        :return: The group_type of this DistributionGroupDetailsResponse.
        :rtype: str
        """
        return self._group_type

    @group_type.setter
    def group_type(self, group_type):
        """Sets the group_type of this DistributionGroupDetailsResponse.

        Type of group (Default, HockeyAppDefault or MicrosoftDogfooding)

        :param group_type: The group_type of this DistributionGroupDetailsResponse.
        :type group_type: str
        """
        allowed_values = ["Default", "HockeyAppDefault", "MicrosoftDogfooding"]  # noqa: E501
        if group_type not in allowed_values:
            raise ValueError(
                "Invalid value for `group_type` ({0}), must be one of {1}"
                .format(group_type, allowed_values)
            )

        self._group_type = group_type

    @property
    def is_shared(self):
        """Gets the is_shared of this DistributionGroupDetailsResponse.

        Whether the distribution group is shared group or not

        :return: The is_shared of this DistributionGroupDetailsResponse.
        :rtype: bool
        """
        return self._is_shared

    @is_shared.setter
    def is_shared(self, is_shared):
        """Sets the is_shared of this DistributionGroupDetailsResponse.

        Whether the distribution group is shared group or not

        :param is_shared: The is_shared of this DistributionGroupDetailsResponse.
        :type is_shared: bool
        """
        if is_shared is None:
            raise ValueError("Invalid value for `is_shared`, must not be `None`")

        self._is_shared = is_shared

    @property
    def notified_user_count(self):
        """Gets the notified_user_count of this DistributionGroupDetailsResponse.

        The count of non-pending users in the distribution group who will be notified by new releases

        :return: The notified_user_count of this DistributionGroupDetailsResponse.
        :rtype: float
        """
        return self._notified_user_count

    @notified_user_count.setter
    def notified_user_count(self, notified_user_count):
        """Sets the notified_user_count of this DistributionGroupDetailsResponse.

        The count of non-pending users in the distribution group who will be notified by new releases

        :param notified_user_count: The notified_user_count of this DistributionGroupDetailsResponse.
        :type notified_user_count: float
        """
        if notified_user_count is None:
            raise ValueError("Invalid value for `notified_user_count`, must not be `None`")

        self._notified_user_count = notified_user_count

    @property
    def total_apps_count(self):
        """Gets the total_apps_count of this DistributionGroupDetailsResponse.

        The count of apps associated with this distribution group

        :return: The total_apps_count of this DistributionGroupDetailsResponse.
        :rtype: float
        """
        return self._total_apps_count

    @total_apps_count.setter
    def total_apps_count(self, total_apps_count):
        """Sets the total_apps_count of this DistributionGroupDetailsResponse.

        The count of apps associated with this distribution group

        :param total_apps_count: The total_apps_count of this DistributionGroupDetailsResponse.
        :type total_apps_count: float
        """
        if total_apps_count is None:
            raise ValueError("Invalid value for `total_apps_count`, must not be `None`")

        self._total_apps_count = total_apps_count

    @property
    def total_user_count(self):
        """Gets the total_user_count of this DistributionGroupDetailsResponse.

        The count of users in the distribution group

        :return: The total_user_count of this DistributionGroupDetailsResponse.
        :rtype: float
        """
        return self._total_user_count

    @total_user_count.setter
    def total_user_count(self, total_user_count):
        """Sets the total_user_count of this DistributionGroupDetailsResponse.

        The count of users in the distribution group

        :param total_user_count: The total_user_count of this DistributionGroupDetailsResponse.
        :type total_user_count: float
        """
        if total_user_count is None:
            raise ValueError("Invalid value for `total_user_count`, must not be `None`")

        self._total_user_count = total_user_count

    @property
    def users(self):
        """Gets the users of this DistributionGroupDetailsResponse.

        The distribution group users

        :return: The users of this DistributionGroupDetailsResponse.
        :rtype: List[DistributionGroupsListUsers200ResponseInner]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this DistributionGroupDetailsResponse.

        The distribution group users

        :param users: The users of this DistributionGroupDetailsResponse.
        :type users: List[DistributionGroupsListUsers200ResponseInner]
        """
        if users is None:
            raise ValueError("Invalid value for `users`, must not be `None`")

        self._users = users
