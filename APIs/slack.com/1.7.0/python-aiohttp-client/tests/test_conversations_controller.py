# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.conversations_archive_error_schema import ConversationsArchiveErrorSchema
from openapi_server.models.conversations_archive_success_schema import ConversationsArchiveSuccessSchema
from openapi_server.models.conversations_close_error_schema import ConversationsCloseErrorSchema
from openapi_server.models.conversations_close_success_schema import ConversationsCloseSuccessSchema
from openapi_server.models.conversations_create_error_schema import ConversationsCreateErrorSchema
from openapi_server.models.conversations_create_success_schema import ConversationsCreateSuccessSchema
from openapi_server.models.conversations_history_error_schema import ConversationsHistoryErrorSchema
from openapi_server.models.conversations_history_success_schema import ConversationsHistorySuccessSchema
from openapi_server.models.conversations_info_error_schema import ConversationsInfoErrorSchema
from openapi_server.models.conversations_info_success_schema import ConversationsInfoSuccessSchema
from openapi_server.models.conversations_invite_error_schema import ConversationsInviteErrorSchema
from openapi_server.models.conversations_invite_error_schema1 import ConversationsInviteErrorSchema1
from openapi_server.models.conversations_join_error_schema import ConversationsJoinErrorSchema
from openapi_server.models.conversations_join_success_schema import ConversationsJoinSuccessSchema
from openapi_server.models.conversations_kick_error_schema import ConversationsKickErrorSchema
from openapi_server.models.conversations_kick_success_schema import ConversationsKickSuccessSchema
from openapi_server.models.conversations_leave_error_schema import ConversationsLeaveErrorSchema
from openapi_server.models.conversations_leave_success_schema import ConversationsLeaveSuccessSchema
from openapi_server.models.conversations_list_error_schema import ConversationsListErrorSchema
from openapi_server.models.conversations_list_success_schema import ConversationsListSuccessSchema
from openapi_server.models.conversations_mark_error_schema import ConversationsMarkErrorSchema
from openapi_server.models.conversations_mark_success_schema import ConversationsMarkSuccessSchema
from openapi_server.models.conversations_members_error_schema import ConversationsMembersErrorSchema
from openapi_server.models.conversations_members_success_schema import ConversationsMembersSuccessSchema
from openapi_server.models.conversations_open_error_schema import ConversationsOpenErrorSchema
from openapi_server.models.conversations_open_success_schema import ConversationsOpenSuccessSchema
from openapi_server.models.conversations_rename_error_schema import ConversationsRenameErrorSchema
from openapi_server.models.conversations_rename_success_schema import ConversationsRenameSuccessSchema
from openapi_server.models.conversations_replies_error_schema import ConversationsRepliesErrorSchema
from openapi_server.models.conversations_replies_success_schema import ConversationsRepliesSuccessSchema
from openapi_server.models.conversations_set_purpose_error_schema import ConversationsSetPurposeErrorSchema
from openapi_server.models.conversations_set_purpose_success_schema import ConversationsSetPurposeSuccessSchema
from openapi_server.models.conversations_set_topic_error_schema import ConversationsSetTopicErrorSchema
from openapi_server.models.conversations_set_topic_success_schema import ConversationsSetTopicSuccessSchema
from openapi_server.models.conversations_unarchive_error_schema import ConversationsUnarchiveErrorSchema
from openapi_server.models.conversations_unarchive_success_schema import ConversationsUnarchiveSuccessSchema


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_conversations_archive(client):
    """Test case for conversations_archive

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'channel': 'channel_example'
        }
    response = await client.request(
        method='POST',
        path='/api/conversations.archive',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_conversations_close(client):
    """Test case for conversations_close

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'channel': 'channel_example'
        }
    response = await client.request(
        method='POST',
        path='/api/conversations.close',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_conversations_create(client):
    """Test case for conversations_create

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'is_private': True,
        'name': 'name_example'
        }
    response = await client.request(
        method='POST',
        path='/api/conversations.create',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_conversations_history(client):
    """Test case for conversations_history

    
    """
    params = [('token', 'token_example'),
                    ('channel', 'channel_example'),
                    ('latest', 3.4),
                    ('oldest', 3.4),
                    ('inclusive', True),
                    ('limit', 56),
                    ('cursor', 'cursor_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/conversations.history',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_conversations_info(client):
    """Test case for conversations_info

    
    """
    params = [('token', 'token_example'),
                    ('channel', 'channel_example'),
                    ('include_locale', True),
                    ('include_num_members', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/conversations.info',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_conversations_invite(client):
    """Test case for conversations_invite

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'channel': 'channel_example',
        'users': 'users_example'
        }
    response = await client.request(
        method='POST',
        path='/api/conversations.invite',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_conversations_join(client):
    """Test case for conversations_join

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'channel': 'channel_example'
        }
    response = await client.request(
        method='POST',
        path='/api/conversations.join',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_conversations_kick(client):
    """Test case for conversations_kick

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'channel': 'channel_example',
        'user': 'user_example'
        }
    response = await client.request(
        method='POST',
        path='/api/conversations.kick',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_conversations_leave(client):
    """Test case for conversations_leave

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'channel': 'channel_example'
        }
    response = await client.request(
        method='POST',
        path='/api/conversations.leave',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_conversations_list(client):
    """Test case for conversations_list

    
    """
    params = [('token', 'token_example'),
                    ('exclude_archived', True),
                    ('types', 'types_example'),
                    ('limit', 56),
                    ('cursor', 'cursor_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/conversations.list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_conversations_mark(client):
    """Test case for conversations_mark

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'channel': 'channel_example',
        'ts': 3.4
        }
    response = await client.request(
        method='POST',
        path='/api/conversations.mark',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_conversations_members(client):
    """Test case for conversations_members

    
    """
    params = [('token', 'token_example'),
                    ('channel', 'channel_example'),
                    ('limit', 56),
                    ('cursor', 'cursor_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/conversations.members',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_conversations_open(client):
    """Test case for conversations_open

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'channel': 'channel_example',
        'return_im': True,
        'users': 'users_example'
        }
    response = await client.request(
        method='POST',
        path='/api/conversations.open',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_conversations_rename(client):
    """Test case for conversations_rename

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'channel': 'channel_example',
        'name': 'name_example'
        }
    response = await client.request(
        method='POST',
        path='/api/conversations.rename',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_conversations_replies(client):
    """Test case for conversations_replies

    
    """
    params = [('token', 'token_example'),
                    ('channel', 'channel_example'),
                    ('ts', 3.4),
                    ('latest', 3.4),
                    ('oldest', 3.4),
                    ('inclusive', True),
                    ('limit', 56),
                    ('cursor', 'cursor_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/conversations.replies',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_conversations_set_purpose(client):
    """Test case for conversations_set_purpose

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'channel': 'channel_example',
        'purpose': 'purpose_example'
        }
    response = await client.request(
        method='POST',
        path='/api/conversations.setPurpose',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_conversations_set_topic(client):
    """Test case for conversations_set_topic

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'channel': 'channel_example',
        'topic': 'topic_example'
        }
    response = await client.request(
        method='POST',
        path='/api/conversations.setTopic',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_conversations_unarchive(client):
    """Test case for conversations_unarchive

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'channel': 'channel_example'
        }
    response = await client.request(
        method='POST',
        path='/api/conversations.unarchive',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

