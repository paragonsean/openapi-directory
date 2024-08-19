# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.message_response import MessageResponse
from openapi_server.models.messages_response import MessagesResponse
from openapi_server.models.send_messages_request import SendMessagesRequest
from openapi_server.models.send_messages_response import SendMessagesResponse


pytestmark = pytest.mark.asyncio

async def test_messages_fetch(client):
    """Test case for messages_fetch

    Fetch message by id
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/accounts/{account_id}/messages/{message_id}'.format(account_id='account_id_example', message_id='message_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_messages_fetch_all(client):
    """Test case for messages_fetch_all

    Fetch messages
    """
    params = [('offset', 56),
                    ('limit', 56),
                    ('contactId', 'contact_id_example'),
                    ('conversationId', 'conversation_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/accounts/{account_id}/messages'.format(account_id='account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_messages_send(client):
    """Test case for messages_send

    Send Messages
    """
    body = {"template":"template","phoneNumberFilter":{"group":{"id":"id"}},"conversationStrategy":"conversationStrategy","filters":{"attributes":["{}","{}"],"tags":["tags","tags"]},"media":[{"url":"url"},{"url":"url"}],"type":"SMS","conversations":["conversations","conversations"],"contacts":[{"firstName":"Chris","lastName":"Bloggs","mobile":{"country":"country","number":"123-456-7890"},"id":"id","email":"chris@sakari.io","tags":[{"visible":True,"tag":"tag"},{"visible":True,"tag":"tag"}]},{"firstName":"Chris","lastName":"Bloggs","mobile":{"country":"country","number":"123-456-7890"},"id":"id","email":"chris@sakari.io","tags":[{"visible":True,"tag":"tag"},{"visible":True,"tag":"tag"}]}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/accounts/{account_id}/messages'.format(account_id='account_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

