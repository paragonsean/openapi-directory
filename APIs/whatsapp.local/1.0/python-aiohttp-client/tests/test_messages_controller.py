# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.mark_message_as_read_request_body import MarkMessageAsReadRequestBody
from openapi_server.models.message_response import MessageResponse
from openapi_server.models.send_message_request_body import SendMessageRequestBody


pytestmark = pytest.mark.asyncio

async def test_mark_message_as_read(client):
    """Test case for mark_message_as_read

    Mark-Message-As-Read
    """
    body = {"status":"read"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/messages/{message_id}'.format(message_id='message_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_send_message(client):
    """Test case for send_message

    Send-Message
    """
    body = {"recipient_type":"individual","text":{"body":"<Message Text>"},"to":"{{Recipient-WA-ID}}","type":"text"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/messages',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

