# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.place_detail import PlaceDetail
from openapi_server.models.places_search_response import PlacesSearchResponse


pytestmark = pytest.mark.asyncio

async def test_places_get(client):
    """Test case for places_get

    Venues, landmarks, regions, these are all places to search.
    """
    params = [('category', ['category_example']),
                    ('function', ['function_example']),
                    ('ambience', ['ambience_example']),
                    ('tag', ['tag_example']),
                    ('type', 'type_example'),
                    ('name', 'name_example'),
                    ('exact', True),
                    ('capacity_min', 3.4),
                    ('capacity_max', 3.4),
                    ('street', 'street_example'),
                    ('locality', 'locality_example'),
                    ('region', 'region_example'),
                    ('postal_code', 'postal_code_example'),
                    ('country', 'country_example'),
                    ('center', 'center_example'),
                    ('radius', 56),
                    ('bbox', ['bbox_example']),
                    ('polygon', ['polygon_example']),
                    ('within', 'within_example'),
                    ('offset', 56),
                    ('limit', 56),
                    ('fieldset', context)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/places',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_places_id_get(client):
    """Test case for places_id_get

    Get specific place details
    """
    params = [('fieldset', summary)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/places/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

