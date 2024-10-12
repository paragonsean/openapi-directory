# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.azure_iaa_svm_error_info import AzureIaaSVMErrorInfo
from openapi_server.models.azure_iaa_svm_job_extended_info import AzureIaaSVMJobExtendedInfo
from openapi_server.models.job import Job
from openapi_server import util


class AzureIaaSVMJob(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, actions_info: List[str]=None, duration: str=None, error_details: List[AzureIaaSVMErrorInfo]=None, extended_info: AzureIaaSVMJobExtendedInfo=None, virtual_machine_version: str=None, activity_id: str=None, backup_management_type: str=None, end_time: datetime=None, entity_friendly_name: str=None, job_type: str=None, operation: str=None, start_time: datetime=None, status: str=None):
        """AzureIaaSVMJob - a model defined in OpenAPI

        :param actions_info: The actions_info of this AzureIaaSVMJob.
        :param duration: The duration of this AzureIaaSVMJob.
        :param error_details: The error_details of this AzureIaaSVMJob.
        :param extended_info: The extended_info of this AzureIaaSVMJob.
        :param virtual_machine_version: The virtual_machine_version of this AzureIaaSVMJob.
        :param activity_id: The activity_id of this AzureIaaSVMJob.
        :param backup_management_type: The backup_management_type of this AzureIaaSVMJob.
        :param end_time: The end_time of this AzureIaaSVMJob.
        :param entity_friendly_name: The entity_friendly_name of this AzureIaaSVMJob.
        :param job_type: The job_type of this AzureIaaSVMJob.
        :param operation: The operation of this AzureIaaSVMJob.
        :param start_time: The start_time of this AzureIaaSVMJob.
        :param status: The status of this AzureIaaSVMJob.
        """
        self.openapi_types = {
            'actions_info': List[str],
            'duration': str,
            'error_details': List[AzureIaaSVMErrorInfo],
            'extended_info': AzureIaaSVMJobExtendedInfo,
            'virtual_machine_version': str,
            'activity_id': str,
            'backup_management_type': str,
            'end_time': datetime,
            'entity_friendly_name': str,
            'job_type': str,
            'operation': str,
            'start_time': datetime,
            'status': str
        }

        self.attribute_map = {
            'actions_info': 'actionsInfo',
            'duration': 'duration',
            'error_details': 'errorDetails',
            'extended_info': 'extendedInfo',
            'virtual_machine_version': 'virtualMachineVersion',
            'activity_id': 'activityId',
            'backup_management_type': 'backupManagementType',
            'end_time': 'endTime',
            'entity_friendly_name': 'entityFriendlyName',
            'job_type': 'jobType',
            'operation': 'operation',
            'start_time': 'startTime',
            'status': 'status'
        }

        self._actions_info = actions_info
        self._duration = duration
        self._error_details = error_details
        self._extended_info = extended_info
        self._virtual_machine_version = virtual_machine_version
        self._activity_id = activity_id
        self._backup_management_type = backup_management_type
        self._end_time = end_time
        self._entity_friendly_name = entity_friendly_name
        self._job_type = job_type
        self._operation = operation
        self._start_time = start_time
        self._status = status

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AzureIaaSVMJob':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The AzureIaaSVMJob of this AzureIaaSVMJob.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def actions_info(self):
        """Gets the actions_info of this AzureIaaSVMJob.

        Gets or sets the state/actions applicable on this job like cancel/retry.

        :return: The actions_info of this AzureIaaSVMJob.
        :rtype: List[str]
        """
        return self._actions_info

    @actions_info.setter
    def actions_info(self, actions_info):
        """Sets the actions_info of this AzureIaaSVMJob.

        Gets or sets the state/actions applicable on this job like cancel/retry.

        :param actions_info: The actions_info of this AzureIaaSVMJob.
        :type actions_info: List[str]
        """
        allowed_values = ["Invalid", "Cancellable", "Retriable"]  # noqa: E501
        if not set(actions_info).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `actions_info` [{0}], must be a subset of [{1}]"
                .format(", ".join(map(str, set(actions_info) - set(allowed_values))),
                        ", ".join(map(str, allowed_values)))
            )

        self._actions_info = actions_info

    @property
    def duration(self):
        """Gets the duration of this AzureIaaSVMJob.

        Time elapsed during the execution of this job.

        :return: The duration of this AzureIaaSVMJob.
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this AzureIaaSVMJob.

        Time elapsed during the execution of this job.

        :param duration: The duration of this AzureIaaSVMJob.
        :type duration: str
        """

        self._duration = duration

    @property
    def error_details(self):
        """Gets the error_details of this AzureIaaSVMJob.

        Error details on execution of this job.

        :return: The error_details of this AzureIaaSVMJob.
        :rtype: List[AzureIaaSVMErrorInfo]
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """Sets the error_details of this AzureIaaSVMJob.

        Error details on execution of this job.

        :param error_details: The error_details of this AzureIaaSVMJob.
        :type error_details: List[AzureIaaSVMErrorInfo]
        """

        self._error_details = error_details

    @property
    def extended_info(self):
        """Gets the extended_info of this AzureIaaSVMJob.


        :return: The extended_info of this AzureIaaSVMJob.
        :rtype: AzureIaaSVMJobExtendedInfo
        """
        return self._extended_info

    @extended_info.setter
    def extended_info(self, extended_info):
        """Sets the extended_info of this AzureIaaSVMJob.


        :param extended_info: The extended_info of this AzureIaaSVMJob.
        :type extended_info: AzureIaaSVMJobExtendedInfo
        """

        self._extended_info = extended_info

    @property
    def virtual_machine_version(self):
        """Gets the virtual_machine_version of this AzureIaaSVMJob.

        Specifies whether the backup item is a Classic or an Azure Resource Manager VM.

        :return: The virtual_machine_version of this AzureIaaSVMJob.
        :rtype: str
        """
        return self._virtual_machine_version

    @virtual_machine_version.setter
    def virtual_machine_version(self, virtual_machine_version):
        """Sets the virtual_machine_version of this AzureIaaSVMJob.

        Specifies whether the backup item is a Classic or an Azure Resource Manager VM.

        :param virtual_machine_version: The virtual_machine_version of this AzureIaaSVMJob.
        :type virtual_machine_version: str
        """

        self._virtual_machine_version = virtual_machine_version

    @property
    def activity_id(self):
        """Gets the activity_id of this AzureIaaSVMJob.

        ActivityId of job.

        :return: The activity_id of this AzureIaaSVMJob.
        :rtype: str
        """
        return self._activity_id

    @activity_id.setter
    def activity_id(self, activity_id):
        """Sets the activity_id of this AzureIaaSVMJob.

        ActivityId of job.

        :param activity_id: The activity_id of this AzureIaaSVMJob.
        :type activity_id: str
        """

        self._activity_id = activity_id

    @property
    def backup_management_type(self):
        """Gets the backup_management_type of this AzureIaaSVMJob.

        Backup management type to execute the current job.

        :return: The backup_management_type of this AzureIaaSVMJob.
        :rtype: str
        """
        return self._backup_management_type

    @backup_management_type.setter
    def backup_management_type(self, backup_management_type):
        """Sets the backup_management_type of this AzureIaaSVMJob.

        Backup management type to execute the current job.

        :param backup_management_type: The backup_management_type of this AzureIaaSVMJob.
        :type backup_management_type: str
        """
        allowed_values = ["Invalid", "AzureIaasVM", "MAB", "DPM", "AzureBackupServer", "AzureSql"]  # noqa: E501
        if backup_management_type not in allowed_values:
            raise ValueError(
                "Invalid value for `backup_management_type` ({0}), must be one of {1}"
                .format(backup_management_type, allowed_values)
            )

        self._backup_management_type = backup_management_type

    @property
    def end_time(self):
        """Gets the end_time of this AzureIaaSVMJob.

        The end time.

        :return: The end_time of this AzureIaaSVMJob.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this AzureIaaSVMJob.

        The end time.

        :param end_time: The end_time of this AzureIaaSVMJob.
        :type end_time: datetime
        """

        self._end_time = end_time

    @property
    def entity_friendly_name(self):
        """Gets the entity_friendly_name of this AzureIaaSVMJob.

        Friendly name of the entity on which the current job is executing.

        :return: The entity_friendly_name of this AzureIaaSVMJob.
        :rtype: str
        """
        return self._entity_friendly_name

    @entity_friendly_name.setter
    def entity_friendly_name(self, entity_friendly_name):
        """Sets the entity_friendly_name of this AzureIaaSVMJob.

        Friendly name of the entity on which the current job is executing.

        :param entity_friendly_name: The entity_friendly_name of this AzureIaaSVMJob.
        :type entity_friendly_name: str
        """

        self._entity_friendly_name = entity_friendly_name

    @property
    def job_type(self):
        """Gets the job_type of this AzureIaaSVMJob.

        This property will be used as the discriminator for deciding the specific types in the polymorhpic chain of types.

        :return: The job_type of this AzureIaaSVMJob.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this AzureIaaSVMJob.

        This property will be used as the discriminator for deciding the specific types in the polymorhpic chain of types.

        :param job_type: The job_type of this AzureIaaSVMJob.
        :type job_type: str
        """
        if job_type is None:
            raise ValueError("Invalid value for `job_type`, must not be `None`")

        self._job_type = job_type

    @property
    def operation(self):
        """Gets the operation of this AzureIaaSVMJob.

        The operation name.

        :return: The operation of this AzureIaaSVMJob.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this AzureIaaSVMJob.

        The operation name.

        :param operation: The operation of this AzureIaaSVMJob.
        :type operation: str
        """

        self._operation = operation

    @property
    def start_time(self):
        """Gets the start_time of this AzureIaaSVMJob.

        The start time.

        :return: The start_time of this AzureIaaSVMJob.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this AzureIaaSVMJob.

        The start time.

        :param start_time: The start_time of this AzureIaaSVMJob.
        :type start_time: datetime
        """

        self._start_time = start_time

    @property
    def status(self):
        """Gets the status of this AzureIaaSVMJob.

        Job status.

        :return: The status of this AzureIaaSVMJob.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AzureIaaSVMJob.

        Job status.

        :param status: The status of this AzureIaaSVMJob.
        :type status: str
        """

        self._status = status
