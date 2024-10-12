# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_product_rating200_response import GetProductRating200Response


pytestmark = pytest.mark.asyncio

async def test_get_product_rating(client):
    """Test case for get_product_rating

    Get Product Rating
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rating/{product_id}'.format(product_id='1'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

