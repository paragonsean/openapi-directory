from typing import List, Dict
from aiohttp import web

from openapi_server.models.collaborator_invitation import CollaboratorInvitation
from openapi_server.models.collaborator_invitation_create import CollaboratorInvitationCreate
from openapi_server import util


async def collaborator_invitations_get(request: web.Request, ) -> web.Response:
    """List your collaborator invitations

    List your collaborator invitations.


    """
    return web.Response(status=200)


async def collaborator_invitations_id_delete(request: web.Request, id) -> web.Response:
    """Delete collaborator invitation

    Delete collaborator invitation.

    :param id: Collaborator invitation id
    :type id: int

    """
    return web.Response(status=200)


async def collaborator_invitations_id_get(request: web.Request, id) -> web.Response:
    """Show collaborator invitation

    Show collaborator invitation

    :param id: Collaborator invitation id
    :type id: int

    """
    return web.Response(status=200)


async def collaborator_invitations_id_patch(request: web.Request, id) -> web.Response:
    """Accept collaborator invitation.

    Accept collaborator invitation.

    :param id: Collaborator invitation id
    :type id: int

    """
    return web.Response(status=200)


async def collaborator_invitations_post(request: web.Request, body=None) -> web.Response:
    """Invite user to collaborate on map

    Invite user to collaborate on map.

    :param body: Supply map_id and either a comma separated list of user_ids or emails. Optionally you can provide a &#39;is_admin&#39; parameter with &#39;true&#39; or &#39;false&#39; to give the invited users admin privileges.
    :type body: dict | bytes

    """
    body = CollaboratorInvitationCreate.from_dict(body)
    return web.Response(status=200)
