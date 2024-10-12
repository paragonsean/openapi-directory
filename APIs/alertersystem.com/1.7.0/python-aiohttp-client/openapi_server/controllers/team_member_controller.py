from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_team_member_get_collection200_response import ApiTeamMemberGetCollection200Response
from openapi_server.models.team_member_get import TeamMemberGet
from openapi_server.models.team_member_jsonld_get import TeamMemberJsonldGet
from openapi_server.models.team_member_jsonld_put import TeamMemberJsonldPut
from openapi_server.models.team_member_patch import TeamMemberPatch
from openapi_server.models.team_member_put import TeamMemberPut
from openapi_server import util


async def api_team_member_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, user_account=None, user_account2=None, properties=None) -> web.Response:
    """Retrieves the collection of TeamMember resources.

    Retrieves the collection of TeamMember resources.

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
    :param user_account: 
    :type user_account: str
    :param user_account2: 
    :type user_account2: List[str]
    :param properties: Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]&#x3D;{propertyName}&amp;properties[]&#x3D;{anotherPropertyName}&amp;properties[{nestedPropertyParent}][]&#x3D;{nestedProperty}
    :type properties: List[str]

    """
    return web.Response(status=200)


async def api_team_member_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TeamMember resource.

    Removes the TeamMember resource.

    :param id: TeamMember identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_team_member_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TeamMember resource.

    Retrieves a TeamMember resource.

    :param id: TeamMember identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_team_member_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TeamMember resource.

    Updates the TeamMember resource.

    :param id: TeamMember identifier
    :type id: str
    :param body: The updated TeamMember resource
    :type body: dict | bytes

    """
    body = TeamMemberPatch.from_dict(body)
    return web.Response(status=200)


async def api_team_member_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TeamMember resource.

    Replaces the TeamMember resource.

    :param id: TeamMember identifier
    :type id: str
    :param body: The updated TeamMember resource
    :type body: dict | bytes

    """
    body = TeamMemberPut.from_dict(body)
    return web.Response(status=200)
