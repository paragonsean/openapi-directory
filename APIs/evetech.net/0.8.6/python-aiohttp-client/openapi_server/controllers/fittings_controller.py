from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.error_limited import ErrorLimited
from openapi_server.models.forbidden import Forbidden
from openapi_server.models.gateway_timeout import GatewayTimeout
from openapi_server.models.get_characters_character_id_fittings200_ok import GetCharactersCharacterIdFittings200Ok
from openapi_server.models.internal_server_error import InternalServerError
from openapi_server.models.post_characters_character_id_fittings_created import PostCharactersCharacterIdFittingsCreated
from openapi_server.models.post_characters_character_id_fittings_fitting import PostCharactersCharacterIdFittingsFitting
from openapi_server.models.service_unavailable import ServiceUnavailable
from openapi_server.models.unauthorized import Unauthorized
from openapi_server import util


async def delete_characters_character_id_fittings_fitting_id(request: web.Request, character_id, fitting_id, datasource=None, token=None) -> web.Response:
    """Delete fitting

    Delete a fitting from a character  --- Alternate route: &#x60;/dev/characters/{character_id}/fittings/{fitting_id}/&#x60;  Alternate route: &#x60;/legacy/characters/{character_id}/fittings/{fitting_id}/&#x60;  Alternate route: &#x60;/v1/characters/{character_id}/fittings/{fitting_id}/&#x60; 

    :param character_id: An EVE character ID
    :type character_id: int
    :param fitting_id: ID for a fitting of this character
    :type fitting_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    return web.Response(status=200)


async def get_characters_character_id_fittings(request: web.Request, character_id, datasource=None, if_none_match=None, token=None) -> web.Response:
    """Get fittings

    Return fittings of a character  --- Alternate route: &#x60;/dev/characters/{character_id}/fittings/&#x60;  Alternate route: &#x60;/legacy/characters/{character_id}/fittings/&#x60;  Alternate route: &#x60;/v1/characters/{character_id}/fittings/&#x60;  --- This route is cached for up to 300 seconds

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


async def post_characters_character_id_fittings(request: web.Request, character_id, fitting, datasource=None, token=None) -> web.Response:
    """Create fitting

    Save a new fitting for a character  --- Alternate route: &#x60;/dev/characters/{character_id}/fittings/&#x60;  Alternate route: &#x60;/legacy/characters/{character_id}/fittings/&#x60;  Alternate route: &#x60;/v1/characters/{character_id}/fittings/&#x60; 

    :param character_id: An EVE character ID
    :type character_id: int
    :param fitting: Details about the new fitting
    :type fitting: dict | bytes
    :param datasource: The server name you would like data from
    :type datasource: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    fitting = PostCharactersCharacterIdFittingsFitting.from_dict(fitting)
    return web.Response(status=200)
