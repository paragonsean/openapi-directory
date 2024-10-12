# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.column_item import ColumnItem
from openapi_server.models.group_name import GroupName
from openapi_server.models.new_user_details import NewUserDetails
from openapi_server.models.page_bean_user import PageBeanUser
from openapi_server.models.unrestricted_user_email import UnrestrictedUserEmail
from openapi_server.models.user import User
from openapi_server.models.user_migration_bean import UserMigrationBean


pytestmark = pytest.mark.asyncio

async def test_bulk_get_users(client):
    """Test case for bulk_get_users

    Bulk get users
    """
    params = [('startAt', 0),
                    ('maxResults', 10),
                    ('username', ['username_example']),
                    ('key', ['key_example']),
                    ('accountId', ['5b10ac8d82e05b22cc7d4ef5'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/user/bulk',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bulk_get_users_migration(client):
    """Test case for bulk_get_users_migration

    Get account IDs for users
    """
    params = [('startAt', 0),
                    ('maxResults', 10),
                    ('username', ['username_example']),
                    ('key', ['key_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/user/bulk/migration',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_user(client):
    """Test case for create_user

    Create user
    """
    body = {"applicationKeys":["applicationKeys","applicationKeys"],"emailAddress":"emailAddress","password":"password","displayName":"displayName","name":"name","self":"self","key":"key","products":["products","products"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/user',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_users(client):
    """Test case for get_all_users

    Get all users
    """
    params = [('startAt', 0),
                    ('maxResults', 50)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/users/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_users_default(client):
    """Test case for get_all_users_default

    Get all users default
    """
    params = [('startAt', 0),
                    ('maxResults', 50)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/users',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user(client):
    """Test case for get_user

    Get user
    """
    params = [('accountId', '5b10ac8d82e05b22cc7d4ef5'),
                    ('username', 'username_example'),
                    ('key', 'key_example'),
                    ('expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/user',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_default_columns(client):
    """Test case for get_user_default_columns

    Get user default columns
    """
    params = [('accountId', '5b10ac8d82e05b22cc7d4ef5'),
                    ('username', 'username_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/user/columns',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_email(client):
    """Test case for get_user_email

    Get user email
    """
    params = [('accountId', 'account_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/user/email',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_email_bulk(client):
    """Test case for get_user_email_bulk

    Get user email bulk
    """
    params = [('accountId', ['account_id_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/user/email/bulk',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_groups(client):
    """Test case for get_user_groups

    Get user groups
    """
    params = [('accountId', '5b10ac8d82e05b22cc7d4ef5'),
                    ('username', 'username_example'),
                    ('key', 'key_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/user/groups',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_user(client):
    """Test case for remove_user

    Delete user
    """
    params = [('accountId', '5b10ac8d82e05b22cc7d4ef5'),
                    ('username', 'username_example'),
                    ('key', 'key_example')]
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/user',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reset_user_columns(client):
    """Test case for reset_user_columns

    Reset user default columns
    """
    params = [('accountId', '5b10ac8d82e05b22cc7d4ef5'),
                    ('username', 'username_example')]
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/user/columns',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_set_user_columns(client):
    """Test case for set_user_columns

    Set user default columns
    """
    body = ['body_example']
    params = [('accountId', '5b10ac8d82e05b22cc7d4ef5')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/user/columns',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

