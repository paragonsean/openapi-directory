# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.ban_request import BanRequest
from openapi_server.models.connect_request import ConnectRequest
from openapi_server.models.deactivate_user_request import DeactivateUserRequest
from openapi_server.models.deactivate_user_response import DeactivateUserResponse
from openapi_server.models.deactivate_users_request import DeactivateUsersRequest
from openapi_server.models.deactivate_users_response import DeactivateUsersResponse
from openapi_server.models.delete_user_response import DeleteUserResponse
from openapi_server.models.delete_users_request import DeleteUsersRequest
from openapi_server.models.delete_users_response import DeleteUsersResponse
from openapi_server.models.export_user_response import ExportUserResponse
from openapi_server.models.export_users_request import ExportUsersRequest
from openapi_server.models.export_users_response import ExportUsersResponse
from openapi_server.models.flag_request import FlagRequest
from openapi_server.models.flag_response import FlagResponse
from openapi_server.models.guest_request import GuestRequest
from openapi_server.models.guest_response import GuestResponse
from openapi_server.models.mute_user_request import MuteUserRequest
from openapi_server.models.mute_user_response import MuteUserResponse
from openapi_server.models.query_banned_users_request import QueryBannedUsersRequest
from openapi_server.models.query_banned_users_response import QueryBannedUsersResponse
from openapi_server.models.query_users_request import QueryUsersRequest
from openapi_server.models.reactivate_user_request import ReactivateUserRequest
from openapi_server.models.reactivate_user_response import ReactivateUserResponse
from openapi_server.models.reactivate_users_request import ReactivateUsersRequest
from openapi_server.models.reactivate_users_response import ReactivateUsersResponse
from openapi_server.models.response import Response
from openapi_server.models.restore_users_request import RestoreUsersRequest
from openapi_server.models.unmute_response import UnmuteResponse
from openapi_server.models.unmute_user_request import UnmuteUserRequest
from openapi_server.models.update_user_partial_request import UpdateUserPartialRequest
from openapi_server.models.update_users_request import UpdateUsersRequest
from openapi_server.models.update_users_response import UpdateUsersResponse
from openapi_server.models.users_response import UsersResponse


pytestmark = pytest.mark.asyncio

