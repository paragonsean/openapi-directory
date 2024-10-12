from typing import List, Dict
from aiohttp import web

from openapi_server.models.controller import Controller
from openapi_server.models.controller_connection_details_list import ControllerConnectionDetailsList
from openapi_server.models.controller_list import ControllerList
from openapi_server.models.controller_update_parameters import ControllerUpdateParameters
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def controllers_create(request: web.Request, api_version, subscription_id, resource_group_name, name, controller) -> web.Response:
    """Creates an Azure Dev Spaces Controller.

    Creates an Azure Dev Spaces Controller with the specified create parameters.

    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the resource.
    :type name: str
    :param controller: Controller create parameters.
    :type controller: dict | bytes

    """
    controller = Controller.from_dict(controller)
    return web.Response(status=200)


async def controllers_delete(request: web.Request, api_version, subscription_id, resource_group_name, name) -> web.Response:
    """Deletes an Azure Dev Spaces Controller.

    Deletes an existing Azure Dev Spaces Controller.

    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the resource.
    :type name: str

    """
    return web.Response(status=200)


async def controllers_get(request: web.Request, api_version, subscription_id, resource_group_name, name) -> web.Response:
    """Gets an Azure Dev Spaces Controller.

    Gets the properties for an Azure Dev Spaces Controller.

    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the resource.
    :type name: str

    """
    return web.Response(status=200)


async def controllers_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """Lists the Azure Dev Spaces Controllers in a subscription.

    Lists all the Azure Dev Spaces Controllers with their properties in the subscription.

    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Azure subscription ID.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def controllers_list_by_resource_group(request: web.Request, api_version, subscription_id, resource_group_name) -> web.Response:
    """Lists the Azure Dev Spaces Controllers in a resource group.

    Lists all the Azure Dev Spaces Controllers with their properties in the specified resource group and subscription.

    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Resource group to which the resource belongs.
    :type resource_group_name: str

    """
    return web.Response(status=200)


async def controllers_list_connection_details(request: web.Request, api_version, subscription_id, resource_group_name, name) -> web.Response:
    """Lists connection details for an Azure Dev Spaces Controller.

    Lists connection details for the underlying container resources of an Azure Dev Spaces Controller.

    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the resource.
    :type name: str

    """
    return web.Response(status=200)


async def controllers_update(request: web.Request, api_version, subscription_id, resource_group_name, name, controller_update_parameters) -> web.Response:
    """Updates an Azure Dev Spaces Controller.

    Updates the properties of an existing Azure Dev Spaces Controller with the specified update parameters.

    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the resource.
    :type name: str
    :param controller_update_parameters: Parameters for updating the Azure Dev Spaces Controller.
    :type controller_update_parameters: dict | bytes

    """
    controller_update_parameters = ControllerUpdateParameters.from_dict(controller_update_parameters)
    return web.Response(status=200)
