from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.error_limited import ErrorLimited
from openapi_server.models.forbidden import Forbidden
from openapi_server.models.gateway_timeout import GatewayTimeout
from openapi_server.models.get_corporations_corporation_id_alliancehistory200_ok import GetCorporationsCorporationIdAlliancehistory200Ok
from openapi_server.models.get_corporations_corporation_id_blueprints200_ok import GetCorporationsCorporationIdBlueprints200Ok
from openapi_server.models.get_corporations_corporation_id_containers_logs200_ok import GetCorporationsCorporationIdContainersLogs200Ok
from openapi_server.models.get_corporations_corporation_id_divisions_ok import GetCorporationsCorporationIdDivisionsOk
from openapi_server.models.get_corporations_corporation_id_facilities200_ok import GetCorporationsCorporationIdFacilities200Ok
from openapi_server.models.get_corporations_corporation_id_icons_not_found import GetCorporationsCorporationIdIconsNotFound
from openapi_server.models.get_corporations_corporation_id_icons_ok import GetCorporationsCorporationIdIconsOk
from openapi_server.models.get_corporations_corporation_id_medals200_ok import GetCorporationsCorporationIdMedals200Ok
from openapi_server.models.get_corporations_corporation_id_medals_issued200_ok import GetCorporationsCorporationIdMedalsIssued200Ok
from openapi_server.models.get_corporations_corporation_id_members_titles200_ok import GetCorporationsCorporationIdMembersTitles200Ok
from openapi_server.models.get_corporations_corporation_id_membertracking200_ok import GetCorporationsCorporationIdMembertracking200Ok
from openapi_server.models.get_corporations_corporation_id_not_found import GetCorporationsCorporationIdNotFound
from openapi_server.models.get_corporations_corporation_id_ok import GetCorporationsCorporationIdOk
from openapi_server.models.get_corporations_corporation_id_roles200_ok import GetCorporationsCorporationIdRoles200Ok
from openapi_server.models.get_corporations_corporation_id_roles_history200_ok import GetCorporationsCorporationIdRolesHistory200Ok
from openapi_server.models.get_corporations_corporation_id_shareholders200_ok import GetCorporationsCorporationIdShareholders200Ok
from openapi_server.models.get_corporations_corporation_id_standings200_ok import GetCorporationsCorporationIdStandings200Ok
from openapi_server.models.get_corporations_corporation_id_starbases200_ok import GetCorporationsCorporationIdStarbases200Ok
from openapi_server.models.get_corporations_corporation_id_starbases_starbase_id_ok import GetCorporationsCorporationIdStarbasesStarbaseIdOk
from openapi_server.models.get_corporations_corporation_id_structures200_ok import GetCorporationsCorporationIdStructures200Ok
from openapi_server.models.get_corporations_corporation_id_titles200_ok import GetCorporationsCorporationIdTitles200Ok
from openapi_server.models.internal_server_error import InternalServerError
from openapi_server.models.service_unavailable import ServiceUnavailable
from openapi_server.models.unauthorized import Unauthorized
from openapi_server import util


async def get_corporations_corporation_id(request: web.Request, corporation_id, datasource=None, if_none_match=None) -> web.Response:
    """Get corporation information

    Public information about a corporation  --- Alternate route: &#x60;/dev/corporations/{corporation_id}/&#x60;  Alternate route: &#x60;/v4/corporations/{corporation_id}/&#x60;  --- This route is cached for up to 3600 seconds

    :param corporation_id: An EVE corporation ID
    :type corporation_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_corporations_corporation_id_alliancehistory(request: web.Request, corporation_id, datasource=None, if_none_match=None) -> web.Response:
    """Get alliance history

    Get a list of all the alliances a corporation has been a member of  --- Alternate route: &#x60;/dev/corporations/{corporation_id}/alliancehistory/&#x60;  Alternate route: &#x60;/v2/corporations/{corporation_id}/alliancehistory/&#x60;  --- This route is cached for up to 3600 seconds

    :param corporation_id: An EVE corporation ID
    :type corporation_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_corporations_corporation_id_blueprints(request: web.Request, corporation_id, datasource=None, if_none_match=None, page=None, token=None) -> web.Response:
    """Get corporation blueprints

    Returns a list of blueprints the corporation owns  --- Alternate route: &#x60;/dev/corporations/{corporation_id}/blueprints/&#x60;  Alternate route: &#x60;/v2/corporations/{corporation_id}/blueprints/&#x60;  --- This route is cached for up to 3600 seconds  --- Requires one of the following EVE corporation role(s): Director 

    :param corporation_id: An EVE corporation ID
    :type corporation_id: int
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


async def get_corporations_corporation_id_containers_logs(request: web.Request, corporation_id, datasource=None, if_none_match=None, page=None, token=None) -> web.Response:
    """Get all corporation ALSC logs

    Returns logs recorded in the past seven days from all audit log secure containers (ALSC) owned by a given corporation  --- Alternate route: &#x60;/dev/corporations/{corporation_id}/containers/logs/&#x60;  Alternate route: &#x60;/v2/corporations/{corporation_id}/containers/logs/&#x60;  --- This route is cached for up to 600 seconds  --- Requires one of the following EVE corporation role(s): Director 

    :param corporation_id: An EVE corporation ID
    :type corporation_id: int
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


