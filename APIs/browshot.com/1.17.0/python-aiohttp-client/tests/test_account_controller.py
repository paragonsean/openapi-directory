# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account import Account
from openapi_server.models.account_error import AccountError


pytestmark = pytest.mark.asyncio

async def test_get_account_info(client):
    """Test case for get_account_info

    Get information about your account
    """
    params = [('details', 1)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/account/info',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

