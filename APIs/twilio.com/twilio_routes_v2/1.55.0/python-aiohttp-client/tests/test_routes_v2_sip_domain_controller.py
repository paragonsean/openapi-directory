# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.routes_v2_sip_domain import RoutesV2SipDomain


pytestmark = pytest.mark.asyncio

async def test_fetch_sip_domain(client):
    """Test case for fetch_sip_domain

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/SipDomains/{sip_domain}'.format(sip_domain='sip_domain_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_sip_domain(client):
    """Test case for update_sip_domain

    
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
        path='/v2/SipDomains/{sip_domain}'.format(sip_domain='sip_domain_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

