# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.web_hook import WebHook


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_add_presence_web_hook(client):
    """Test case for add_presence_web_hook

    Registers Presence WebHook registration
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'url': 'url_example',
        'user_ids': ['user_ids_example']
        }
    response = await client.request(
        method='POST',
        path='/rest/v2/webhooks/presence',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_add_web_hook(client):
    """Test case for add_web_hook

    Registers a WebHook
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'filter': ['filter_example'],
        'url': 'url_example'
        }
    response = await client.request(
        method='POST',
        path='/rest/v2/webhooks',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_web_hook(client):
    """Test case for get_web_hook

    Gets a list of webHooks
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest/v2/webhooks',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_web_hook_by_id(client):
    """Test case for get_web_hook_by_id

    Gets a webHook
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest/v2/webhooks/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_web_hook(client):
    """Test case for remove_web_hook

    Removes a registered webHook
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/v2/webhooks/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_web_hooks(client):
    """Test case for remove_web_hooks

    Removes all webHooks
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/v2/webhooks',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_presence_web_hook(client):
    """Test case for update_presence_web_hook

    Updates a Presence WebHook registration
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'url': 'url_example',
        'user_ids': ['user_ids_example']
        }
    response = await client.request(
        method='PUT',
        path='/rest/v2/webhooks/presence/{id}'.format(id='id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_web_hook(client):
    """Test case for update_web_hook

    Updates a WebHook registration
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'filter': ['filter_example'],
        'url': 'url_example'
        }
    response = await client.request(
        method='PUT',
        path='/rest/v2/webhooks/{id}'.format(id='id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

