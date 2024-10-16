# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ProjectsProjectIdPutRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, contact_id: str=None, description: str=None, erp_project_id: str=None, erp_task_id: str=None, name: str=None, project_status_id: str=None, start_time: str=None, street_name: str=None):
        """ProjectsProjectIdPutRequest - a model defined in OpenAPI

        :param contact_id: The contact_id of this ProjectsProjectIdPutRequest.
        :param description: The description of this ProjectsProjectIdPutRequest.
        :param erp_project_id: The erp_project_id of this ProjectsProjectIdPutRequest.
        :param erp_task_id: The erp_task_id of this ProjectsProjectIdPutRequest.
        :param name: The name of this ProjectsProjectIdPutRequest.
        :param project_status_id: The project_status_id of this ProjectsProjectIdPutRequest.
        :param start_time: The start_time of this ProjectsProjectIdPutRequest.
        :param street_name: The street_name of this ProjectsProjectIdPutRequest.
        """
        self.openapi_types = {
            'contact_id': str,
            'description': str,
            'erp_project_id': str,
            'erp_task_id': str,
            'name': str,
            'project_status_id': str,
            'start_time': str,
            'street_name': str
        }

        self.attribute_map = {
            'contact_id': 'contact_id',
            'description': 'description',
            'erp_project_id': 'erp_project_id',
            'erp_task_id': 'erp_task_id',
            'name': 'name',
            'project_status_id': 'project_status_id',
            'start_time': 'start_time',
            'street_name': 'street_name'
        }

        self._contact_id = contact_id
        self._description = description
        self._erp_project_id = erp_project_id
        self._erp_task_id = erp_task_id
        self._name = name
        self._project_status_id = project_status_id
        self._start_time = start_time
        self._street_name = street_name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ProjectsProjectIdPutRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The _projects__project_id__put_request of this ProjectsProjectIdPutRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def contact_id(self):
        """Gets the contact_id of this ProjectsProjectIdPutRequest.


        :return: The contact_id of this ProjectsProjectIdPutRequest.
        :rtype: str
        """
        return self._contact_id

    @contact_id.setter
    def contact_id(self, contact_id):
        """Sets the contact_id of this ProjectsProjectIdPutRequest.


        :param contact_id: The contact_id of this ProjectsProjectIdPutRequest.
        :type contact_id: str
        """

        self._contact_id = contact_id

    @property
    def description(self):
        """Gets the description of this ProjectsProjectIdPutRequest.


        :return: The description of this ProjectsProjectIdPutRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProjectsProjectIdPutRequest.


        :param description: The description of this ProjectsProjectIdPutRequest.
        :type description: str
        """
        if description is not None and len(description) > 8192:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `8192`")

        self._description = description

    @property
    def erp_project_id(self):
        """Gets the erp_project_id of this ProjectsProjectIdPutRequest.


        :return: The erp_project_id of this ProjectsProjectIdPutRequest.
        :rtype: str
        """
        return self._erp_project_id

    @erp_project_id.setter
    def erp_project_id(self, erp_project_id):
        """Sets the erp_project_id of this ProjectsProjectIdPutRequest.


        :param erp_project_id: The erp_project_id of this ProjectsProjectIdPutRequest.
        :type erp_project_id: str
        """
        if erp_project_id is not None and len(erp_project_id) > 255:
            raise ValueError("Invalid value for `erp_project_id`, length must be less than or equal to `255`")

        self._erp_project_id = erp_project_id

    @property
    def erp_task_id(self):
        """Gets the erp_task_id of this ProjectsProjectIdPutRequest.


        :return: The erp_task_id of this ProjectsProjectIdPutRequest.
        :rtype: str
        """
        return self._erp_task_id

    @erp_task_id.setter
    def erp_task_id(self, erp_task_id):
        """Sets the erp_task_id of this ProjectsProjectIdPutRequest.


        :param erp_task_id: The erp_task_id of this ProjectsProjectIdPutRequest.
        :type erp_task_id: str
        """
        if erp_task_id is not None and len(erp_task_id) > 255:
            raise ValueError("Invalid value for `erp_task_id`, length must be less than or equal to `255`")

        self._erp_task_id = erp_task_id

    @property
    def name(self):
        """Gets the name of this ProjectsProjectIdPutRequest.


        :return: The name of this ProjectsProjectIdPutRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProjectsProjectIdPutRequest.


        :param name: The name of this ProjectsProjectIdPutRequest.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")

        self._name = name

    @property
    def project_status_id(self):
        """Gets the project_status_id of this ProjectsProjectIdPutRequest.


        :return: The project_status_id of this ProjectsProjectIdPutRequest.
        :rtype: str
        """
        return self._project_status_id

    @project_status_id.setter
    def project_status_id(self, project_status_id):
        """Sets the project_status_id of this ProjectsProjectIdPutRequest.


        :param project_status_id: The project_status_id of this ProjectsProjectIdPutRequest.
        :type project_status_id: str
        """

        self._project_status_id = project_status_id

    @property
    def start_time(self):
        """Gets the start_time of this ProjectsProjectIdPutRequest.


        :return: The start_time of this ProjectsProjectIdPutRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ProjectsProjectIdPutRequest.


        :param start_time: The start_time of this ProjectsProjectIdPutRequest.
        :type start_time: str
        """

        self._start_time = start_time

    @property
    def street_name(self):
        """Gets the street_name of this ProjectsProjectIdPutRequest.


        :return: The street_name of this ProjectsProjectIdPutRequest.
        :rtype: str
        """
        return self._street_name

    @street_name.setter
    def street_name(self, street_name):
        """Sets the street_name of this ProjectsProjectIdPutRequest.


        :param street_name: The street_name of this ProjectsProjectIdPutRequest.
        :type street_name: str
        """
        if street_name is not None and len(street_name) > 255:
            raise ValueError("Invalid value for `street_name`, length must be less than or equal to `255`")

        self._street_name = street_name
