# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.search_version_number_geometry_search_query_ext_post_request import SearchVersionNumberGeometrySearchQueryExtPostRequest
from openapi_server.models.search_version_number_search_along_route_query_ext_post_request import SearchVersionNumberSearchAlongRouteQueryExtPostRequest


pytestmark = pytest.mark.asyncio

async def test_search_version_number_category_search_query_ext_get(client):
    """Test case for search_version_number_category_search_query_ext_get

    Category Search
    """
    params = [('typeahead', False),
                    ('limit', 10),
                    ('ofs', 0),
                    ('countrySet', 'FR'),
                    ('lat', 37.337),
                    ('lon', -121.89),
                    ('radius', 56),
                    ('topLeft', '37.553,-122.453'),
                    ('btmRight', '37.4,-122.55'),
                    ('language', 'language_example'),
                    ('extendedPostalCodesFor', 'extended_postal_codes_for_example'),
                    ('view', Unified)]
    headers = { 
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/search/{version_number}/categorySearch/{query_ext}'.format(version_number=56, query='pizza', ext='xml'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_version_number_cs_category_ext_get(client):
    """Test case for search_version_number_cs_category_ext_get

    Low Bandwith Category Search
    """
    params = [('typeahead', False),
                    ('limit', 10),
                    ('ofs', 0),
                    ('countrySet', 'FR'),
                    ('lat', 37.337),
                    ('lon', -121.89),
                    ('radius', 56),
                    ('topLeft', '37.553,-122.453'),
                    ('btmRight', '37.4,-122.55'),
                    ('language', 'language_example'),
                    ('idxSet', 'POI'),
                    ('view', Unified)]
    headers = { 
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/search/{version_number}/cS/{category_ext}'.format(version_number=56, category='pizza', ext='xml'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_version_number_geometry_search_query_ext_get(client):
    """Test case for search_version_number_geometry_search_query_ext_get

    Geometry Search
    """
    params = [('geometryList', '[{\"type\":\"POLYGON\", \"vertices\":[\"37.7524152343544, -122.43576049804686\", \"37.70660472542312, -122.43301391601562\", \"37.712059855877314, -122.36434936523438\", \"37.75350561243041, -122.37396240234374\"]}, {\"type\":\"CIRCLE\", \"position\":\"37.71205, -121.36434\", \"radius\":6000}, {\"type\":\"CIRCLE\", \"position\":\"37.31205, -121.36434\", \"radius\":1000}]'),
                    ('limit', 10),
                    ('language', 'language_example'),
                    ('extendedPostalCodesFor', 'extended_postal_codes_for_example'),
                    ('idxSet', 'POI')]
    headers = { 
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/search/{version_number}/geometrySearch/{query_ext}'.format(version_number=56, query='pizza', ext='xml'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_version_number_geometry_search_query_ext_post(client):
    """Test case for search_version_number_geometry_search_query_ext_post

    Geometry Search
    """
    body = openapi_server.SearchVersionNumberGeometrySearchQueryExtPostRequest()
    params = [('limit', 10),
                    ('language', 'language_example'),
                    ('extendedPostalCodesFor', 'extended_postal_codes_for_example'),
                    ('idxSet', 'POI')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/search/{version_number}/geometrySearch/{query_ext}'.format(version_number=56, query='pizza', ext='xml'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_version_number_nearby_search_ext_get(client):
    """Test case for search_version_number_nearby_search_ext_get

    Nearby Search
    """
    params = [('lat', 37.337),
                    ('lon', -121.89),
                    ('limit', 10),
                    ('ofs', 0),
                    ('countrySet', 'FR'),
                    ('radius', 10000),
                    ('topLeft', '37.553,-122.453'),
                    ('btmRight', '37.4,-122.55'),
                    ('language', 'language_example'),
                    ('extendedPostalCodesFor', 'extended_postal_codes_for_example'),
                    ('minFuzzyLevel', 1),
                    ('maxFuzzyLevel', 2),
                    ('idxSet', 'POI'),
                    ('view', Unified)]
    headers = { 
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/search/{version_number}/nearbySearch/.{ext}'.format(version_number=56, ext='xml'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_version_number_poi_search_query_ext_get(client):
    """Test case for search_version_number_poi_search_query_ext_get

    Points of Interest Search
    """
    params = [('typeahead', False),
                    ('limit', 10),
                    ('ofs', 0),
                    ('countrySet', 'FR'),
                    ('lat', 37.337),
                    ('lon', -121.89),
                    ('radius', 56),
                    ('topLeft', '37.553,-122.453'),
                    ('btmRight', '37.4,-122.55'),
                    ('language', 'language_example'),
                    ('extendedPostalCodesFor', 'extended_postal_codes_for_example'),
                    ('view', Unified)]
    headers = { 
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/search/{version_number}/poiSearch/{query_ext}'.format(version_number=56, query='pizza', ext='xml'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_version_number_routed_search_query_position_heading_ext_get(client):
    """Test case for search_version_number_routed_search_query_position_heading_ext_get

    Routed Search
    """
    params = [('typeahead', False),
                    ('limit', 10),
                    ('multiplier', 2),
                    ('routingTimeout', 4000),
                    ('language', 'language_example'),
                    ('extendedPostalCodesFor', 'extended_postal_codes_for_example'),
                    ('idxSet', 'POI')]
    headers = { 
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/search/{version_number}/routedSearch/{query}/{position}/{heading_ext}'.format(version_number=56, query='gas', position='37.8328,-122.27669', heading=90, ext='xml'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_version_number_s_query_ext_get(client):
    """Test case for search_version_number_s_query_ext_get

    Low bandwith Search
    """
    params = [('typeahead', False),
                    ('limit', 10),
                    ('ofs', 0),
                    ('countrySet', 'FR'),
                    ('lat', 37.337),
                    ('lon', -121.89),
                    ('radius', 56),
                    ('topLeft', '37.553,-122.453'),
                    ('btmRight', '37.4,-122.55'),
                    ('language', 'language_example'),
                    ('idxSet', 'POI'),
                    ('view', Unified)]
    headers = { 
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/search/{version_number}/s/{query_ext}'.format(version_number=56, query='pizza', ext='xml'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_version_number_search_along_route_query_ext_post(client):
    """Test case for search_version_number_search_along_route_query_ext_post

    Along Route Search
    """
    body = openapi_server.SearchVersionNumberSearchAlongRouteQueryExtPostRequest()
    params = [('maxDetourTime', 1200),
                    ('limit', 10)]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/search/{version_number}/searchAlongRoute/{query_ext}'.format(version_number=56, query='pizza', ext='xml'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_version_number_search_query_ext_get(client):
    """Test case for search_version_number_search_query_ext_get

    Fuzzy Search
    """
    params = [('typeahead', False),
                    ('limit', 10),
                    ('ofs', 0),
                    ('countrySet', 'FR'),
                    ('lat', 37.337),
                    ('lon', -121.89),
                    ('radius', 56),
                    ('topLeft', '37.553,-122.453'),
                    ('btmRight', '37.4,-122.55'),
                    ('language', 'language_example'),
                    ('extendedPostalCodesFor', 'extended_postal_codes_for_example'),
                    ('minFuzzyLevel', 1),
                    ('maxFuzzyLevel', 2),
                    ('idxSet', 'POI'),
                    ('view', Unified)]
    headers = { 
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/search/{version_number}/search/{query_ext}'.format(version_number=56, query='pizza', ext='xml'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

