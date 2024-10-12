from typing import List, Dict
from aiohttp import web

from openapi_server.models.entity_response_version import EntityResponseVersion
from openapi_server import util


async def add_entities(request: web.Request, content_type, user_entities, config_id=None) -> web.Response:
    """Add user entities

    This method adds user entities on Semantria side.

    :param content_type: 
    :type content_type: str
    :param user_entities: List of parametrized JSON or XML objects.
    :type user_entities: 
    :param config_id: Identifier of configuration user entities linked to.
    :type config_id: str

    """
    return web.Response(status=200)


async def delete_entities(request: web.Request, content_type) -> web.Response:
    """Remove user entities

    This method removes certain user entities by their names on Semantria side.

    :param content_type: 
    :type content_type: str

    """
    return web.Response(status=200)


async def get_entities(request: web.Request, content_type, config_id=None) -> web.Response:
    """Retrieve user entities

    This method retrieves list of user entities available on Semantria side.

    :param content_type: 
    :type content_type: str
    :param config_id: Identifier of configuration user entities linked to.
    :type config_id: str

    """
    return web.Response(status=200)


async def update_entities(request: web.Request, content_type, user_entities, config_id=None) -> web.Response:
    """Update user entities

    This method updates user entities by unique IDs on Semantria side.

    :param content_type: 
    :type content_type: str
    :param user_entities: List of parametrized JSON or XML objects.
    :type user_entities: 
    :param config_id: Identifier of configuration user entities linked to.
    :type config_id: str

    """
    return web.Response(status=200)
