# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account_response import AccountResponse


pytestmark = pytest.mark.asyncio

async def test_get_account(client):
    """Test case for get_account

    Get information about account
    """
    headers = { 
        'Accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/vlm/account',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

