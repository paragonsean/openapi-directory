# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.flex_v1_interaction_interaction_channel import FlexV1InteractionInteractionChannel
from openapi_server.models.interaction_channel_enum_update_channel_status import InteractionChannelEnumUpdateChannelStatus
from openapi_server.models.list_interaction_channel_response import ListInteractionChannelResponse


pytestmark = pytest.mark.asyncio

async def test_fetch_interaction_channel(client):
    """Test case for fetch_interaction_channel

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Interactions/{interaction_sid}/Channels/{sid}'.format(interaction_sid='interaction_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_interaction_channel(client):
    """Test case for list_interaction_channel

    
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
        path='/v1/Interactions/{interaction_sid}/Channels'.format(interaction_sid='interaction_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_interaction_channel(client):
    """Test case for update_interaction_channel

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'routing': None,
        'status': openapi_server.InteractionChannelEnumUpdateChannelStatus()
        }
    response = await client.request(
        method='POST',
        path='/v1/Interactions/{interaction_sid}/Channels/{sid}'.format(interaction_sid='interaction_sid_example', sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

