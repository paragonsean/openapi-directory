from typing import List, Dict
from aiohttp import web

from openapi_server.models.container_host_mapping import ContainerHostMapping
from openapi_server.models.dev_spaces_error_response import DevSpacesErrorResponse
from openapi_server import util


async def container_host_mappings_get_container_host_mapping(request: web.Request, api_version, subscription_id, resource_group_name, location, container_host_mapping) -> web.Response:
    """Returns container host mapping object for a container host resource ID if an associated controller exists.

    

    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Resource group to which the resource belongs.
    :type resource_group_name: str
    :param location: Location of the container host.
    :type location: str
    :param container_host_mapping: 
    :type container_host_mapping: dict | bytes

    """
    container_host_mapping = ContainerHostMapping.from_dict(container_host_mapping)
    return web.Response(status=200)
