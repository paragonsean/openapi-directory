# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.admin_conversations_archive_error_schema import AdminConversationsArchiveErrorSchema
from openapi_server.models.admin_conversations_archive_schema import AdminConversationsArchiveSchema
from openapi_server.models.admin_conversations_convert_to_private_error_schema import AdminConversationsConvertToPrivateErrorSchema
from openapi_server.models.admin_conversations_convert_to_private_schema import AdminConversationsConvertToPrivateSchema
from openapi_server.models.admin_conversations_create_error_schema import AdminConversationsCreateErrorSchema
from openapi_server.models.admin_conversations_create_schema import AdminConversationsCreateSchema
from openapi_server.models.admin_conversations_delete_error_schema import AdminConversationsDeleteErrorSchema
from openapi_server.models.admin_conversations_delete_schema import AdminConversationsDeleteSchema
from openapi_server.models.admin_conversations_disconnect_shared_error_schema import AdminConversationsDisconnectSharedErrorSchema
from openapi_server.models.admin_conversations_get_conversation_prefs_schema import AdminConversationsGetConversationPrefsSchema
from openapi_server.models.admin_conversations_get_teams_error_schema import AdminConversationsGetTeamsErrorSchema
from openapi_server.models.admin_conversations_get_teams_schema import AdminConversationsGetTeamsSchema
from openapi_server.models.admin_conversations_invite_error_schema import AdminConversationsInviteErrorSchema
from openapi_server.models.admin_conversations_invite_schema import AdminConversationsInviteSchema
from openapi_server.models.admin_conversations_rename_schema import AdminConversationsRenameSchema
from openapi_server.models.admin_conversations_rename_schema1 import AdminConversationsRenameSchema1
from openapi_server.models.admin_conversations_search_error_schema import AdminConversationsSearchErrorSchema
from openapi_server.models.admin_conversations_search_schema import AdminConversationsSearchSchema
from openapi_server.models.admin_conversations_set_conversation_prefs_error_schema import AdminConversationsSetConversationPrefsErrorSchema
from openapi_server.models.admin_conversations_set_conversation_prefs_schema import AdminConversationsSetConversationPrefsSchema
from openapi_server.models.admin_conversations_unarchive_error_schema import AdminConversationsUnarchiveErrorSchema
from openapi_server.models.admin_conversations_unarchive_error_schema1 import AdminConversationsUnarchiveErrorSchema1
from openapi_server.models.admin_conversations_unarchive_error_schema2 import AdminConversationsUnarchiveErrorSchema2
from openapi_server.models.admin_conversations_unarchive_schema import AdminConversationsUnarchiveSchema
from openapi_server.models.default_error_template import DefaultErrorTemplate
from openapi_server.models.default_success_template import DefaultSuccessTemplate


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_conversations_archive(client):
    """Test case for admin_conversations_archive

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'channel_id': 'channel_id_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.conversations.archive',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_conversations_convert_to_private(client):
    """Test case for admin_conversations_convert_to_private

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'channel_id': 'channel_id_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.conversations.convertToPrivate',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_conversations_create(client):
    """Test case for admin_conversations_create

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'description': 'description_example',
        'is_private': True,
        'name': 'name_example',
        'org_wide': True,
        'team_id': 'team_id_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.conversations.create',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_conversations_delete(client):
    """Test case for admin_conversations_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'channel_id': 'channel_id_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.conversations.delete',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_conversations_disconnect_shared(client):
    """Test case for admin_conversations_disconnect_shared

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'channel_id': 'channel_id_example',
        'leaving_team_ids': 'leaving_team_ids_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.conversations.disconnectShared',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_conversations_get_conversation_prefs(client):
    """Test case for admin_conversations_get_conversation_prefs

    
    """
    params = [('channel_id', 'channel_id_example')]
    headers = { 
        'Accept': 'application/json',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/admin.conversations.getConversationPrefs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_conversations_get_teams(client):
    """Test case for admin_conversations_get_teams

    
    """
    params = [('channel_id', 'channel_id_example'),
                    ('cursor', 'cursor_example'),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/admin.conversations.getTeams',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_conversations_invite(client):
    """Test case for admin_conversations_invite

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'channel_id': 'channel_id_example',
        'user_ids': 'user_ids_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.conversations.invite',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_conversations_rename(client):
    """Test case for admin_conversations_rename

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'channel_id': 'channel_id_example',
        'name': 'name_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.conversations.rename',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_conversations_search(client):
    """Test case for admin_conversations_search

    
    """
    params = [('team_ids', 'team_ids_example'),
                    ('query', 'query_example'),
                    ('limit', 56),
                    ('cursor', 'cursor_example'),
                    ('search_channel_types', 'search_channel_types_example'),
                    ('sort', 'sort_example'),
                    ('sort_dir', 'sort_dir_example')]
    headers = { 
        'Accept': 'application/json',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/admin.conversations.search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_conversations_set_conversation_prefs(client):
    """Test case for admin_conversations_set_conversation_prefs

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'channel_id': 'channel_id_example',
        'prefs': 'prefs_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.conversations.setConversationPrefs',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_conversations_set_teams(client):
    """Test case for admin_conversations_set_teams

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'channel_id': 'channel_id_example',
        'org_channel': True,
        'target_team_ids': 'target_team_ids_example',
        'team_id': 'team_id_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.conversations.setTeams',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_conversations_unarchive(client):
    """Test case for admin_conversations_unarchive

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'channel_id': 'channel_id_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.conversations.unarchive',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

