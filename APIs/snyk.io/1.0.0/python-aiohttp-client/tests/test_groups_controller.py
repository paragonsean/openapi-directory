# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_a_member_to_an_organization_within_a_group_request import AddAMemberToAnOrganizationWithinAGroupRequest
from openapi_server.models.delete_tag_from_group200_response import DeleteTagFromGroup200Response
from openapi_server.models.delete_tag_from_group_request import DeleteTagFromGroupRequest
from openapi_server.models.list_all_tags_in_a_group200_response import ListAllTagsInAGroup200Response
from openapi_server.models.view_group_settings200_response import ViewGroupSettings200Response


pytestmark = pytest.mark.asyncio

async def test_add_a_member_to_an_organization_within_a_group(client):
    """Test case for add_a_member_to_an_organization_within_a_group

    Add a member to an organization within a group
    """
    body = openapi_server.AddAMemberToAnOrganizationWithinAGroupRequest()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/group/{group_id}/org/{org_id}/members'.format(group_id='4a18d42f-0706-4ad0-b127-24078731fbed', org_id='4a18d42f-0706-4ad0-b127-24078731fbed'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_tag_from_group(client):
    """Test case for delete_tag_from_group

    Delete tag from group
    """
    body = openapi_server.DeleteTagFromGroupRequest()
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/group/{group_id}/tags/delete'.format(group_id='4a18d42f-0706-4ad0-b127-24078731fbed'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_all_members_in_a_group(client):
    """Test case for list_all_members_in_a_group

    List all members in a group
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
    }
    response = await client.request(
        method='GET',
        path='/v1/group/{group_id}/members'.format(group_id='4a18d42f-0706-4ad0-b127-24078731fbed'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_all_organizations_in_a_group(client):
    """Test case for list_all_organizations_in_a_group

    List all organizations in a group
    """
    params = [('perPage', 100),
                    ('page', 1),
                    ('name', 'my')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
    }
    response = await client.request(
        method='GET',
        path='/v1/group/{group_id}/orgs'.format(group_id='a060a49f-636e-480f-9e14-38e773b2a97f'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_all_roles_in_a_group(client):
    """Test case for list_all_roles_in_a_group

    List all roles in a group
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
    }
    response = await client.request(
        method='GET',
        path='/v1/group/{group_id}/roles'.format(group_id='a060a49f-636e-480f-9e14-38e773b2a97f'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_all_tags_in_a_group(client):
    """Test case for list_all_tags_in_a_group

    List all tags in a group
    """
    params = [('perPage', 10),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
    }
    response = await client.request(
        method='GET',
        path='/v1/group/{group_id}/tags'.format(group_id='4a18d42f-0706-4ad0-b127-24078731fbed'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_group_settings(client):
    """Test case for update_group_settings

    Update group settings
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='PUT',
        path='/v1/group/{group_id}/settings'.format(group_id='group_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_view_group_settings(client):
    """Test case for view_group_settings

    View group settings
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v1/group/{group_id}/settings'.format(group_id='b61bc07c-27c6-42b3-8b04-0f228ed31a67'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

