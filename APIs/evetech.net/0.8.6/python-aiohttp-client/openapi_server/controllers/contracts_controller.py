from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.error_limited import ErrorLimited
from openapi_server.models.forbidden import Forbidden
from openapi_server.models.gateway_timeout import GatewayTimeout
from openapi_server.models.get_characters_character_id_contracts200_ok import GetCharactersCharacterIdContracts200Ok
from openapi_server.models.get_characters_character_id_contracts_contract_id_bids200_ok import GetCharactersCharacterIdContractsContractIdBids200Ok
from openapi_server.models.get_characters_character_id_contracts_contract_id_bids_not_found import GetCharactersCharacterIdContractsContractIdBidsNotFound
from openapi_server.models.get_characters_character_id_contracts_contract_id_items200_ok import GetCharactersCharacterIdContractsContractIdItems200Ok
from openapi_server.models.get_characters_character_id_contracts_contract_id_items_not_found import GetCharactersCharacterIdContractsContractIdItemsNotFound
from openapi_server.models.get_contracts_public_bids_contract_id200_ok import GetContractsPublicBidsContractId200Ok
from openapi_server.models.get_contracts_public_bids_contract_id_forbidden import GetContractsPublicBidsContractIdForbidden
from openapi_server.models.get_contracts_public_bids_contract_id_not_found import GetContractsPublicBidsContractIdNotFound
from openapi_server.models.get_contracts_public_items_contract_id200_ok import GetContractsPublicItemsContractId200Ok
from openapi_server.models.get_contracts_public_items_contract_id_forbidden import GetContractsPublicItemsContractIdForbidden
from openapi_server.models.get_contracts_public_items_contract_id_not_found import GetContractsPublicItemsContractIdNotFound
from openapi_server.models.get_contracts_public_region_id200_ok import GetContractsPublicRegionId200Ok
from openapi_server.models.get_contracts_public_region_id_not_found import GetContractsPublicRegionIdNotFound
from openapi_server.models.get_corporations_corporation_id_contracts200_ok import GetCorporationsCorporationIdContracts200Ok
from openapi_server.models.get_corporations_corporation_id_contracts_contract_id_bids200_ok import GetCorporationsCorporationIdContractsContractIdBids200Ok
from openapi_server.models.get_corporations_corporation_id_contracts_contract_id_bids_not_found import GetCorporationsCorporationIdContractsContractIdBidsNotFound
from openapi_server.models.get_corporations_corporation_id_contracts_contract_id_items200_ok import GetCorporationsCorporationIdContractsContractIdItems200Ok
from openapi_server.models.get_corporations_corporation_id_contracts_contract_id_items_error520 import GetCorporationsCorporationIdContractsContractIdItemsError520
from openapi_server.models.get_corporations_corporation_id_contracts_contract_id_items_not_found import GetCorporationsCorporationIdContractsContractIdItemsNotFound
from openapi_server.models.internal_server_error import InternalServerError
from openapi_server.models.service_unavailable import ServiceUnavailable
from openapi_server.models.unauthorized import Unauthorized
from openapi_server import util


async def get_characters_character_id_contracts(request: web.Request, character_id, datasource=None, if_none_match=None, page=None, token=None) -> web.Response:
    """Get contracts

    Returns contracts available to a character, only if the character is issuer, acceptor or assignee. Only returns contracts no older than 30 days, or if the status is \&quot;in_progress\&quot;.  --- Alternate route: &#x60;/dev/characters/{character_id}/contracts/&#x60;  Alternate route: &#x60;/legacy/characters/{character_id}/contracts/&#x60;  Alternate route: &#x60;/v1/characters/{character_id}/contracts/&#x60;  --- This route is cached for up to 300 seconds

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


async def get_characters_character_id_contracts_contract_id_bids(request: web.Request, character_id, contract_id, datasource=None, if_none_match=None, token=None) -> web.Response:
    """Get contract bids

    Lists bids on a particular auction contract  --- Alternate route: &#x60;/dev/characters/{character_id}/contracts/{contract_id}/bids/&#x60;  Alternate route: &#x60;/legacy/characters/{character_id}/contracts/{contract_id}/bids/&#x60;  Alternate route: &#x60;/v1/characters/{character_id}/contracts/{contract_id}/bids/&#x60;  --- This route is cached for up to 300 seconds

    :param character_id: An EVE character ID
    :type character_id: int
    :param contract_id: ID of a contract
    :type contract_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    return web.Response(status=200)


