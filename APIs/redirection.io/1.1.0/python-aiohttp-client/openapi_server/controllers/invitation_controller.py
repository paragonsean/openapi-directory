from typing import List, Dict
from aiohttp import web

from openapi_server.models.invitation import Invitation
from openapi_server.models.invitation_read import InvitationRead
from openapi_server.models.invitation_write import InvitationWrite
from openapi_server import util


async def accept_invitation_item(request: web.Request, token, invitation) -> web.Response:
    """Creates a Invitation resource.

    

    :param token: The invitation acceptation token
    :type token: str
    :param invitation: The new Invitation resource
    :type invitation: dict | bytes

    """
    invitation = Invitation.from_dict(invitation)
    return web.Response(status=200)


async def delete_invitation_item(request: web.Request, id) -> web.Response:
    """Removes the Invitation resource.

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_invitation_collection(request: web.Request, target_id, target_type) -> web.Response:
    """Retrieves the collection of Invitation resources.

    

    :param target_id: 
    :type target_id: str
    :param target_type: 
    :type target_type: str

    """
    return web.Response(status=200)


async def get_invitation_item(request: web.Request, id) -> web.Response:
    """Retrieves a Invitation resource.

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def post_invitation_collection(request: web.Request, invitation=None) -> web.Response:
    """Creates a Invitation resource.

    

    :param invitation: The new Invitation resource
    :type invitation: dict | bytes

    """
    invitation = InvitationWrite.from_dict(invitation)
    return web.Response(status=200)
