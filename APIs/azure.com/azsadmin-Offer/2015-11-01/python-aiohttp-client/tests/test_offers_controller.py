# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.offer_list import OfferList


pytestmark = pytest.mark.asyncio

async def test_offers_list(client):
    """Test case for offers_list

    
    """
    params = [('api-version', '2015-11-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/offers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

