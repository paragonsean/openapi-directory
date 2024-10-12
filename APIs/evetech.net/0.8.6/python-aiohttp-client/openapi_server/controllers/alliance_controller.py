from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.error_limited import ErrorLimited
from openapi_server.models.gateway_timeout import GatewayTimeout
from openapi_server.models.get_alliances_alliance_id_icons_not_found import GetAlliancesAllianceIdIconsNotFound
from openapi_server.models.get_alliances_alliance_id_icons_ok import GetAlliancesAllianceIdIconsOk
from openapi_server.models.get_alliances_alliance_id_not_found import GetAlliancesAllianceIdNotFound
from openapi_server.models.get_alliances_alliance_id_ok import GetAlliancesAllianceIdOk
from openapi_server.models.internal_server_error import InternalServerError
from openapi_server.models.service_unavailable import ServiceUnavailable
from openapi_server import util


async def get_alliances(request: web.Request, datasource=None, if_none_match=None) -> web.Response:
    """List all alliances

    List all active player alliances  --- Alternate route: &#x60;/dev/alliances/&#x60;  Alternate route: &#x60;/legacy/alliances/&#x60;  Alternate route: &#x60;/v1/alliances/&#x60;  --- This route is cached for up to 3600 seconds

    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_alliances_alliance_id(request: web.Request, alliance_id, datasource=None, if_none_match=None) -> web.Response:
    """Get alliance information

    Public information about an alliance  --- Alternate route: &#x60;/dev/alliances/{alliance_id}/&#x60;  Alternate route: &#x60;/v3/alliances/{alliance_id}/&#x60;  --- This route is cached for up to 3600 seconds

    :param alliance_id: An EVE alliance ID
    :type alliance_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_alliances_alliance_id_corporations(request: web.Request, alliance_id, datasource=None, if_none_match=None) -> web.Response:
    """List alliance&#39;s corporations

    List all current member corporations of an alliance  --- Alternate route: &#x60;/dev/alliances/{alliance_id}/corporations/&#x60;  Alternate route: &#x60;/legacy/alliances/{alliance_id}/corporations/&#x60;  Alternate route: &#x60;/v1/alliances/{alliance_id}/corporations/&#x60;  --- This route is cached for up to 3600 seconds

    :param alliance_id: An EVE alliance ID
    :type alliance_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_alliances_alliance_id_icons(request: web.Request, alliance_id, datasource=None, if_none_match=None) -> web.Response:
    """Get alliance icon

    Get the icon urls for a alliance  --- Alternate route: &#x60;/dev/alliances/{alliance_id}/icons/&#x60;  Alternate route: &#x60;/legacy/alliances/{alliance_id}/icons/&#x60;  Alternate route: &#x60;/v1/alliances/{alliance_id}/icons/&#x60;  --- This route expires daily at 11:05

    :param alliance_id: An EVE alliance ID
    :type alliance_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str

    """
    return web.Response(status=200)
