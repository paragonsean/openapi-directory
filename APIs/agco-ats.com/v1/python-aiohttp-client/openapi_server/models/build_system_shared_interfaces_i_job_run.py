# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.build_system_shared_interfaces_i_activity_run import BuildSystemSharedInterfacesIActivityRun
from openapi_server.models.build_system_shared_interfaces_i_parameter_value import BuildSystemSharedInterfacesIParameterValue
from openapi_server import util


class BuildSystemSharedInterfacesIJobRun(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, activity_runs: List[BuildSystemSharedInterfacesIActivityRun]=None, end_date: datetime=None, job_id: int=None, job_run_id: int=None, parameters: List[BuildSystemSharedInterfacesIParameterValue]=None, start_date: datetime=None, status: str=None):
        """BuildSystemSharedInterfacesIJobRun - a model defined in OpenAPI

        :param activity_runs: The activity_runs of this BuildSystemSharedInterfacesIJobRun.
        :param end_date: The end_date of this BuildSystemSharedInterfacesIJobRun.
        :param job_id: The job_id of this BuildSystemSharedInterfacesIJobRun.
        :param job_run_id: The job_run_id of this BuildSystemSharedInterfacesIJobRun.
        :param parameters: The parameters of this BuildSystemSharedInterfacesIJobRun.
        :param start_date: The start_date of this BuildSystemSharedInterfacesIJobRun.
        :param status: The status of this BuildSystemSharedInterfacesIJobRun.
        """
        self.openapi_types = {
            'activity_runs': List[BuildSystemSharedInterfacesIActivityRun],
            'end_date': datetime,
            'job_id': int,
            'job_run_id': int,
            'parameters': List[BuildSystemSharedInterfacesIParameterValue],
            'start_date': datetime,
            'status': str
        }

        self.attribute_map = {
            'activity_runs': 'ActivityRuns',
            'end_date': 'EndDate',
            'job_id': 'JobID',
            'job_run_id': 'JobRunID',
            'parameters': 'Parameters',
            'start_date': 'StartDate',
            'status': 'Status'
        }

        self._activity_runs = activity_runs
        self._end_date = end_date
        self._job_id = job_id
        self._job_run_id = job_run_id
        self._parameters = parameters
        self._start_date = start_date
        self._status = status

    @classmethod
    def from_dict(cls, dikt: dict) -> 'BuildSystemSharedInterfacesIJobRun':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The BuildSystem.Shared.Interfaces.IJobRun of this BuildSystemSharedInterfacesIJobRun.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def activity_runs(self):
        """Gets the activity_runs of this BuildSystemSharedInterfacesIJobRun.

        ActivityRuns

        :return: The activity_runs of this BuildSystemSharedInterfacesIJobRun.
        :rtype: List[BuildSystemSharedInterfacesIActivityRun]
        """
        return self._activity_runs

    @activity_runs.setter
    def activity_runs(self, activity_runs):
        """Sets the activity_runs of this BuildSystemSharedInterfacesIJobRun.

        ActivityRuns

        :param activity_runs: The activity_runs of this BuildSystemSharedInterfacesIJobRun.
        :type activity_runs: List[BuildSystemSharedInterfacesIActivityRun]
        """

        self._activity_runs = activity_runs

    @property
    def end_date(self):
        """Gets the end_date of this BuildSystemSharedInterfacesIJobRun.

        end date

        :return: The end_date of this BuildSystemSharedInterfacesIJobRun.
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this BuildSystemSharedInterfacesIJobRun.

        end date

        :param end_date: The end_date of this BuildSystemSharedInterfacesIJobRun.
        :type end_date: datetime
        """

        self._end_date = end_date

    @property
    def job_id(self):
        """Gets the job_id of this BuildSystemSharedInterfacesIJobRun.

        job id

        :return: The job_id of this BuildSystemSharedInterfacesIJobRun.
        :rtype: int
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this BuildSystemSharedInterfacesIJobRun.

        job id

        :param job_id: The job_id of this BuildSystemSharedInterfacesIJobRun.
        :type job_id: int
        """

        self._job_id = job_id

    @property
    def job_run_id(self):
        """Gets the job_run_id of this BuildSystemSharedInterfacesIJobRun.

        JobRunID

        :return: The job_run_id of this BuildSystemSharedInterfacesIJobRun.
        :rtype: int
        """
        return self._job_run_id

    @job_run_id.setter
    def job_run_id(self, job_run_id):
        """Sets the job_run_id of this BuildSystemSharedInterfacesIJobRun.

        JobRunID

        :param job_run_id: The job_run_id of this BuildSystemSharedInterfacesIJobRun.
        :type job_run_id: int
        """

        self._job_run_id = job_run_id

    @property
    def parameters(self):
        """Gets the parameters of this BuildSystemSharedInterfacesIJobRun.

        Parameters

        :return: The parameters of this BuildSystemSharedInterfacesIJobRun.
        :rtype: List[BuildSystemSharedInterfacesIParameterValue]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this BuildSystemSharedInterfacesIJobRun.

        Parameters

        :param parameters: The parameters of this BuildSystemSharedInterfacesIJobRun.
        :type parameters: List[BuildSystemSharedInterfacesIParameterValue]
        """

        self._parameters = parameters

    @property
    def start_date(self):
        """Gets the start_date of this BuildSystemSharedInterfacesIJobRun.

        Start Date

        :return: The start_date of this BuildSystemSharedInterfacesIJobRun.
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this BuildSystemSharedInterfacesIJobRun.

        Start Date

        :param start_date: The start_date of this BuildSystemSharedInterfacesIJobRun.
        :type start_date: datetime
        """

        self._start_date = start_date

    @property
    def status(self):
        """Gets the status of this BuildSystemSharedInterfacesIJobRun.

        status

        :return: The status of this BuildSystemSharedInterfacesIJobRun.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BuildSystemSharedInterfacesIJobRun.

        status

        :param status: The status of this BuildSystemSharedInterfacesIJobRun.
        :type status: str
        """
        allowed_values = ["Ready", "InProgress", "Succeeded", "Cancelled", "Failed"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status
