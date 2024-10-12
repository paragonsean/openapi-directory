# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.get_reactions_response import GetReactionsResponse
from openapi_server.models.reaction_removal_response import ReactionRemovalResponse
from openapi_server.models.reaction_response import ReactionResponse
from openapi_server.models.send_reaction_request import SendReactionRequest


pytestmark = pytest.mark.asyncio

async def test_delete_reaction_0(client):
    """Test case for delete_reaction_0

    Delete reaction
    """
    params = [('user_id', 'user_id_example')]
    headers = { 
        'Accept': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/messages/{id}/reaction/{type}'.format(id='id_example', type='type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_reactions_0(client):
    """Test case for get_reactions_0

    Get reactions
    """
    params = [('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/messages/{id}/reactions'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_send_reaction_0(client):
    """Test case for send_reaction_0

    Send reaction
    """
    body = {"skip_push":True,"reaction":{"score":7,"user_id":"user_id","message_id":"message_id","type":"type","user":{"push_notifications":{"disabled_until":"2000-01-23T04:56:07.000+00:00","disabled":True},"role":"role","teams":["teams","teams"],"revoke_tokens_issued_before":"2000-01-23T04:56:07.000+00:00","invisible":True,"ban_expires":"2000-01-23T04:56:07.000+00:00","language":"language","banned":True,"id":"id"}},"enforce_unique":True,"ID":"ID"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/messages/{id}/reaction'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

