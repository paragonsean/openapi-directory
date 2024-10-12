# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.tfl_api_presentation_entities_place import TflApiPresentationEntitiesPlace
from openapi_server.models.tfl_api_presentation_entities_place_category import TflApiPresentationEntitiesPlaceCategory
from openapi_server.models.tfl_api_presentation_entities_stop_point import TflApiPresentationEntitiesStopPoint


pytestmark = pytest.mark.asyncio

async def test_place_get(client):
    """Test case for place_get

    Gets the place with the given id.
    """
    params = [('includeChildren', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Place/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_place_get_at(client):
    """Test case for place_get_at

    Gets any places of the given type whose geography intersects the given latitude and longitude. In practice this means the Place              must be polygonal e.g. a BoroughBoundary.
    """
    params = [('lat', 'lat_example'),
                    ('lon', 'lon_example'),
                    ('location.lat', 3.4),
                    ('location.lon', 3.4)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Place/{type}/At/{lat}/{lon}'.format(type=['type_example'], lat2='lat_example', lon2='lon_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_place_get_by_geo(client):
    """Test case for place_get_by_geo

    Gets the places that lie within a geographic region. The geographic region of interest can either be specified              by using a lat/lon geo-point and a radius in metres to return places within the locus defined by the lat/lon of              its centre or alternatively, by the use of a bounding box defined by the lat/lon of its north-west and south-east corners.              Optionally filters on type and can strip properties for a smaller payload.
    """
    params = [('radius', 3.4),
                    ('categories', ['categories_example']),
                    ('includeChildren', True),
                    ('type', ['type_example']),
                    ('activeOnly', True),
                    ('numberOfPlacesToReturn', 56),
                    ('placeGeo.swLat', 3.4),
                    ('placeGeo.swLon', 3.4),
                    ('placeGeo.neLat', 3.4),
                    ('placeGeo.neLon', 3.4),
                    ('placeGeo.lat', 3.4),
                    ('placeGeo.lon', 3.4)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Place',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_place_get_by_type(client):
    """Test case for place_get_by_type

    Gets all places of a given type
    """
    params = [('activeOnly', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Place/Type/{types}'.format(types=['types_example']),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_place_get_overlay(client):
    """Test case for place_get_overlay

    Gets the place overlay for a given set of co-ordinates and a given width/height.
    """
    params = [('lat', 'lat_example'),
                    ('lon', 'lon_example'),
                    ('location.lat', 3.4),
                    ('location.lon', 3.4)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Place/{type}/overlay/{z}/{lat}/{lon}/{width}/{height}'.format(z=56, type=['type_example'], width=56, height=56, lat2='lat_example', lon2='lon_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_place_get_streets_by_post_code(client):
    """Test case for place_get_streets_by_post_code

    Gets the set of streets associated with a post code.
    """
    params = [('postcode', 'postcode_example'),
                    ('postcodeInput.postcode', 'postcode_input_postcode_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Place/Address/Streets/{postcode}'.format(postcode2='postcode_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_place_meta_categories(client):
    """Test case for place_meta_categories

    Gets a list of all of the available place property categories and keys.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Place/Meta/Categories',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_place_meta_place_types(client):
    """Test case for place_meta_place_types

    Gets a list of the available types of Place.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Place/Meta/PlaceTypes',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_place_search(client):
    """Test case for place_search

    Gets all places that matches the given query
    """
    params = [('name', 'name_example'),
                    ('types', ['types_example'])]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Place/Search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

