from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.error_limited import ErrorLimited
from openapi_server.models.forbidden import Forbidden
from openapi_server.models.gateway_timeout import GatewayTimeout
from openapi_server.models.get_characters_character_id_orders200_ok import GetCharactersCharacterIdOrders200Ok
from openapi_server.models.get_characters_character_id_orders_history200_ok import GetCharactersCharacterIdOrdersHistory200Ok
from openapi_server.models.get_corporations_corporation_id_orders200_ok import GetCorporationsCorporationIdOrders200Ok
from openapi_server.models.get_corporations_corporation_id_orders_history200_ok import GetCorporationsCorporationIdOrdersHistory200Ok
from openapi_server.models.get_markets_groups_market_group_id_not_found import GetMarketsGroupsMarketGroupIdNotFound
from openapi_server.models.get_markets_groups_market_group_id_ok import GetMarketsGroupsMarketGroupIdOk
from openapi_server.models.get_markets_prices200_ok import GetMarketsPrices200Ok
from openapi_server.models.get_markets_region_id_history200_ok import GetMarketsRegionIdHistory200Ok
from openapi_server.models.get_markets_region_id_history_error520 import GetMarketsRegionIdHistoryError520
from openapi_server.models.get_markets_region_id_history_not_found import GetMarketsRegionIdHistoryNotFound
from openapi_server.models.get_markets_region_id_history_unprocessable_entity import GetMarketsRegionIdHistoryUnprocessableEntity
from openapi_server.models.get_markets_region_id_orders200_ok import GetMarketsRegionIdOrders200Ok
from openapi_server.models.get_markets_region_id_orders_not_found import GetMarketsRegionIdOrdersNotFound
from openapi_server.models.get_markets_region_id_orders_unprocessable_entity import GetMarketsRegionIdOrdersUnprocessableEntity
from openapi_server.models.get_markets_structures_structure_id200_ok import GetMarketsStructuresStructureId200Ok
from openapi_server.models.internal_server_error import InternalServerError
from openapi_server.models.service_unavailable import ServiceUnavailable
from openapi_server.models.unauthorized import Unauthorized
from openapi_server import util


async def get_characters_character_id_orders(request: web.Request, character_id, datasource=None, if_none_match=None, token=None) -> web.Response:
    """List open orders from a character

    List open market orders placed by a character  --- Alternate route: &#x60;/dev/characters/{character_id}/orders/&#x60;  Alternate route: &#x60;/v2/characters/{character_id}/orders/&#x60;  --- This route is cached for up to 1200 seconds

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


async def get_characters_character_id_orders_history(request: web.Request, character_id, datasource=None, if_none_match=None, page=None, token=None) -> web.Response:
    """List historical orders by a character

    List cancelled and expired market orders placed by a character up to 90 days in the past.  --- Alternate route: &#x60;/dev/characters/{character_id}/orders/history/&#x60;  Alternate route: &#x60;/legacy/characters/{character_id}/orders/history/&#x60;  Alternate route: &#x60;/v1/characters/{character_id}/orders/history/&#x60;  --- This route is cached for up to 3600 seconds

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


async def get_corporations_corporation_id_orders(request: web.Request, corporation_id, datasource=None, if_none_match=None, page=None, token=None) -> web.Response:
    """List open orders from a corporation

    List open market orders placed on behalf of a corporation  --- Alternate route: &#x60;/dev/corporations/{corporation_id}/orders/&#x60;  Alternate route: &#x60;/v3/corporations/{corporation_id}/orders/&#x60;  --- This route is cached for up to 1200 seconds  --- Requires one of the following EVE corporation role(s): Accountant, Trader 

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


async def get_corporations_corporation_id_orders_history(request: web.Request, corporation_id, datasource=None, if_none_match=None, page=None, token=None) -> web.Response:
    """List historical orders from a corporation

    List cancelled and expired market orders placed on behalf of a corporation up to 90 days in the past.  --- Alternate route: &#x60;/dev/corporations/{corporation_id}/orders/history/&#x60;  Alternate route: &#x60;/v2/corporations/{corporation_id}/orders/history/&#x60;  --- This route is cached for up to 3600 seconds  --- Requires one of the following EVE corporation role(s): Accountant, Trader 

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


