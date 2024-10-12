# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.channel import Channel
from openapi_server.models.channel_response import ChannelResponse
from openapi_server.models.function7 import Function7
from openapi_server.models.function_response import FunctionResponse
from openapi_server.models.rule import Rule


pytestmark = pytest.mark.asyncio

async def test_add_channel(client):
    """Test case for add_channel

    
    """
    channel_object = {"functions":[{"name":"name","id":"id","type":"action","parameters":[{"value":"value","key":"key"},{"value":"value","key":"key"}]},{"name":"name","id":"id","type":"action","parameters":[{"value":"value","key":"key"},{"value":"value","key":"key"}]}],"name":"name","description":"description","id":"id","type":"{}"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/channels',
        headers=headers,
        json=channel_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_channel_function(client):
    """Test case for add_channel_function

    
    """
    channel_function_object = {"endpoint":"endpoint","name":"name","requestParameters":[{"schema":{"default":"default","datatype":"{}","style":"postbody","expose":"{}","required":"{}"},"name":"name","description":"description","label":"label","fieldType":"fieldType"},{"schema":{"default":"default","datatype":"{}","style":"postbody","expose":"{}","required":"{}"},"name":"name","description":"description","label":"label","fieldType":"fieldType"}],"responseFormat":"Html","httpMethod":"DELETE","type":"action","apiType":"Internal","desc":"desc"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/channels/{channel_id}/functions'.format(channel_id='channel_id_example'),
        headers=headers,
        json=channel_function_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_channel(client):
    """Test case for get_channel

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/channels/{channel_id}'.format(channel_id='channel_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_channel_function(client):
    """Test case for get_channel_function

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/channels/{channel_id}/functions/{function_id}'.format(channel_id='channel_id_example', function_id='function_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_anonymous_channels(client):
    """Test case for list_anonymous_channels

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/channels/anonymous',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_channel_functions(client):
    """Test case for list_channel_functions

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/channels/{channel_id}/functions'.format(channel_id='channel_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_channels(client):
    """Test case for list_channels

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/channels',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_channel(client):
    """Test case for remove_channel

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/channels/{channel_id}'.format(channel_id='channel_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_channel(client):
    """Test case for update_channel

    
    """
    channel_object = {"actionIds":"actionIds","triggerIds":"triggerIds","name":"name","description":"description","status":"active"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/channels/{channel_id}'.format(channel_id='channel_id_example'),
        headers=headers,
        json=channel_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

