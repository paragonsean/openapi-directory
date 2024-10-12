from typing import List, Dict
from aiohttp import web

from openapi_server.models.sso_users import SsoUsers
from openapi_server import util


async def create_sso_users(request: web.Request, body) -> web.Response:
    """Create a SSO User

    Create a SSO User

    :param body: JSON object SsoUsers
    :type body: dict | bytes

    """
    body = SsoUsers.from_dict(body)
    return web.Response(status=200)


async def delete_sso_user_by_id(request: web.Request, id) -> web.Response:
    """Delete a specific SSO User

    Delete a specific SSO User

    :param id: ID of SSO User that needs to be deleted
    :type id: int

    """
    return web.Response(status=200)


async def get_sso_users(request: web.Request, ) -> web.Response:
    """Get a list of SSO Users

    Returns a list of SSO Users


    """
    return web.Response(status=200)


async def get_sso_users_by_id(request: web.Request, id, fields=None) -> web.Response:
    """Find SSO User by ID

    Returns a SSO User based on ID

    :param id: ID of SSO User that needs to be fetched
    :type id: int
    :param fields: Fields to return separate by comas: name,id
    :type fields: str

    """
    return web.Response(status=200)


async def update_sso_users(request: web.Request, id, body) -> web.Response:
    """Update a SSO User

    Update a SSO User

    :param id: ID of SSO User that needs to be updated
    :type id: int
    :param body: JSON object SsoUsers
    :type body: dict | bytes

    """
    body = SsoUsers.from_dict(body)
    return web.Response(status=200)
