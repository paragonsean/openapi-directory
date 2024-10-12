from typing import List, Dict
from aiohttp import web

from openapi_server.models.build import Build
from openapi_server.models.build_get_log_result import BuildGetLogResult
from openapi_server.models.build_list_result import BuildListResult
from openapi_server.models.build_update_parameters import BuildUpdateParameters
from openapi_server import util


async def builds_cancel(request: web.Request, subscription_id, resource_group_name, registry_name, api_version, build_id) -> web.Response:
    """builds_cancel

    Cancel an existing build.

    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the container registry belongs.
    :type resource_group_name: str
    :param registry_name: The name of the container registry.
    :type registry_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param build_id: The build ID.
    :type build_id: str

    """
    return web.Response(status=200)


async def builds_get(request: web.Request, subscription_id, resource_group_name, registry_name, api_version, build_id) -> web.Response:
    """builds_get

    Gets the detailed information for a given build.

    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the container registry belongs.
    :type resource_group_name: str
    :param registry_name: The name of the container registry.
    :type registry_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param build_id: The build ID.
    :type build_id: str

    """
    return web.Response(status=200)


async def builds_get_log_link(request: web.Request, subscription_id, resource_group_name, registry_name, api_version, build_id) -> web.Response:
    """builds_get_log_link

    Gets a link to download the build logs.

    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the container registry belongs.
    :type resource_group_name: str
    :param registry_name: The name of the container registry.
    :type registry_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param build_id: The build ID.
    :type build_id: str

    """
    return web.Response(status=200)


async def builds_list(request: web.Request, subscription_id, resource_group_name, registry_name, api_version, filter=None, top=None, skip_token=None) -> web.Response:
    """builds_list

    Gets all the builds for a registry.

    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the container registry belongs.
    :type resource_group_name: str
    :param registry_name: The name of the container registry.
    :type registry_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param filter: The builds filter to apply on the operation.
    :type filter: str
    :param top: $top is supported for get list of builds, which limits the maximum number of builds to return.
    :type top: int
    :param skip_token: $skipToken is supported on get list of builds, which provides the next page in the list of builds.
    :type skip_token: str

    """
    return web.Response(status=200)


async def builds_update(request: web.Request, subscription_id, resource_group_name, registry_name, api_version, build_id, build_update_parameters) -> web.Response:
    """builds_update

    Patch the build properties.

    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the container registry belongs.
    :type resource_group_name: str
    :param registry_name: The name of the container registry.
    :type registry_name: str
    :param api_version: The client API version.
    :type api_version: str
    :param build_id: The build ID.
    :type build_id: str
    :param build_update_parameters: The build update properties.
    :type build_update_parameters: dict | bytes

    """
    build_update_parameters = BuildUpdateParameters.from_dict(build_update_parameters)
    return web.Response(status=200)
