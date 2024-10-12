# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_get_cached_image(client):
    """Test case for get_cached_image

    Fetch cached image
    """
    params = [('api_key', 'api_key_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/image/cache/car/{listing_id}/{image_id}'.format(listing_id='listing_id_example', image_id='image_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

