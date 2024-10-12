# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.users_invite_vendor_user_post_request import UsersInviteVendorUserPostRequest
from openapi_server.models.vendor_users_post_request import VendorUsersPostRequest


pytestmark = pytest.mark.asyncio

async def test_users_invite_vendor_user_post_0(client):
    """Test case for users_invite_vendor_user_post_0

    Invite a VendorUser (Team member)
    """
    data = openapi_server.UsersInviteVendorUserPostRequest()
    headers = { 
        'Content-Type': 'application/json',
        'userApiKey (request header)': 'special-key',
        'userApiKey (query parameter)': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/users/invite_vendor_user',
        headers=headers,
        json=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vendor_users_post_0(client):
    """Test case for vendor_users_post_0

    Create or update a team member by their external_id
    """
    data = openapi_server.VendorUsersPostRequest()
    headers = { 
        'Content-Type': 'application/json',
        'userApiKey (request header)': 'special-key',
        'userApiKey (query parameter)': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/vendor_users',
        headers=headers,
        json=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