async def get_markets_groups(request: web.Request, datasource=None, if_none_match=None) -> web.Response:
    """Get item groups

    Get a list of item groups  --- Alternate route: &#x60;/dev/markets/groups/&#x60;  Alternate route: &#x60;/legacy/markets/groups/&#x60;  Alternate route: &#x60;/v1/markets/groups/&#x60;  --- This route expires daily at 11:05

    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_markets_groups_market_group_id(request: web.Request, market_group_id, accept_language=None, datasource=None, if_none_match=None, language=None) -> web.Response:
    """Get item group information

    Get information on an item group  --- Alternate route: &#x60;/dev/markets/groups/{market_group_id}/&#x60;  Alternate route: &#x60;/legacy/markets/groups/{market_group_id}/&#x60;  Alternate route: &#x60;/v1/markets/groups/{market_group_id}/&#x60;  --- This route expires daily at 11:05

    :param market_group_id: An Eve item group ID
    :type market_group_id: int
    :param accept_language: Language to use in the response
    :type accept_language: str
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str
    :param language: Language to use in the response, takes precedence over Accept-Language
    :type language: str

    """
    return web.Response(status=200)


async def get_markets_prices(request: web.Request, datasource=None, if_none_match=None) -> web.Response:
    """List market prices

    Return a list of prices  --- Alternate route: &#x60;/dev/markets/prices/&#x60;  Alternate route: &#x60;/legacy/markets/prices/&#x60;  Alternate route: &#x60;/v1/markets/prices/&#x60;  --- This route is cached for up to 3600 seconds

    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_markets_region_id_history(request: web.Request, region_id, type_id, datasource=None, if_none_match=None) -> web.Response:
    """List historical market statistics in a region

    Return a list of historical market statistics for the specified type in a region  --- Alternate route: &#x60;/dev/markets/{region_id}/history/&#x60;  Alternate route: &#x60;/legacy/markets/{region_id}/history/&#x60;  Alternate route: &#x60;/v1/markets/{region_id}/history/&#x60;  --- This route expires daily at 11:05

    :param region_id: Return statistics in this region
    :type region_id: int
    :param type_id: Return statistics for this type
    :type type_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_markets_region_id_orders(request: web.Request, order_type, region_id, datasource=None, if_none_match=None, page=None, type_id=None) -> web.Response:
    """List orders in a region

    Return a list of orders in a region  --- Alternate route: &#x60;/dev/markets/{region_id}/orders/&#x60;  Alternate route: &#x60;/legacy/markets/{region_id}/orders/&#x60;  Alternate route: &#x60;/v1/markets/{region_id}/orders/&#x60;  --- This route is cached for up to 300 seconds

    :param order_type: Filter buy/sell orders, return all orders by default. If you query without type_id, we always return both buy and sell orders
    :type order_type: str
    :param region_id: Return orders in this region
    :type region_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str
    :param page: Which page of results to return
    :type page: int
    :param type_id: Return orders only for this type
    :type type_id: int

    """
    return web.Response(status=200)


async def get_markets_region_id_types(request: web.Request, region_id, datasource=None, if_none_match=None, page=None) -> web.Response:
    """List type IDs relevant to a market

    Return a list of type IDs that have active orders in the region, for efficient market indexing.  --- Alternate route: &#x60;/dev/markets/{region_id}/types/&#x60;  Alternate route: &#x60;/legacy/markets/{region_id}/types/&#x60;  Alternate route: &#x60;/v1/markets/{region_id}/types/&#x60;  --- This route is cached for up to 600 seconds

    :param region_id: Return statistics in this region
    :type region_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str
    :param page: Which page of results to return
    :type page: int

    """
    return web.Response(status=200)


async def get_markets_structures_structure_id(request: web.Request, structure_id, datasource=None, if_none_match=None, page=None, token=None) -> web.Response:
    """List orders in a structure

    Return all orders in a structure  --- Alternate route: &#x60;/dev/markets/structures/{structure_id}/&#x60;  Alternate route: &#x60;/legacy/markets/structures/{structure_id}/&#x60;  Alternate route: &#x60;/v1/markets/structures/{structure_id}/&#x60;  --- This route is cached for up to 300 seconds

    :param structure_id: Return orders in this structure
    :type structure_id: int
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
