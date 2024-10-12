from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.error_limited import ErrorLimited
from openapi_server.models.forbidden import Forbidden
from openapi_server.models.gateway_timeout import GatewayTimeout
from openapi_server.models.get_characters_character_id_agents_research200_ok import GetCharactersCharacterIdAgentsResearch200Ok
from openapi_server.models.get_characters_character_id_blueprints200_ok import GetCharactersCharacterIdBlueprints200Ok
from openapi_server.models.get_characters_character_id_corporationhistory200_ok import GetCharactersCharacterIdCorporationhistory200Ok
from openapi_server.models.get_characters_character_id_fatigue_ok import GetCharactersCharacterIdFatigueOk
from openapi_server.models.get_characters_character_id_medals200_ok import GetCharactersCharacterIdMedals200Ok
from openapi_server.models.get_characters_character_id_not_found import GetCharactersCharacterIdNotFound
from openapi_server.models.get_characters_character_id_notifications200_ok import GetCharactersCharacterIdNotifications200Ok
from openapi_server.models.get_characters_character_id_notifications_contacts200_ok import GetCharactersCharacterIdNotificationsContacts200Ok
from openapi_server.models.get_characters_character_id_ok import GetCharactersCharacterIdOk
from openapi_server.models.get_characters_character_id_portrait_not_found import GetCharactersCharacterIdPortraitNotFound
from openapi_server.models.get_characters_character_id_portrait_ok import GetCharactersCharacterIdPortraitOk
from openapi_server.models.get_characters_character_id_roles_ok import GetCharactersCharacterIdRolesOk
from openapi_server.models.get_characters_character_id_standings200_ok import GetCharactersCharacterIdStandings200Ok
from openapi_server.models.get_characters_character_id_stats200_ok import GetCharactersCharacterIdStats200Ok
from openapi_server.models.get_characters_character_id_titles200_ok import GetCharactersCharacterIdTitles200Ok
from openapi_server.models.internal_server_error import InternalServerError
from openapi_server.models.post_characters_affiliation200_ok import PostCharactersAffiliation200Ok
from openapi_server.models.post_characters_affiliation_not_found import PostCharactersAffiliationNotFound
from openapi_server.models.service_unavailable import ServiceUnavailable
from openapi_server.models.unauthorized import Unauthorized
from openapi_server import util


async def get_characters_character_id(request: web.Request, character_id, datasource=None, if_none_match=None) -> web.Response:
    """Get character&#39;s public information

    Public information about a character  --- Alternate route: &#x60;/dev/characters/{character_id}/&#x60;  Alternate route: &#x60;/v4/characters/{character_id}/&#x60;  --- This route is cached for up to 3600 seconds

    :param character_id: An EVE character ID
    :type character_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_characters_character_id_agents_research(request: web.Request, character_id, datasource=None, if_none_match=None, token=None) -> web.Response:
    """Get agents research

    Return a list of agents research information for a character. The formula for finding the current research points with an agent is: currentPoints &#x3D; remainderPoints + pointsPerDay * days(currentTime - researchStartDate)  --- Alternate route: &#x60;/dev/characters/{character_id}/agents_research/&#x60;  Alternate route: &#x60;/legacy/characters/{character_id}/agents_research/&#x60;  Alternate route: &#x60;/v1/characters/{character_id}/agents_research/&#x60;  --- This route is cached for up to 3600 seconds

    :param character_id: An EVE character ID
    :type character_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    return web.Response(status=200)


async def get_characters_character_id_blueprints(request: web.Request, character_id, datasource=None, if_none_match=None, page=None, token=None) -> web.Response:
    """Get blueprints

    Return a list of blueprints the character owns  --- Alternate route: &#x60;/dev/characters/{character_id}/blueprints/&#x60;  Alternate route: &#x60;/v2/characters/{character_id}/blueprints/&#x60;  --- This route is cached for up to 3600 seconds

    :param character_id: An EVE character ID
    :type character_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str
    :param page: Which page of results to return
    :type page: int
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    return web.Response(status=200)


async def get_characters_character_id_corporationhistory(request: web.Request, character_id, datasource=None, if_none_match=None) -> web.Response:
    """Get corporation history

    Get a list of all the corporations a character has been a member of  --- Alternate route: &#x60;/dev/characters/{character_id}/corporationhistory/&#x60;  Alternate route: &#x60;/legacy/characters/{character_id}/corporationhistory/&#x60;  Alternate route: &#x60;/v1/characters/{character_id}/corporationhistory/&#x60;  --- This route is cached for up to 3600 seconds

    :param character_id: An EVE character ID
    :type character_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_characters_character_id_fatigue(request: web.Request, character_id, datasource=None, if_none_match=None, token=None) -> web.Response:
    """Get jump fatigue

    Return a character&#39;s jump activation and fatigue information  --- Alternate route: &#x60;/dev/characters/{character_id}/fatigue/&#x60;  Alternate route: &#x60;/legacy/characters/{character_id}/fatigue/&#x60;  Alternate route: &#x60;/v1/characters/{character_id}/fatigue/&#x60;  --- This route is cached for up to 300 seconds

    :param character_id: An EVE character ID
    :type character_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    return web.Response(status=200)


async def get_characters_character_id_medals(request: web.Request, character_id, datasource=None, if_none_match=None, token=None) -> web.Response:
    """Get medals

    Return a list of medals the character has  --- Alternate route: &#x60;/dev/characters/{character_id}/medals/&#x60;  Alternate route: &#x60;/legacy/characters/{character_id}/medals/&#x60;  Alternate route: &#x60;/v1/characters/{character_id}/medals/&#x60;  --- This route is cached for up to 3600 seconds

    :param character_id: An EVE character ID
    :type character_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    return web.Response(status=200)


