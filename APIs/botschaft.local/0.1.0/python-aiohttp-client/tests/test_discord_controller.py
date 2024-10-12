# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.discord_message_request import DiscordMessageRequest
from openapi_server.models.http_validation_error import HTTPValidationError


pytestmark = pytest.mark.asyncio

async def test_discord_get_discord_get(client):
    """Test case for discord_get_discord_get

    Discord Get
    """
    params = [('channel', 'channel_example'),
                    ('message', 'message_example'),
                    ('base64_message', 'base64_message_example')]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/discord',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_discord_post_discord_post(client):
    """Test case for discord_post_discord_post

    Discord Post
    """
    body = {"base64_message":"base64_message","channel":"channel","message":"message"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/discord',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

