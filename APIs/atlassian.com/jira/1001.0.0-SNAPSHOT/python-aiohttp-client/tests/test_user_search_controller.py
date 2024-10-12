# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.found_users import FoundUsers
from openapi_server.models.page_bean_user import PageBeanUser
from openapi_server.models.page_bean_user_key import PageBeanUserKey
from openapi_server.models.user import User


pytestmark = pytest.mark.asyncio

async def test_find_assignable_users(client):
    """Test case for find_assignable_users

    Find users assignable to issues
    """
    params = [('query', 'query'),
                    ('sessionId', 'session_id_example'),
                    ('username', 'username_example'),
                    ('accountId', 'account_id_example'),
                    ('project', 'project_example'),
                    ('issueKey', 'issue_key_example'),
                    ('startAt', 0),
                    ('maxResults', 50),
                    ('actionDescriptorId', 56),
                    ('recommend', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/user/assignable/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_bulk_assignable_users(client):
    """Test case for find_bulk_assignable_users

    Find users assignable to projects
    """
    params = [('query', 'query'),
                    ('username', 'username_example'),
                    ('accountId', 'account_id_example'),
                    ('projectKeys', 'project_keys_example'),
                    ('startAt', 0),
                    ('maxResults', 50)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/user/assignable/multiProjectSearch',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_user_keys_by_query(client):
    """Test case for find_user_keys_by_query

    Find user keys by query
    """
    params = [('query', 'query_example'),
                    ('startAt', 0),
                    ('maxResults', 100)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/user/search/query/key',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_users(client):
    """Test case for find_users

    Find users
    """
    params = [('query', 'query'),
                    ('username', 'username_example'),
                    ('accountId', 'account_id_example'),
                    ('startAt', 0),
                    ('maxResults', 50),
                    ('property', '_property_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/user/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_users_by_query(client):
    """Test case for find_users_by_query

    Find users by query
    """
    params = [('query', 'query_example'),
                    ('startAt', 0),
                    ('maxResults', 100)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/user/search/query',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_users_for_picker(client):
    """Test case for find_users_for_picker

    Find users for picker
    """
    params = [('query', 'query_example'),
                    ('maxResults', 50),
                    ('showAvatar', False),
                    ('exclude', ['exclude_example']),
                    ('excludeAccountIds', ['exclude_account_ids_example']),
                    ('avatarSize', 'avatar_size_example'),
                    ('excludeConnectUsers', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/user/picker',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_users_with_all_permissions(client):
    """Test case for find_users_with_all_permissions

    Find users with permissions
    """
    params = [('query', 'query'),
                    ('username', 'username_example'),
                    ('accountId', 'account_id_example'),
                    ('permissions', 'permissions_example'),
                    ('issueKey', 'issue_key_example'),
                    ('projectKey', 'project_key_example'),
                    ('startAt', 0),
                    ('maxResults', 50)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/user/permission/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_users_with_browse_permission(client):
    """Test case for find_users_with_browse_permission

    Find users with browse permission
    """
    params = [('query', 'query'),
                    ('username', 'username_example'),
                    ('accountId', 'account_id_example'),
                    ('issueKey', 'issue_key_example'),
                    ('projectKey', 'project_key_example'),
                    ('startAt', 0),
                    ('maxResults', 50)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/user/viewissue/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

