# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.routes_v2_phone_number import RoutesV2PhoneNumber


pytestmark = pytest.mark.asyncio

async def test_fetch_phone_number(client):
    """Test case for fetch_phone_number

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/PhoneNumbers/{phone_number}'.format(phone_number='phone_number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_phone_number(client):
    """Test case for update_phone_number

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'friendly_name': 'friendly_name_example',
        'voice_region': 'voice_region_example'
        }
    response = await client.request(
        method='POST',
        path='/v2/PhoneNumbers/{phone_number}'.format(phone_number='phone_number_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

