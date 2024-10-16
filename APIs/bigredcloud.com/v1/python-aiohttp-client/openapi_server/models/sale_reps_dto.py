# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class SaleRepsDto(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, code: str=None, company_id: int=None, email: str=None, id: int=None, name: str=None, phone: str=None, time_stamp: str=None):
        """SaleRepsDto - a model defined in OpenAPI

        :param code: The code of this SaleRepsDto.
        :param company_id: The company_id of this SaleRepsDto.
        :param email: The email of this SaleRepsDto.
        :param id: The id of this SaleRepsDto.
        :param name: The name of this SaleRepsDto.
        :param phone: The phone of this SaleRepsDto.
        :param time_stamp: The time_stamp of this SaleRepsDto.
        """
        self.openapi_types = {
            'code': str,
            'company_id': int,
            'email': str,
            'id': int,
            'name': str,
            'phone': str,
            'time_stamp': str
        }

        self.attribute_map = {
            'code': 'code',
            'company_id': 'companyId',
            'email': 'email',
            'id': 'id',
            'name': 'name',
            'phone': 'phone',
            'time_stamp': 'timeStamp'
        }

        self._code = code
        self._company_id = company_id
        self._email = email
        self._id = id
        self._name = name
        self._phone = phone
        self._time_stamp = time_stamp

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SaleRepsDto':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The SaleRepsDto of this SaleRepsDto.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self):
        """Gets the code of this SaleRepsDto.


        :return: The code of this SaleRepsDto.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this SaleRepsDto.


        :param code: The code of this SaleRepsDto.
        :type code: str
        """

        self._code = code

    @property
    def company_id(self):
        """Gets the company_id of this SaleRepsDto.


        :return: The company_id of this SaleRepsDto.
        :rtype: int
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id):
        """Sets the company_id of this SaleRepsDto.


        :param company_id: The company_id of this SaleRepsDto.
        :type company_id: int
        """

        self._company_id = company_id

    @property
    def email(self):
        """Gets the email of this SaleRepsDto.


        :return: The email of this SaleRepsDto.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this SaleRepsDto.


        :param email: The email of this SaleRepsDto.
        :type email: str
        """

        self._email = email

    @property
    def id(self):
        """Gets the id of this SaleRepsDto.


        :return: The id of this SaleRepsDto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SaleRepsDto.


        :param id: The id of this SaleRepsDto.
        :type id: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this SaleRepsDto.


        :return: The name of this SaleRepsDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SaleRepsDto.


        :param name: The name of this SaleRepsDto.
        :type name: str
        """

        self._name = name

    @property
    def phone(self):
        """Gets the phone of this SaleRepsDto.


        :return: The phone of this SaleRepsDto.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this SaleRepsDto.


        :param phone: The phone of this SaleRepsDto.
        :type phone: str
        """

        self._phone = phone

    @property
    def time_stamp(self):
        """Gets the time_stamp of this SaleRepsDto.


        :return: The time_stamp of this SaleRepsDto.
        :rtype: str
        """
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp):
        """Sets the time_stamp of this SaleRepsDto.


        :param time_stamp: The time_stamp of this SaleRepsDto.
        :type time_stamp: str
        """

        self._time_stamp = time_stamp
