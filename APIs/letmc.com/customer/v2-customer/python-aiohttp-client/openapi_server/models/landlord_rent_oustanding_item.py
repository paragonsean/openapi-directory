# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class LandlordRentOustandingItem(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, debt_days: int=None, outstanding_rent: float=None, _property: str=None, tenant: str=None, tenant_id: str=None):
        """LandlordRentOustandingItem - a model defined in OpenAPI

        :param debt_days: The debt_days of this LandlordRentOustandingItem.
        :param outstanding_rent: The outstanding_rent of this LandlordRentOustandingItem.
        :param _property: The _property of this LandlordRentOustandingItem.
        :param tenant: The tenant of this LandlordRentOustandingItem.
        :param tenant_id: The tenant_id of this LandlordRentOustandingItem.
        """
        self.openapi_types = {
            'debt_days': int,
            'outstanding_rent': float,
            '_property': str,
            'tenant': str,
            'tenant_id': str
        }

        self.attribute_map = {
            'debt_days': 'DebtDays',
            'outstanding_rent': 'OutstandingRent',
            '_property': 'Property',
            'tenant': 'Tenant',
            'tenant_id': 'TenantID'
        }

        self._debt_days = debt_days
        self._outstanding_rent = outstanding_rent
        self.__property = _property
        self._tenant = tenant
        self._tenant_id = tenant_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'LandlordRentOustandingItem':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The LandlordRentOustandingItem of this LandlordRentOustandingItem.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def debt_days(self):
        """Gets the debt_days of this LandlordRentOustandingItem.

        Days since the tenant went into arrears

        :return: The debt_days of this LandlordRentOustandingItem.
        :rtype: int
        """
        return self._debt_days

    @debt_days.setter
    def debt_days(self, debt_days):
        """Sets the debt_days of this LandlordRentOustandingItem.

        Days since the tenant went into arrears

        :param debt_days: The debt_days of this LandlordRentOustandingItem.
        :type debt_days: int
        """

        self._debt_days = debt_days

    @property
    def outstanding_rent(self):
        """Gets the outstanding_rent of this LandlordRentOustandingItem.

        Outstanding Rent

        :return: The outstanding_rent of this LandlordRentOustandingItem.
        :rtype: float
        """
        return self._outstanding_rent

    @outstanding_rent.setter
    def outstanding_rent(self, outstanding_rent):
        """Sets the outstanding_rent of this LandlordRentOustandingItem.

        Outstanding Rent

        :param outstanding_rent: The outstanding_rent of this LandlordRentOustandingItem.
        :type outstanding_rent: float
        """

        self._outstanding_rent = outstanding_rent

    @property
    def _property(self):
        """Gets the _property of this LandlordRentOustandingItem.

        Property

        :return: The _property of this LandlordRentOustandingItem.
        :rtype: str
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        """Sets the _property of this LandlordRentOustandingItem.

        Property

        :param _property: The _property of this LandlordRentOustandingItem.
        :type _property: str
        """

        self.__property = _property

    @property
    def tenant(self):
        """Gets the tenant of this LandlordRentOustandingItem.

        Tenant

        :return: The tenant of this LandlordRentOustandingItem.
        :rtype: str
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """Sets the tenant of this LandlordRentOustandingItem.

        Tenant

        :param tenant: The tenant of this LandlordRentOustandingItem.
        :type tenant: str
        """

        self._tenant = tenant

    @property
    def tenant_id(self):
        """Gets the tenant_id of this LandlordRentOustandingItem.

        TenantID

        :return: The tenant_id of this LandlordRentOustandingItem.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this LandlordRentOustandingItem.

        TenantID

        :param tenant_id: The tenant_id of this LandlordRentOustandingItem.
        :type tenant_id: str
        """

        self._tenant_id = tenant_id
