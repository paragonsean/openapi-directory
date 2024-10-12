# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_origination_url_response import ListOriginationUrlResponse
from openapi_server.models.trunking_v1_trunk_origination_url import TrunkingV1TrunkOriginationUrl


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_origination_url(client):
    """Test case for create_origination_url

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'enabled': True,
        'friendly_name': 'friendly_name_example',
        'priority': 56,
        'sip_url': 'sip_url_example',
        'weight': 56
        }
    response = await client.request(
        method='POST',
        path='/v1/Trunks/{trunk_sid}/OriginationUrls'.format(trunk_sid='trunk_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_origination_url(client):
    """Test case for delete_origination_url

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/Trunks/{trunk_sid}/OriginationUrls/{sid}'.format(trunk_sid='trunk_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_origination_url(client):
    """Test case for fetch_origination_url

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Trunks/{trunk_sid}/OriginationUrls/{sid}'.format(trunk_sid='trunk_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_origination_url(client):
    """Test case for list_origination_url

    
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
        path='/v1/Trunks/{trunk_sid}/OriginationUrls'.format(trunk_sid='trunk_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_origination_url(client):
    """Test case for update_origination_url

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'enabled': True,
        'friendly_name': 'friendly_name_example',
        'priority': 56,
        'sip_url': 'sip_url_example',
        'weight': 56
        }
    response = await client.request(
        method='POST',
        path='/v1/Trunks/{trunk_sid}/OriginationUrls/{sid}'.format(trunk_sid='trunk_sid_example', sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

