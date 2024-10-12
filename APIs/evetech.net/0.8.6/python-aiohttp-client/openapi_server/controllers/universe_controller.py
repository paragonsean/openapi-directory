from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.error_limited import ErrorLimited
from openapi_server.models.forbidden import Forbidden
from openapi_server.models.gateway_timeout import GatewayTimeout
from openapi_server.models.get_universe_ancestries200_ok import GetUniverseAncestries200Ok
from openapi_server.models.get_universe_asteroid_belts_asteroid_belt_id_not_found import GetUniverseAsteroidBeltsAsteroidBeltIdNotFound
from openapi_server.models.get_universe_asteroid_belts_asteroid_belt_id_ok import GetUniverseAsteroidBeltsAsteroidBeltIdOk
from openapi_server.models.get_universe_bloodlines200_ok import GetUniverseBloodlines200Ok
from openapi_server.models.get_universe_categories_category_id_not_found import GetUniverseCategoriesCategoryIdNotFound
from openapi_server.models.get_universe_categories_category_id_ok import GetUniverseCategoriesCategoryIdOk
from openapi_server.models.get_universe_constellations_constellation_id_not_found import GetUniverseConstellationsConstellationIdNotFound
from openapi_server.models.get_universe_constellations_constellation_id_ok import GetUniverseConstellationsConstellationIdOk
from openapi_server.models.get_universe_factions200_ok import GetUniverseFactions200Ok
from openapi_server.models.get_universe_graphics_graphic_id_not_found import GetUniverseGraphicsGraphicIdNotFound
from openapi_server.models.get_universe_graphics_graphic_id_ok import GetUniverseGraphicsGraphicIdOk
from openapi_server.models.get_universe_groups_group_id_not_found import GetUniverseGroupsGroupIdNotFound
from openapi_server.models.get_universe_groups_group_id_ok import GetUniverseGroupsGroupIdOk
from openapi_server.models.get_universe_moons_moon_id_not_found import GetUniverseMoonsMoonIdNotFound
from openapi_server.models.get_universe_moons_moon_id_ok import GetUniverseMoonsMoonIdOk
from openapi_server.models.get_universe_planets_planet_id_not_found import GetUniversePlanetsPlanetIdNotFound
from openapi_server.models.get_universe_planets_planet_id_ok import GetUniversePlanetsPlanetIdOk
from openapi_server.models.get_universe_races200_ok import GetUniverseRaces200Ok
from openapi_server.models.get_universe_regions_region_id_not_found import GetUniverseRegionsRegionIdNotFound
from openapi_server.models.get_universe_regions_region_id_ok import GetUniverseRegionsRegionIdOk
from openapi_server.models.get_universe_stargates_stargate_id_not_found import GetUniverseStargatesStargateIdNotFound
from openapi_server.models.get_universe_stargates_stargate_id_ok import GetUniverseStargatesStargateIdOk
from openapi_server.models.get_universe_stars_star_id_ok import GetUniverseStarsStarIdOk
from openapi_server.models.get_universe_stations_station_id_not_found import GetUniverseStationsStationIdNotFound
from openapi_server.models.get_universe_stations_station_id_ok import GetUniverseStationsStationIdOk
from openapi_server.models.get_universe_structures_structure_id_not_found import GetUniverseStructuresStructureIdNotFound
from openapi_server.models.get_universe_structures_structure_id_ok import GetUniverseStructuresStructureIdOk
from openapi_server.models.get_universe_system_jumps200_ok import GetUniverseSystemJumps200Ok
from openapi_server.models.get_universe_system_kills200_ok import GetUniverseSystemKills200Ok
from openapi_server.models.get_universe_systems_system_id_not_found import GetUniverseSystemsSystemIdNotFound
from openapi_server.models.get_universe_systems_system_id_ok import GetUniverseSystemsSystemIdOk
from openapi_server.models.get_universe_types_type_id_not_found import GetUniverseTypesTypeIdNotFound
from openapi_server.models.get_universe_types_type_id_ok import GetUniverseTypesTypeIdOk
from openapi_server.models.internal_server_error import InternalServerError
from openapi_server.models.post_universe_ids_ok import PostUniverseIdsOk
from openapi_server.models.post_universe_names200_ok import PostUniverseNames200Ok
from openapi_server.models.post_universe_names_not_found import PostUniverseNamesNotFound
from openapi_server.models.service_unavailable import ServiceUnavailable
from openapi_server.models.unauthorized import Unauthorized
from openapi_server import util


