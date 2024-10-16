# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerSlotsInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, model: str=None, number: int=None, serial: str=None, status: str=None):
        """GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerSlotsInner - a model defined in OpenAPI

        :param model: The model of this GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerSlotsInner.
        :param number: The number of this GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerSlotsInner.
        :param serial: The serial of this GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerSlotsInner.
        :param status: The status of this GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerSlotsInner.
        """
        self.openapi_types = {
            'model': str,
            'number': int,
            'serial': str,
            'status': str
        }

        self.attribute_map = {
            'model': 'model',
            'number': 'number',
            'serial': 'serial',
            'status': 'status'
        }

        self._model = model
        self._number = number
        self._serial = serial
        self._status = status

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerSlotsInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The getOrganizationDevicesPowerModulesStatusesByDevice_200_response_inner_slots_inner of this GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerSlotsInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def model(self):
        """Gets the model of this GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerSlotsInner.

        The power supply unit model.

        :return: The model of this GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerSlotsInner.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerSlotsInner.

        The power supply unit model.

        :param model: The model of this GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerSlotsInner.
        :type model: str
        """

        self._model = model

    @property
    def number(self):
        """Gets the number of this GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerSlotsInner.

        Which slot the AC power supply occupies. Possible values are: 0, 1, 2.

        :return: The number of this GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerSlotsInner.
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerSlotsInner.

        Which slot the AC power supply occupies. Possible values are: 0, 1, 2.

        :param number: The number of this GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerSlotsInner.
        :type number: int
        """
        allowed_values = [0, 1, 2]  # noqa: E501
        if number not in allowed_values:
            raise ValueError(
                "Invalid value for `number` ({0}), must be one of {1}"
                .format(number, allowed_values)
            )

        self._number = number

    @property
    def serial(self):
        """Gets the serial of this GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerSlotsInner.

        The power supply unit serial number.

        :return: The serial of this GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerSlotsInner.
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """Sets the serial of this GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerSlotsInner.

        The power supply unit serial number.

        :param serial: The serial of this GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerSlotsInner.
        :type serial: str
        """

        self._serial = serial

    @property
    def status(self):
        """Gets the status of this GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerSlotsInner.

        Status of the power supply unit. Possible values are: connected, not connected, powering.

        :return: The status of this GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerSlotsInner.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerSlotsInner.

        Status of the power supply unit. Possible values are: connected, not connected, powering.

        :param status: The status of this GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerSlotsInner.
        :type status: str
        """
        allowed_values = ["connected", "not connected", "powering"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status
