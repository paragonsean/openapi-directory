# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account import Account
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_get_account(client):
    """Test case for get_account

    Account info
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/t/vbc.prod/vis/v1/self/account',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

