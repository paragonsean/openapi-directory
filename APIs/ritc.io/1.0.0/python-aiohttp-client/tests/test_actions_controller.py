# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.action59 import Action59
from openapi_server.models.action_full_response import ActionFullResponse
from openapi_server.models.action_short_response import ActionShortResponse


pytestmark = pytest.mark.asyncio

async def test_add_action(client):
    """Test case for add_action

    
    """
    action_object = {"codes":"{}","functionId":"functionId","name":"name","parameters":"{}","channelId":0,"desc":"desc"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/actions',
        headers=headers,
        json=action_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_action(client):
    """Test case for get_action

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/actions/{action_id}'.format(action_id='action_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_actions(client):
    """Test case for list_actions

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/actions',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_action(client):
    """Test case for remove_action

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/actions/{action_id}'.format(action_id='action_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_action(client):
    """Test case for update_action

    
    """
    action_object = {"codes":"{}","functionId":"functionId","name":"name","parameters":"{}","channelId":0,"desc":"desc"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/actions/{action_id}'.format(action_id='action_id_example'),
        headers=headers,
        json=action_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