async def get_corporations_corporation_id_divisions(request: web.Request, corporation_id, datasource=None, if_none_match=None, token=None) -> web.Response:
    """Get corporation divisions

    Return corporation hangar and wallet division names, only show if a division is not using the default name  --- Alternate route: &#x60;/dev/corporations/{corporation_id}/divisions/&#x60;  Alternate route: &#x60;/legacy/corporations/{corporation_id}/divisions/&#x60;  Alternate route: &#x60;/v1/corporations/{corporation_id}/divisions/&#x60;  --- This route is cached for up to 3600 seconds  --- Requires one of the following EVE corporation role(s): Director 

    :param corporation_id: An EVE corporation ID
    :type corporation_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    return web.Response(status=200)


async def get_corporations_corporation_id_facilities(request: web.Request, corporation_id, datasource=None, if_none_match=None, token=None) -> web.Response:
    """Get corporation facilities

    Return a corporation&#39;s facilities  --- Alternate route: &#x60;/dev/corporations/{corporation_id}/facilities/&#x60;  Alternate route: &#x60;/legacy/corporations/{corporation_id}/facilities/&#x60;  Alternate route: &#x60;/v1/corporations/{corporation_id}/facilities/&#x60;  --- This route is cached for up to 3600 seconds  --- Requires one of the following EVE corporation role(s): Factory_Manager 

    :param corporation_id: An EVE corporation ID
    :type corporation_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    return web.Response(status=200)


async def get_corporations_corporation_id_icons(request: web.Request, corporation_id, datasource=None, if_none_match=None) -> web.Response:
    """Get corporation icon

    Get the icon urls for a corporation  --- Alternate route: &#x60;/dev/corporations/{corporation_id}/icons/&#x60;  Alternate route: &#x60;/legacy/corporations/{corporation_id}/icons/&#x60;  Alternate route: &#x60;/v1/corporations/{corporation_id}/icons/&#x60;  --- This route is cached for up to 3600 seconds

    :param corporation_id: An EVE corporation ID
    :type corporation_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_corporations_corporation_id_medals(request: web.Request, corporation_id, datasource=None, if_none_match=None, page=None, token=None) -> web.Response:
    """Get corporation medals

    Returns a corporation&#39;s medals  --- Alternate route: &#x60;/dev/corporations/{corporation_id}/medals/&#x60;  Alternate route: &#x60;/legacy/corporations/{corporation_id}/medals/&#x60;  Alternate route: &#x60;/v1/corporations/{corporation_id}/medals/&#x60;  --- This route is cached for up to 3600 seconds

    :param corporation_id: An EVE corporation ID
    :type corporation_id: int
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


async def get_corporations_corporation_id_medals_issued(request: web.Request, corporation_id, datasource=None, if_none_match=None, page=None, token=None) -> web.Response:
    """Get corporation issued medals

    Returns medals issued by a corporation  --- Alternate route: &#x60;/dev/corporations/{corporation_id}/medals/issued/&#x60;  Alternate route: &#x60;/legacy/corporations/{corporation_id}/medals/issued/&#x60;  Alternate route: &#x60;/v1/corporations/{corporation_id}/medals/issued/&#x60;  --- This route is cached for up to 3600 seconds  --- Requires one of the following EVE corporation role(s): Director 

    :param corporation_id: An EVE corporation ID
    :type corporation_id: int
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


async def get_corporations_corporation_id_members(request: web.Request, corporation_id, datasource=None, if_none_match=None, token=None) -> web.Response:
    """Get corporation members

    Return the current member list of a corporation, the token&#39;s character need to be a member of the corporation.  --- Alternate route: &#x60;/dev/corporations/{corporation_id}/members/&#x60;  Alternate route: &#x60;/v3/corporations/{corporation_id}/members/&#x60;  --- This route is cached for up to 3600 seconds

    :param corporation_id: An EVE corporation ID
    :type corporation_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    return web.Response(status=200)