async def test_ban(client):
    """Test case for ban

    Ban user
    """
    body = {"reason":"reason","ip_ban":True,"shadow":True,"user_id":"user_id","id":"id","target_user_id":"target_user_id","type":"type","banned_by":{"push_notifications":{"disabled_until":"2000-01-23T04:56:07.000+00:00","disabled":True},"role":"role","teams":["teams","teams"],"revoke_tokens_issued_before":"2000-01-23T04:56:07.000+00:00","invisible":True,"ban_expires":"2000-01-23T04:56:07.000+00:00","language":"language","banned":True,"id":"id"},"banned_by_id":"banned_by_id","user":{"push_notifications":{"disabled_until":"2000-01-23T04:56:07.000+00:00","disabled":True},"role":"role","teams":["teams","teams"],"revoke_tokens_issued_before":"2000-01-23T04:56:07.000+00:00","invisible":True,"ban_expires":"2000-01-23T04:56:07.000+00:00","language":"language","banned":True,"id":"id"},"timeout":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/moderation/ban',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connect(client):
    """Test case for connect

    Connect (WebSocket)
    """
    params = [('json', openapi_server.ConnectRequest())]
    headers = { 
        'Accept': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/connect',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_guest(client):
    """Test case for create_guest

    Create guest
    """
    body = {"user":{"push_notifications":{"disabled_until":"2000-01-23T04:56:07.000+00:00","disabled":True},"role":"role","teams":["teams","teams"],"revoke_tokens_issued_before":"2000-01-23T04:56:07.000+00:00","invisible":True,"ban_expires":"2000-01-23T04:56:07.000+00:00","language":"language","banned":True,"id":"id"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/guest',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deactivate_user(client):
    """Test case for deactivate_user

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

async def test_deactivate_users(client):
    """Test case for deactivate_users

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

async def test_delete_user(client):
    """Test case for delete_user

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

async def test_delete_users(client):
    """Test case for delete_users

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

async def test_export_user(client):
    """Test case for export_user

    Export users
    """
    body = {"user_ids":["user_ids","user_ids"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/export/users',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_flag_1(client):
    """Test case for flag_1

    Flag
    """
    body = {"user_id":"user_id","target_message_id":"target_message_id","target_user_id":"target_user_id","user":{"push_notifications":{"disabled_until":"2000-01-23T04:56:07.000+00:00","disabled":True},"role":"role","teams":["teams","teams"],"revoke_tokens_issued_before":"2000-01-23T04:56:07.000+00:00","invisible":True,"ban_expires":"2000-01-23T04:56:07.000+00:00","language":"language","banned":True,"id":"id"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/moderation/flag',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_long_poll(client):
    """Test case for long_poll

    Long Poll (Transport)
    """
    params = [('json', openapi_server.ConnectRequest()),
                    ('connection_id', 'connection_id_example')]
    headers = { 
        'Accept': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/longpoll',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mute_user(client):
    """Test case for mute_user

    Mute user
    """
    body = {"user_id":"user_id","target_ids":["target_ids","target_ids"],"user":{"push_notifications":{"disabled_until":"2000-01-23T04:56:07.000+00:00","disabled":True},"role":"role","teams":["teams","teams"],"revoke_tokens_issued_before":"2000-01-23T04:56:07.000+00:00","invisible":True,"ban_expires":"2000-01-23T04:56:07.000+00:00","language":"language","banned":True,"id":"id"},"timeout":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/moderation/mute',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_banned_users(client):
    """Test case for query_banned_users

    Query Banned Users
    """
    params = [('payload', openapi_server.QueryBannedUsersRequest())]
    headers = { 
        'Accept': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/query_banned_users',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_users(client):
    """Test case for query_users

    Query users
    """
    params = [('payload', openapi_server.QueryUsersRequest())]
    headers = { 
        'Accept': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/users',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reactivate_user(client):
    """Test case for reactivate_user

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

async def test_reactivate_users(client):
    """Test case for reactivate_users

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


pytestmark = pytest.mark.asyncio

async def test_restore_users(client):
    """Test case for restore_users

    Restore users
    """
    body = {"user_ids":["user_ids","user_ids"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/users/restore',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unban(client):
    """Test case for unban

    Unban user
    """
    params = [('target_user_id', 'target_user_id_example'),
                    ('type', 'type_example'),
                    ('id', 'id_example')]
    headers = { 
        'Accept': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/moderation/ban',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unflag_1(client):
    """Test case for unflag_1

    Unflag
    """
    body = {"user_id":"user_id","target_message_id":"target_message_id","target_user_id":"target_user_id","user":{"push_notifications":{"disabled_until":"2000-01-23T04:56:07.000+00:00","disabled":True},"role":"role","teams":["teams","teams"],"revoke_tokens_issued_before":"2000-01-23T04:56:07.000+00:00","invisible":True,"ban_expires":"2000-01-23T04:56:07.000+00:00","language":"language","banned":True,"id":"id"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/moderation/unflag',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unmute_user(client):
    """Test case for unmute_user

    Unmute user
    """
    body = {"user_id":"user_id","target_id":"target_id","target_ids":["target_ids","target_ids"],"user":{"push_notifications":{"disabled_until":"2000-01-23T04:56:07.000+00:00","disabled":True},"role":"role","teams":["teams","teams"],"revoke_tokens_issued_before":"2000-01-23T04:56:07.000+00:00","invisible":True,"ban_expires":"2000-01-23T04:56:07.000+00:00","language":"language","banned":True,"id":"id"},"timeout":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/moderation/unmute',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_users(client):
    """Test case for update_users

    Upsert users
    """
    body = {"users":{"key":{"push_notifications":{"disabled_until":"2000-01-23T04:56:07.000+00:00","disabled":True},"role":"role","teams":["teams","teams"],"revoke_tokens_issued_before":"2000-01-23T04:56:07.000+00:00","invisible":True,"ban_expires":"2000-01-23T04:56:07.000+00:00","language":"language","banned":True,"id":"id"}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/users',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_users_partial(client):
    """Test case for update_users_partial

    Partially update user
    """
    body = {"set":{"key":""},"id":"id","unset":["unset","unset"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/users',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_user_id_export_get(client):
    """Test case for users_user_id_export_get

    Export user
    """
    headers = { 
        'Accept': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/users/{user_id}/export'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

