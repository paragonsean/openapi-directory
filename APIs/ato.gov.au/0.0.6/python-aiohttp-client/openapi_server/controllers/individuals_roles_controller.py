from typing import List, Dict
from aiohttp import web

from openapi_server.models.invalid_argument import InvalidArgument
from openapi_server.models.not_found import NotFound
from openapi_server.models.party_role import PartyRole
from openapi_server.models.unauthenticated import Unauthenticated
from openapi_server import util


async def individuals_party_id_roles_get(request: web.Request, api_key, party_id) -> web.Response:
    """Retrieve a list of roles

    

    :param api_key: The API key.
    :type api_key: str
    :param party_id: The party identifier.
    :type party_id: str

    """
    return web.Response(status=200)


async def individuals_party_id_roles_post(request: web.Request, api_key, party_id, body) -> web.Response:
    """Create a role

    Create a role 

    :param api_key: The API key.
    :type api_key: str
    :param party_id: The party identifier.
    :type party_id: str
    :param body: Role resource
    :type body: dict | bytes

    """
    body = PartyRole.from_dict(body)
    return web.Response(status=200)


async def individuals_party_id_roles_role_id_delete(request: web.Request, api_key, party_id, role_id) -> web.Response:
    """Delete a role

    Delete a role 

    :param api_key: The API key.
    :type api_key: str
    :param party_id: The party identifier.
    :type party_id: str
    :param role_id: The role identifier.
    :type role_id: str

    """
    return web.Response(status=200)


async def individuals_party_id_roles_role_id_get(request: web.Request, api_key, party_id, role_id) -> web.Response:
    """Retrieve a role

    Retrieve a role 

    :param api_key: The API key.
    :type api_key: str
    :param party_id: The party identifier.
    :type party_id: str
    :param role_id: The role identifier.
    :type role_id: str

    """
    return web.Response(status=200)


async def individuals_party_id_roles_role_id_put(request: web.Request, api_key, party_id, role_id, body) -> web.Response:
    """Update a role

    Update a role 

    :param api_key: The API key.
    :type api_key: str
    :param party_id: The party identifier.
    :type party_id: str
    :param role_id: The role identifier.
    :type role_id: str
    :param body: Role resource
    :type body: dict | bytes

    """
    body = PartyRole.from_dict(body)
    return web.Response(status=200)
