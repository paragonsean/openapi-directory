# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_gift_list200_response import GetGiftList200Response


pytestmark = pytest.mark.asyncio

async def test_get_gift_list(client):
    """Test case for get_gift_list

    Get Gift List
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
        path='/api/addon/pvt/giftlist/get/{list_id}'.format(list_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

