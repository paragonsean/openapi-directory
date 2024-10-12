# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.flex_v1_interaction_interaction_channel_interaction_channel_invite import FlexV1InteractionInteractionChannelInteractionChannelInvite
from openapi_server.models.list_interaction_channel_invite_response import ListInteractionChannelInviteResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_interaction_channel_invite(client):
    """Test case for create_interaction_channel_invite

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'routing': None
        }
    response = await client.request(
        method='POST',
        path='/v1/Interactions/{interaction_sid}/Channels/{channel_sid}/Invites'.format(interaction_sid='interaction_sid_example', channel_sid='channel_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_interaction_channel_invite(client):
    """Test case for list_interaction_channel_invite

    
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
        path='/v1/Interactions/{interaction_sid}/Channels/{channel_sid}/Invites'.format(interaction_sid='interaction_sid_example', channel_sid='channel_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

