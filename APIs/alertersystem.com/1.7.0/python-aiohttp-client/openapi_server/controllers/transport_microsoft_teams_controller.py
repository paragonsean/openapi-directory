from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_transport_microsoft_teams_get_collection200_response import ApiTransportMicrosoftTeamsGetCollection200Response
from openapi_server.models.transport_microsoft_teams_get import TransportMicrosoftTeamsGet
from openapi_server.models.transport_microsoft_teams_jsonld_get import TransportMicrosoftTeamsJsonldGet
from openapi_server.models.transport_microsoft_teams_jsonld_post import TransportMicrosoftTeamsJsonldPost
from openapi_server.models.transport_microsoft_teams_jsonld_put import TransportMicrosoftTeamsJsonldPut
from openapi_server.models.transport_microsoft_teams_patch import TransportMicrosoftTeamsPatch
from openapi_server.models.transport_microsoft_teams_post import TransportMicrosoftTeamsPost
from openapi_server.models.transport_microsoft_teams_put import TransportMicrosoftTeamsPut
from openapi_server import util


async def api_transport_microsoft_teams_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, partition=None, partition2=None, properties=None) -> web.Response:
    """Retrieves the collection of TransportMicrosoftTeams resources.

    Retrieves the collection of TransportMicrosoftTeams resources.

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
    :param properties: Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]&#x3D;{propertyName}&amp;properties[]&#x3D;{anotherPropertyName}&amp;properties[{nestedPropertyParent}][]&#x3D;{nestedProperty}
    :type properties: List[str]

    """
    return web.Response(status=200)


async def api_transport_microsoft_teams_id_delete(request: web.Request, id) -> web.Response:
    """Removes the TransportMicrosoftTeams resource.

    Removes the TransportMicrosoftTeams resource.

    :param id: TransportMicrosoftTeams identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_microsoft_teams_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a TransportMicrosoftTeams resource.

    Retrieves a TransportMicrosoftTeams resource.

    :param id: TransportMicrosoftTeams identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_transport_microsoft_teams_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the TransportMicrosoftTeams resource.

    Updates the TransportMicrosoftTeams resource.

    :param id: TransportMicrosoftTeams identifier
    :type id: str
    :param body: The updated TransportMicrosoftTeams resource
    :type body: dict | bytes

    """
    body = TransportMicrosoftTeamsPatch.from_dict(body)
    return web.Response(status=200)


async def api_transport_microsoft_teams_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the TransportMicrosoftTeams resource.

    Replaces the TransportMicrosoftTeams resource.

    :param id: TransportMicrosoftTeams identifier
    :type id: str
    :param body: The updated TransportMicrosoftTeams resource
    :type body: dict | bytes

    """
    body = TransportMicrosoftTeamsPut.from_dict(body)
    return web.Response(status=200)


async def api_transport_microsoft_teams_post(request: web.Request, body) -> web.Response:
    """Creates a TransportMicrosoftTeams resource.

    Creates a TransportMicrosoftTeams resource.

    :param body: The new TransportMicrosoftTeams resource
    :type body: dict | bytes

    """
    body = TransportMicrosoftTeamsPost.from_dict(body)
    return web.Response(status=200)
