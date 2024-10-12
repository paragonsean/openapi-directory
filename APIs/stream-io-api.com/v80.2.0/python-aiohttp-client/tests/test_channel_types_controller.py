# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.create_channel_type_request import CreateChannelTypeRequest
from openapi_server.models.create_channel_type_response import CreateChannelTypeResponse
from openapi_server.models.list_channel_types_response import ListChannelTypesResponse
from openapi_server.models.response import Response
from openapi_server.models.update_channel_type_request import UpdateChannelTypeRequest
from openapi_server.models.update_channel_type_response import UpdateChannelTypeResponse


pytestmark = pytest.mark.asyncio

async def test_create_channel_type_0(client):
    """Test case for create_channel_type_0

    Create channel type
    """
    body = {"blocklist":"blocklist","grants":{"key":["grants","grants"]},"push_notifications":True,"custom_events":True,"automod":"disabled","message_retention":"message_retention","url_enrichment":True,"mutes":True,"read_events":True,"blocklist_behavior":"flag","uploads":True,"connect_events":True,"automod_behavior":"flag","search":True,"replies":True,"permissions":[{"owner":True,"roles":["roles","roles"],"name":"name","action":"Deny","resources":["resources","resources"],"priority":602},{"owner":True,"roles":["roles","roles"],"name":"name","action":"Deny","resources":["resources","resources"],"priority":602}],"name":"name","reactions":True,"max_message_length":0,"typing_events":True,"commands":["commands","commands"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/channeltypes',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_channel_type_0(client):
    """Test case for delete_channel_type_0

    Delete channel type
    """
    headers = { 
        'Accept': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/channeltypes/{name}'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_channel_type_0(client):
    """Test case for get_channel_type_0

    Get channel type
    """
    headers = { 
        'Accept': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/channeltypes/{name}'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_channel_types_0(client):
    """Test case for list_channel_types_0

    List channel types
    """
    headers = { 
        'Accept': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/channeltypes',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_channel_type_0(client):
    """Test case for update_channel_type_0

    Update channel type
    """
    body = {"blocklist":"blocklist","grants":{"key":["grants","grants"]},"push_notifications":True,"reminders":True,"custom_events":True,"automod":"disabled","message_retention":"message_retention","url_enrichment":True,"mutes":True,"read_events":True,"NameFromPath":"NameFromPath","blocklist_behavior":"flag","quotes":True,"uploads":True,"connect_events":True,"automod_behavior":"flag","search":True,"replies":True,"automod_thresholds":{"explicit":{"flag":0.5637377,"block":0.5962134},"toxic":{"flag":0.5637377,"block":0.5962134},"spam":{"flag":0.5637377,"block":0.5962134}},"permissions":[{"owner":True,"roles":["roles","roles"],"name":"name","action":"Deny","resources":["resources","resources"],"priority":602},{"owner":True,"roles":["roles","roles"],"name":"name","action":"Deny","resources":["resources","resources"],"priority":602}],"reactions":True,"max_message_length":1601,"typing_events":True,"commands":["commands","commands"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/channeltypes/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

