# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_byoc_trunk_response import ListByocTrunkResponse
from openapi_server.models.voice_v1_byoc_trunk import VoiceV1ByocTrunk


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_byoc_trunk(client):
    """Test case for create_byoc_trunk

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'cnam_lookup_enabled': True,
        'connection_policy_sid': 'connection_policy_sid_example',
        'friendly_name': 'friendly_name_example',
        'from_domain_sid': 'from_domain_sid_example',
        'status_callback_method': 'status_callback_method_example',
        'status_callback_url': 'status_callback_url_example',
        'voice_fallback_method': 'voice_fallback_method_example',
        'voice_fallback_url': 'voice_fallback_url_example',
        'voice_method': 'voice_method_example',
        'voice_url': 'voice_url_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/ByocTrunks',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_byoc_trunk(client):
    """Test case for delete_byoc_trunk

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/ByocTrunks/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_byoc_trunk(client):
    """Test case for fetch_byoc_trunk

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/ByocTrunks/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_byoc_trunk(client):
    """Test case for list_byoc_trunk

    
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
        path='/v1/ByocTrunks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_byoc_trunk(client):
    """Test case for update_byoc_trunk

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'cnam_lookup_enabled': True,
        'connection_policy_sid': 'connection_policy_sid_example',
        'friendly_name': 'friendly_name_example',
        'from_domain_sid': 'from_domain_sid_example',
        'status_callback_method': 'status_callback_method_example',
        'status_callback_url': 'status_callback_url_example',
        'voice_fallback_method': 'voice_fallback_method_example',
        'voice_fallback_url': 'voice_fallback_url_example',
        'voice_method': 'voice_method_example',
        'voice_url': 'voice_url_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/ByocTrunks/{sid}'.format(sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

