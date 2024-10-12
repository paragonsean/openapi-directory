# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.sns_message_request import SnsMessageRequest


pytestmark = pytest.mark.asyncio

async def test_sns_get_sns_get(client):
    """Test case for sns_get_sns_get

    Sns Get
    """
    params = [('message', 'message_example'),
                    ('base64_message', 'base64_message_example')]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/sns',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sns_post_sns_post(client):
    """Test case for sns_post_sns_post

    Sns Post
    """
    body = {"base64_message":"base64_message","message":"message"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/sns',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

