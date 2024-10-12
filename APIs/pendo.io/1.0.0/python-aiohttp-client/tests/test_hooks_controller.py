# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.hooks_post_request import HooksPostRequest
from openapi_server.models.hooks_unsubscribe_post_request import HooksUnsubscribePostRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_hooks_post(client):
    """Test case for hooks_post

    Subscribe to webhooks
    """
    data = openapi_server.HooksPostRequest()
    headers = { 
        'Content-Type': 'application/json',
        'userApiKey (request header)': 'special-key',
        'userApiKey (query parameter)': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/hooks',
        headers=headers,
        json=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_hooks_unsubscribe_post(client):
    """Test case for hooks_unsubscribe_post

    Unsubscribe from webhooks
    """
    data = openapi_server.HooksUnsubscribePostRequest()
    headers = { 
        'Content-Type': 'application/json',
        'userApiKey (request header)': 'special-key',
        'userApiKey (query parameter)': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/hooks/unsubscribe',
        headers=headers,
        json=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