async def get_characters_character_id_contracts_contract_id_items(request: web.Request, character_id, contract_id, datasource=None, if_none_match=None, token=None) -> web.Response:
    """Get contract items

    Lists items of a particular contract  --- Alternate route: &#x60;/dev/characters/{character_id}/contracts/{contract_id}/items/&#x60;  Alternate route: &#x60;/legacy/characters/{character_id}/contracts/{contract_id}/items/&#x60;  Alternate route: &#x60;/v1/characters/{character_id}/contracts/{contract_id}/items/&#x60;  --- This route is cached for up to 3600 seconds

    :param character_id: An EVE character ID
    :type character_id: int
    :param contract_id: ID of a contract
    :type contract_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    return web.Response(status=200)


async def get_contracts_public_bids_contract_id(request: web.Request, contract_id, datasource=None, if_none_match=None, page=None) -> web.Response:
    """Get public contract bids

    Lists bids on a public auction contract  --- Alternate route: &#x60;/dev/contracts/public/bids/{contract_id}/&#x60;  Alternate route: &#x60;/legacy/contracts/public/bids/{contract_id}/&#x60;  Alternate route: &#x60;/v1/contracts/public/bids/{contract_id}/&#x60;  --- This route is cached for up to 300 seconds

    :param contract_id: ID of a contract
    :type contract_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str
    :param page: Which page of results to return
    :type page: int

    """
    return web.Response(status=200)


async def get_contracts_public_items_contract_id(request: web.Request, contract_id, datasource=None, if_none_match=None, page=None) -> web.Response:
    """Get public contract items

    Lists items of a public contract  --- Alternate route: &#x60;/dev/contracts/public/items/{contract_id}/&#x60;  Alternate route: &#x60;/legacy/contracts/public/items/{contract_id}/&#x60;  Alternate route: &#x60;/v1/contracts/public/items/{contract_id}/&#x60;  --- This route is cached for up to 3600 seconds

    :param contract_id: ID of a contract
    :type contract_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str
    :param page: Which page of results to return
    :type page: int

    """
    return web.Response(status=200)


async def get_contracts_public_region_id(request: web.Request, region_id, datasource=None, if_none_match=None, page=None) -> web.Response:
    """Get public contracts

    Returns a paginated list of all public contracts in the given region  --- Alternate route: &#x60;/dev/contracts/public/{region_id}/&#x60;  Alternate route: &#x60;/legacy/contracts/public/{region_id}/&#x60;  Alternate route: &#x60;/v1/contracts/public/{region_id}/&#x60;  --- This route is cached for up to 1800 seconds

    :param region_id: An EVE region id
    :type region_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str
    :param page: Which page of results to return
    :type page: int

    """
    return web.Response(status=200)


async def get_corporations_corporation_id_contracts(request: web.Request, corporation_id, datasource=None, if_none_match=None, page=None, token=None) -> web.Response:
    """Get corporation contracts

    Returns contracts available to a corporation, only if the corporation is issuer, acceptor or assignee. Only returns contracts no older than 30 days, or if the status is \&quot;in_progress\&quot;.  --- Alternate route: &#x60;/dev/corporations/{corporation_id}/contracts/&#x60;  Alternate route: &#x60;/legacy/corporations/{corporation_id}/contracts/&#x60;  Alternate route: &#x60;/v1/corporations/{corporation_id}/contracts/&#x60;  --- This route is cached for up to 300 seconds

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


async def get_corporations_corporation_id_contracts_contract_id_bids(request: web.Request, contract_id, corporation_id, datasource=None, if_none_match=None, page=None, token=None) -> web.Response:
    """Get corporation contract bids

    Lists bids on a particular auction contract  --- Alternate route: &#x60;/dev/corporations/{corporation_id}/contracts/{contract_id}/bids/&#x60;  Alternate route: &#x60;/legacy/corporations/{corporation_id}/contracts/{contract_id}/bids/&#x60;  Alternate route: &#x60;/v1/corporations/{corporation_id}/contracts/{contract_id}/bids/&#x60;  --- This route is cached for up to 3600 seconds

    :param contract_id: ID of a contract
    :type contract_id: int
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


async def get_corporations_corporation_id_contracts_contract_id_items(request: web.Request, contract_id, corporation_id, datasource=None, if_none_match=None, token=None) -> web.Response:
    """Get corporation contract items

    Lists items of a particular contract  --- Alternate route: &#x60;/dev/corporations/{corporation_id}/contracts/{contract_id}/items/&#x60;  Alternate route: &#x60;/legacy/corporations/{corporation_id}/contracts/{contract_id}/items/&#x60;  Alternate route: &#x60;/v1/corporations/{corporation_id}/contracts/{contract_id}/items/&#x60;  --- This route is cached for up to 3600 seconds

    :param contract_id: ID of a contract
    :type contract_id: int
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
