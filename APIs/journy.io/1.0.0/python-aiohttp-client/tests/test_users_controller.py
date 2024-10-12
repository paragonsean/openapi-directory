# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.delete_account202_response import DeleteAccount202Response
from openapi_server.models.delete_account400_response import DeleteAccount400Response
from openapi_server.models.delete_user_request import DeleteUserRequest
from openapi_server.models.link_request import LinkRequest
from openapi_server.models.upsert_user201_response import UpsertUser201Response
from openapi_server.models.upsert_user_request import UpsertUserRequest


pytestmark = pytest.mark.asyncio

async def test_delete_user(client):
    """Test case for delete_user

    Delete user
    """
    body = openapi_server.DeleteUserRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/users',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_link(client):
    """Test case for link

    Link web activity to user
    """
    body = openapi_server.LinkRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/link',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_upsert_user(client):
    """Test case for upsert_user

    Create or update user
    """
    body = openapi_server.UpsertUserRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/users/upsert',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

