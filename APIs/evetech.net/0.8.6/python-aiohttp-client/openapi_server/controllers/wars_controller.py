from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.error_limited import ErrorLimited
from openapi_server.models.gateway_timeout import GatewayTimeout
from openapi_server.models.get_wars_war_id_killmails200_ok import GetWarsWarIdKillmails200Ok
from openapi_server.models.get_wars_war_id_killmails_unprocessable_entity import GetWarsWarIdKillmailsUnprocessableEntity
from openapi_server.models.get_wars_war_id_ok import GetWarsWarIdOk
from openapi_server.models.get_wars_war_id_unprocessable_entity import GetWarsWarIdUnprocessableEntity
from openapi_server.models.internal_server_error import InternalServerError
from openapi_server.models.service_unavailable import ServiceUnavailable
from openapi_server import util


async def get_wars(request: web.Request, datasource=None, if_none_match=None, max_war_id=None) -> web.Response:
    """List wars

    Return a list of wars  --- Alternate route: &#x60;/dev/wars/&#x60;  Alternate route: &#x60;/legacy/wars/&#x60;  Alternate route: &#x60;/v1/wars/&#x60;  --- This route is cached for up to 3600 seconds

    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str
    :param max_war_id: Only return wars with ID smaller than this
    :type max_war_id: int

    """
    return web.Response(status=200)


async def get_wars_war_id(request: web.Request, war_id, datasource=None, if_none_match=None) -> web.Response:
    """Get war information

    Return details about a war  --- Alternate route: &#x60;/dev/wars/{war_id}/&#x60;  Alternate route: &#x60;/legacy/wars/{war_id}/&#x60;  Alternate route: &#x60;/v1/wars/{war_id}/&#x60;  --- This route is cached for up to 3600 seconds

    :param war_id: ID for a war
    :type war_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_wars_war_id_killmails(request: web.Request, war_id, datasource=None, if_none_match=None, page=None) -> web.Response:
    """List kills for a war

    Return a list of kills related to a war  --- Alternate route: &#x60;/dev/wars/{war_id}/killmails/&#x60;  Alternate route: &#x60;/legacy/wars/{war_id}/killmails/&#x60;  Alternate route: &#x60;/v1/wars/{war_id}/killmails/&#x60;  --- This route is cached for up to 3600 seconds

    :param war_id: A valid war ID
    :type war_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str
    :param page: Which page of results to return
    :type page: int

    """
    return web.Response(status=200)
