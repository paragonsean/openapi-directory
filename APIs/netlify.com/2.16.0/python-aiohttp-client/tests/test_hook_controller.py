# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.hook import Hook


pytestmark = pytest.mark.asyncio

async def test_create_hook_by_site_id(client):
    """Test case for create_hook_by_site_id

    
    """
    hook = openapi_server.Hook()
    params = [('site_id', 'site_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/hooks',
        headers=headers,
        json=hook,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_hook(client):
    """Test case for delete_hook

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/hooks/{hook_id}'.format(hook_id='hook_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enable_hook(client):
    """Test case for enable_hook

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/hooks/{hook_id}/enable'.format(hook_id='hook_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_hook(client):
    """Test case for get_hook

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/hooks/{hook_id}'.format(hook_id='hook_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_hooks_by_site_id(client):
    """Test case for list_hooks_by_site_id

    
    """
    params = [('site_id', 'site_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/hooks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_hook(client):
    """Test case for update_hook

    
    """
    hook = openapi_server.Hook()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/hooks/{hook_id}'.format(hook_id='hook_id_example'),
        headers=headers,
        json=hook,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

