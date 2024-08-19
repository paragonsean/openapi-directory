from typing import List, Dict
from aiohttp import web

from openapi_server.models.collaborator_update import CollaboratorUpdate
from openapi_server.models.error import Error
from openapi_server.models.user_account import UserAccount
from openapi_server.models.user_account_roles_results import UserAccountRolesResults
from openapi_server import util


async def delete_collaborator(request: web.Request, user_id) -> web.Response:
    """Delete collaborator

    

    :param user_id: User ID
    :type user_id: int

    """
    return web.Response(status=200)


async def get_collaborator(request: web.Request, user_id) -> web.Response:
    """Get collaborator

    

    :param user_id: User ID
    :type user_id: int

    """
    return web.Response(status=200)


async def get_collaborators(request: web.Request, ) -> web.Response:
    """Get collaborators

    


    """
    return web.Response(status=200)


async def update_collaborator(request: web.Request, body) -> web.Response:
    """Update collaborator

    

    :param body: 
    :type body: dict | bytes

    """
    body = CollaboratorUpdate.from_dict(body)
    return web.Response(status=200)
