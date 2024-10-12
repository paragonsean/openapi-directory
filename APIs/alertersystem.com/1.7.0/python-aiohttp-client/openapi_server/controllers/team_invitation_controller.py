from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_team_invitation_get_collection200_response import ApiTeamInvitationGetCollection200Response
from openapi_server.models.team_invitation_get import TeamInvitationGet
from openapi_server.models.team_invitation_jsonld_get import TeamInvitationJsonldGet
from openapi_server.models.team_invitation_jsonld_post import TeamInvitationJsonldPost
from openapi_server.models.team_invitation_post import TeamInvitationPost
from openapi_server import util


async def api_team_invitation_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, invitee_email=None, invitee_email2=None, properties=None) -> web.Response:
    """Retrieves the collection of TeamInvitation resources.

    Retrieves the collection of TeamInvitation resources.

    :param page: The collection page number
    :type page: int
    :param data_segment_code: 
    :type data_segment_code: str
    :param data_segment_code2: 
    :type data_segment_code2: List[str]
    :param partition: 
    :type partition: str
    :param partition2: 
    :type partition2: List[str]
    :param invitee_email: 
    :type invitee_email: str
    :param invitee_email2: 
    :type invitee_email2: List[str]
    :param properties: Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]&#x3D;{propertyName}&amp;properties[]&#x3D;{anotherPropertyName}&amp;properties[{nestedPropertyParent}][]&#x3D;{nestedProperty}
    :type properties: List[str]

    """
    return web.Response(status=200)


async def api_team_invitation_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TeamInvitation resource.

    Removes the TeamInvitation resource.

    :param id: TeamInvitation identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_team_invitation_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TeamInvitation resource.

    Retrieves a TeamInvitation resource.

    :param id: TeamInvitation identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_team_invitation_post(request: web.Request, body) -> web.Response:
    """Creates a TeamInvitation resource.

    Creates a TeamInvitation resource.

    :param body: The new TeamInvitation resource
    :type body: dict | bytes

    """
    body = TeamInvitationPost.from_dict(body)
    return web.Response(status=200)