async def get_universe_ancestries(request: web.Request, accept_language=None, datasource=None, if_none_match=None, language=None) -> web.Response:
    """Get ancestries

    Get all character ancestries  --- Alternate route: &#x60;/dev/universe/ancestries/&#x60;  Alternate route: &#x60;/legacy/universe/ancestries/&#x60;  Alternate route: &#x60;/v1/universe/ancestries/&#x60;  --- This route expires daily at 11:05

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


async def get_universe_asteroid_belts_asteroid_belt_id(request: web.Request, asteroid_belt_id, datasource=None, if_none_match=None) -> web.Response:
    """Get asteroid belt information

    Get information on an asteroid belt  --- Alternate route: &#x60;/dev/universe/asteroid_belts/{asteroid_belt_id}/&#x60;  Alternate route: &#x60;/legacy/universe/asteroid_belts/{asteroid_belt_id}/&#x60;  Alternate route: &#x60;/v1/universe/asteroid_belts/{asteroid_belt_id}/&#x60;  --- This route expires daily at 11:05

    :param asteroid_belt_id: asteroid_belt_id integer
    :type asteroid_belt_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_universe_bloodlines(request: web.Request, accept_language=None, datasource=None, if_none_match=None, language=None) -> web.Response:
    """Get bloodlines

    Get a list of bloodlines  --- Alternate route: &#x60;/dev/universe/bloodlines/&#x60;  Alternate route: &#x60;/legacy/universe/bloodlines/&#x60;  Alternate route: &#x60;/v1/universe/bloodlines/&#x60;  --- This route expires daily at 11:05

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


async def get_universe_categories(request: web.Request, datasource=None, if_none_match=None) -> web.Response:
    """Get item categories

    Get a list of item categories  --- Alternate route: &#x60;/dev/universe/categories/&#x60;  Alternate route: &#x60;/legacy/universe/categories/&#x60;  Alternate route: &#x60;/v1/universe/categories/&#x60;  --- This route expires daily at 11:05

    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_universe_categories_category_id(request: web.Request, category_id, accept_language=None, datasource=None, if_none_match=None, language=None) -> web.Response:
    """Get item category information

    Get information of an item category  --- Alternate route: &#x60;/dev/universe/categories/{category_id}/&#x60;  Alternate route: &#x60;/legacy/universe/categories/{category_id}/&#x60;  Alternate route: &#x60;/v1/universe/categories/{category_id}/&#x60;  --- This route expires daily at 11:05

    :param category_id: An Eve item category ID
    :type category_id: int
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


async def get_universe_constellations(request: web.Request, datasource=None, if_none_match=None) -> web.Response:
    """Get constellations

    Get a list of constellations  --- Alternate route: &#x60;/dev/universe/constellations/&#x60;  Alternate route: &#x60;/legacy/universe/constellations/&#x60;  Alternate route: &#x60;/v1/universe/constellations/&#x60;  --- This route expires daily at 11:05

    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_universe_constellations_constellation_id(request: web.Request, constellation_id, accept_language=None, datasource=None, if_none_match=None, language=None) -> web.Response:
    """Get constellation information

    Get information on a constellation  --- Alternate route: &#x60;/dev/universe/constellations/{constellation_id}/&#x60;  Alternate route: &#x60;/legacy/universe/constellations/{constellation_id}/&#x60;  Alternate route: &#x60;/v1/universe/constellations/{constellation_id}/&#x60;  --- This route expires daily at 11:05

    :param constellation_id: constellation_id integer
    :type constellation_id: int
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


async def get_universe_factions(request: web.Request, accept_language=None, datasource=None, if_none_match=None, language=None) -> web.Response:
    """Get factions

    Get a list of factions  --- Alternate route: &#x60;/dev/universe/factions/&#x60;  Alternate route: &#x60;/v2/universe/factions/&#x60;  --- This route expires daily at 11:05

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


