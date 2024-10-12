# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.build_hook import BuildHook
from openapi_server.models.build_hook_setup import BuildHookSetup
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_create_site_build_hook(client):
    """Test case for create_site_build_hook

    
    """
    build_hook = openapi_server.BuildHookSetup()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/sites/{site_id}/build_hooks'.format(site_id='site_id_example'),
        headers=headers,
        json=build_hook,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_site_build_hook(client):
    """Test case for delete_site_build_hook

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/sites/{site_id}/build_hooks/{id}'.format(site_id='site_id_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_site_build_hook(client):
    """Test case for get_site_build_hook

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/sites/{site_id}/build_hooks/{id}'.format(site_id='site_id_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_site_build_hooks(client):
    """Test case for list_site_build_hooks

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/sites/{site_id}/build_hooks'.format(site_id='site_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_site_build_hook(client):
    """Test case for update_site_build_hook

    
    """
    build_hook = openapi_server.BuildHookSetup()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/sites/{site_id}/build_hooks/{id}'.format(site_id='site_id_example', id='id_example'),
        headers=headers,
        json=build_hook,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