async def get_corporations_corporation_id_members_limit(request: web.Request, corporation_id, datasource=None, if_none_match=None, token=None) -> web.Response:
    """Get corporation member limit

    Return a corporation&#39;s member limit, not including CEO himself  --- Alternate route: &#x60;/dev/corporations/{corporation_id}/members/limit/&#x60;  Alternate route: &#x60;/legacy/corporations/{corporation_id}/members/limit/&#x60;  Alternate route: &#x60;/v1/corporations/{corporation_id}/members/limit/&#x60;  --- This route is cached for up to 3600 seconds  --- Requires one of the following EVE corporation role(s): Director 

    :param corporation_id: An EVE corporation ID
    :type corporation_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    return web.Response(status=200)


async def get_corporations_corporation_id_members_titles(request: web.Request, corporation_id, datasource=None, if_none_match=None, token=None) -> web.Response:
    """Get corporation&#39;s members&#39; titles

    Returns a corporation&#39;s members&#39; titles  --- Alternate route: &#x60;/dev/corporations/{corporation_id}/members/titles/&#x60;  Alternate route: &#x60;/legacy/corporations/{corporation_id}/members/titles/&#x60;  Alternate route: &#x60;/v1/corporations/{corporation_id}/members/titles/&#x60;  --- This route is cached for up to 3600 seconds  --- Requires one of the following EVE corporation role(s): Director 

    :param corporation_id: An EVE corporation ID
    :type corporation_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    return web.Response(status=200)


async def get_corporations_corporation_id_membertracking(request: web.Request, corporation_id, datasource=None, if_none_match=None, token=None) -> web.Response:
    """Track corporation members

    Returns additional information about a corporation&#39;s members which helps tracking their activities  --- Alternate route: &#x60;/dev/corporations/{corporation_id}/membertracking/&#x60;  Alternate route: &#x60;/legacy/corporations/{corporation_id}/membertracking/&#x60;  Alternate route: &#x60;/v1/corporations/{corporation_id}/membertracking/&#x60;  --- This route is cached for up to 3600 seconds  --- Requires one of the following EVE corporation role(s): Director 

    :param corporation_id: An EVE corporation ID
    :type corporation_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    return web.Response(status=200)


async def get_corporations_corporation_id_roles(request: web.Request, corporation_id, datasource=None, if_none_match=None, token=None) -> web.Response:
    """Get corporation member roles

    Return the roles of all members if the character has the personnel manager role or any grantable role.  --- Alternate route: &#x60;/dev/corporations/{corporation_id}/roles/&#x60;  Alternate route: &#x60;/legacy/corporations/{corporation_id}/roles/&#x60;  Alternate route: &#x60;/v1/corporations/{corporation_id}/roles/&#x60;  --- This route is cached for up to 3600 seconds

    :param corporation_id: An EVE corporation ID
    :type corporation_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    return web.Response(status=200)


async def get_corporations_corporation_id_roles_history(request: web.Request, corporation_id, datasource=None, if_none_match=None, page=None, token=None) -> web.Response:
    """Get corporation member roles history

    Return how roles have changed for a coporation&#39;s members, up to a month  --- Alternate route: &#x60;/dev/corporations/{corporation_id}/roles/history/&#x60;  Alternate route: &#x60;/legacy/corporations/{corporation_id}/roles/history/&#x60;  Alternate route: &#x60;/v1/corporations/{corporation_id}/roles/history/&#x60;  --- This route is cached for up to 3600 seconds  --- Requires one of the following EVE corporation role(s): Director 

    :param corporation_id: An EVE corporation ID
    :type corporation_id: int
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


async def get_corporations_corporation_id_shareholders(request: web.Request, corporation_id, datasource=None, if_none_match=None, page=None, token=None) -> web.Response:
    """Get corporation shareholders

    Return the current shareholders of a corporation.  --- Alternate route: &#x60;/dev/corporations/{corporation_id}/shareholders/&#x60;  Alternate route: &#x60;/legacy/corporations/{corporation_id}/shareholders/&#x60;  Alternate route: &#x60;/v1/corporations/{corporation_id}/shareholders/&#x60;  --- This route is cached for up to 3600 seconds  --- Requires one of the following EVE corporation role(s): Director 

    :param corporation_id: An EVE corporation ID
    :type corporation_id: int
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