async def get_universe_graphics(request: web.Request, datasource=None, if_none_match=None) -> web.Response:
    """Get graphics

    Get a list of graphics  --- Alternate route: &#x60;/dev/universe/graphics/&#x60;  Alternate route: &#x60;/legacy/universe/graphics/&#x60;  Alternate route: &#x60;/v1/universe/graphics/&#x60;  --- This route expires daily at 11:05

    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_universe_graphics_graphic_id(request: web.Request, graphic_id, datasource=None, if_none_match=None) -> web.Response:
    """Get graphic information

    Get information on a graphic  --- Alternate route: &#x60;/dev/universe/graphics/{graphic_id}/&#x60;  Alternate route: &#x60;/legacy/universe/graphics/{graphic_id}/&#x60;  Alternate route: &#x60;/v1/universe/graphics/{graphic_id}/&#x60;  --- This route expires daily at 11:05

    :param graphic_id: graphic_id integer
    :type graphic_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_universe_groups(request: web.Request, datasource=None, if_none_match=None, page=None) -> web.Response:
    """Get item groups

    Get a list of item groups  --- Alternate route: &#x60;/dev/universe/groups/&#x60;  Alternate route: &#x60;/legacy/universe/groups/&#x60;  Alternate route: &#x60;/v1/universe/groups/&#x60;  --- This route expires daily at 11:05

    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str
    :param page: Which page of results to return
    :type page: int

    """
    return web.Response(status=200)


async def get_universe_groups_group_id(request: web.Request, group_id, accept_language=None, datasource=None, if_none_match=None, language=None) -> web.Response:
    """Get item group information

    Get information on an item group  --- Alternate route: &#x60;/dev/universe/groups/{group_id}/&#x60;  Alternate route: &#x60;/legacy/universe/groups/{group_id}/&#x60;  Alternate route: &#x60;/v1/universe/groups/{group_id}/&#x60;  --- This route expires daily at 11:05

    :param group_id: An Eve item group ID
    :type group_id: int
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


async def get_universe_moons_moon_id(request: web.Request, moon_id, datasource=None, if_none_match=None) -> web.Response:
    """Get moon information

    Get information on a moon  --- Alternate route: &#x60;/dev/universe/moons/{moon_id}/&#x60;  Alternate route: &#x60;/legacy/universe/moons/{moon_id}/&#x60;  Alternate route: &#x60;/v1/universe/moons/{moon_id}/&#x60;  --- This route expires daily at 11:05

    :param moon_id: moon_id integer
    :type moon_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_universe_planets_planet_id(request: web.Request, planet_id, datasource=None, if_none_match=None) -> web.Response:
    """Get planet information

    Get information on a planet  --- Alternate route: &#x60;/dev/universe/planets/{planet_id}/&#x60;  Alternate route: &#x60;/legacy/universe/planets/{planet_id}/&#x60;  Alternate route: &#x60;/v1/universe/planets/{planet_id}/&#x60;  --- This route expires daily at 11:05

    :param planet_id: planet_id integer
    :type planet_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_universe_races(request: web.Request, accept_language=None, datasource=None, if_none_match=None, language=None) -> web.Response:
    """Get character races

    Get a list of character races  --- Alternate route: &#x60;/dev/universe/races/&#x60;  Alternate route: &#x60;/legacy/universe/races/&#x60;  Alternate route: &#x60;/v1/universe/races/&#x60;  --- This route expires daily at 11:05

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


