from typing import List, Dict
from aiohttp import web

from openapi_server.models.service_list import ServiceList
from openapi_server.models.service_resource_description import ServiceResourceDescription
from openapi_server import util


async def service_get(request: web.Request, subscription_id, api_version, resource_group_name, application_name, service_name) -> web.Response:
    """Gets the properties of the service.

    The operation returns the properties of the service.

    :param subscription_id: The customer subscription identifier
    :type subscription_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#x60;2018-07-01-preview&#x60;.
    :type api_version: str
    :param resource_group_name: Azure resource group name
    :type resource_group_name: str
    :param application_name: The identity of the application.
    :type application_name: str
    :param service_name: The identity of the service.
    :type service_name: str

    """
    return web.Response(status=200)


async def service_list_by_application_name(request: web.Request, subscription_id, api_version, resource_group_name, application_name) -> web.Response:
    """Gets services of a given application.

    Gets the information about all services of a given service of an application. The information includes the runtime properties of the service instance.

    :param subscription_id: The customer subscription identifier
    :type subscription_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#x60;2018-07-01-preview&#x60;.
    :type api_version: str
    :param resource_group_name: Azure resource group name
    :type resource_group_name: str
    :param application_name: The identity of the application.
    :type application_name: str

    """
    return web.Response(status=200)
