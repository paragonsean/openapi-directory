# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.twilio_message_request import TwilioMessageRequest


pytestmark = pytest.mark.asyncio

async def test_twilio_message_get_twilio_get(client):
    """Test case for twilio_message_get_twilio_get

    Twilio Message Get
    """
    params = [('to', 'to_example'),
                    ('message', 'message_example'),
                    ('base64_message', 'base64_message_example')]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/twilio',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_twilio_message_post_twilio_post(client):
    """Test case for twilio_message_post_twilio_post

    Twilio Message Post
    """
    body = {"base64_message":"base64_message","to":"to","message":"message"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/twilio',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

