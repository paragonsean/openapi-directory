from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.environment_operations_payload import EnvironmentOperationsPayload
from openapi_server.models.get_environment_response import GetEnvironmentResponse
from openapi_server.models.get_personal_preferences_response import GetPersonalPreferencesResponse
from openapi_server.models.list_environments_payload import ListEnvironmentsPayload
from openapi_server.models.list_environments_response import ListEnvironmentsResponse
from openapi_server.models.list_labs_response import ListLabsResponse
from openapi_server.models.operation_batch_status_payload import OperationBatchStatusPayload
from openapi_server.models.operation_batch_status_response import OperationBatchStatusResponse
from openapi_server.models.operation_status_payload import OperationStatusPayload
from openapi_server.models.operation_status_response import OperationStatusResponse
from openapi_server.models.personal_preferences_operations_payload import PersonalPreferencesOperationsPayload
from openapi_server.models.register_payload import RegisterPayload
from openapi_server.models.reset_password_payload import ResetPasswordPayload
from openapi_server import util


async def global_users_get_environment(request: web.Request, user_name, api_version, environment_operations_payload, expand=None) -> web.Response:
    """global_users_get_environment

    Gets the virtual machine details

    :param user_name: The name of the user.
    :type user_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param environment_operations_payload: Represents payload for any Environment operations like get, start, stop, connect
    :type environment_operations_payload: dict | bytes
    :param expand: Specify the $expand query. Example: &#39;properties($expand&#x3D;environment)&#39;
    :type expand: str

    """
    environment_operations_payload = EnvironmentOperationsPayload.from_dict(environment_operations_payload)
    return web.Response(status=200)


async def global_users_get_operation_batch_status(request: web.Request, user_name, api_version, operation_batch_status_payload) -> web.Response:
    """global_users_get_operation_batch_status

    Get batch operation status

    :param user_name: The name of the user.
    :type user_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param operation_batch_status_payload: Payload to get the status of an operation
    :type operation_batch_status_payload: dict | bytes

    """
    operation_batch_status_payload = OperationBatchStatusPayload.from_dict(operation_batch_status_payload)
    return web.Response(status=200)


async def global_users_get_operation_status(request: web.Request, user_name, api_version, operation_status_payload) -> web.Response:
    """global_users_get_operation_status

    Gets the status of long running operation

    :param user_name: The name of the user.
    :type user_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param operation_status_payload: Payload to get the status of an operation
    :type operation_status_payload: dict | bytes

    """
    operation_status_payload = OperationStatusPayload.from_dict(operation_status_payload)
    return web.Response(status=200)


async def global_users_get_personal_preferences(request: web.Request, user_name, api_version, personal_preferences_operations_payload) -> web.Response:
    """global_users_get_personal_preferences

    Get personal preferences for a user

    :param user_name: The name of the user.
    :type user_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param personal_preferences_operations_payload: Represents payload for any Environment operations like get, start, stop, connect
    :type personal_preferences_operations_payload: dict | bytes

    """
    personal_preferences_operations_payload = PersonalPreferencesOperationsPayload.from_dict(personal_preferences_operations_payload)
    return web.Response(status=200)


async def global_users_list_environments(request: web.Request, user_name, api_version, list_environments_payload) -> web.Response:
    """global_users_list_environments

    List Environments for the user

    :param user_name: The name of the user.
    :type user_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param list_environments_payload: Represents the payload to list environments owned by a user
    :type list_environments_payload: dict | bytes

    """
    list_environments_payload = ListEnvironmentsPayload.from_dict(list_environments_payload)
    return web.Response(status=200)


async def global_users_list_labs(request: web.Request, user_name, api_version) -> web.Response:
    """global_users_list_labs

    List labs for the user.

    :param user_name: The name of the user.
    :type user_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def global_users_register(request: web.Request, user_name, api_version, register_payload) -> web.Response:
    """global_users_register

    Register a user to a managed lab

    :param user_name: The name of the user.
    :type user_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param register_payload: Represents payload for Register action.
    :type register_payload: dict | bytes

    """
    register_payload = RegisterPayload.from_dict(register_payload)
    return web.Response(status=200)


async def global_users_reset_password(request: web.Request, user_name, api_version, reset_password_payload) -> web.Response:
    """global_users_reset_password

    Resets the user password on an environment This operation can take a while to complete

    :param user_name: The name of the user.
    :type user_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param reset_password_payload: Represents the payload for resetting passwords.
    :type reset_password_payload: dict | bytes

    """
    reset_password_payload = ResetPasswordPayload.from_dict(reset_password_payload)
    return web.Response(status=200)


async def global_users_start_environment(request: web.Request, user_name, api_version, environment_operations_payload) -> web.Response:
    """global_users_start_environment

    Starts an environment by starting all resources inside the environment. This operation can take a while to complete

    :param user_name: The name of the user.
    :type user_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param environment_operations_payload: Represents payload for any Environment operations like get, start, stop, connect
    :type environment_operations_payload: dict | bytes

    """
    environment_operations_payload = EnvironmentOperationsPayload.from_dict(environment_operations_payload)
    return web.Response(status=200)


async def global_users_stop_environment(request: web.Request, user_name, api_version, environment_operations_payload) -> web.Response:
    """global_users_stop_environment

    Stops an environment by stopping all resources inside the environment This operation can take a while to complete

    :param user_name: The name of the user.
    :type user_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param environment_operations_payload: Represents payload for any Environment operations like get, start, stop, connect
    :type environment_operations_payload: dict | bytes

    """
    environment_operations_payload = EnvironmentOperationsPayload.from_dict(environment_operations_payload)
    return web.Response(status=200)
