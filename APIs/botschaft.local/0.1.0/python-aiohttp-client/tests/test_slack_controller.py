# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.slack_message_request import SlackMessageRequest


pytestmark = pytest.mark.asyncio

async def test_slack_get_slack_get(client):
    """Test case for slack_get_slack_get

    Slack Get
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
        path='/slack',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_slack_post_slack_post(client):
    """Test case for slack_post_slack_post

    Slack Post
    """
    body = {"base64_message":"base64_message","channel":"channel","message":"message"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/slack',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

