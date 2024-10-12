# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.access_requester import AccessRequester
from openapi_server.models.group import Group
from openapi_server.models.group_detail import GroupDetail
from openapi_server.models.issue import Issue
from openapi_server.models.member import Member
from openapi_server.models.notification_setting import NotificationSetting
from openapi_server.models.post_v3_groups_id_members_request import PostV3GroupsIdMembersRequest
from openapi_server.models.post_v3_groups_request import PostV3GroupsRequest
from openapi_server.models.project import Project
from openapi_server.models.put_v3_groups_id_access_requests_user_id_approve_request import PutV3GroupsIdAccessRequestsUserIdApproveRequest
from openapi_server.models.put_v3_groups_id_members_user_id_request import PutV3GroupsIdMembersUserIdRequest
from openapi_server.models.put_v3_groups_id_notification_settings_request import PutV3GroupsIdNotificationSettingsRequest
from openapi_server.models.put_v3_groups_id_request import PutV3GroupsIdRequest


pytestmark = pytest.mark.asyncio

async def test_delete_v3_groups_id(client):
    """Test case for delete_v3_groups_id

    Remove a group.
    """
    headers = { 
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/groups/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_v3_groups_id_access_requests_user_id(client):
    """Test case for delete_v3_groups_id_access_requests_user_id

    Denies an access request for the given user.
    """
    headers = { 
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/groups/{id}/access_requests/{user_id}'.format(id='id_example', user_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_v3_groups_id_members_user_id(client):
    """Test case for delete_v3_groups_id_members_user_id

    Removes a user from a group or project.
    """
    headers = { 
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/groups/{id}/members/{user_id}'.format(id='id_example', user_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_get_v3_groups(client):
    """Test case for get_v3_groups

    Get a groups list
    """
    params = [('statistics', True),
                    ('all_available', True),
                    ('search', 'search_example'),
                    ('order_by', name),
                    ('sort', asc),
                    ('page', 56),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    data = FormData()
    data.add_field('skip_groups', [56])
    response = await client.request(
        method='GET',
        path='/api/v3/groups',
        headers=headers,
        data=data,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_groups_id(client):
    """Test case for get_v3_groups_id

    Get a single group, with containing projects.
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/groups/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_groups_id_access_requests(client):
    """Test case for get_v3_groups_id_access_requests

    Gets a list of access requests for a group.
    """
    params = [('page', 56),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/groups/{id}/access_requests'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_groups_id_issues(client):
    """Test case for get_v3_groups_id_issues

    Get a list of group issues
    """
    params = [('state', opened),
                    ('labels', 'labels_example'),
                    ('milestone', 'milestone_example'),
                    ('order_by', created_at),
                    ('sort', desc),
                    ('page', 56),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/groups/{id}/issues'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_groups_id_members(client):
    """Test case for get_v3_groups_id_members

    Gets a list of group or project members viewable by the authenticated user.
    """
    params = [('query', 'query_example'),
                    ('page', 56),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/groups/{id}/members'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_groups_id_members_user_id(client):
    """Test case for get_v3_groups_id_members_user_id

    Gets a member of a group or project.
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/groups/{id}/members/{user_id}'.format(id='id_example', user_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_groups_id_notification_settings(client):
    """Test case for get_v3_groups_id_notification_settings

    Get group level notification level settings, defaults to Global
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/groups/{id}/notification_settings'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_groups_id_projects(client):
    """Test case for get_v3_groups_id_projects

    Get a list of projects in this group.
    """
    params = [('archived', True),
                    ('visibility', 'visibility_example'),
                    ('search', 'search_example'),
                    ('order_by', created_at),
                    ('sort', desc),
                    ('simple', True),
                    ('page', 56),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/groups/{id}/projects'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_groups_owned(client):
    """Test case for get_v3_groups_owned

    Get list of owned groups for authenticated user
    """
    params = [('page', 56),
                    ('per_page', 56),
                    ('statistics', True)]
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/groups/owned',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_groups(client):
    """Test case for post_v3_groups

    Create a group. Available only for users who can create groups.
    """
    body = openapi_server.PostV3GroupsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/groups',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_groups_id_access_requests(client):
    """Test case for post_v3_groups_id_access_requests

    Requests access for the authenticated user to a group.
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/groups/{id}/access_requests'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_groups_id_members(client):
    """Test case for post_v3_groups_id_members

    Adds a member to a group or project.
    """
    body = openapi_server.PostV3GroupsIdMembersRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/groups/{id}/members'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_groups_id_projects_project_id(client):
    """Test case for post_v3_groups_id_projects_project_id

    Transfer a project to the group namespace. Available only for admin.
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/groups/{id}/projects/{project_id}'.format(id='id_example', project_id='project_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_v3_groups_id(client):
    """Test case for put_v3_groups_id

    Update a group. Available only for users who can administrate groups.
    """
    body = openapi_server.PutV3GroupsIdRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/groups/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_v3_groups_id_access_requests_user_id_approve(client):
    """Test case for put_v3_groups_id_access_requests_user_id_approve

    Approves an access request for the given user.
    """
    body = openapi_server.PutV3GroupsIdAccessRequestsUserIdApproveRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/groups/{id}/access_requests/{user_id}/approve'.format(id='id_example', user_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_v3_groups_id_members_user_id(client):
    """Test case for put_v3_groups_id_members_user_id

    Updates a member of a group or project.
    """
    body = openapi_server.PutV3GroupsIdMembersUserIdRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/groups/{id}/members/{user_id}'.format(id='id_example', user_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_v3_groups_id_notification_settings(client):
    """Test case for put_v3_groups_id_notification_settings

    Update group level notification level settings, defaults to Global
    """
    body = openapi_server.PutV3GroupsIdNotificationSettingsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/groups/{id}/notification_settings'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

