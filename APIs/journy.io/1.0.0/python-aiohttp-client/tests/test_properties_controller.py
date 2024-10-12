# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.delete_account202_response import DeleteAccount202Response
from openapi_server.models.delete_account400_response import DeleteAccount400Response
from openapi_server.models.get_account_properties200_response import GetAccountProperties200Response


pytestmark = pytest.mark.asyncio

async def test_get_account_properties(client):
    """Test case for get_account_properties

    Get account properties
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/properties/accounts',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_properties(client):
    """Test case for get_user_properties

    Get user properties
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/properties/users',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

