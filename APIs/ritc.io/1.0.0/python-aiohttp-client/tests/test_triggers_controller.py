# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.trigger54 import Trigger54
from openapi_server.models.trigger_full_response import TriggerFullResponse
from openapi_server.models.trigger_short_response import TriggerShortResponse


pytestmark = pytest.mark.asyncio

async def test_add_trigger(client):
    """Test case for add_trigger

    
    """
    trigger_object = {"codes":"{}","functionId":"functionId","name":"name","parameters":"{}","channelId":0,"desc":"desc"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/triggers',
        headers=headers,
        json=trigger_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_trigger(client):
    """Test case for get_trigger

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/triggers/{trigger_id}'.format(trigger_id='trigger_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_triggers(client):
    """Test case for list_triggers

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/triggers',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_trigger(client):
    """Test case for remove_trigger

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/triggers/{trigger_id}'.format(trigger_id='trigger_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_trigger(client):
    """Test case for update_trigger

    
    """
    trigger_object = {"codes":"{}","functionId":"functionId","name":"name","parameters":"{}","channelId":0,"desc":"desc"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/triggers/{trigger_id}'.format(trigger_id='trigger_id_example'),
        headers=headers,
        json=trigger_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

