from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.error_limited import ErrorLimited
from openapi_server.models.forbidden import Forbidden
from openapi_server.models.gateway_timeout import GatewayTimeout
from openapi_server.models.get_characters_character_id_planets200_ok import GetCharactersCharacterIdPlanets200Ok
from openapi_server.models.get_characters_character_id_planets_planet_id_not_found import GetCharactersCharacterIdPlanetsPlanetIdNotFound
from openapi_server.models.get_characters_character_id_planets_planet_id_ok import GetCharactersCharacterIdPlanetsPlanetIdOk
from openapi_server.models.get_corporations_corporation_id_customs_offices200_ok import GetCorporationsCorporationIdCustomsOffices200Ok
from openapi_server.models.get_universe_schematics_schematic_id_not_found import GetUniverseSchematicsSchematicIdNotFound
from openapi_server.models.get_universe_schematics_schematic_id_ok import GetUniverseSchematicsSchematicIdOk
from openapi_server.models.internal_server_error import InternalServerError
from openapi_server.models.service_unavailable import ServiceUnavailable
from openapi_server.models.unauthorized import Unauthorized
from openapi_server import util


async def get_characters_character_id_planets(request: web.Request, character_id, datasource=None, if_none_match=None, token=None) -> web.Response:
    """Get colonies

    Returns a list of all planetary colonies owned by a character.  --- Alternate route: &#x60;/dev/characters/{character_id}/planets/&#x60;  Alternate route: &#x60;/legacy/characters/{character_id}/planets/&#x60;  Alternate route: &#x60;/v1/characters/{character_id}/planets/&#x60;  --- This route is cached for up to 600 seconds

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


async def get_characters_character_id_planets_planet_id(request: web.Request, character_id, planet_id, datasource=None, if_none_match=None, token=None) -> web.Response:
    """Get colony layout

    Returns full details on the layout of a single planetary colony, including links, pins and routes. Note: Planetary information is only recalculated when the colony is viewed through the client. Information will not update until this criteria is met.  --- Alternate route: &#x60;/dev/characters/{character_id}/planets/{planet_id}/&#x60;  Alternate route: &#x60;/v3/characters/{character_id}/planets/{planet_id}/&#x60;  --- This route is cached for up to 600 seconds

    :param character_id: An EVE character ID
    :type character_id: int
    :param planet_id: Planet id of the target planet
    :type planet_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    return web.Response(status=200)


async def get_corporations_corporation_id_customs_offices(request: web.Request, corporation_id, datasource=None, if_none_match=None, page=None, token=None) -> web.Response:
    """List corporation customs offices

    List customs offices owned by a corporation  --- Alternate route: &#x60;/dev/corporations/{corporation_id}/customs_offices/&#x60;  Alternate route: &#x60;/legacy/corporations/{corporation_id}/customs_offices/&#x60;  Alternate route: &#x60;/v1/corporations/{corporation_id}/customs_offices/&#x60;  --- This route is cached for up to 3600 seconds  --- Requires one of the following EVE corporation role(s): Director 

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


async def get_universe_schematics_schematic_id(request: web.Request, schematic_id, datasource=None, if_none_match=None) -> web.Response:
    """Get schematic information

    Get information on a planetary factory schematic  --- Alternate route: &#x60;/dev/universe/schematics/{schematic_id}/&#x60;  Alternate route: &#x60;/legacy/universe/schematics/{schematic_id}/&#x60;  Alternate route: &#x60;/v1/universe/schematics/{schematic_id}/&#x60;  --- This route is cached for up to 3600 seconds

    :param schematic_id: A PI schematic ID
    :type schematic_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str

    """
    return web.Response(status=200)
