# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_internal import ErrorInternal
from openapi_server.models.error_payment_required import ErrorPaymentRequired
from openapi_server.models.error_throttled import ErrorThrottled
from openapi_server.models.send_message202_response import SendMessage202Response
from openapi_server.models.send_message401_response import SendMessage401Response
from openapi_server.models.send_message422_response import SendMessage422Response
from openapi_server.models.send_message_request import SendMessageRequest


pytestmark = pytest.mark.asyncio

async def test_send_message(client):
    """Test case for send_message

    Send a message to the given channel.
    """
    body = openapi_server.SendMessageRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/messages/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

