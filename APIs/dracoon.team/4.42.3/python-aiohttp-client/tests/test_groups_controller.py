# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.change_group_members_request import ChangeGroupMembersRequest
from openapi_server.models.create_group_request import CreateGroupRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.group import Group
from openapi_server.models.group_list import GroupList
from openapi_server.models.group_user_list import GroupUserList
from openapi_server.models.last_admin_group_room_list import LastAdminGroupRoomList
from openapi_server.models.role_list import RoleList
from openapi_server.models.room_tree_data_list import RoomTreeDataList
from openapi_server.models.update_group_request import UpdateGroupRequest


pytestmark = pytest.mark.asyncio

async def test_add_group_members(client):
    """Test case for add_group_members

    Add group members
    """
    body = {"ids":[0,0]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/groups/{group_id}/users'.format(group_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_group(client):
    """Test case for create_group

    Create new user group
    """
    body = {"name":"name","expiration":{"enableExpiration":True,"expireAt":"2000-01-23T04:56:07.000+00:00"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/groups',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_group(client):
    """Test case for remove_group

    Remove user group
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v4/groups/{group_id}'.format(group_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_group_members(client):
    """Test case for remove_group_members

    Remove group members
    """
    body = {"ids":[0,0]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v4/groups/{group_id}/users'.format(group_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_group(client):
    """Test case for request_group

    Request user group
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/groups/{group_id}'.format(group_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_group_members(client):
    """Test case for request_group_members

    Request group member users or / and users who can become a member
    """
    params = [('offset', 56),
                    ('limit', 56),
                    ('filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/groups/{group_id}/users'.format(group_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_group_roles(client):
    """Test case for request_group_roles

    Request list of roles assigned to the group
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/groups/{group_id}/roles'.format(group_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_group_rooms(client):
    """Test case for request_group_rooms

    Request rooms granted to the group or / and rooms that can be granted
    """
    params = [('offset', 56),
                    ('limit', 56),
                    ('filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/groups/{group_id}/rooms'.format(group_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_groups(client):
    """Test case for request_groups

    Request list of user groups
    """
    params = [('offset', 56),
                    ('limit', 56),
                    ('filter', 'filter_example'),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/groups',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_last_admin_rooms_groups(client):
    """Test case for request_last_admin_rooms_groups

    Request rooms where the group is defined as last admin group
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/groups/{group_id}/last_admin_rooms'.format(group_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_group(client):
    """Test case for update_group

    Update user group's metadata
    """
    body = {"name":"name","expiration":{"enableExpiration":True,"expireAt":"2000-01-23T04:56:07.000+00:00"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v4/groups/{group_id}'.format(group_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

