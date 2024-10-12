# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.deactivate_user_request import DeactivateUserRequest
from openapi_server.models.deactivate_user_response import DeactivateUserResponse
from openapi_server.models.deactivate_users_request import DeactivateUsersRequest
from openapi_server.models.deactivate_users_response import DeactivateUsersResponse
from openapi_server.models.delete_channels_request import DeleteChannelsRequest
from openapi_server.models.delete_channels_response import DeleteChannelsResponse
from openapi_server.models.delete_user_response import DeleteUserResponse
from openapi_server.models.delete_users_request import DeleteUsersRequest
from openapi_server.models.delete_users_response import DeleteUsersResponse
from openapi_server.models.reactivate_user_request import ReactivateUserRequest
from openapi_server.models.reactivate_user_response import ReactivateUserResponse
from openapi_server.models.reactivate_users_request import ReactivateUsersRequest
from openapi_server.models.reactivate_users_response import ReactivateUsersResponse


pytestmark = pytest.mark.asyncio

async def test_deactivate_user_0(client):
    """Test case for deactivate_user_0

    Deactivate user
    """
    body = {"user_id":"user_id","created_by_id":"created_by_id","mark_messages_deleted":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/users/{user_id}/deactivate'.format(user_id='user_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deactivate_users_0(client):
    """Test case for deactivate_users_0

    Deactivate users
    """
    body = {"user_ids":["user_ids","user_ids"],"created_by_id":"created_by_id","mark_messages_deleted":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/users/deactivate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_channels_0(client):
    """Test case for delete_channels_0

    Deletes channels asynchronously
    """
    body = {"cids":["cids","cids"],"hard_delete":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/channels/delete',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_user_0(client):
    """Test case for delete_user_0

    Delete user
    """
    params = [('mark_messages_deleted', True),
                    ('hard_delete', True),
                    ('delete_conversation_channels', True)]
    headers = { 
        'Accept': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/users/{user_id}'.format(user_id='user_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_users_0(client):
    """Test case for delete_users_0

    Delete Users
    """
    body = {"new_channel_owner_id":"new_channel_owner_id","user_ids":["user_ids","user_ids"],"messages":"soft","conversations":"soft","user":"soft"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/users/delete',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reactivate_user_0(client):
    """Test case for reactivate_user_0

    Reactivate user
    """
    body = {"restore_messages":True,"user_id":"user_id","name":"name","created_by_id":"created_by_id"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/users/{user_id}/reactivate'.format(user_id='user_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reactivate_users_0(client):
    """Test case for reactivate_users_0

    Reactivate users
    """
    body = {"restore_messages":True,"user_ids":["user_ids","user_ids"],"created_by_id":"created_by_id"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/users/reactivate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

