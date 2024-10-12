# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.image_response_base import ImageResponseBase
from openapi_server.models.iot_module_settings import IotModuleSettings
from openapi_server.models.model_error_response import ModelErrorResponse
from openapi_server.models.service_response_base import ServiceResponseBase
from openapi_server import util


class IotServiceResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, compute_type: str=None, created_time: datetime=None, deployment_type: str=None, description: str=None, error: ModelErrorResponse=None, id: str=None, kv_tags: Dict[str, str]=None, name: str=None, operation_id: str=None, properties: Dict[str, str]=None, state: str=None, updated_time: datetime=None, auth_enabled: bool=None, compute_name: str=None, image_details: ImageResponseBase=None, image_id: str=None, iot_device_id: str=None, iot_edge_modules: List[IotModuleSettings]=None, routes: Dict[str, str]=None):
        """IotServiceResponse - a model defined in OpenAPI

        :param compute_type: The compute_type of this IotServiceResponse.
        :param created_time: The created_time of this IotServiceResponse.
        :param deployment_type: The deployment_type of this IotServiceResponse.
        :param description: The description of this IotServiceResponse.
        :param error: The error of this IotServiceResponse.
        :param id: The id of this IotServiceResponse.
        :param kv_tags: The kv_tags of this IotServiceResponse.
        :param name: The name of this IotServiceResponse.
        :param operation_id: The operation_id of this IotServiceResponse.
        :param properties: The properties of this IotServiceResponse.
        :param state: The state of this IotServiceResponse.
        :param updated_time: The updated_time of this IotServiceResponse.
        :param auth_enabled: The auth_enabled of this IotServiceResponse.
        :param compute_name: The compute_name of this IotServiceResponse.
        :param image_details: The image_details of this IotServiceResponse.
        :param image_id: The image_id of this IotServiceResponse.
        :param iot_device_id: The iot_device_id of this IotServiceResponse.
        :param iot_edge_modules: The iot_edge_modules of this IotServiceResponse.
        :param routes: The routes of this IotServiceResponse.
        """
        self.openapi_types = {
            'compute_type': str,
            'created_time': datetime,
            'deployment_type': str,
            'description': str,
            'error': ModelErrorResponse,
            'id': str,
            'kv_tags': Dict[str, str],
            'name': str,
            'operation_id': str,
            'properties': Dict[str, str],
            'state': str,
            'updated_time': datetime,
            'auth_enabled': bool,
            'compute_name': str,
            'image_details': ImageResponseBase,
            'image_id': str,
            'iot_device_id': str,
            'iot_edge_modules': List[IotModuleSettings],
            'routes': Dict[str, str]
        }

        self.attribute_map = {
            'compute_type': 'computeType',
            'created_time': 'createdTime',
            'deployment_type': 'deploymentType',
            'description': 'description',
            'error': 'error',
            'id': 'id',
            'kv_tags': 'kvTags',
            'name': 'name',
            'operation_id': 'operationId',
            'properties': 'properties',
            'state': 'state',
            'updated_time': 'updatedTime',
            'auth_enabled': 'authEnabled',
            'compute_name': 'computeName',
            'image_details': 'imageDetails',
            'image_id': 'imageId',
            'iot_device_id': 'iotDeviceId',
            'iot_edge_modules': 'iotEdgeModules',
            'routes': 'routes'
        }

        self._compute_type = compute_type
        self._created_time = created_time
        self._deployment_type = deployment_type
        self._description = description
        self._error = error
        self._id = id
        self._kv_tags = kv_tags
        self._name = name
        self._operation_id = operation_id
        self._properties = properties
        self._state = state
        self._updated_time = updated_time
        self._auth_enabled = auth_enabled
        self._compute_name = compute_name
        self._image_details = image_details
        self._image_id = image_id
        self._iot_device_id = iot_device_id
        self._iot_edge_modules = iot_edge_modules
        self._routes = routes

    @classmethod
    def from_dict(cls, dikt: dict) -> 'IotServiceResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The IotServiceResponse of this IotServiceResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def compute_type(self):
        """Gets the compute_type of this IotServiceResponse.

        The compute environment type for the service.

        :return: The compute_type of this IotServiceResponse.
        :rtype: str
        """
        return self._compute_type

    @compute_type.setter
    def compute_type(self, compute_type):
        """Sets the compute_type of this IotServiceResponse.

        The compute environment type for the service.

        :param compute_type: The compute_type of this IotServiceResponse.
        :type compute_type: str
        """
        allowed_values = ["ACI", "AKS", "AMLCOMPUTE", "IOT", "AKSENDPOINT", "UNKNOWN"]  # noqa: E501
        if compute_type not in allowed_values:
            raise ValueError(
                "Invalid value for `compute_type` ({0}), must be one of {1}"
                .format(compute_type, allowed_values)
            )

        self._compute_type = compute_type

    @property
    def created_time(self):
        """Gets the created_time of this IotServiceResponse.

        The time the service was created.

        :return: The created_time of this IotServiceResponse.
        :rtype: datetime
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this IotServiceResponse.

        The time the service was created.

        :param created_time: The created_time of this IotServiceResponse.
        :type created_time: datetime
        """

        self._created_time = created_time

    @property
    def deployment_type(self):
        """Gets the deployment_type of this IotServiceResponse.

        The deployment type for the service.

        :return: The deployment_type of this IotServiceResponse.
        :rtype: str
        """
        return self._deployment_type

    @deployment_type.setter
    def deployment_type(self, deployment_type):
        """Sets the deployment_type of this IotServiceResponse.

        The deployment type for the service.

        :param deployment_type: The deployment_type of this IotServiceResponse.
        :type deployment_type: str
        """
        allowed_values = ["GRPCRealtimeEndpoint", "HttpRealtimeEndpoint", "Batch"]  # noqa: E501
        if deployment_type not in allowed_values:
            raise ValueError(
                "Invalid value for `deployment_type` ({0}), must be one of {1}"
                .format(deployment_type, allowed_values)
            )

        self._deployment_type = deployment_type

    @property
    def description(self):
        """Gets the description of this IotServiceResponse.

        The service description.

        :return: The description of this IotServiceResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IotServiceResponse.

        The service description.

        :param description: The description of this IotServiceResponse.
        :type description: str
        """

        self._description = description

    @property
    def error(self):
        """Gets the error of this IotServiceResponse.


        :return: The error of this IotServiceResponse.
        :rtype: ModelErrorResponse
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this IotServiceResponse.


        :param error: The error of this IotServiceResponse.
        :type error: ModelErrorResponse
        """

        self._error = error

    @property
    def id(self):
        """Gets the id of this IotServiceResponse.

        The service Id.

        :return: The id of this IotServiceResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IotServiceResponse.

        The service Id.

        :param id: The id of this IotServiceResponse.
        :type id: str
        """

        self._id = id

    @property
    def kv_tags(self):
        """Gets the kv_tags of this IotServiceResponse.

        The service tag dictionary. Tags are mutable.

        :return: The kv_tags of this IotServiceResponse.
        :rtype: Dict[str, str]
        """
        return self._kv_tags

    @kv_tags.setter
    def kv_tags(self, kv_tags):
        """Sets the kv_tags of this IotServiceResponse.

        The service tag dictionary. Tags are mutable.

        :param kv_tags: The kv_tags of this IotServiceResponse.
        :type kv_tags: Dict[str, str]
        """

        self._kv_tags = kv_tags

    @property
    def name(self):
        """Gets the name of this IotServiceResponse.

        The service name.

        :return: The name of this IotServiceResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IotServiceResponse.

        The service name.

        :param name: The name of this IotServiceResponse.
        :type name: str
        """

        self._name = name

    @property
    def operation_id(self):
        """Gets the operation_id of this IotServiceResponse.

        The ID of the latest asynchronous operation for this service.

        :return: The operation_id of this IotServiceResponse.
        :rtype: str
        """
        return self._operation_id

    @operation_id.setter
    def operation_id(self, operation_id):
        """Sets the operation_id of this IotServiceResponse.

        The ID of the latest asynchronous operation for this service.

        :param operation_id: The operation_id of this IotServiceResponse.
        :type operation_id: str
        """

        self._operation_id = operation_id

    @property
    def properties(self):
        """Gets the properties of this IotServiceResponse.

        The service property dictionary. Properties are immutable.

        :return: The properties of this IotServiceResponse.
        :rtype: Dict[str, str]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this IotServiceResponse.

        The service property dictionary. Properties are immutable.

        :param properties: The properties of this IotServiceResponse.
        :type properties: Dict[str, str]
        """

        self._properties = properties

    @property
    def state(self):
        """Gets the state of this IotServiceResponse.

        The current state of the service.

        :return: The state of this IotServiceResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this IotServiceResponse.

        The current state of the service.

        :param state: The state of this IotServiceResponse.
        :type state: str
        """
        allowed_values = ["Transitioning", "Healthy", "Unhealthy", "Failed"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def updated_time(self):
        """Gets the updated_time of this IotServiceResponse.

        The time the service was updated.

        :return: The updated_time of this IotServiceResponse.
        :rtype: datetime
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        """Sets the updated_time of this IotServiceResponse.

        The time the service was updated.

        :param updated_time: The updated_time of this IotServiceResponse.
        :type updated_time: datetime
        """

        self._updated_time = updated_time

    @property
    def auth_enabled(self):
        """Gets the auth_enabled of this IotServiceResponse.


        :return: The auth_enabled of this IotServiceResponse.
        :rtype: bool
        """
        return self._auth_enabled

    @auth_enabled.setter
    def auth_enabled(self, auth_enabled):
        """Sets the auth_enabled of this IotServiceResponse.


        :param auth_enabled: The auth_enabled of this IotServiceResponse.
        :type auth_enabled: bool
        """

        self._auth_enabled = auth_enabled

    @property
    def compute_name(self):
        """Gets the compute_name of this IotServiceResponse.


        :return: The compute_name of this IotServiceResponse.
        :rtype: str
        """
        return self._compute_name

    @compute_name.setter
    def compute_name(self, compute_name):
        """Sets the compute_name of this IotServiceResponse.


        :param compute_name: The compute_name of this IotServiceResponse.
        :type compute_name: str
        """

        self._compute_name = compute_name

    @property
    def image_details(self):
        """Gets the image_details of this IotServiceResponse.


        :return: The image_details of this IotServiceResponse.
        :rtype: ImageResponseBase
        """
        return self._image_details

    @image_details.setter
    def image_details(self, image_details):
        """Sets the image_details of this IotServiceResponse.


        :param image_details: The image_details of this IotServiceResponse.
        :type image_details: ImageResponseBase
        """

        self._image_details = image_details

    @property
    def image_id(self):
        """Gets the image_id of this IotServiceResponse.


        :return: The image_id of this IotServiceResponse.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this IotServiceResponse.


        :param image_id: The image_id of this IotServiceResponse.
        :type image_id: str
        """

        self._image_id = image_id

    @property
    def iot_device_id(self):
        """Gets the iot_device_id of this IotServiceResponse.


        :return: The iot_device_id of this IotServiceResponse.
        :rtype: str
        """
        return self._iot_device_id

    @iot_device_id.setter
    def iot_device_id(self, iot_device_id):
        """Sets the iot_device_id of this IotServiceResponse.


        :param iot_device_id: The iot_device_id of this IotServiceResponse.
        :type iot_device_id: str
        """

        self._iot_device_id = iot_device_id

    @property
    def iot_edge_modules(self):
        """Gets the iot_edge_modules of this IotServiceResponse.


        :return: The iot_edge_modules of this IotServiceResponse.
        :rtype: List[IotModuleSettings]
        """
        return self._iot_edge_modules

    @iot_edge_modules.setter
    def iot_edge_modules(self, iot_edge_modules):
        """Sets the iot_edge_modules of this IotServiceResponse.


        :param iot_edge_modules: The iot_edge_modules of this IotServiceResponse.
        :type iot_edge_modules: List[IotModuleSettings]
        """

        self._iot_edge_modules = iot_edge_modules

    @property
    def routes(self):
        """Gets the routes of this IotServiceResponse.


        :return: The routes of this IotServiceResponse.
        :rtype: Dict[str, str]
        """
        return self._routes

    @routes.setter
    def routes(self, routes):
        """Sets the routes of this IotServiceResponse.


        :param routes: The routes of this IotServiceResponse.
        :type routes: Dict[str, str]
        """

        self._routes = routes
