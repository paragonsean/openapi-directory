# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account_get200_response import AccountGet200Response
from openapi_server.models.auth_failed import AuthFailed
from openapi_server.models.rate_limit import RateLimit


pytestmark = pytest.mark.asyncio

async def test_account_get(client):
    """Test case for account_get

    Fetch credit balance and free API calls.
    """
    headers = { 
        'Accept': '*/*',
        'APIKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.0/account',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

