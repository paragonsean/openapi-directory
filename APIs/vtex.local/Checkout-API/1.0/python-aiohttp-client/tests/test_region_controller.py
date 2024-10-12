# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_sellers_by_region200_response import GetSellersByRegion200Response


pytestmark = pytest.mark.asyncio

async def test_get_sellers_by_region(client):
    """Test case for get_sellers_by_region

    Get sellers by region or address
    """
    params = [('country', 'BRA'),
                    ('postalCode', '1234000'),
                    ('geoCoordinates', [-47.924747467041016,-15.832582473754883])]
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/checkout/pub/regions/{region_id}'.format(region_id='v2.1BB18CE648B5111D0933734ED83EC783'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

