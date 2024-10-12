# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.hook import Hook
from openapi_server.models.hook_output import HookOutput


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_hook(client):
    """Test case for create_hook

    Creates a hook subscription
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'api-key': 'special-key',
    }
    data = {
        'actions': ['actions_example'],
        'event_type': 'event_type_example',
        'status': 'status_example',
        'subscriber_address': 'subscriber_address_example',
        'subscriber_language': 'subscriber_language_example',
        'subscriber_name': 'subscriber_name_example',
        'subscriber_type': 'subscriber_type_example',
        'subscriber_url': 'subscriber_url_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/hooks',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delet_hook(client):
    """Test case for delet_hook

    Deletes hook
    """
    headers = { 
        'Accept': 'application/json',
        'api-key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/hooks/{hook_id}'.format(hook_id='hook_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_hook(client):
    """Test case for list_hook

    Lists all hooks
    """
    headers = { 
        'Accept': 'application/json',
        'api-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/hooks',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_hook(client):
    """Test case for update_hook

    Updates hook
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'api-key': 'special-key',
    }
    data = {
        'actions': ['actions_example'],
        'event_type': 'event_type_example',
        'status': 'status_example',
        'subscriber_address': 'subscriber_address_example',
        'subscriber_language': 'subscriber_language_example',
        'subscriber_name': 'subscriber_name_example',
        'subscriber_type': 'subscriber_type_example',
        'subscriber_url': 'subscriber_url_example'
        }
    response = await client.request(
        method='PUT',
        path='/v1/hooks/{hook_id}'.format(hook_id='hook_id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

