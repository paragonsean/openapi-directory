# coding: utf-8

import pytest
import json
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


pytestmark = pytest.mark.asyncio

async def test_get_universe_ancestries(client):
    """Test case for get_universe_ancestries

    Get ancestries
    """
    params = [('datasource', tranquility),
                    ('language', en-us)]
    headers = { 
        'Accept': 'application/json',
        'accept_language': en-us,
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/universe/ancestries/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_universe_asteroid_belts_asteroid_belt_id(client):
    """Test case for get_universe_asteroid_belts_asteroid_belt_id

    Get asteroid belt information
    """
    params = [('datasource', tranquility)]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/universe/asteroid_belts/{asteroid_belt_id}'.format(asteroid_belt_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_universe_bloodlines(client):
    """Test case for get_universe_bloodlines

    Get bloodlines
    """
    params = [('datasource', tranquility),
                    ('language', en-us)]
    headers = { 
        'Accept': 'application/json',
        'accept_language': en-us,
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/universe/bloodlines/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_universe_categories(client):
    """Test case for get_universe_categories

    Get item categories
    """
    params = [('datasource', tranquility)]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/universe/categories/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_universe_categories_category_id(client):
    """Test case for get_universe_categories_category_id

    Get item category information
    """
    params = [('datasource', tranquility),
                    ('language', en-us)]
    headers = { 
        'Accept': 'application/json',
        'accept_language': en-us,
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/universe/categories/{category_id}'.format(category_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_universe_constellations(client):
    """Test case for get_universe_constellations

    Get constellations
    """
    params = [('datasource', tranquility)]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/universe/constellations/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_universe_constellations_constellation_id(client):
    """Test case for get_universe_constellations_constellation_id

    Get constellation information
    """
    params = [('datasource', tranquility),
                    ('language', en-us)]
    headers = { 
        'Accept': 'application/json',
        'accept_language': en-us,
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/universe/constellations/{constellation_id}'.format(constellation_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_universe_factions(client):
    """Test case for get_universe_factions

    Get factions
    """
    params = [('datasource', tranquility),
                    ('language', en-us)]
    headers = { 
        'Accept': 'application/json',
        'accept_language': en-us,
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/universe/factions/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_universe_graphics(client):
    """Test case for get_universe_graphics

    Get graphics
    """
    params = [('datasource', tranquility)]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/universe/graphics/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_universe_graphics_graphic_id(client):
    """Test case for get_universe_graphics_graphic_id

    Get graphic information
    """
    params = [('datasource', tranquility)]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/universe/graphics/{graphic_id}'.format(graphic_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_universe_groups(client):
    """Test case for get_universe_groups

    Get item groups
    """
    params = [('datasource', tranquility),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/universe/groups/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_universe_groups_group_id(client):
    """Test case for get_universe_groups_group_id

    Get item group information
    """
    params = [('datasource', tranquility),
                    ('language', en-us)]
    headers = { 
        'Accept': 'application/json',
        'accept_language': en-us,
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/universe/groups/{group_id}'.format(group_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_universe_moons_moon_id(client):
    """Test case for get_universe_moons_moon_id

    Get moon information
    """
    params = [('datasource', tranquility)]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/universe/moons/{moon_id}'.format(moon_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_universe_planets_planet_id(client):
    """Test case for get_universe_planets_planet_id

    Get planet information
    """
    params = [('datasource', tranquility)]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/universe/planets/{planet_id}'.format(planet_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_universe_races(client):
    """Test case for get_universe_races

    Get character races
    """
    params = [('datasource', tranquility),
                    ('language', en-us)]
    headers = { 
        'Accept': 'application/json',
        'accept_language': en-us,
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/universe/races/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_universe_regions(client):
    """Test case for get_universe_regions

    Get regions
    """
    params = [('datasource', tranquility)]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/universe/regions/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_universe_regions_region_id(client):
    """Test case for get_universe_regions_region_id

    Get region information
    """
    params = [('datasource', tranquility),
                    ('language', en-us)]
    headers = { 
        'Accept': 'application/json',
        'accept_language': en-us,
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/universe/regions/{region_id}'.format(region_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_universe_stargates_stargate_id(client):
    """Test case for get_universe_stargates_stargate_id

    Get stargate information
    """
    params = [('datasource', tranquility)]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/universe/stargates/{stargate_id}'.format(stargate_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_universe_stars_star_id(client):
    """Test case for get_universe_stars_star_id

    Get star information
    """
    params = [('datasource', tranquility)]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/universe/stars/{star_id}'.format(star_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_universe_stations_station_id(client):
    """Test case for get_universe_stations_station_id

    Get station information
    """
    params = [('datasource', tranquility)]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/universe/stations/{station_id}'.format(station_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_universe_structures(client):
    """Test case for get_universe_structures

    List all public structures
    """
    params = [('datasource', tranquility),
                    ('filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/universe/structures/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_universe_structures_structure_id(client):
    """Test case for get_universe_structures_structure_id

    Get structure information
    """
    params = [('datasource', tranquility),
                    ('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/latest/universe/structures/{structure_id}'.format(structure_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_universe_system_jumps(client):
    """Test case for get_universe_system_jumps

    Get system jumps
    """
    params = [('datasource', tranquility)]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/universe/system_jumps/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_universe_system_kills(client):
    """Test case for get_universe_system_kills

    Get system kills
    """
    params = [('datasource', tranquility)]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/universe/system_kills/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_universe_systems(client):
    """Test case for get_universe_systems

    Get solar systems
    """
    params = [('datasource', tranquility)]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/universe/systems/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_universe_systems_system_id(client):
    """Test case for get_universe_systems_system_id

    Get solar system information
    """
    params = [('datasource', tranquility),
                    ('language', en-us)]
    headers = { 
        'Accept': 'application/json',
        'accept_language': en-us,
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/universe/systems/{system_id}'.format(system_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_universe_types(client):
    """Test case for get_universe_types

    Get types
    """
    params = [('datasource', tranquility),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/universe/types/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_universe_types_type_id(client):
    """Test case for get_universe_types_type_id

    Get type information
    """
    params = [('datasource', tranquility),
                    ('language', en-us)]
    headers = { 
        'Accept': 'application/json',
        'accept_language': en-us,
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/universe/types/{type_id}'.format(type_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_universe_ids(client):
    """Test case for post_universe_ids

    Bulk names to IDs
    """
    names = ['names_example']
    params = [('datasource', tranquility),
                    ('language', en-us)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept_language': en-us,
    }
    response = await client.request(
        method='POST',
        path='/latest/universe/ids/',
        headers=headers,
        json=names,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_universe_names(client):
    """Test case for post_universe_names

    Get names and categories for a set of ID's
    """
    ids = [56]
    params = [('datasource', tranquility)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/latest/universe/names/',
        headers=headers,
        json=ids,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