async def get_universe_regions(request: web.Request, datasource=None, if_none_match=None) -> web.Response:
    """Get regions

    Get a list of regions  --- Alternate route: &#x60;/dev/universe/regions/&#x60;  Alternate route: &#x60;/legacy/universe/regions/&#x60;  Alternate route: &#x60;/v1/universe/regions/&#x60;  --- This route expires daily at 11:05

    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_universe_regions_region_id(request: web.Request, region_id, accept_language=None, datasource=None, if_none_match=None, language=None) -> web.Response:
    """Get region information

    Get information on a region  --- Alternate route: &#x60;/dev/universe/regions/{region_id}/&#x60;  Alternate route: &#x60;/legacy/universe/regions/{region_id}/&#x60;  Alternate route: &#x60;/v1/universe/regions/{region_id}/&#x60;  --- This route expires daily at 11:05

    :param region_id: region_id integer
    :type region_id: int
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


async def get_universe_stargates_stargate_id(request: web.Request, stargate_id, datasource=None, if_none_match=None) -> web.Response:
    """Get stargate information

    Get information on a stargate  --- Alternate route: &#x60;/dev/universe/stargates/{stargate_id}/&#x60;  Alternate route: &#x60;/legacy/universe/stargates/{stargate_id}/&#x60;  Alternate route: &#x60;/v1/universe/stargates/{stargate_id}/&#x60;  --- This route expires daily at 11:05

    :param stargate_id: stargate_id integer
    :type stargate_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_universe_stars_star_id(request: web.Request, star_id, datasource=None, if_none_match=None) -> web.Response:
    """Get star information

    Get information on a star  --- Alternate route: &#x60;/dev/universe/stars/{star_id}/&#x60;  Alternate route: &#x60;/legacy/universe/stars/{star_id}/&#x60;  Alternate route: &#x60;/v1/universe/stars/{star_id}/&#x60;  --- This route expires daily at 11:05

    :param star_id: star_id integer
    :type star_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_universe_stations_station_id(request: web.Request, station_id, datasource=None, if_none_match=None) -> web.Response:
    """Get station information

    Get information on a station  --- Alternate route: &#x60;/dev/universe/stations/{station_id}/&#x60;  Alternate route: &#x60;/v2/universe/stations/{station_id}/&#x60;  --- This route expires daily at 11:05

    :param station_id: station_id integer
    :type station_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_universe_structures(request: web.Request, datasource=None, filter=None, if_none_match=None) -> web.Response:
    """List all public structures

    List all public structures  --- Alternate route: &#x60;/dev/universe/structures/&#x60;  Alternate route: &#x60;/legacy/universe/structures/&#x60;  Alternate route: &#x60;/v1/universe/structures/&#x60;  --- This route is cached for up to 3600 seconds

    :param datasource: The server name you would like data from
    :type datasource: str
    :param filter: Only list public structures that have this service online
    :type filter: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_universe_structures_structure_id(request: web.Request, structure_id, datasource=None, if_none_match=None, token=None) -> web.Response:
    """Get structure information

    Returns information on requested structure if you are on the ACL. Otherwise, returns \&quot;Forbidden\&quot; for all inputs.  --- Alternate route: &#x60;/dev/universe/structures/{structure_id}/&#x60;  Alternate route: &#x60;/v2/universe/structures/{structure_id}/&#x60;  --- This route is cached for up to 3600 seconds

    :param structure_id: An Eve structure ID
    :type structure_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str
    :param token: Access token to use if unable to set a header
    :type token: str

    """
    return web.Response(status=200)