async def get_corporations_corporation_id_standings(request: web.Request, corporation_id, datasource=None, if_none_match=None, page=None, token=None) -> web.Response:
    """Get corporation standings

    Return corporation standings from agents, NPC corporations, and factions  --- Alternate route: &#x60;/dev/corporations/{corporation_id}/standings/&#x60;  Alternate route: &#x60;/legacy/corporations/{corporation_id}/standings/&#x60;  Alternate route: &#x60;/v1/corporations/{corporation_id}/standings/&#x60;  --- This route is cached for up to 3600 seconds

    :param corporation_id: An EVE corporation ID
    :type corporation_id: int
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


async def get_corporations_corporation_id_starbases(request: web.Request, corporation_id, datasource=None, if_none_match=None, page=None, token=None) -> web.Response:
    """Get corporation starbases (POSes)

    Returns list of corporation starbases (POSes)  --- Alternate route: &#x60;/dev/corporations/{corporation_id}/starbases/&#x60;  Alternate route: &#x60;/legacy/corporations/{corporation_id}/starbases/&#x60;  Alternate route: &#x60;/v1/corporations/{corporation_id}/starbases/&#x60;  --- This route is cached for up to 3600 seconds  --- Requires one of the following EVE corporation role(s): Director 

    :param corporation_id: An EVE corporation ID
    :type corporation_id: int
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


async def get_corporations_corporation_id_starbases_starbase_id(request: web.Request, corporation_id, starbase_id, system_id, datasource=None, if_none_match=None, token=None) -> web.Response:
    """Get starbase (POS) detail

    Returns various settings and fuels of a starbase (POS)  --- Alternate route: &#x60;/dev/corporations/{corporation_id}/starbases/{starbase_id}/&#x60;  Alternate route: &#x60;/legacy/corporations/{corporation_id}/starbases/{starbase_id}/&#x60;  Alternate route: &#x60;/v1/corporations/{corporation_id}/starbases/{starbase_id}/&#x60;  --- This route is cached for up to 3600 seconds  --- Requires one of the following EVE corporation role(s): Director 

    :param corporation_id: An EVE corporation ID
    :type corporation_id: int
    :param starbase_id: An EVE starbase (POS) ID
    :type starbase_id: int
    :param system_id: The solar system this starbase (POS) is located in,
    :type system_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    return web.Response(status=200)


async def get_corporations_corporation_id_structures(request: web.Request, corporation_id, accept_language=None, datasource=None, if_none_match=None, language=None, page=None, token=None) -> web.Response:
    """Get corporation structures

    Get a list of corporation structures. This route&#39;s version includes the changes to structures detailed in this blog: https://www.eveonline.com/article/upwell-2.0-structures-changes-coming-on-february-13th Note: this route will not return any flex structures owned by a corporation, use the v3 route to have those included in the response. A list of FLEX structures can be found here: https://support.eveonline.com/hc/en-us/articles/213021829-Upwell-Structures  --- Alternate route: &#x60;/v2/corporations/{corporation_id}/structures/&#x60;  --- This route is cached for up to 3600 seconds  --- Requires one of the following EVE corporation role(s): Station_Manager   --- Warning: This route has an upgrade available  --- [Diff of the upcoming changes](https://esi.evetech.net/diff/latest/dev/#GET-/corporations/{corporation_id}/structures/)

    :param corporation_id: An EVE corporation ID
    :type corporation_id: int
    :param accept_language: Language to use in the response
    :type accept_language: str
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str
    :param language: Language to use in the response, takes precedence over Accept-Language
    :type language: str
    :param page: Which page of results to return
    :type page: int
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    return web.Response(status=200)


async def get_corporations_corporation_id_titles(request: web.Request, corporation_id, datasource=None, if_none_match=None, token=None) -> web.Response:
    """Get corporation titles

    Returns a corporation&#39;s titles  --- Alternate route: &#x60;/dev/corporations/{corporation_id}/titles/&#x60;  Alternate route: &#x60;/legacy/corporations/{corporation_id}/titles/&#x60;  Alternate route: &#x60;/v1/corporations/{corporation_id}/titles/&#x60;  --- This route is cached for up to 3600 seconds  --- Requires one of the following EVE corporation role(s): Director 

    :param corporation_id: An EVE corporation ID
    :type corporation_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    return web.Response(status=200)


async def get_corporations_npccorps(request: web.Request, datasource=None, if_none_match=None) -> web.Response:
    """Get npc corporations

    Get a list of npc corporations  --- Alternate route: &#x60;/dev/corporations/npccorps/&#x60;  Alternate route: &#x60;/legacy/corporations/npccorps/&#x60;  Alternate route: &#x60;/v1/corporations/npccorps/&#x60;  --- This route expires daily at 11:05

    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str

    """
    return web.Response(status=200)
