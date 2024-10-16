# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.build_system_shared_dto_job_activity import BuildSystemSharedDTOJobActivity
from openapi_server.models.build_system_shared_dto_parameter import BuildSystemSharedDTOParameter
from openapi_server import util


class BuildSystemSharedDTOJob(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, activities: List[BuildSystemSharedDTOJobActivity]=None, deleted: bool=None, job_id: int=None, name: str=None, parameters: List[BuildSystemSharedDTOParameter]=None):
        """BuildSystemSharedDTOJob - a model defined in OpenAPI

        :param activities: The activities of this BuildSystemSharedDTOJob.
        :param deleted: The deleted of this BuildSystemSharedDTOJob.
        :param job_id: The job_id of this BuildSystemSharedDTOJob.
        :param name: The name of this BuildSystemSharedDTOJob.
        :param parameters: The parameters of this BuildSystemSharedDTOJob.
        """
        self.openapi_types = {
            'activities': List[BuildSystemSharedDTOJobActivity],
            'deleted': bool,
            'job_id': int,
            'name': str,
            'parameters': List[BuildSystemSharedDTOParameter]
        }

        self.attribute_map = {
            'activities': 'Activities',
            'deleted': 'Deleted',
            'job_id': 'JobID',
            'name': 'Name',
            'parameters': 'Parameters'
        }

        self._activities = activities
        self._deleted = deleted
        self._job_id = job_id
        self._name = name
        self._parameters = parameters

    @classmethod
    def from_dict(cls, dikt: dict) -> 'BuildSystemSharedDTOJob':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The BuildSystem.Shared.DTO.Job of this BuildSystemSharedDTOJob.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def activities(self):
        """Gets the activities of this BuildSystemSharedDTOJob.

        The activities which are performed for the job

        :return: The activities of this BuildSystemSharedDTOJob.
        :rtype: List[BuildSystemSharedDTOJobActivity]
        """
        return self._activities

    @activities.setter
    def activities(self, activities):
        """Sets the activities of this BuildSystemSharedDTOJob.

        The activities which are performed for the job

        :param activities: The activities of this BuildSystemSharedDTOJob.
        :type activities: List[BuildSystemSharedDTOJobActivity]
        """

        self._activities = activities

    @property
    def deleted(self):
        """Gets the deleted of this BuildSystemSharedDTOJob.

        Indicates if the job has been deleted.

        :return: The deleted of this BuildSystemSharedDTOJob.
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this BuildSystemSharedDTOJob.

        Indicates if the job has been deleted.

        :param deleted: The deleted of this BuildSystemSharedDTOJob.
        :type deleted: bool
        """

        self._deleted = deleted

    @property
    def job_id(self):
        """Gets the job_id of this BuildSystemSharedDTOJob.

        The ID of the job

        :return: The job_id of this BuildSystemSharedDTOJob.
        :rtype: int
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this BuildSystemSharedDTOJob.

        The ID of the job

        :param job_id: The job_id of this BuildSystemSharedDTOJob.
        :type job_id: int
        """

        self._job_id = job_id

    @property
    def name(self):
        """Gets the name of this BuildSystemSharedDTOJob.

        The name of the job

        :return: The name of this BuildSystemSharedDTOJob.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BuildSystemSharedDTOJob.

        The name of the job

        :param name: The name of this BuildSystemSharedDTOJob.
        :type name: str
        """

        self._name = name

    @property
    def parameters(self):
        """Gets the parameters of this BuildSystemSharedDTOJob.

        The parameters for the job

        :return: The parameters of this BuildSystemSharedDTOJob.
        :rtype: List[BuildSystemSharedDTOParameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this BuildSystemSharedDTOJob.

        The parameters for the job

        :param parameters: The parameters of this BuildSystemSharedDTOJob.
        :type parameters: List[BuildSystemSharedDTOParameter]
        """

        self._parameters = parameters
