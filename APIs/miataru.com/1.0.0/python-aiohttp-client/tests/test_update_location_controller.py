# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.ack import ACK
from openapi_server.models.miataru_update_location_request import MiataruUpdateLocationRequest


pytestmark = pytest.mark.asyncio

async def test_update_location(client):
    """Test case for update_location

    
    """
    body = {"MiataruConfig":{"LocationDataRetentionTime":"30","EnableLocationHistory":"False"},"MiataruLocation":[{"HorizontalAccuracy":"50","Device":"7b8e6e0ee5296db345162dc2ef652c1350761823","Latitude":"41.079351","Longitude":"-4.394531","Timestamp":"1441360863"},{"HorizontalAccuracy":"50","Device":"7b8e6e0ee5296db345162dc2ef652c1350761823","Latitude":"41.079351","Longitude":"-4.394531","Timestamp":"1441360863"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/UpdateLocation',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

