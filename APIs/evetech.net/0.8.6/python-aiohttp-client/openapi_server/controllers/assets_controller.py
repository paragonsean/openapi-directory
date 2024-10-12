from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.error_limited import ErrorLimited
from openapi_server.models.forbidden import Forbidden
from openapi_server.models.gateway_timeout import GatewayTimeout
from openapi_server.models.get_characters_character_id_assets200_ok import GetCharactersCharacterIdAssets200Ok
from openapi_server.models.get_corporations_corporation_id_assets200_ok import GetCorporationsCorporationIdAssets200Ok
from openapi_server.models.internal_server_error import InternalServerError
from openapi_server.models.post_characters_character_id_assets_locations200_ok import PostCharactersCharacterIdAssetsLocations200Ok
from openapi_server.models.post_characters_character_id_assets_names200_ok import PostCharactersCharacterIdAssetsNames200Ok
from openapi_server.models.post_corporations_corporation_id_assets_locations200_ok import PostCorporationsCorporationIdAssetsLocations200Ok
from openapi_server.models.post_corporations_corporation_id_assets_locations_not_found import PostCorporationsCorporationIdAssetsLocationsNotFound
from openapi_server.models.post_corporations_corporation_id_assets_names200_ok import PostCorporationsCorporationIdAssetsNames200Ok
from openapi_server.models.post_corporations_corporation_id_assets_names_not_found import PostCorporationsCorporationIdAssetsNamesNotFound
from openapi_server.models.service_unavailable import ServiceUnavailable
from openapi_server.models.unauthorized import Unauthorized
from openapi_server import util


async def get_characters_character_id_assets(request: web.Request, character_id, datasource=None, if_none_match=None, page=None, token=None) -> web.Response:
    """Get character assets

    Return a list of the characters assets  --- Alternate route: &#x60;/dev/characters/{character_id}/assets/&#x60;  Alternate route: &#x60;/v3/characters/{character_id}/assets/&#x60;  --- This route is cached for up to 3600 seconds

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


async def get_corporations_corporation_id_assets(request: web.Request, corporation_id, datasource=None, if_none_match=None, page=None, token=None) -> web.Response:
    """Get corporation assets

    Return a list of the corporation assets  --- Alternate route: &#x60;/dev/corporations/{corporation_id}/assets/&#x60;  Alternate route: &#x60;/v3/corporations/{corporation_id}/assets/&#x60;  --- This route is cached for up to 3600 seconds  --- Requires one of the following EVE corporation role(s): Director 

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


async def post_characters_character_id_assets_locations(request: web.Request, character_id, item_ids, datasource=None, token=None) -> web.Response:
    """Get character asset locations

    Return locations for a set of item ids, which you can get from character assets endpoint. Coordinates for items in hangars or stations are set to (0,0,0)  --- Alternate route: &#x60;/dev/characters/{character_id}/assets/locations/&#x60;  Alternate route: &#x60;/v2/characters/{character_id}/assets/locations/&#x60; 

    :param character_id: An EVE character ID
    :type character_id: int
    :param item_ids: A list of item ids
    :type item_ids: List[int]
    :param datasource: The server name you would like data from
    :type datasource: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    return web.Response(status=200)


async def post_characters_character_id_assets_names(request: web.Request, character_id, item_ids, datasource=None, token=None) -> web.Response:
    """Get character asset names

    Return names for a set of item ids, which you can get from character assets endpoint. Typically used for items that can customize names, like containers or ships.  --- Alternate route: &#x60;/dev/characters/{character_id}/assets/names/&#x60;  Alternate route: &#x60;/legacy/characters/{character_id}/assets/names/&#x60;  Alternate route: &#x60;/v1/characters/{character_id}/assets/names/&#x60; 

    :param character_id: An EVE character ID
    :type character_id: int
    :param item_ids: A list of item ids
    :type item_ids: List[int]
    :param datasource: The server name you would like data from
    :type datasource: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    return web.Response(status=200)


async def post_corporations_corporation_id_assets_locations(request: web.Request, corporation_id, item_ids, datasource=None, token=None) -> web.Response:
    """Get corporation asset locations

    Return locations for a set of item ids, which you can get from corporation assets endpoint. Coordinates for items in hangars or stations are set to (0,0,0)  --- Alternate route: &#x60;/dev/corporations/{corporation_id}/assets/locations/&#x60;  Alternate route: &#x60;/v2/corporations/{corporation_id}/assets/locations/&#x60;   --- Requires one of the following EVE corporation role(s): Director 

    :param corporation_id: An EVE corporation ID
    :type corporation_id: int
    :param item_ids: A list of item ids
    :type item_ids: List[int]
    :param datasource: The server name you would like data from
    :type datasource: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    return web.Response(status=200)


async def post_corporations_corporation_id_assets_names(request: web.Request, corporation_id, item_ids, datasource=None, token=None) -> web.Response:
    """Get corporation asset names

    Return names for a set of item ids, which you can get from corporation assets endpoint. Only valid for items that can customize names, like containers or ships  --- Alternate route: &#x60;/dev/corporations/{corporation_id}/assets/names/&#x60;  Alternate route: &#x60;/legacy/corporations/{corporation_id}/assets/names/&#x60;  Alternate route: &#x60;/v1/corporations/{corporation_id}/assets/names/&#x60;   --- Requires one of the following EVE corporation role(s): Director 

    :param corporation_id: An EVE corporation ID
    :type corporation_id: int
    :param item_ids: A list of item ids
    :type item_ids: List[int]
    :param datasource: The server name you would like data from
    :type datasource: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    return web.Response(status=200)
