# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.user_savings_response import UserSavingsResponse


pytestmark = pytest.mark.asyncio

async def test_usersavings_get(client):
    """Test case for usersavings_get

    Returns Savings for the User
    """
    params = [('FId', '999999'),
                    ('UserToken', 'user_token_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/plo/v1/usersavings',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

