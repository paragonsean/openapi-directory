from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.error_limited import ErrorLimited
from openapi_server.models.forbidden import Forbidden
from openapi_server.models.gateway_timeout import GatewayTimeout
from openapi_server.models.get_characters_character_id_wallet_journal200_ok import GetCharactersCharacterIdWalletJournal200Ok
from openapi_server.models.get_characters_character_id_wallet_transactions200_ok import GetCharactersCharacterIdWalletTransactions200Ok
from openapi_server.models.get_corporations_corporation_id_wallets200_ok import GetCorporationsCorporationIdWallets200Ok
from openapi_server.models.get_corporations_corporation_id_wallets_division_journal200_ok import GetCorporationsCorporationIdWalletsDivisionJournal200Ok
from openapi_server.models.get_corporations_corporation_id_wallets_division_transactions200_ok import GetCorporationsCorporationIdWalletsDivisionTransactions200Ok
from openapi_server.models.internal_server_error import InternalServerError
from openapi_server.models.service_unavailable import ServiceUnavailable
from openapi_server.models.unauthorized import Unauthorized
from openapi_server import util


async def get_characters_character_id_wallet(request: web.Request, character_id, datasource=None, if_none_match=None, token=None) -> web.Response:
    """Get a character&#39;s wallet balance

    Returns a character&#39;s wallet balance  --- Alternate route: &#x60;/dev/characters/{character_id}/wallet/&#x60;  Alternate route: &#x60;/legacy/characters/{character_id}/wallet/&#x60;  Alternate route: &#x60;/v1/characters/{character_id}/wallet/&#x60;  --- This route is cached for up to 120 seconds

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


async def get_characters_character_id_wallet_journal(request: web.Request, character_id, datasource=None, if_none_match=None, page=None, token=None) -> web.Response:
    """Get character wallet journal

    Retrieve the given character&#39;s wallet journal going 30 days back  --- Alternate route: &#x60;/legacy/characters/{character_id}/wallet/journal/&#x60;  Alternate route: &#x60;/v4/characters/{character_id}/wallet/journal/&#x60;  --- This route is cached for up to 3600 seconds  --- Warning: This route has an upgrade available  --- [Diff of the upcoming changes](https://esi.evetech.net/diff/latest/dev/#GET-/characters/{character_id}/wallet/journal/)

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


async def get_characters_character_id_wallet_transactions(request: web.Request, character_id, datasource=None, from_id=None, if_none_match=None, token=None) -> web.Response:
    """Get wallet transactions

    Get wallet transactions of a character  --- Alternate route: &#x60;/dev/characters/{character_id}/wallet/transactions/&#x60;  Alternate route: &#x60;/legacy/characters/{character_id}/wallet/transactions/&#x60;  Alternate route: &#x60;/v1/characters/{character_id}/wallet/transactions/&#x60;  --- This route is cached for up to 3600 seconds

    :param character_id: An EVE character ID
    :type character_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param from_id: Only show transactions happened before the one referenced by this id
    :type from_id: int
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    return web.Response(status=200)


async def get_corporations_corporation_id_wallets(request: web.Request, corporation_id, datasource=None, if_none_match=None, token=None) -> web.Response:
    """Returns a corporation&#39;s wallet balance

    Get a corporation&#39;s wallets  --- Alternate route: &#x60;/dev/corporations/{corporation_id}/wallets/&#x60;  Alternate route: &#x60;/legacy/corporations/{corporation_id}/wallets/&#x60;  Alternate route: &#x60;/v1/corporations/{corporation_id}/wallets/&#x60;  --- This route is cached for up to 300 seconds  --- Requires one of the following EVE corporation role(s): Accountant, Junior_Accountant 

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


async def get_corporations_corporation_id_wallets_division_journal(request: web.Request, corporation_id, division, datasource=None, if_none_match=None, page=None, token=None) -> web.Response:
    """Get corporation wallet journal

    Retrieve the given corporation&#39;s wallet journal for the given division going 30 days back. Note: any journal records having to do with the new navigation structures from the release of Onslaught will not show up in this version. To see those, use the v4 version of this route.  --- Alternate route: &#x60;/legacy/corporations/{corporation_id}/wallets/{division}/journal/&#x60;  Alternate route: &#x60;/v3/corporations/{corporation_id}/wallets/{division}/journal/&#x60;  --- This route is cached for up to 3600 seconds  --- Requires one of the following EVE corporation role(s): Accountant, Junior_Accountant   --- Warning: This route has an upgrade available  --- [Diff of the upcoming changes](https://esi.evetech.net/diff/latest/dev/#GET-/corporations/{corporation_id}/wallets/{division}/journal/)

    :param corporation_id: An EVE corporation ID
    :type corporation_id: int
    :param division: Wallet key of the division to fetch journals from
    :type division: int
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


async def get_corporations_corporation_id_wallets_division_transactions(request: web.Request, corporation_id, division, datasource=None, from_id=None, if_none_match=None, token=None) -> web.Response:
    """Get corporation wallet transactions

    Get wallet transactions of a corporation  --- Alternate route: &#x60;/dev/corporations/{corporation_id}/wallets/{division}/transactions/&#x60;  Alternate route: &#x60;/legacy/corporations/{corporation_id}/wallets/{division}/transactions/&#x60;  Alternate route: &#x60;/v1/corporations/{corporation_id}/wallets/{division}/transactions/&#x60;  --- This route is cached for up to 3600 seconds  --- Requires one of the following EVE corporation role(s): Accountant, Junior_Accountant 

    :param corporation_id: An EVE corporation ID
    :type corporation_id: int
    :param division: Wallet key of the division to fetch journals from
    :type division: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param from_id: Only show journal entries happened before the transaction referenced by this id
    :type from_id: int
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    return web.Response(status=200)
