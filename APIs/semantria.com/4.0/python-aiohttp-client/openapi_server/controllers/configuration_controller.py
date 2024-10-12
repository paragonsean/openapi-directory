from typing import List, Dict
from aiohttp import web

from openapi_server.models.configuration_response_version import ConfigurationResponseVersion
from openapi_server import util


async def add_configurations(request: web.Request, content_type, configurations) -> web.Response:
    """Create user configurations

    This method creates configurations on Semantria side.

    :param content_type: 
    :type content_type: str
    :param configurations: List of parametrized JSON or XML objects.
    :type configurations: 

    """
    return web.Response(status=200)


async def delete_configurations(request: web.Request, content_type, configuration_ids) -> web.Response:
    """Remove user configurations

    This method removes certain configuration by unique ID on Semantria side.

    :param content_type: 
    :type content_type: str
    :param configuration_ids: List of configuration identifiers.
    :type configuration_ids: List[str]

    """
    return web.Response(status=200)


async def get_configurations(request: web.Request, content_type) -> web.Response:
    """Retrieve user configurations

    This method retrieves all user configurations available on Semantria side.

    :param content_type: 
    :type content_type: str

    """
    return web.Response(status=200)


async def update_configurations(request: web.Request, content_type, configurations) -> web.Response:
    """Update user configurations

    This method updates specific configurations by unique IDs on Semantria side.

    :param content_type: 
    :type content_type: str
    :param configurations: List of parametrized JSON or XML objects.
    :type configurations: 

    """
    return web.Response(status=200)
