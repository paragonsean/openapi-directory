# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.update_user_address_request import UpdateUserAddressRequest
from openapi_server.models.user_address200_response import UserAddress200Response
from openapi_server.models.user_address_request import UserAddressRequest


pytestmark = pytest.mark.asyncio

async def test_update_user_address(client):
    """Test case for update_user_address

    update the user's return address information
    """
    body = openapi_server.UpdateUserAddressRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/profile/updateAddress',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_address(client):
    """Test case for user_address

    gets the user's return address information
    """
    body = openapi_server.UserAddressRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/profile/address',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

