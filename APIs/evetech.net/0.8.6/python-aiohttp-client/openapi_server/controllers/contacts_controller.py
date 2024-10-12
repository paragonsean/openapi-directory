from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.error_limited import ErrorLimited
from openapi_server.models.forbidden import Forbidden
from openapi_server.models.gateway_timeout import GatewayTimeout
from openapi_server.models.get_alliances_alliance_id_contacts200_ok import GetAlliancesAllianceIdContacts200Ok
from openapi_server.models.get_alliances_alliance_id_contacts_labels200_ok import GetAlliancesAllianceIdContactsLabels200Ok
from openapi_server.models.get_characters_character_id_contacts200_ok import GetCharactersCharacterIdContacts200Ok
from openapi_server.models.get_characters_character_id_contacts_labels200_ok import GetCharactersCharacterIdContactsLabels200Ok
from openapi_server.models.get_corporations_corporation_id_contacts200_ok import GetCorporationsCorporationIdContacts200Ok
from openapi_server.models.get_corporations_corporation_id_contacts_labels200_ok import GetCorporationsCorporationIdContactsLabels200Ok
from openapi_server.models.internal_server_error import InternalServerError
from openapi_server.models.post_characters_character_id_contacts_error520 import PostCharactersCharacterIdContactsError520
from openapi_server.models.service_unavailable import ServiceUnavailable
from openapi_server.models.unauthorized import Unauthorized
from openapi_server import util


async def delete_characters_character_id_contacts(request: web.Request, character_id, contact_ids, datasource=None, token=None) -> web.Response:
    """Delete contacts

    Bulk delete contacts  --- Alternate route: &#x60;/dev/characters/{character_id}/contacts/&#x60;  Alternate route: &#x60;/v2/characters/{character_id}/contacts/&#x60; 

    :param character_id: An EVE character ID
    :type character_id: int
    :param contact_ids: A list of contacts to delete
    :type contact_ids: List[int]
    :param datasource: The server name you would like data from
    :type datasource: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    return web.Response(status=200)


async def get_alliances_alliance_id_contacts(request: web.Request, alliance_id, datasource=None, if_none_match=None, page=None, token=None) -> web.Response:
    """Get alliance contacts

    Return contacts of an alliance  --- Alternate route: &#x60;/dev/alliances/{alliance_id}/contacts/&#x60;  Alternate route: &#x60;/v2/alliances/{alliance_id}/contacts/&#x60;  --- This route is cached for up to 300 seconds

    :param alliance_id: An EVE alliance ID
    :type alliance_id: int
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


async def get_alliances_alliance_id_contacts_labels(request: web.Request, alliance_id, datasource=None, if_none_match=None, token=None) -> web.Response:
    """Get alliance contact labels

    Return custom labels for an alliance&#39;s contacts  --- Alternate route: &#x60;/dev/alliances/{alliance_id}/contacts/labels/&#x60;  Alternate route: &#x60;/legacy/alliances/{alliance_id}/contacts/labels/&#x60;  Alternate route: &#x60;/v1/alliances/{alliance_id}/contacts/labels/&#x60;  --- This route is cached for up to 300 seconds

    :param alliance_id: An EVE alliance ID
    :type alliance_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    return web.Response(status=200)


async def get_characters_character_id_contacts(request: web.Request, character_id, datasource=None, if_none_match=None, page=None, token=None) -> web.Response:
    """Get contacts

    Return contacts of a character  --- Alternate route: &#x60;/dev/characters/{character_id}/contacts/&#x60;  Alternate route: &#x60;/v2/characters/{character_id}/contacts/&#x60;  --- This route is cached for up to 300 seconds

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


async def get_characters_character_id_contacts_labels(request: web.Request, character_id, datasource=None, if_none_match=None, token=None) -> web.Response:
    """Get contact labels

    Return custom labels for a character&#39;s contacts  --- Alternate route: &#x60;/dev/characters/{character_id}/contacts/labels/&#x60;  Alternate route: &#x60;/legacy/characters/{character_id}/contacts/labels/&#x60;  Alternate route: &#x60;/v1/characters/{character_id}/contacts/labels/&#x60;  --- This route is cached for up to 300 seconds

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


async def get_corporations_corporation_id_contacts(request: web.Request, corporation_id, datasource=None, if_none_match=None, page=None, token=None) -> web.Response:
    """Get corporation contacts

    Return contacts of a corporation  --- Alternate route: &#x60;/dev/corporations/{corporation_id}/contacts/&#x60;  Alternate route: &#x60;/v2/corporations/{corporation_id}/contacts/&#x60;  --- This route is cached for up to 300 seconds

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


async def get_corporations_corporation_id_contacts_labels(request: web.Request, corporation_id, datasource=None, if_none_match=None, token=None) -> web.Response:
    """Get corporation contact labels

    Return custom labels for a corporation&#39;s contacts  --- Alternate route: &#x60;/dev/corporations/{corporation_id}/contacts/labels/&#x60;  Alternate route: &#x60;/legacy/corporations/{corporation_id}/contacts/labels/&#x60;  Alternate route: &#x60;/v1/corporations/{corporation_id}/contacts/labels/&#x60;  --- This route is cached for up to 300 seconds

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


async def post_characters_character_id_contacts(request: web.Request, character_id, standing, contact_ids, datasource=None, label_ids=None, token=None, watched=None) -> web.Response:
    """Add contacts

    Bulk add contacts with same settings  --- Alternate route: &#x60;/dev/characters/{character_id}/contacts/&#x60;  Alternate route: &#x60;/v2/characters/{character_id}/contacts/&#x60; 

    :param character_id: An EVE character ID
    :type character_id: int
    :param standing: Standing for the contact
    :type standing: float
    :param contact_ids: A list of contacts
    :type contact_ids: List[int]
    :param datasource: The server name you would like data from
    :type datasource: str
    :param label_ids: Add custom labels to the new contact
    :type label_ids: List[int]
    :param token: Access token to use if unable to set a header
    :type token: str
    :param watched: Whether the contact should be watched, note this is only effective on characters
    :type watched: bool

    """
    return web.Response(status=200)


async def put_characters_character_id_contacts(request: web.Request, character_id, standing, contact_ids, datasource=None, label_ids=None, token=None, watched=None) -> web.Response:
    """Edit contacts

    Bulk edit contacts with same settings  --- Alternate route: &#x60;/dev/characters/{character_id}/contacts/&#x60;  Alternate route: &#x60;/v2/characters/{character_id}/contacts/&#x60; 

    :param character_id: An EVE character ID
    :type character_id: int
    :param standing: Standing for the contact
    :type standing: float
    :param contact_ids: A list of contacts
    :type contact_ids: List[int]
    :param datasource: The server name you would like data from
    :type datasource: str
    :param label_ids: Add custom labels to the contact
    :type label_ids: List[int]
    :param token: Access token to use if unable to set a header
    :type token: str
    :param watched: Whether the contact should be watched, note this is only effective on characters
    :type watched: bool

    """
    return web.Response(status=200)
