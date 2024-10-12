# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.request_access_token_request import RequestAccessTokenRequest
from openapi_server.models.token_details import TokenDetails


pytestmark = pytest.mark.asyncio

async def test_request_access_token(client):
    """Test case for request_access_token

    Request an access token
    """
    body = {"capability":{"channel1":["publish","subscribe"],"wildcard:channels:*":["publish"]},"keyName":"YourKey.Name","timestamp":"1559124196551"}
    params = [('format', 'format_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_ably_version': 'x_ably_version_example',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/keys/{key_name}/requestToken'.format(key_name='key_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

