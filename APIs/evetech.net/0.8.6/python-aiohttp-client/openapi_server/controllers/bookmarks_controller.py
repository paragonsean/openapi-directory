from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.error_limited import ErrorLimited
from openapi_server.models.forbidden import Forbidden
from openapi_server.models.gateway_timeout import GatewayTimeout
from openapi_server.models.get_characters_character_id_bookmarks200_ok import GetCharactersCharacterIdBookmarks200Ok
from openapi_server.models.get_characters_character_id_bookmarks_folders200_ok import GetCharactersCharacterIdBookmarksFolders200Ok
from openapi_server.models.get_corporations_corporation_id_bookmarks200_ok import GetCorporationsCorporationIdBookmarks200Ok
from openapi_server.models.get_corporations_corporation_id_bookmarks_folders200_ok import GetCorporationsCorporationIdBookmarksFolders200Ok
from openapi_server.models.internal_server_error import InternalServerError
from openapi_server.models.service_unavailable import ServiceUnavailable
from openapi_server.models.unauthorized import Unauthorized
from openapi_server import util


async def get_characters_character_id_bookmarks(request: web.Request, character_id, datasource=None, if_none_match=None, page=None, token=None) -> web.Response:
    """List bookmarks

    A list of your character&#39;s personal bookmarks  --- Alternate route: &#x60;/dev/characters/{character_id}/bookmarks/&#x60;  Alternate route: &#x60;/v2/characters/{character_id}/bookmarks/&#x60;  --- This route is cached for up to 3600 seconds

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


async def get_characters_character_id_bookmarks_folders(request: web.Request, character_id, datasource=None, if_none_match=None, page=None, token=None) -> web.Response:
    """List bookmark folders

    A list of your character&#39;s personal bookmark folders  --- Alternate route: &#x60;/dev/characters/{character_id}/bookmarks/folders/&#x60;  Alternate route: &#x60;/v2/characters/{character_id}/bookmarks/folders/&#x60;  --- This route is cached for up to 3600 seconds

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


async def get_corporations_corporation_id_bookmarks(request: web.Request, corporation_id, datasource=None, if_none_match=None, page=None, token=None) -> web.Response:
    """List corporation bookmarks

    A list of your corporation&#39;s bookmarks  --- Alternate route: &#x60;/dev/corporations/{corporation_id}/bookmarks/&#x60;  Alternate route: &#x60;/legacy/corporations/{corporation_id}/bookmarks/&#x60;  Alternate route: &#x60;/v1/corporations/{corporation_id}/bookmarks/&#x60;  --- This route is cached for up to 3600 seconds

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


async def get_corporations_corporation_id_bookmarks_folders(request: web.Request, corporation_id, datasource=None, if_none_match=None, page=None, token=None) -> web.Response:
    """List corporation bookmark folders

    A list of your corporation&#39;s bookmark folders  --- Alternate route: &#x60;/dev/corporations/{corporation_id}/bookmarks/folders/&#x60;  Alternate route: &#x60;/legacy/corporations/{corporation_id}/bookmarks/folders/&#x60;  Alternate route: &#x60;/v1/corporations/{corporation_id}/bookmarks/folders/&#x60;  --- This route is cached for up to 3600 seconds

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
