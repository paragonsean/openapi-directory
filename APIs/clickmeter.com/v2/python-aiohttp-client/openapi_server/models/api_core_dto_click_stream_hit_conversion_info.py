# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ApiCoreDtoClickStreamHitConversionInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, access_time: str=None, comcost: float=None, cost: float=None, _date: str=None, deleted: bool=None, id: int=None, name: str=None, parameter: str=None, value: float=None):
        """ApiCoreDtoClickStreamHitConversionInfo - a model defined in OpenAPI

        :param access_time: The access_time of this ApiCoreDtoClickStreamHitConversionInfo.
        :param comcost: The comcost of this ApiCoreDtoClickStreamHitConversionInfo.
        :param cost: The cost of this ApiCoreDtoClickStreamHitConversionInfo.
        :param _date: The _date of this ApiCoreDtoClickStreamHitConversionInfo.
        :param deleted: The deleted of this ApiCoreDtoClickStreamHitConversionInfo.
        :param id: The id of this ApiCoreDtoClickStreamHitConversionInfo.
        :param name: The name of this ApiCoreDtoClickStreamHitConversionInfo.
        :param parameter: The parameter of this ApiCoreDtoClickStreamHitConversionInfo.
        :param value: The value of this ApiCoreDtoClickStreamHitConversionInfo.
        """
        self.openapi_types = {
            'access_time': str,
            'comcost': float,
            'cost': float,
            '_date': str,
            'deleted': bool,
            'id': int,
            'name': str,
            'parameter': str,
            'value': float
        }

        self.attribute_map = {
            'access_time': 'accessTime',
            'comcost': 'comcost',
            'cost': 'cost',
            '_date': 'date',
            'deleted': 'deleted',
            'id': 'id',
            'name': 'name',
            'parameter': 'parameter',
            'value': 'value'
        }

        self._access_time = access_time
        self._comcost = comcost
        self._cost = cost
        self.__date = _date
        self._deleted = deleted
        self._id = id
        self._name = name
        self._parameter = parameter
        self._value = value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ApiCoreDtoClickStreamHitConversionInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Api.Core.Dto.ClickStream.HitConversionInfo of this ApiCoreDtoClickStreamHitConversionInfo.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def access_time(self):
        """Gets the access_time of this ApiCoreDtoClickStreamHitConversionInfo.

         (A date in \"YmdHis\" format)

        :return: The access_time of this ApiCoreDtoClickStreamHitConversionInfo.
        :rtype: str
        """
        return self._access_time

    @access_time.setter
    def access_time(self, access_time):
        """Sets the access_time of this ApiCoreDtoClickStreamHitConversionInfo.

         (A date in \"YmdHis\" format)

        :param access_time: The access_time of this ApiCoreDtoClickStreamHitConversionInfo.
        :type access_time: str
        """

        self._access_time = access_time

    @property
    def comcost(self):
        """Gets the comcost of this ApiCoreDtoClickStreamHitConversionInfo.


        :return: The comcost of this ApiCoreDtoClickStreamHitConversionInfo.
        :rtype: float
        """
        return self._comcost

    @comcost.setter
    def comcost(self, comcost):
        """Sets the comcost of this ApiCoreDtoClickStreamHitConversionInfo.


        :param comcost: The comcost of this ApiCoreDtoClickStreamHitConversionInfo.
        :type comcost: float
        """

        self._comcost = comcost

    @property
    def cost(self):
        """Gets the cost of this ApiCoreDtoClickStreamHitConversionInfo.


        :return: The cost of this ApiCoreDtoClickStreamHitConversionInfo.
        :rtype: float
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """Sets the cost of this ApiCoreDtoClickStreamHitConversionInfo.


        :param cost: The cost of this ApiCoreDtoClickStreamHitConversionInfo.
        :type cost: float
        """

        self._cost = cost

    @property
    def _date(self):
        """Gets the _date of this ApiCoreDtoClickStreamHitConversionInfo.

         (A date in \"YmdHis\" format)

        :return: The _date of this ApiCoreDtoClickStreamHitConversionInfo.
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this ApiCoreDtoClickStreamHitConversionInfo.

         (A date in \"YmdHis\" format)

        :param _date: The _date of this ApiCoreDtoClickStreamHitConversionInfo.
        :type _date: str
        """

        self.__date = _date

    @property
    def deleted(self):
        """Gets the deleted of this ApiCoreDtoClickStreamHitConversionInfo.


        :return: The deleted of this ApiCoreDtoClickStreamHitConversionInfo.
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this ApiCoreDtoClickStreamHitConversionInfo.


        :param deleted: The deleted of this ApiCoreDtoClickStreamHitConversionInfo.
        :type deleted: bool
        """

        self._deleted = deleted

    @property
    def id(self):
        """Gets the id of this ApiCoreDtoClickStreamHitConversionInfo.


        :return: The id of this ApiCoreDtoClickStreamHitConversionInfo.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiCoreDtoClickStreamHitConversionInfo.


        :param id: The id of this ApiCoreDtoClickStreamHitConversionInfo.
        :type id: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ApiCoreDtoClickStreamHitConversionInfo.


        :return: The name of this ApiCoreDtoClickStreamHitConversionInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiCoreDtoClickStreamHitConversionInfo.


        :param name: The name of this ApiCoreDtoClickStreamHitConversionInfo.
        :type name: str
        """

        self._name = name

    @property
    def parameter(self):
        """Gets the parameter of this ApiCoreDtoClickStreamHitConversionInfo.


        :return: The parameter of this ApiCoreDtoClickStreamHitConversionInfo.
        :rtype: str
        """
        return self._parameter

    @parameter.setter
    def parameter(self, parameter):
        """Sets the parameter of this ApiCoreDtoClickStreamHitConversionInfo.


        :param parameter: The parameter of this ApiCoreDtoClickStreamHitConversionInfo.
        :type parameter: str
        """

        self._parameter = parameter

    @property
    def value(self):
        """Gets the value of this ApiCoreDtoClickStreamHitConversionInfo.


        :return: The value of this ApiCoreDtoClickStreamHitConversionInfo.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ApiCoreDtoClickStreamHitConversionInfo.


        :param value: The value of this ApiCoreDtoClickStreamHitConversionInfo.
        :type value: float
        """

        self._value = value
