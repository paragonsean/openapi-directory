# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_group_bean import AddGroupBean
from openapi_server.models.found_groups import FoundGroups
from openapi_server.models.group import Group
from openapi_server.models.page_bean_group_details import PageBeanGroupDetails
from openapi_server.models.page_bean_user_details import PageBeanUserDetails
from openapi_server.models.update_user_to_group_bean import UpdateUserToGroupBean


pytestmark = pytest.mark.asyncio

async def test_add_user_to_group(client):
    """Test case for add_user_to_group

    Add user to group
    """
    body = {"accountId":"accountId","name":"name"}
    params = [('groupname', 'groupname_example'),
                    ('groupId', 'group_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/group/user',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bulk_get_groups(client):
    """Test case for bulk_get_groups

    Bulk get groups
    """
    params = [('startAt', 0),
                    ('maxResults', 50),
                    ('groupId', ['3571b9a7-348f-414a-9087-8e1ea03a7df8']),
                    ('groupName', ['group_name_example']),
                    ('accessType', 'access_type_example'),
                    ('applicationKey', 'application_key_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/group/bulk',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_group(client):
    """Test case for create_group

    Create group
    """
    body = {"name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/group',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_groups(client):
    """Test case for find_groups

    Find groups
    """
    params = [('accountId', 'account_id_example'),
                    ('query', 'query'),
                    ('exclude', ['exclude_example']),
                    ('excludeId', ['exclude_id_example']),
                    ('maxResults', 56),
                    ('caseInsensitive', False),
                    ('userName', 'user_name_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/groups/picker',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_group(client):
    """Test case for get_group

    Get group
    """
    params = [('groupname', 'groupname_example'),
                    ('groupId', 'group_id_example'),
                    ('expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/group',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_users_from_group(client):
    """Test case for get_users_from_group

    Get users from group
    """
    params = [('groupname', 'groupname_example'),
                    ('groupId', 'group_id_example'),
                    ('includeInactiveUsers', False),
                    ('startAt', 0),
                    ('maxResults', 50)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/group/member',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_group(client):
    """Test case for remove_group

    Remove group
    """
    params = [('groupname', 'groupname_example'),
                    ('groupId', 'group_id_example'),
                    ('swapGroup', 'swap_group_example'),
                    ('swapGroupId', 'swap_group_id_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/group',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_user_from_group(client):
    """Test case for remove_user_from_group

    Remove user from group
    """
    params = [('groupname', 'groupname_example'),
                    ('groupId', 'group_id_example'),
                    ('username', 'username_example'),
                    ('accountId', '5b10ac8d82e05b22cc7d4ef5')]
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/group/user',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

