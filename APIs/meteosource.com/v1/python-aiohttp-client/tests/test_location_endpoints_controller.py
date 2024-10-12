# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.find_places_model import FindPlacesModel
from openapi_server.models.general_request_error import GeneralRequestError
from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.language import Language


pytestmark = pytest.mark.asyncio

async def test_find_places_find_places_get(client):
    """Test case for find_places_find_places_get

    Search for places. Complete words required.
    """
    params = [('text', 'text_example'),
                    ('language', openapi_server.Language()),
                    ('key', 'key_example')]
    headers = { 
        'Accept': 'application/json',
        'APIKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/premium/find_places',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_places_prefix_find_places_prefix_get(client):
    """Test case for find_places_prefix_find_places_prefix_get

    Prefix search for places. Useful for autocomplete forms.
    """
    params = [('text', 'text_example'),
                    ('language', openapi_server.Language()),
                    ('key', 'key_example')]
    headers = { 
        'Accept': 'application/json',
        'APIKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/premium/find_places_prefix',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nearest_place_nearest_place_get(client):
    """Test case for nearest_place_nearest_place_get

    Returns the nearest named location for a given GPS coordinates.
    """
    params = [('lat', 'lat_example'),
                    ('lon', 'lon_example'),
                    ('language', openapi_server.Language()),
                    ('key', 'key_example')]
    headers = { 
        'Accept': 'application/json',
        'APIKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/premium/nearest_place',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

