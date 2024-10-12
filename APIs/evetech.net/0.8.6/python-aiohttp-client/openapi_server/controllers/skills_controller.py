from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.error_limited import ErrorLimited
from openapi_server.models.forbidden import Forbidden
from openapi_server.models.gateway_timeout import GatewayTimeout
from openapi_server.models.get_characters_character_id_attributes_ok import GetCharactersCharacterIdAttributesOk
from openapi_server.models.get_characters_character_id_skillqueue200_ok import GetCharactersCharacterIdSkillqueue200Ok
from openapi_server.models.get_characters_character_id_skills_ok import GetCharactersCharacterIdSkillsOk
from openapi_server.models.internal_server_error import InternalServerError
from openapi_server.models.service_unavailable import ServiceUnavailable
from openapi_server.models.unauthorized import Unauthorized
from openapi_server import util


async def get_characters_character_id_attributes(request: web.Request, character_id, datasource=None, if_none_match=None, token=None) -> web.Response:
    """Get character attributes

    Return attributes of a character  --- Alternate route: &#x60;/dev/characters/{character_id}/attributes/&#x60;  Alternate route: &#x60;/legacy/characters/{character_id}/attributes/&#x60;  Alternate route: &#x60;/v1/characters/{character_id}/attributes/&#x60;  --- This route is cached for up to 3600 seconds

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


async def get_characters_character_id_skillqueue(request: web.Request, character_id, datasource=None, if_none_match=None, token=None) -> web.Response:
    """Get character&#39;s skill queue

    List the configured skill queue for the given character  --- Alternate route: &#x60;/dev/characters/{character_id}/skillqueue/&#x60;  Alternate route: &#x60;/legacy/characters/{character_id}/skillqueue/&#x60;  Alternate route: &#x60;/v2/characters/{character_id}/skillqueue/&#x60;  --- This route is cached for up to 120 seconds

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


async def get_characters_character_id_skills(request: web.Request, character_id, datasource=None, if_none_match=None, token=None) -> web.Response:
    """Get character skills

    List all trained skills for the given character  --- Alternate route: &#x60;/dev/characters/{character_id}/skills/&#x60;  Alternate route: &#x60;/v4/characters/{character_id}/skills/&#x60;  --- This route is cached for up to 120 seconds

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