async def get_universe_system_jumps(request: web.Request, datasource=None, if_none_match=None) -> web.Response:
    """Get system jumps

    Get the number of jumps in solar systems within the last hour ending at the timestamp of the Last-Modified header, excluding wormhole space. Only systems with jumps will be listed  --- Alternate route: &#x60;/dev/universe/system_jumps/&#x60;  Alternate route: &#x60;/legacy/universe/system_jumps/&#x60;  Alternate route: &#x60;/v1/universe/system_jumps/&#x60;  --- This route is cached for up to 3600 seconds

    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_universe_system_kills(request: web.Request, datasource=None, if_none_match=None) -> web.Response:
    """Get system kills

    Get the number of ship, pod and NPC kills per solar system within the last hour ending at the timestamp of the Last-Modified header, excluding wormhole space. Only systems with kills will be listed  --- Alternate route: &#x60;/dev/universe/system_kills/&#x60;  Alternate route: &#x60;/v2/universe/system_kills/&#x60;  --- This route is cached for up to 3600 seconds

    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_universe_systems(request: web.Request, datasource=None, if_none_match=None) -> web.Response:
    """Get solar systems

    Get a list of solar systems  --- Alternate route: &#x60;/dev/universe/systems/&#x60;  Alternate route: &#x60;/legacy/universe/systems/&#x60;  Alternate route: &#x60;/v1/universe/systems/&#x60;  --- This route expires daily at 11:05

    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_universe_systems_system_id(request: web.Request, system_id, accept_language=None, datasource=None, if_none_match=None, language=None) -> web.Response:
    """Get solar system information

    Get information on a solar system.  --- Alternate route: &#x60;/dev/universe/systems/{system_id}/&#x60;  Alternate route: &#x60;/v4/universe/systems/{system_id}/&#x60;  --- This route expires daily at 11:05

    :param system_id: system_id integer
    :type system_id: int
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


async def get_universe_types(request: web.Request, datasource=None, if_none_match=None, page=None) -> web.Response:
    """Get types

    Get a list of type ids  --- Alternate route: &#x60;/dev/universe/types/&#x60;  Alternate route: &#x60;/legacy/universe/types/&#x60;  Alternate route: &#x60;/v1/universe/types/&#x60;  --- This route expires daily at 11:05

    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str
    :param page: Which page of results to return
    :type page: int

    """
    return web.Response(status=200)


async def get_universe_types_type_id(request: web.Request, type_id, accept_language=None, datasource=None, if_none_match=None, language=None) -> web.Response:
    """Get type information

    Get information on a type  --- Alternate route: &#x60;/dev/universe/types/{type_id}/&#x60;  Alternate route: &#x60;/v3/universe/types/{type_id}/&#x60;  --- This route expires daily at 11:05

    :param type_id: An Eve item type ID
    :type type_id: int
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


async def post_universe_ids(request: web.Request, names, accept_language=None, datasource=None, language=None) -> web.Response:
    """Bulk names to IDs

    Resolve a set of names to IDs in the following categories: agents, alliances, characters, constellations, corporations factions, inventory_types, regions, stations, and systems. Only exact matches will be returned. All names searched for are cached for 12 hours  --- Alternate route: &#x60;/dev/universe/ids/&#x60;  Alternate route: &#x60;/legacy/universe/ids/&#x60;  Alternate route: &#x60;/v1/universe/ids/&#x60; 

    :param names: The names to resolve
    :type names: List[str]
    :param accept_language: Language to use in the response
    :type accept_language: str
    :param datasource: The server name you would like data from
    :type datasource: str
    :param language: Language to use in the response, takes precedence over Accept-Language
    :type language: str

    """
    return web.Response(status=200)


async def post_universe_names(request: web.Request, ids, datasource=None) -> web.Response:
    """Get names and categories for a set of ID&#39;s

    Resolve a set of IDs to names and categories. Supported ID&#39;s for resolving are: Characters, Corporations, Alliances, Stations, Solar Systems, Constellations, Regions, Types  --- Alternate route: &#x60;/dev/universe/names/&#x60;  Alternate route: &#x60;/v2/universe/names/&#x60; 

    :param ids: The ids to resolve
    :type ids: List[int]
    :param datasource: The server name you would like data from
    :type datasource: str

    """
    return web.Response(status=200)
