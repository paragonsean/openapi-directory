# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_user_channel_response import ListUserChannelResponse


pytestmark = pytest.mark.asyncio

async def test_list_user_channel(client):
    """Test case for list_user_channel

    
    """
    params = [('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Services/{service_sid}/Users/{user_sid}/Channels'.format(service_sid='service_sid_example', user_sid='user_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

