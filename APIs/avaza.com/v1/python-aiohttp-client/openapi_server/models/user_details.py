# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.role_details import RoleDetails
from openapi_server.models.user_tag_details import UserTagDetails
from openapi_server import util


class UserDetails(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, account_idfk: int=None, company_idfk: int=None, company_name: str=None, default_billable_rate: float=None, default_cost_rate: float=None, email: str=None, firstname: str=None, friday_available_hours: float=None, iana_timezone: str=None, lastname: str=None, mobile: str=None, monday_available_hours: float=None, phone: str=None, position_title: str=None, roles: List[RoleDetails]=None, saturday_available_hours: float=None, sunday_available_hours: float=None, tags: List[UserTagDetails]=None, thursday_available_hours: float=None, time_zone: str=None, tuesday_available_hours: float=None, user_id: int=None, wednesday_available_hours: float=None, is_team_member: bool=None):
        """UserDetails - a model defined in OpenAPI

        :param account_idfk: The account_idfk of this UserDetails.
        :param company_idfk: The company_idfk of this UserDetails.
        :param company_name: The company_name of this UserDetails.
        :param default_billable_rate: The default_billable_rate of this UserDetails.
        :param default_cost_rate: The default_cost_rate of this UserDetails.
        :param email: The email of this UserDetails.
        :param firstname: The firstname of this UserDetails.
        :param friday_available_hours: The friday_available_hours of this UserDetails.
        :param iana_timezone: The iana_timezone of this UserDetails.
        :param lastname: The lastname of this UserDetails.
        :param mobile: The mobile of this UserDetails.
        :param monday_available_hours: The monday_available_hours of this UserDetails.
        :param phone: The phone of this UserDetails.
        :param position_title: The position_title of this UserDetails.
        :param roles: The roles of this UserDetails.
        :param saturday_available_hours: The saturday_available_hours of this UserDetails.
        :param sunday_available_hours: The sunday_available_hours of this UserDetails.
        :param tags: The tags of this UserDetails.
        :param thursday_available_hours: The thursday_available_hours of this UserDetails.
        :param time_zone: The time_zone of this UserDetails.
        :param tuesday_available_hours: The tuesday_available_hours of this UserDetails.
        :param user_id: The user_id of this UserDetails.
        :param wednesday_available_hours: The wednesday_available_hours of this UserDetails.
        :param is_team_member: The is_team_member of this UserDetails.
        """
        self.openapi_types = {
            'account_idfk': int,
            'company_idfk': int,
            'company_name': str,
            'default_billable_rate': float,
            'default_cost_rate': float,
            'email': str,
            'firstname': str,
            'friday_available_hours': float,
            'iana_timezone': str,
            'lastname': str,
            'mobile': str,
            'monday_available_hours': float,
            'phone': str,
            'position_title': str,
            'roles': List[RoleDetails],
            'saturday_available_hours': float,
            'sunday_available_hours': float,
            'tags': List[UserTagDetails],
            'thursday_available_hours': float,
            'time_zone': str,
            'tuesday_available_hours': float,
            'user_id': int,
            'wednesday_available_hours': float,
            'is_team_member': bool
        }

        self.attribute_map = {
            'account_idfk': 'AccountIDFK',
            'company_idfk': 'CompanyIDFK',
            'company_name': 'CompanyName',
            'default_billable_rate': 'DefaultBillableRate',
            'default_cost_rate': 'DefaultCostRate',
            'email': 'Email',
            'firstname': 'Firstname',
            'friday_available_hours': 'FridayAvailableHours',
            'iana_timezone': 'IANATimezone',
            'lastname': 'Lastname',
            'mobile': 'Mobile',
            'monday_available_hours': 'MondayAvailableHours',
            'phone': 'Phone',
            'position_title': 'PositionTitle',
            'roles': 'Roles',
            'saturday_available_hours': 'SaturdayAvailableHours',
            'sunday_available_hours': 'SundayAvailableHours',
            'tags': 'Tags',
            'thursday_available_hours': 'ThursdayAvailableHours',
            'time_zone': 'TimeZone',
            'tuesday_available_hours': 'TuesdayAvailableHours',
            'user_id': 'UserID',
            'wednesday_available_hours': 'WednesdayAvailableHours',
            'is_team_member': 'isTeamMember'
        }

        self._account_idfk = account_idfk
        self._company_idfk = company_idfk
        self._company_name = company_name
        self._default_billable_rate = default_billable_rate
        self._default_cost_rate = default_cost_rate
        self._email = email
        self._firstname = firstname
        self._friday_available_hours = friday_available_hours
        self._iana_timezone = iana_timezone
        self._lastname = lastname
        self._mobile = mobile
        self._monday_available_hours = monday_available_hours
        self._phone = phone
        self._position_title = position_title
        self._roles = roles
        self._saturday_available_hours = saturday_available_hours
        self._sunday_available_hours = sunday_available_hours
        self._tags = tags
        self._thursday_available_hours = thursday_available_hours
        self._time_zone = time_zone
        self._tuesday_available_hours = tuesday_available_hours
        self._user_id = user_id
        self._wednesday_available_hours = wednesday_available_hours
        self._is_team_member = is_team_member

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UserDetails':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The UserDetails of this UserDetails.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def account_idfk(self):
        """Gets the account_idfk of this UserDetails.


        :return: The account_idfk of this UserDetails.
        :rtype: int
        """
        return self._account_idfk

    @account_idfk.setter
    def account_idfk(self, account_idfk):
        """Sets the account_idfk of this UserDetails.


        :param account_idfk: The account_idfk of this UserDetails.
        :type account_idfk: int
        """

        self._account_idfk = account_idfk

    @property
    def company_idfk(self):
        """Gets the company_idfk of this UserDetails.


        :return: The company_idfk of this UserDetails.
        :rtype: int
        """
        return self._company_idfk

    @company_idfk.setter
    def company_idfk(self, company_idfk):
        """Sets the company_idfk of this UserDetails.


        :param company_idfk: The company_idfk of this UserDetails.
        :type company_idfk: int
        """

        self._company_idfk = company_idfk

    @property
    def company_name(self):
        """Gets the company_name of this UserDetails.


        :return: The company_name of this UserDetails.
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this UserDetails.


        :param company_name: The company_name of this UserDetails.
        :type company_name: str
        """

        self._company_name = company_name

    @property
    def default_billable_rate(self):
        """Gets the default_billable_rate of this UserDetails.


        :return: The default_billable_rate of this UserDetails.
        :rtype: float
        """
        return self._default_billable_rate

    @default_billable_rate.setter
    def default_billable_rate(self, default_billable_rate):
        """Sets the default_billable_rate of this UserDetails.


        :param default_billable_rate: The default_billable_rate of this UserDetails.
        :type default_billable_rate: float
        """

        self._default_billable_rate = default_billable_rate

    @property
    def default_cost_rate(self):
        """Gets the default_cost_rate of this UserDetails.


        :return: The default_cost_rate of this UserDetails.
        :rtype: float
        """
        return self._default_cost_rate

    @default_cost_rate.setter
    def default_cost_rate(self, default_cost_rate):
        """Sets the default_cost_rate of this UserDetails.


        :param default_cost_rate: The default_cost_rate of this UserDetails.
        :type default_cost_rate: float
        """

        self._default_cost_rate = default_cost_rate

    @property
    def email(self):
        """Gets the email of this UserDetails.


        :return: The email of this UserDetails.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserDetails.


        :param email: The email of this UserDetails.
        :type email: str
        """

        self._email = email

    @property
    def firstname(self):
        """Gets the firstname of this UserDetails.


        :return: The firstname of this UserDetails.
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """Sets the firstname of this UserDetails.


        :param firstname: The firstname of this UserDetails.
        :type firstname: str
        """

        self._firstname = firstname

    @property
    def friday_available_hours(self):
        """Gets the friday_available_hours of this UserDetails.


        :return: The friday_available_hours of this UserDetails.
        :rtype: float
        """
        return self._friday_available_hours

    @friday_available_hours.setter
    def friday_available_hours(self, friday_available_hours):
        """Sets the friday_available_hours of this UserDetails.


        :param friday_available_hours: The friday_available_hours of this UserDetails.
        :type friday_available_hours: float
        """

        self._friday_available_hours = friday_available_hours

    @property
    def iana_timezone(self):
        """Gets the iana_timezone of this UserDetails.

        IANA tz database timezone name

        :return: The iana_timezone of this UserDetails.
        :rtype: str
        """
        return self._iana_timezone

    @iana_timezone.setter
    def iana_timezone(self, iana_timezone):
        """Sets the iana_timezone of this UserDetails.

        IANA tz database timezone name

        :param iana_timezone: The iana_timezone of this UserDetails.
        :type iana_timezone: str
        """

        self._iana_timezone = iana_timezone

    @property
    def lastname(self):
        """Gets the lastname of this UserDetails.


        :return: The lastname of this UserDetails.
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """Sets the lastname of this UserDetails.


        :param lastname: The lastname of this UserDetails.
        :type lastname: str
        """

        self._lastname = lastname

    @property
    def mobile(self):
        """Gets the mobile of this UserDetails.


        :return: The mobile of this UserDetails.
        :rtype: str
        """
        return self._mobile

    @mobile.setter
    def mobile(self, mobile):
        """Sets the mobile of this UserDetails.


        :param mobile: The mobile of this UserDetails.
        :type mobile: str
        """

        self._mobile = mobile

    @property
    def monday_available_hours(self):
        """Gets the monday_available_hours of this UserDetails.


        :return: The monday_available_hours of this UserDetails.
        :rtype: float
        """
        return self._monday_available_hours

    @monday_available_hours.setter
    def monday_available_hours(self, monday_available_hours):
        """Sets the monday_available_hours of this UserDetails.


        :param monday_available_hours: The monday_available_hours of this UserDetails.
        :type monday_available_hours: float
        """

        self._monday_available_hours = monday_available_hours

    @property
    def phone(self):
        """Gets the phone of this UserDetails.


        :return: The phone of this UserDetails.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this UserDetails.


        :param phone: The phone of this UserDetails.
        :type phone: str
        """

        self._phone = phone

    @property
    def position_title(self):
        """Gets the position_title of this UserDetails.


        :return: The position_title of this UserDetails.
        :rtype: str
        """
        return self._position_title

    @position_title.setter
    def position_title(self, position_title):
        """Sets the position_title of this UserDetails.


        :param position_title: The position_title of this UserDetails.
        :type position_title: str
        """

        self._position_title = position_title

    @property
    def roles(self):
        """Gets the roles of this UserDetails.


        :return: The roles of this UserDetails.
        :rtype: List[RoleDetails]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this UserDetails.


        :param roles: The roles of this UserDetails.
        :type roles: List[RoleDetails]
        """

        self._roles = roles

    @property
    def saturday_available_hours(self):
        """Gets the saturday_available_hours of this UserDetails.


        :return: The saturday_available_hours of this UserDetails.
        :rtype: float
        """
        return self._saturday_available_hours

    @saturday_available_hours.setter
    def saturday_available_hours(self, saturday_available_hours):
        """Sets the saturday_available_hours of this UserDetails.


        :param saturday_available_hours: The saturday_available_hours of this UserDetails.
        :type saturday_available_hours: float
        """

        self._saturday_available_hours = saturday_available_hours

    @property
    def sunday_available_hours(self):
        """Gets the sunday_available_hours of this UserDetails.


        :return: The sunday_available_hours of this UserDetails.
        :rtype: float
        """
        return self._sunday_available_hours

    @sunday_available_hours.setter
    def sunday_available_hours(self, sunday_available_hours):
        """Sets the sunday_available_hours of this UserDetails.


        :param sunday_available_hours: The sunday_available_hours of this UserDetails.
        :type sunday_available_hours: float
        """

        self._sunday_available_hours = sunday_available_hours

    @property
    def tags(self):
        """Gets the tags of this UserDetails.


        :return: The tags of this UserDetails.
        :rtype: List[UserTagDetails]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this UserDetails.


        :param tags: The tags of this UserDetails.
        :type tags: List[UserTagDetails]
        """

        self._tags = tags

    @property
    def thursday_available_hours(self):
        """Gets the thursday_available_hours of this UserDetails.


        :return: The thursday_available_hours of this UserDetails.
        :rtype: float
        """
        return self._thursday_available_hours

    @thursday_available_hours.setter
    def thursday_available_hours(self, thursday_available_hours):
        """Sets the thursday_available_hours of this UserDetails.


        :param thursday_available_hours: The thursday_available_hours of this UserDetails.
        :type thursday_available_hours: float
        """

        self._thursday_available_hours = thursday_available_hours

    @property
    def time_zone(self):
        """Gets the time_zone of this UserDetails.

        Windows Timezone ID

        :return: The time_zone of this UserDetails.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this UserDetails.

        Windows Timezone ID

        :param time_zone: The time_zone of this UserDetails.
        :type time_zone: str
        """

        self._time_zone = time_zone

    @property
    def tuesday_available_hours(self):
        """Gets the tuesday_available_hours of this UserDetails.


        :return: The tuesday_available_hours of this UserDetails.
        :rtype: float
        """
        return self._tuesday_available_hours

    @tuesday_available_hours.setter
    def tuesday_available_hours(self, tuesday_available_hours):
        """Sets the tuesday_available_hours of this UserDetails.


        :param tuesday_available_hours: The tuesday_available_hours of this UserDetails.
        :type tuesday_available_hours: float
        """

        self._tuesday_available_hours = tuesday_available_hours

    @property
    def user_id(self):
        """Gets the user_id of this UserDetails.


        :return: The user_id of this UserDetails.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this UserDetails.


        :param user_id: The user_id of this UserDetails.
        :type user_id: int
        """

        self._user_id = user_id

    @property
    def wednesday_available_hours(self):
        """Gets the wednesday_available_hours of this UserDetails.


        :return: The wednesday_available_hours of this UserDetails.
        :rtype: float
        """
        return self._wednesday_available_hours

    @wednesday_available_hours.setter
    def wednesday_available_hours(self, wednesday_available_hours):
        """Sets the wednesday_available_hours of this UserDetails.


        :param wednesday_available_hours: The wednesday_available_hours of this UserDetails.
        :type wednesday_available_hours: float
        """

        self._wednesday_available_hours = wednesday_available_hours

    @property
    def is_team_member(self):
        """Gets the is_team_member of this UserDetails.


        :return: The is_team_member of this UserDetails.
        :rtype: bool
        """
        return self._is_team_member

    @is_team_member.setter
    def is_team_member(self, is_team_member):
        """Sets the is_team_member of this UserDetails.


        :param is_team_member: The is_team_member of this UserDetails.
        :type is_team_member: bool
        """

        self._is_team_member = is_team_member
