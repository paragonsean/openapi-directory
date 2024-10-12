# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.routes_v2_trunks import RoutesV2Trunks


pytestmark = pytest.mark.asyncio

async def test_fetch_trunks(client):
    """Test case for fetch_trunks

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/Trunks/{sip_trunk_domain}'.format(sip_trunk_domain='sip_trunk_domain_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_trunks(client):
    """Test case for update_trunks

    
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
        path='/v2/Trunks/{sip_trunk_domain}'.format(sip_trunk_domain='sip_trunk_domain_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

