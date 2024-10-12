# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_user_group import AddUserGroup
from openapi_server.models.add_user_group_member import AddUserGroupMember
from openapi_server.models.error import Error
from openapi_server.models.group_id import GroupId
from openapi_server.models.user import User
from openapi_server.models.user_group import UserGroup
from openapi_server.models.user_id import UserId


pytestmark = pytest.mark.asyncio

async def test_orgunits_orgid_usergroups_get(client):
    """Test case for orgunits_orgid_usergroups_get

    List User Groups.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/orgunits/{orgid}/usergroups'.format(orgid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orgunits_orgid_usergroups_groupid_get(client):
    """Test case for orgunits_orgid_usergroups_groupid_get

    Get user group
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/orgunits/{orgid}/usergroups/{groupid}'.format(orgid=56, groupid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orgunits_orgid_usergroups_groupid_members_get(client):
    """Test case for orgunits_orgid_usergroups_groupid_members_get

    List of all users in group.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/orgunits/{orgid}/usergroups/{groupid}/members'.format(orgid=56, groupid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_orgunits_orgid_usergroups_groupid_members_post(client):
    """Test case for orgunits_orgid_usergroups_groupid_members_post

    Add user group member.
    """
    body = openapi_server.AddUserGroupMember()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/orgunits/{orgid}/usergroups/{groupid}/members'.format(orgid=56, groupid=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_orgunits_orgid_usergroups_groupid_members_uuid_delete(client):
    """Test case for orgunits_orgid_usergroups_groupid_members_uuid_delete

    Remove user group member.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/orgunits/{orgid}/usergroups/{groupid}/members/{uuid}'.format(orgid=56, groupid=56, uuid='uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_orgunits_orgid_usergroups_post(client):
    """Test case for orgunits_orgid_usergroups_post

    Create a User Group.
    """
    body = openapi_server.AddUserGroup()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/orgunits/{orgid}/usergroups'.format(orgid=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

