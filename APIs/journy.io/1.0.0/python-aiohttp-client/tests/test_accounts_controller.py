# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_user_to_account_request import AddUserToAccountRequest
from openapi_server.models.delete_account202_response import DeleteAccount202Response
from openapi_server.models.delete_account400_response import DeleteAccount400Response
from openapi_server.models.delete_account_request import DeleteAccountRequest
from openapi_server.models.upsert_account201_response import UpsertAccount201Response
from openapi_server.models.upsert_account_request import UpsertAccountRequest


pytestmark = pytest.mark.asyncio

async def test_add_user_to_account(client):
    """Test case for add_user_to_account

    Add users to an account
    """
    body = openapi_server.AddUserToAccountRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/accounts/users/add',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_account(client):
    """Test case for delete_account

    Delete account
    """
    body = openapi_server.DeleteAccountRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/accounts',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_user_from_account(client):
    """Test case for remove_user_from_account

    Remove user from account
    """
    body = openapi_server.AddUserToAccountRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/accounts/users/remove',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_upsert_account(client):
    """Test case for upsert_account

    Create or update account
    """
    body = openapi_server.UpsertAccountRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/accounts/upsert',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