async def get_characters_character_id_notifications(request: web.Request, character_id, datasource=None, if_none_match=None, token=None) -> web.Response:
    """Get character notifications

    Return character notifications  --- Alternate route: &#x60;/dev/characters/{character_id}/notifications/&#x60;  Alternate route: &#x60;/v4/characters/{character_id}/notifications/&#x60;  --- This route is cached for up to 600 seconds

    :param character_id: An EVE character ID
    :type character_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    return web.Response(status=200)


async def get_characters_character_id_notifications_contacts(request: web.Request, character_id, datasource=None, if_none_match=None, token=None) -> web.Response:
    """Get new contact notifications

    Return notifications about having been added to someone&#39;s contact list  --- Alternate route: &#x60;/dev/characters/{character_id}/notifications/contacts/&#x60;  Alternate route: &#x60;/legacy/characters/{character_id}/notifications/contacts/&#x60;  Alternate route: &#x60;/v1/characters/{character_id}/notifications/contacts/&#x60;  --- This route is cached for up to 600 seconds

    :param character_id: An EVE character ID
    :type character_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    return web.Response(status=200)


async def get_characters_character_id_portrait(request: web.Request, character_id, datasource=None, if_none_match=None) -> web.Response:
    """Get character portraits

    Get portrait urls for a character  --- Alternate route: &#x60;/dev/characters/{character_id}/portrait/&#x60;  Alternate route: &#x60;/v2/characters/{character_id}/portrait/&#x60;  --- This route expires daily at 11:05

    :param character_id: An EVE character ID
    :type character_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_characters_character_id_roles(request: web.Request, character_id, datasource=None, if_none_match=None, token=None) -> web.Response:
    """Get character corporation roles

    Returns a character&#39;s corporation roles  --- Alternate route: &#x60;/dev/characters/{character_id}/roles/&#x60;  Alternate route: &#x60;/v2/characters/{character_id}/roles/&#x60;  --- This route is cached for up to 3600 seconds

    :param character_id: An EVE character ID
    :type character_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    return web.Response(status=200)


async def get_characters_character_id_standings(request: web.Request, character_id, datasource=None, if_none_match=None, token=None) -> web.Response:
    """Get standings

    Return character standings from agents, NPC corporations, and factions  --- Alternate route: &#x60;/dev/characters/{character_id}/standings/&#x60;  Alternate route: &#x60;/legacy/characters/{character_id}/standings/&#x60;  Alternate route: &#x60;/v1/characters/{character_id}/standings/&#x60;  --- This route is cached for up to 3600 seconds

    :param character_id: An EVE character ID
    :type character_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    return web.Response(status=200)


async def get_characters_character_id_stats(request: web.Request, character_id, datasource=None, if_none_match=None, token=None) -> web.Response:
    """Yearly aggregate stats

    Returns aggregate yearly stats for a character  --- Alternate route: &#x60;/dev/characters/{character_id}/stats/&#x60;  Alternate route: &#x60;/v2/characters/{character_id}/stats/&#x60;  --- This route is cached for up to 86400 seconds

    :param character_id: An EVE character ID
    :type character_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    return web.Response(status=200)


async def get_characters_character_id_titles(request: web.Request, character_id, datasource=None, if_none_match=None, token=None) -> web.Response:
    """Get character corporation titles

    Returns a character&#39;s titles  --- Alternate route: &#x60;/dev/characters/{character_id}/titles/&#x60;  Alternate route: &#x60;/legacy/characters/{character_id}/titles/&#x60;  Alternate route: &#x60;/v1/characters/{character_id}/titles/&#x60;  --- This route is cached for up to 3600 seconds

    :param character_id: An EVE character ID
    :type character_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    return web.Response(status=200)


async def post_characters_affiliation(request: web.Request, characters, datasource=None) -> web.Response:
    """Character affiliation

    Bulk lookup of character IDs to corporation, alliance and faction  --- Alternate route: &#x60;/dev/characters/affiliation/&#x60;  Alternate route: &#x60;/legacy/characters/affiliation/&#x60;  Alternate route: &#x60;/v1/characters/affiliation/&#x60;  --- This route is cached for up to 3600 seconds

    :param characters: The character IDs to fetch affiliations for. All characters must exist, or none will be returned
    :type characters: List[int]
    :param datasource: The server name you would like data from
    :type datasource: str

    """
    return web.Response(status=200)


async def post_characters_character_id_cspa(request: web.Request, character_id, characters, datasource=None, token=None) -> web.Response:
    """Calculate a CSPA charge cost

    Takes a source character ID in the url and a set of target character ID&#39;s in the body, returns a CSPA charge cost  --- Alternate route: &#x60;/dev/characters/{character_id}/cspa/&#x60;  Alternate route: &#x60;/v4/characters/{character_id}/cspa/&#x60; 

    :param character_id: An EVE character ID
    :type character_id: int
    :param characters: The target characters to calculate the charge for
    :type characters: List[int]
    :param datasource: The server name you would like data from
    :type datasource: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    return web.Response(status=200)
