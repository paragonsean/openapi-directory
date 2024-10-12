from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.log_profile_collection import LogProfileCollection
from openapi_server.models.log_profile_resource import LogProfileResource
from openapi_server import util


async def log_profiles_create_or_update(request: web.Request, log_profile_name, api_version, subscription_id, parameters) -> web.Response:
    """log_profiles_create_or_update

    Create or update a log profile in Azure Monitoring REST API.

    :param log_profile_name: The name of the log profile.
    :type log_profile_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: The Azure subscription Id.
    :type subscription_id: str
    :param parameters: Parameters supplied to the operation.
    :type parameters: dict | bytes

    """
    parameters = LogProfileResource.from_dict(parameters)
    return web.Response(status=200)


async def log_profiles_delete(request: web.Request, log_profile_name, api_version, subscription_id) -> web.Response:
    """log_profiles_delete

    Deletes the log profile.

    :param log_profile_name: The name of the log profile.
    :type log_profile_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: The Azure subscription Id.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def log_profiles_get(request: web.Request, log_profile_name, api_version, subscription_id) -> web.Response:
    """log_profiles_get

    Gets the log profile.

    :param log_profile_name: The name of the log profile.
    :type log_profile_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: The Azure subscription Id.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def log_profiles_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """log_profiles_list

    List the log profiles.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: The Azure subscription Id.
    :type subscription_id: str

    """
    return web.Response(status=200)
