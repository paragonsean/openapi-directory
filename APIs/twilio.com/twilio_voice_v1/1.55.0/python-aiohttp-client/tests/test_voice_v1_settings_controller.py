# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.voice_v1_dialing_permissions_dialing_permissions_settings import VoiceV1DialingPermissionsDialingPermissionsSettings


pytestmark = pytest.mark.asyncio

async def test_fetch_dialing_permissions_settings(client):
    """Test case for fetch_dialing_permissions_settings

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Settings',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_dialing_permissions_settings(client):
    """Test case for update_dialing_permissions_settings

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'dialing_permissions_inheritance': True
        }
    response = await client.request(
        method='POST',
        path='/v1/Settings',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

