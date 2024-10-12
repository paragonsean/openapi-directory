# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.user_token_response import UserTokenResponse


pytestmark = pytest.mark.asyncio

async def test_usertoken_get(client):
    """Test case for usertoken_get

    Returns User Session Token
    """
    params = [('FId', '999999'),
                    ('AuthInfo', 'auth_info_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/plo/v1/usertoken',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

