from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.error_limited import ErrorLimited
from openapi_server.models.forbidden import Forbidden
from openapi_server.models.gateway_timeout import GatewayTimeout
from openapi_server.models.get_characters_character_id_loyalty_points200_ok import GetCharactersCharacterIdLoyaltyPoints200Ok
from openapi_server.models.get_loyalty_stores_corporation_id_offers200_ok import GetLoyaltyStoresCorporationIdOffers200Ok
from openapi_server.models.get_loyalty_stores_corporation_id_offers_not_found import GetLoyaltyStoresCorporationIdOffersNotFound
from openapi_server.models.internal_server_error import InternalServerError
from openapi_server.models.service_unavailable import ServiceUnavailable
from openapi_server.models.unauthorized import Unauthorized
from openapi_server import util


async def get_characters_character_id_loyalty_points(request: web.Request, character_id, datasource=None, if_none_match=None, token=None) -> web.Response:
    """Get loyalty points

    Return a list of loyalty points for all corporations the character has worked for  --- Alternate route: &#x60;/dev/characters/{character_id}/loyalty/points/&#x60;  Alternate route: &#x60;/legacy/characters/{character_id}/loyalty/points/&#x60;  Alternate route: &#x60;/v1/characters/{character_id}/loyalty/points/&#x60;  --- This route is cached for up to 3600 seconds

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


async def get_loyalty_stores_corporation_id_offers(request: web.Request, corporation_id, datasource=None, if_none_match=None) -> web.Response:
    """List loyalty store offers

    Return a list of offers from a specific corporation&#39;s loyalty store  --- Alternate route: &#x60;/dev/loyalty/stores/{corporation_id}/offers/&#x60;  Alternate route: &#x60;/legacy/loyalty/stores/{corporation_id}/offers/&#x60;  Alternate route: &#x60;/v1/loyalty/stores/{corporation_id}/offers/&#x60;  --- This route expires daily at 11:05

    :param corporation_id: An EVE corporation ID
    :type corporation_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str

    """
    return web.Response(status=200)
