from typing import List, Dict
from aiohttp import web

from openapi_server.models.fabric_error import FabricError
from openapi_server.models.paged_service_resource_description_list import PagedServiceResourceDescriptionList
from openapi_server.models.service_resource_description import ServiceResourceDescription
from openapi_server import util


async def mesh_service_get(request: web.Request, api_version, application_resource_name, service_resource_name) -> web.Response:
    """Gets the Service resource with the given name.

    Gets the information about the Service resource with the given name. The information include the description and other properties of the Service.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.4-preview&#39;.
    :type api_version: str
    :param application_resource_name: The identity of the application.
    :type application_resource_name: str
    :param service_resource_name: The identity of the service.
    :type service_resource_name: str

    """
    return web.Response(status=200)


async def mesh_service_list(request: web.Request, api_version, application_resource_name) -> web.Response:
    """Lists all the service resources.

    Gets the information about all services of an application resource. The information include the description and other properties of the Service.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.4-preview&#39;.
    :type api_version: str
    :param application_resource_name: The identity of the application.
    :type application_resource_name: str

    """
    return web.Response(status=200)
