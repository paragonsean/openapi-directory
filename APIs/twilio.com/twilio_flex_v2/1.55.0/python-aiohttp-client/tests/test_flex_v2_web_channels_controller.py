# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.flex_v2_web_channel import FlexV2WebChannel


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_web_channel(client):
    """Test case for create_web_channel

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'address_sid': 'address_sid_example',
        'chat_friendly_name': 'chat_friendly_name_example',
        'customer_friendly_name': 'customer_friendly_name_example',
        'pre_engagement_data': 'pre_engagement_data_example'
        }
    response = await client.request(
        method='POST',
        path='/v2/WebChats',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

