# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.composition_hook_enum_format import CompositionHookEnumFormat
from openapi_server.models.list_composition_hook_response import ListCompositionHookResponse
from openapi_server.models.video_v1_composition_hook import VideoV1CompositionHook


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_composition_hook(client):
    """Test case for create_composition_hook

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'audio_sources': ['audio_sources_example'],
        'audio_sources_excluded': ['audio_sources_excluded_example'],
        'enabled': True,
        'format': openapi_server.CompositionHookEnumFormat(),
        'friendly_name': 'friendly_name_example',
        'resolution': 'resolution_example',
        'status_callback': 'status_callback_example',
        'status_callback_method': 'status_callback_method_example',
        'trim': True,
        'video_layout': None
        }
    response = await client.request(
        method='POST',
        path='/v1/CompositionHooks',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_composition_hook(client):
    """Test case for delete_composition_hook

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/CompositionHooks/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_composition_hook(client):
    """Test case for fetch_composition_hook

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/CompositionHooks/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_composition_hook(client):
    """Test case for list_composition_hook

    
    """
    params = [('Enabled', True),
                    ('DateCreatedAfter', '2013-10-20T19:20:30+01:00'),
                    ('DateCreatedBefore', '2013-10-20T19:20:30+01:00'),
                    ('FriendlyName', 'friendly_name_example'),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/CompositionHooks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_composition_hook(client):
    """Test case for update_composition_hook

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'audio_sources': ['audio_sources_example'],
        'audio_sources_excluded': ['audio_sources_excluded_example'],
        'enabled': True,
        'format': openapi_server.CompositionHookEnumFormat(),
        'friendly_name': 'friendly_name_example',
        'resolution': 'resolution_example',
        'status_callback': 'status_callback_example',
        'status_callback_method': 'status_callback_method_example',
        'trim': True,
        'video_layout': None
        }
    response = await client.request(
        method='POST',
        path='/v1/CompositionHooks/{sid}'.format(sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

