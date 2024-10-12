# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class AdvancedLdapConfiguration(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, group_max_level: int=None, group_member_attribute: str=None, group_membership_attribute: str=None, group_search_filter: str=None, user_name_search_attribute: str=None, user_search_filter: str=None):
        """AdvancedLdapConfiguration - a model defined in OpenAPI

        :param group_max_level: The group_max_level of this AdvancedLdapConfiguration.
        :param group_member_attribute: The group_member_attribute of this AdvancedLdapConfiguration.
        :param group_membership_attribute: The group_membership_attribute of this AdvancedLdapConfiguration.
        :param group_search_filter: The group_search_filter of this AdvancedLdapConfiguration.
        :param user_name_search_attribute: The user_name_search_attribute of this AdvancedLdapConfiguration.
        :param user_search_filter: The user_search_filter of this AdvancedLdapConfiguration.
        """
        self.openapi_types = {
            'group_max_level': int,
            'group_member_attribute': str,
            'group_membership_attribute': str,
            'group_search_filter': str,
            'user_name_search_attribute': str,
            'user_search_filter': str
        }

        self.attribute_map = {
            'group_max_level': 'groupMaxLevel',
            'group_member_attribute': 'groupMemberAttribute',
            'group_membership_attribute': 'groupMembershipAttribute',
            'group_search_filter': 'groupSearchFilter',
            'user_name_search_attribute': 'userNameSearchAttribute',
            'user_search_filter': 'userSearchFilter'
        }

        self._group_max_level = group_max_level
        self._group_member_attribute = group_member_attribute
        self._group_membership_attribute = group_membership_attribute
        self._group_search_filter = group_search_filter
        self._user_name_search_attribute = user_name_search_attribute
        self._user_search_filter = user_search_filter

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AdvancedLdapConfiguration':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The AdvancedLdapConfiguration of this AdvancedLdapConfiguration.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def group_max_level(self):
        """Gets the group_max_level of this AdvancedLdapConfiguration.

        Maximum level of groups to query. Set to 1 to query the immediate groups to which a user belongs. Leave blank to query all the groups to which a user belongs. Valid values are between 1 and 50 inclusive. When ldapSearchAcrossIntegrations is set to be true, this value is ignored. When this value is set, then for this ldap service, ldapActiveDirectoryDisableMatchingRuleInChain is ignored and assumed to be true.

        :return: The group_max_level of this AdvancedLdapConfiguration.
        :rtype: int
        """
        return self._group_max_level

    @group_max_level.setter
    def group_max_level(self, group_max_level):
        """Sets the group_max_level of this AdvancedLdapConfiguration.

        Maximum level of groups to query. Set to 1 to query the immediate groups to which a user belongs. Leave blank to query all the groups to which a user belongs. Valid values are between 1 and 50 inclusive. When ldapSearchAcrossIntegrations is set to be true, this value is ignored. When this value is set, then for this ldap service, ldapActiveDirectoryDisableMatchingRuleInChain is ignored and assumed to be true.

        :param group_max_level: The group_max_level of this AdvancedLdapConfiguration.
        :type group_max_level: int
        """

        self._group_max_level = group_max_level

    @property
    def group_member_attribute(self):
        """Gets the group_member_attribute of this AdvancedLdapConfiguration.

        LDAP field that contains the group members. For example, Active Directory uses the field \"member\".

        :return: The group_member_attribute of this AdvancedLdapConfiguration.
        :rtype: str
        """
        return self._group_member_attribute

    @group_member_attribute.setter
    def group_member_attribute(self, group_member_attribute):
        """Sets the group_member_attribute of this AdvancedLdapConfiguration.

        LDAP field that contains the group members. For example, Active Directory uses the field \"member\".

        :param group_member_attribute: The group_member_attribute of this AdvancedLdapConfiguration.
        :type group_member_attribute: str
        """

        self._group_member_attribute = group_member_attribute

    @property
    def group_membership_attribute(self):
        """Gets the group_membership_attribute of this AdvancedLdapConfiguration.

        Points to the group that this entry belongs to. For example, Active Directory uses the field \"memberOf\".

        :return: The group_membership_attribute of this AdvancedLdapConfiguration.
        :rtype: str
        """
        return self._group_membership_attribute

    @group_membership_attribute.setter
    def group_membership_attribute(self, group_membership_attribute):
        """Sets the group_membership_attribute of this AdvancedLdapConfiguration.

        Points to the group that this entry belongs to. For example, Active Directory uses the field \"memberOf\".

        :param group_membership_attribute: The group_membership_attribute of this AdvancedLdapConfiguration.
        :type group_membership_attribute: str
        """

        self._group_membership_attribute = group_membership_attribute

    @property
    def group_search_filter(self):
        """Gets the group_search_filter of this AdvancedLdapConfiguration.

        A string representation of the LDAP group search filter in RFC4515 format. For example, a group search filter for Active Directory has the string representation (objectCategory=group).

        :return: The group_search_filter of this AdvancedLdapConfiguration.
        :rtype: str
        """
        return self._group_search_filter

    @group_search_filter.setter
    def group_search_filter(self, group_search_filter):
        """Sets the group_search_filter of this AdvancedLdapConfiguration.

        A string representation of the LDAP group search filter in RFC4515 format. For example, a group search filter for Active Directory has the string representation (objectCategory=group).

        :param group_search_filter: The group_search_filter of this AdvancedLdapConfiguration.
        :type group_search_filter: str
        """

        self._group_search_filter = group_search_filter

    @property
    def user_name_search_attribute(self):
        """Gets the user_name_search_attribute of this AdvancedLdapConfiguration.

        Specifies the user name. Active Directory searches can use the attributes sAMAccountName and userPrincipalName.

        :return: The user_name_search_attribute of this AdvancedLdapConfiguration.
        :rtype: str
        """
        return self._user_name_search_attribute

    @user_name_search_attribute.setter
    def user_name_search_attribute(self, user_name_search_attribute):
        """Sets the user_name_search_attribute of this AdvancedLdapConfiguration.

        Specifies the user name. Active Directory searches can use the attributes sAMAccountName and userPrincipalName.

        :param user_name_search_attribute: The user_name_search_attribute of this AdvancedLdapConfiguration.
        :type user_name_search_attribute: str
        """

        self._user_name_search_attribute = user_name_search_attribute

    @property
    def user_search_filter(self):
        """Gets the user_search_filter of this AdvancedLdapConfiguration.

        A string representation of the LDAP user search filter in RFC4515 format. For example, an Active Directory user search filter that selects all enabled user objects has the following string representation (&(objectCategory=person) (objectClass=user) (!(userAccountControl:1.2.840.113556.1.4.803:=2))).

        :return: The user_search_filter of this AdvancedLdapConfiguration.
        :rtype: str
        """
        return self._user_search_filter

    @user_search_filter.setter
    def user_search_filter(self, user_search_filter):
        """Sets the user_search_filter of this AdvancedLdapConfiguration.

        A string representation of the LDAP user search filter in RFC4515 format. For example, an Active Directory user search filter that selects all enabled user objects has the following string representation (&(objectCategory=person) (objectClass=user) (!(userAccountControl:1.2.840.113556.1.4.803:=2))).

        :param user_search_filter: The user_search_filter of this AdvancedLdapConfiguration.
        :type user_search_filter: str
        """

        self._user_search_filter = user_search_filter
