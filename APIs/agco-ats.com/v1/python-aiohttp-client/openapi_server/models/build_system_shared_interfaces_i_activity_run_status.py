# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class BuildSystemSharedInterfacesIActivityRunStatus(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, current_step: int=None, status: str=None, step_progress: int=None, step_status: str=None):
        """BuildSystemSharedInterfacesIActivityRunStatus - a model defined in OpenAPI

        :param current_step: The current_step of this BuildSystemSharedInterfacesIActivityRunStatus.
        :param status: The status of this BuildSystemSharedInterfacesIActivityRunStatus.
        :param step_progress: The step_progress of this BuildSystemSharedInterfacesIActivityRunStatus.
        :param step_status: The step_status of this BuildSystemSharedInterfacesIActivityRunStatus.
        """
        self.openapi_types = {
            'current_step': int,
            'status': str,
            'step_progress': int,
            'step_status': str
        }

        self.attribute_map = {
            'current_step': 'CurrentStep',
            'status': 'Status',
            'step_progress': 'StepProgress',
            'step_status': 'StepStatus'
        }

        self._current_step = current_step
        self._status = status
        self._step_progress = step_progress
        self._step_status = step_status

    @classmethod
    def from_dict(cls, dikt: dict) -> 'BuildSystemSharedInterfacesIActivityRunStatus':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The BuildSystem.Shared.Interfaces.IActivityRunStatus of this BuildSystemSharedInterfacesIActivityRunStatus.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def current_step(self):
        """Gets the current_step of this BuildSystemSharedInterfacesIActivityRunStatus.

        Gets or sets the number of the step the activity is currently running.

        :return: The current_step of this BuildSystemSharedInterfacesIActivityRunStatus.
        :rtype: int
        """
        return self._current_step

    @current_step.setter
    def current_step(self, current_step):
        """Sets the current_step of this BuildSystemSharedInterfacesIActivityRunStatus.

        Gets or sets the number of the step the activity is currently running.

        :param current_step: The current_step of this BuildSystemSharedInterfacesIActivityRunStatus.
        :type current_step: int
        """

        self._current_step = current_step

    @property
    def status(self):
        """Gets the status of this BuildSystemSharedInterfacesIActivityRunStatus.

        Gets or sets the status of the activity run.

        :return: The status of this BuildSystemSharedInterfacesIActivityRunStatus.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BuildSystemSharedInterfacesIActivityRunStatus.

        Gets or sets the status of the activity run.

        :param status: The status of this BuildSystemSharedInterfacesIActivityRunStatus.
        :type status: str
        """
        allowed_values = ["Ready", "InProgress", "Succeeded", "Cancelled", "Failed"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def step_progress(self):
        """Gets the step_progress of this BuildSystemSharedInterfacesIActivityRunStatus.

        Gets or sets a measurement of the current progress of the current step.

        :return: The step_progress of this BuildSystemSharedInterfacesIActivityRunStatus.
        :rtype: int
        """
        return self._step_progress

    @step_progress.setter
    def step_progress(self, step_progress):
        """Sets the step_progress of this BuildSystemSharedInterfacesIActivityRunStatus.

        Gets or sets a measurement of the current progress of the current step.

        :param step_progress: The step_progress of this BuildSystemSharedInterfacesIActivityRunStatus.
        :type step_progress: int
        """

        self._step_progress = step_progress

    @property
    def step_status(self):
        """Gets the step_status of this BuildSystemSharedInterfacesIActivityRunStatus.

        Gets or sets a description of the current status of the currently               running step.

        :return: The step_status of this BuildSystemSharedInterfacesIActivityRunStatus.
        :rtype: str
        """
        return self._step_status

    @step_status.setter
    def step_status(self, step_status):
        """Sets the step_status of this BuildSystemSharedInterfacesIActivityRunStatus.

        Gets or sets a description of the current status of the currently               running step.

        :param step_status: The step_status of this BuildSystemSharedInterfacesIActivityRunStatus.
        :type step_status: str
        """

        self._step_status = step_status
