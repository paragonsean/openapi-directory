# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.chat_v2_service_channel_invite import ChatV2ServiceChannelInvite
from openapi_server.models.list_invite_response import ListInviteResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_invite(client):
    """Test case for create_invite

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'identity': 'identity_example',
        'role_sid': 'role_sid_example'
        }
    response = await client.request(
        method='POST',
        path='/v2/Services/{service_sid}/Channels/{channel_sid}/Invites'.format(service_sid='service_sid_example', channel_sid='channel_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_invite(client):
    """Test case for delete_invite

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/Services/{service_sid}/Channels/{channel_sid}/Invites/{sid}'.format(service_sid='service_sid_example', channel_sid='channel_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_invite(client):
    """Test case for fetch_invite

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/Services/{service_sid}/Channels/{channel_sid}/Invites/{sid}'.format(service_sid='service_sid_example', channel_sid='channel_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_invite(client):
    """Test case for list_invite

    
    """
    params = [('Identity', ['identity_example']),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/Services/{service_sid}/Channels/{channel_sid}/Invites'.format(service_sid='service_sid_example', channel_sid='channel_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

