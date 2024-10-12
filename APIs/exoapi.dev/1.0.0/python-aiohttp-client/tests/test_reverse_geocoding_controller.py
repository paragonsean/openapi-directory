# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.barcode_generator_post400_response import BarcodeGeneratorPost400Response
from openapi_server.models.reverse_geocoding_get200_response import ReverseGeocodingGet200Response


pytestmark = pytest.mark.asyncio

async def test_reverse_geocoding_get(client):
    """Test case for reverse_geocoding_get

    
    """
    params = [('lat', 3.4),
                    ('lon', 3.4),
                    ('locale', 'locale_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/reverse-geocoding',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

