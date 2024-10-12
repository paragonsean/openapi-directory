# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account_type import AccountType
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_list_account_types_for_user(client):
    """Test case for list_account_types_for_user

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/accounts/types',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

