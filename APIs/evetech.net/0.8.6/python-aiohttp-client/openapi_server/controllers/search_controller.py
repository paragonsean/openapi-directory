from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.error_limited import ErrorLimited
from openapi_server.models.forbidden import Forbidden
from openapi_server.models.gateway_timeout import GatewayTimeout
from openapi_server.models.get_characters_character_id_search_ok import GetCharactersCharacterIdSearchOk
from openapi_server.models.get_search_ok import GetSearchOk
from openapi_server.models.internal_server_error import InternalServerError
from openapi_server.models.service_unavailable import ServiceUnavailable
from openapi_server.models.unauthorized import Unauthorized
from openapi_server import util


async def get_characters_character_id_search(request: web.Request, categories, character_id, search, accept_language=None, datasource=None, if_none_match=None, language=None, strict=None, token=None) -> web.Response:
    """Search on a string

    Search for entities that match a given sub-string.  --- Alternate route: &#x60;/dev/characters/{character_id}/search/&#x60;  Alternate route: &#x60;/v3/characters/{character_id}/search/&#x60;  --- This route is cached for up to 3600 seconds

    :param categories: Type of entities to search for
    :type categories: List[str]
    :param character_id: An EVE character ID
    :type character_id: int
    :param search: The string to search on
    :type search: str
    :param accept_language: Language to use in the response
    :type accept_language: str
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str
    :param language: Language to use in the response, takes precedence over Accept-Language
    :type language: str
    :param strict: Whether the search should be a strict match
    :type strict: bool
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    return web.Response(status=200)


async def get_search(request: web.Request, categories, search, accept_language=None, datasource=None, if_none_match=None, language=None, strict=None) -> web.Response:
    """Search on a string

    Search for entities that match a given sub-string.  --- Alternate route: &#x60;/dev/search/&#x60;  Alternate route: &#x60;/v2/search/&#x60;  --- This route is cached for up to 3600 seconds

    :param categories: Type of entities to search for
    :type categories: List[str]
    :param search: The string to search on
    :type search: str
    :param accept_language: Language to use in the response
    :type accept_language: str
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str
    :param language: Language to use in the response, takes precedence over Accept-Language
    :type language: str
    :param strict: Whether the search should be a strict match
    :type strict: bool

    """
    return web.Response(status=200)
