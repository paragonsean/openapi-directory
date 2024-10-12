# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account_details import AccountDetails


pytestmark = pytest.mark.asyncio

async def test_account_get(client):
    """Test case for account_get

    Account Details
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/Account',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

