from typing import List, Dict
from aiohttp import web

from openapi_server.models.consumer_invitation import ConsumerInvitation
from openapi_server.models.consumer_invitation_list import ConsumerInvitationList
from openapi_server.models.data_share_error import DataShareError
from openapi_server import util


async def consumer_invitations_get(request: web.Request, location, invitation_id, api_version) -> web.Response:
    """Gets the invitation identified by invitationId

    Get an invitation

    :param location: Location of the invitation
    :type location: str
    :param invitation_id: An invitation id
    :type invitation_id: str
    :param api_version: The api version to use.
    :type api_version: str

    """
    return web.Response(status=200)


async def consumer_invitations_list_invitations(request: web.Request, api_version, skip_token=None) -> web.Response:
    """List the invitations

    Lists invitations

    :param api_version: The api version to use.
    :type api_version: str
    :param skip_token: The continuation token
    :type skip_token: str

    """
    return web.Response(status=200)


async def consumer_invitations_reject_invitation(request: web.Request, location, api_version, invitation) -> web.Response:
    """Rejects the invitation identified by invitationId

    Reject an invitation

    :param location: Location of the invitation
    :type location: str
    :param api_version: The api version to use.
    :type api_version: str
    :param invitation: An invitation payload
    :type invitation: dict | bytes

    """
    invitation = ConsumerInvitation.from_dict(invitation)
    return web.Response(status=200)
