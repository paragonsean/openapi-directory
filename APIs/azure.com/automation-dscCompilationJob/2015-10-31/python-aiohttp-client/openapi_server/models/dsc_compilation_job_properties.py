# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.dsc_configuration_association_property import DscConfigurationAssociationProperty
from openapi_server.models.job_provisioning_state_property import JobProvisioningStateProperty
from openapi_server import util


class DscCompilationJobProperties(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, configuration: DscConfigurationAssociationProperty=None, creation_time: datetime=None, end_time: datetime=None, exception: str=None, job_id: str=None, last_modified_time: datetime=None, last_status_modified_time: datetime=None, parameters: Dict[str, str]=None, provisioning_state: JobProvisioningStateProperty=None, run_on: str=None, start_time: datetime=None, started_by: str=None, status: str=None, status_details: str=None):
        """DscCompilationJobProperties - a model defined in OpenAPI

        :param configuration: The configuration of this DscCompilationJobProperties.
        :param creation_time: The creation_time of this DscCompilationJobProperties.
        :param end_time: The end_time of this DscCompilationJobProperties.
        :param exception: The exception of this DscCompilationJobProperties.
        :param job_id: The job_id of this DscCompilationJobProperties.
        :param last_modified_time: The last_modified_time of this DscCompilationJobProperties.
        :param last_status_modified_time: The last_status_modified_time of this DscCompilationJobProperties.
        :param parameters: The parameters of this DscCompilationJobProperties.
        :param provisioning_state: The provisioning_state of this DscCompilationJobProperties.
        :param run_on: The run_on of this DscCompilationJobProperties.
        :param start_time: The start_time of this DscCompilationJobProperties.
        :param started_by: The started_by of this DscCompilationJobProperties.
        :param status: The status of this DscCompilationJobProperties.
        :param status_details: The status_details of this DscCompilationJobProperties.
        """
        self.openapi_types = {
            'configuration': DscConfigurationAssociationProperty,
            'creation_time': datetime,
            'end_time': datetime,
            'exception': str,
            'job_id': str,
            'last_modified_time': datetime,
            'last_status_modified_time': datetime,
            'parameters': Dict[str, str],
            'provisioning_state': JobProvisioningStateProperty,
            'run_on': str,
            'start_time': datetime,
            'started_by': str,
            'status': str,
            'status_details': str
        }

        self.attribute_map = {
            'configuration': 'configuration',
            'creation_time': 'creationTime',
            'end_time': 'endTime',
            'exception': 'exception',
            'job_id': 'jobId',
            'last_modified_time': 'lastModifiedTime',
            'last_status_modified_time': 'lastStatusModifiedTime',
            'parameters': 'parameters',
            'provisioning_state': 'provisioningState',
            'run_on': 'runOn',
            'start_time': 'startTime',
            'started_by': 'startedBy',
            'status': 'status',
            'status_details': 'statusDetails'
        }

        self._configuration = configuration
        self._creation_time = creation_time
        self._end_time = end_time
        self._exception = exception
        self._job_id = job_id
        self._last_modified_time = last_modified_time
        self._last_status_modified_time = last_status_modified_time
        self._parameters = parameters
        self._provisioning_state = provisioning_state
        self._run_on = run_on
        self._start_time = start_time
        self._started_by = started_by
        self._status = status
        self._status_details = status_details

    @classmethod
    def from_dict(cls, dikt: dict) -> 'DscCompilationJobProperties':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The DscCompilationJobProperties of this DscCompilationJobProperties.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def configuration(self):
        """Gets the configuration of this DscCompilationJobProperties.


        :return: The configuration of this DscCompilationJobProperties.
        :rtype: DscConfigurationAssociationProperty
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """Sets the configuration of this DscCompilationJobProperties.


        :param configuration: The configuration of this DscCompilationJobProperties.
        :type configuration: DscConfigurationAssociationProperty
        """

        self._configuration = configuration

    @property
    def creation_time(self):
        """Gets the creation_time of this DscCompilationJobProperties.

        Gets the creation time of the job.

        :return: The creation_time of this DscCompilationJobProperties.
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this DscCompilationJobProperties.

        Gets the creation time of the job.

        :param creation_time: The creation_time of this DscCompilationJobProperties.
        :type creation_time: datetime
        """

        self._creation_time = creation_time

    @property
    def end_time(self):
        """Gets the end_time of this DscCompilationJobProperties.

        Gets the end time of the job.

        :return: The end_time of this DscCompilationJobProperties.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this DscCompilationJobProperties.

        Gets the end time of the job.

        :param end_time: The end_time of this DscCompilationJobProperties.
        :type end_time: datetime
        """

        self._end_time = end_time

    @property
    def exception(self):
        """Gets the exception of this DscCompilationJobProperties.

        Gets the exception of the job.

        :return: The exception of this DscCompilationJobProperties.
        :rtype: str
        """
        return self._exception

    @exception.setter
    def exception(self, exception):
        """Sets the exception of this DscCompilationJobProperties.

        Gets the exception of the job.

        :param exception: The exception of this DscCompilationJobProperties.
        :type exception: str
        """

        self._exception = exception

    @property
    def job_id(self):
        """Gets the job_id of this DscCompilationJobProperties.

        Gets the id of the job.

        :return: The job_id of this DscCompilationJobProperties.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this DscCompilationJobProperties.

        Gets the id of the job.

        :param job_id: The job_id of this DscCompilationJobProperties.
        :type job_id: str
        """

        self._job_id = job_id

    @property
    def last_modified_time(self):
        """Gets the last_modified_time of this DscCompilationJobProperties.

        Gets the last modified time of the job.

        :return: The last_modified_time of this DscCompilationJobProperties.
        :rtype: datetime
        """
        return self._last_modified_time

    @last_modified_time.setter
    def last_modified_time(self, last_modified_time):
        """Sets the last_modified_time of this DscCompilationJobProperties.

        Gets the last modified time of the job.

        :param last_modified_time: The last_modified_time of this DscCompilationJobProperties.
        :type last_modified_time: datetime
        """

        self._last_modified_time = last_modified_time

    @property
    def last_status_modified_time(self):
        """Gets the last_status_modified_time of this DscCompilationJobProperties.

        Gets the last status modified time of the job.

        :return: The last_status_modified_time of this DscCompilationJobProperties.
        :rtype: datetime
        """
        return self._last_status_modified_time

    @last_status_modified_time.setter
    def last_status_modified_time(self, last_status_modified_time):
        """Sets the last_status_modified_time of this DscCompilationJobProperties.

        Gets the last status modified time of the job.

        :param last_status_modified_time: The last_status_modified_time of this DscCompilationJobProperties.
        :type last_status_modified_time: datetime
        """

        self._last_status_modified_time = last_status_modified_time

    @property
    def parameters(self):
        """Gets the parameters of this DscCompilationJobProperties.

        Gets or sets the parameters of the job.

        :return: The parameters of this DscCompilationJobProperties.
        :rtype: Dict[str, str]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this DscCompilationJobProperties.

        Gets or sets the parameters of the job.

        :param parameters: The parameters of this DscCompilationJobProperties.
        :type parameters: Dict[str, str]
        """

        self._parameters = parameters

    @property
    def provisioning_state(self):
        """Gets the provisioning_state of this DscCompilationJobProperties.


        :return: The provisioning_state of this DscCompilationJobProperties.
        :rtype: JobProvisioningStateProperty
        """
        return self._provisioning_state

    @provisioning_state.setter
    def provisioning_state(self, provisioning_state):
        """Sets the provisioning_state of this DscCompilationJobProperties.


        :param provisioning_state: The provisioning_state of this DscCompilationJobProperties.
        :type provisioning_state: JobProvisioningStateProperty
        """

        self._provisioning_state = provisioning_state

    @property
    def run_on(self):
        """Gets the run_on of this DscCompilationJobProperties.

        Gets or sets the runOn which specifies the group name where the job is to be executed.

        :return: The run_on of this DscCompilationJobProperties.
        :rtype: str
        """
        return self._run_on

    @run_on.setter
    def run_on(self, run_on):
        """Sets the run_on of this DscCompilationJobProperties.

        Gets or sets the runOn which specifies the group name where the job is to be executed.

        :param run_on: The run_on of this DscCompilationJobProperties.
        :type run_on: str
        """

        self._run_on = run_on

    @property
    def start_time(self):
        """Gets the start_time of this DscCompilationJobProperties.

        Gets the start time of the job.

        :return: The start_time of this DscCompilationJobProperties.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this DscCompilationJobProperties.

        Gets the start time of the job.

        :param start_time: The start_time of this DscCompilationJobProperties.
        :type start_time: datetime
        """

        self._start_time = start_time

    @property
    def started_by(self):
        """Gets the started_by of this DscCompilationJobProperties.

        Gets the compilation job started by.

        :return: The started_by of this DscCompilationJobProperties.
        :rtype: str
        """
        return self._started_by

    @started_by.setter
    def started_by(self, started_by):
        """Sets the started_by of this DscCompilationJobProperties.

        Gets the compilation job started by.

        :param started_by: The started_by of this DscCompilationJobProperties.
        :type started_by: str
        """

        self._started_by = started_by

    @property
    def status(self):
        """Gets the status of this DscCompilationJobProperties.

        Gets or sets the status of the job.

        :return: The status of this DscCompilationJobProperties.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DscCompilationJobProperties.

        Gets or sets the status of the job.

        :param status: The status of this DscCompilationJobProperties.
        :type status: str
        """
        allowed_values = ["New", "Activating", "Running", "Completed", "Failed", "Stopped", "Blocked", "Suspended", "Disconnected", "Suspending", "Stopping", "Resuming", "Removing"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def status_details(self):
        """Gets the status_details of this DscCompilationJobProperties.

        Gets or sets the status details of the job.

        :return: The status_details of this DscCompilationJobProperties.
        :rtype: str
        """
        return self._status_details

    @status_details.setter
    def status_details(self, status_details):
        """Sets the status_details of this DscCompilationJobProperties.

        Gets or sets the status details of the job.

        :param status_details: The status_details of this DscCompilationJobProperties.
        :type status_details: str
        """

        self._status_details = status_details
