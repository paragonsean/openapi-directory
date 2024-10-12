# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account import Account


pytestmark = pytest.mark.asyncio

async def test_get_account_info(client):
    """Test case for get_account_info

    Get basic information about your account
    """
    headers = { 
        'Accept': 'application/json',
        'training_key': '{API Key}',
    }
    response = await client.request(
        method='GET',
        path='/customvision/v1.2/Training/account',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

