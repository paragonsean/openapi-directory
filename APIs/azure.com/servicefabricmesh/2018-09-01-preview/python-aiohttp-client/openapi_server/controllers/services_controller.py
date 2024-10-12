from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.service_resource_description import ServiceResourceDescription
from openapi_server.models.service_resource_description_list import ServiceResourceDescriptionList
from openapi_server import util


async def service_get(request: web.Request, subscription_id, api_version, resource_group_name, application_resource_name, service_resource_name) -> web.Response:
    """Gets the service resource with the given name.

    Gets the information about the service resource with the given name. The information include the description and other properties of the service.

    :param subscription_id: The customer subscription identifier
    :type subscription_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;.
    :type api_version: str
    :param resource_group_name: Azure resource group name
    :type resource_group_name: str
    :param application_resource_name: The identity of the application.
    :type application_resource_name: str
    :param service_resource_name: The identity of the service.
    :type service_resource_name: str

    """
    return web.Response(status=200)


async def service_list(request: web.Request, subscription_id, api_version, resource_group_name, application_resource_name) -> web.Response:
    """Lists all the service resources.

    Gets the information about all services of an application resource. The information include the description and other properties of the Service.

    :param subscription_id: The customer subscription identifier
    :type subscription_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;.
    :type api_version: str
    :param resource_group_name: Azure resource group name
    :type resource_group_name: str
    :param application_resource_name: The identity of the application.
    :type application_resource_name: str

    """
    return web.Response(status=200)
