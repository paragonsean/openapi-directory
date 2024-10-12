# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.latest_operation_result import LatestOperationResult
from openapi_server.models.virtual_machine_details import VirtualMachineDetails
from openapi_server import util


class EnvironmentDetails(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, description: str=None, environment_state: str=None, id: str=None, latest_operation_result: LatestOperationResult=None, name: str=None, password_last_reset: datetime=None, provisioning_state: str=None, total_usage: str=None, virtual_machine_details: VirtualMachineDetails=None):
        """EnvironmentDetails - a model defined in OpenAPI

        :param description: The description of this EnvironmentDetails.
        :param environment_state: The environment_state of this EnvironmentDetails.
        :param id: The id of this EnvironmentDetails.
        :param latest_operation_result: The latest_operation_result of this EnvironmentDetails.
        :param name: The name of this EnvironmentDetails.
        :param password_last_reset: The password_last_reset of this EnvironmentDetails.
        :param provisioning_state: The provisioning_state of this EnvironmentDetails.
        :param total_usage: The total_usage of this EnvironmentDetails.
        :param virtual_machine_details: The virtual_machine_details of this EnvironmentDetails.
        """
        self.openapi_types = {
            'description': str,
            'environment_state': str,
            'id': str,
            'latest_operation_result': LatestOperationResult,
            'name': str,
            'password_last_reset': datetime,
            'provisioning_state': str,
            'total_usage': str,
            'virtual_machine_details': VirtualMachineDetails
        }

        self.attribute_map = {
            'description': 'description',
            'environment_state': 'environmentState',
            'id': 'id',
            'latest_operation_result': 'latestOperationResult',
            'name': 'name',
            'password_last_reset': 'passwordLastReset',
            'provisioning_state': 'provisioningState',
            'total_usage': 'totalUsage',
            'virtual_machine_details': 'virtualMachineDetails'
        }

        self._description = description
        self._environment_state = environment_state
        self._id = id
        self._latest_operation_result = latest_operation_result
        self._name = name
        self._password_last_reset = password_last_reset
        self._provisioning_state = provisioning_state
        self._total_usage = total_usage
        self._virtual_machine_details = virtual_machine_details

    @classmethod
    def from_dict(cls, dikt: dict) -> 'EnvironmentDetails':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The EnvironmentDetails of this EnvironmentDetails.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def description(self):
        """Gets the description of this EnvironmentDetails.

        Description of the Environment

        :return: The description of this EnvironmentDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EnvironmentDetails.

        Description of the Environment

        :param description: The description of this EnvironmentDetails.
        :type description: str
        """

        self._description = description

    @property
    def environment_state(self):
        """Gets the environment_state of this EnvironmentDetails.

        Publishing state of the environment setting Possible values are Creating, Created, Failed

        :return: The environment_state of this EnvironmentDetails.
        :rtype: str
        """
        return self._environment_state

    @environment_state.setter
    def environment_state(self, environment_state):
        """Sets the environment_state of this EnvironmentDetails.

        Publishing state of the environment setting Possible values are Creating, Created, Failed

        :param environment_state: The environment_state of this EnvironmentDetails.
        :type environment_state: str
        """

        self._environment_state = environment_state

    @property
    def id(self):
        """Gets the id of this EnvironmentDetails.

        Resource Id of the environment

        :return: The id of this EnvironmentDetails.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EnvironmentDetails.

        Resource Id of the environment

        :param id: The id of this EnvironmentDetails.
        :type id: str
        """

        self._id = id

    @property
    def latest_operation_result(self):
        """Gets the latest_operation_result of this EnvironmentDetails.


        :return: The latest_operation_result of this EnvironmentDetails.
        :rtype: LatestOperationResult
        """
        return self._latest_operation_result

    @latest_operation_result.setter
    def latest_operation_result(self, latest_operation_result):
        """Sets the latest_operation_result of this EnvironmentDetails.


        :param latest_operation_result: The latest_operation_result of this EnvironmentDetails.
        :type latest_operation_result: LatestOperationResult
        """

        self._latest_operation_result = latest_operation_result

    @property
    def name(self):
        """Gets the name of this EnvironmentDetails.

        Name of the Environment

        :return: The name of this EnvironmentDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EnvironmentDetails.

        Name of the Environment

        :param name: The name of this EnvironmentDetails.
        :type name: str
        """

        self._name = name

    @property
    def password_last_reset(self):
        """Gets the password_last_reset of this EnvironmentDetails.

        When the password was last reset on the environment.

        :return: The password_last_reset of this EnvironmentDetails.
        :rtype: datetime
        """
        return self._password_last_reset

    @password_last_reset.setter
    def password_last_reset(self, password_last_reset):
        """Sets the password_last_reset of this EnvironmentDetails.

        When the password was last reset on the environment.

        :param password_last_reset: The password_last_reset of this EnvironmentDetails.
        :type password_last_reset: datetime
        """

        self._password_last_reset = password_last_reset

    @property
    def provisioning_state(self):
        """Gets the provisioning_state of this EnvironmentDetails.

        The provisioning state of the environment. This also includes LabIsFull and NotYetProvisioned status.

        :return: The provisioning_state of this EnvironmentDetails.
        :rtype: str
        """
        return self._provisioning_state

    @provisioning_state.setter
    def provisioning_state(self, provisioning_state):
        """Sets the provisioning_state of this EnvironmentDetails.

        The provisioning state of the environment. This also includes LabIsFull and NotYetProvisioned status.

        :param provisioning_state: The provisioning_state of this EnvironmentDetails.
        :type provisioning_state: str
        """

        self._provisioning_state = provisioning_state

    @property
    def total_usage(self):
        """Gets the total_usage of this EnvironmentDetails.

        How long the environment has been used by a lab user

        :return: The total_usage of this EnvironmentDetails.
        :rtype: str
        """
        return self._total_usage

    @total_usage.setter
    def total_usage(self, total_usage):
        """Sets the total_usage of this EnvironmentDetails.

        How long the environment has been used by a lab user

        :param total_usage: The total_usage of this EnvironmentDetails.
        :type total_usage: str
        """

        self._total_usage = total_usage

    @property
    def virtual_machine_details(self):
        """Gets the virtual_machine_details of this EnvironmentDetails.


        :return: The virtual_machine_details of this EnvironmentDetails.
        :rtype: VirtualMachineDetails
        """
        return self._virtual_machine_details

    @virtual_machine_details.setter
    def virtual_machine_details(self, virtual_machine_details):
        """Sets the virtual_machine_details of this EnvironmentDetails.


        :param virtual_machine_details: The virtual_machine_details of this EnvironmentDetails.
        :type virtual_machine_details: VirtualMachineDetails
        """

        self._virtual_machine_details = virtual_machine_details
