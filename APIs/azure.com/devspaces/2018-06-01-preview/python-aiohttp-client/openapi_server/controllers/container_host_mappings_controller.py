from typing import List, Dict
from aiohttp import web

from openapi_server.models.container_host_mapping import ContainerHostMapping
from openapi_server import util


async def container_host_mappings_get_container_host_mapping(request: web.Request, api_version, location, container_host_mapping) -> web.Response:
    """Returns container host mapping object for a container host resource ID if an associated controller exists.

    

    :param api_version: Client API version.
    :type api_version: str
    :param location: Location of the container host.
    :type location: str
    :param container_host_mapping: 
    :type container_host_mapping: dict | bytes

    """
    container_host_mapping = ContainerHostMapping.from_dict(container_host_mapping)
    return web.Response(status=200)
