# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.create_group_request_body import CreateGroupRequestBody
from openapi_server.models.group_admin_request_body import GroupAdminRequestBody
from openapi_server.models.group_invite_response import GroupInviteResponse
from openapi_server.models.group_response import GroupResponse
from openapi_server.models.groups_response import GroupsResponse
from openapi_server.models.remove_group_participant_request_body import RemoveGroupParticipantRequestBody
from openapi_server.models.update_group_info_request_body import UpdateGroupInfoRequestBody


pytestmark = pytest.mark.asyncio

async def test_create_group(client):
    """Test case for create_group

    Create-Group
    """
    body = {"subject":"<Group Subject>"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/groups',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_delete_group_icon(client):
    """Test case for delete_group_icon

    Delete-Group-Icon
    """
    headers = { 
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    response = await client.request(
        method='DELETE',
        path='/groups/{group_id}/icon'.format(group_id='group_id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_group_invite(client):
    """Test case for delete_group_invite

    Delete-Group-Invite
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/groups/{group_id}/invite'.format(group_id='group_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_demote_group_admin(client):
    """Test case for demote_group_admin

    Demote-Group-Admin
    """
    body = {"wa_ids":["<Recipient WA-ID, from Contacts API>"]}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/groups/{group_id}/admins'.format(group_id='group_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_groups(client):
    """Test case for get_all_groups

    Get-All-Groups
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/groups',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_group_icon_binary(client):
    """Test case for get_group_icon_binary

    Get-Group-Icon-Binary
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/groups/{group_id}/icon'.format(group_id='group_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_group_info(client):
    """Test case for get_group_info

    Get-Group-Info
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/groups/{group_id}'.format(group_id='group_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_group_invite(client):
    """Test case for get_group_invite

    Get-Group-Invite
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/groups/{group_id}/invite'.format(group_id='group_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_leave_group(client):
    """Test case for leave_group

    Leave-Group
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/groups/{group_id}/leave'.format(group_id='group_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_promote_to_group_admin(client):
    """Test case for promote_to_group_admin

    Promote-To-Group-Admin
    """
    body = {"wa_ids":["<Recipient WA-ID, from Contacts API>"]}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/groups/{group_id}/admins'.format(group_id='group_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_group_participant(client):
    """Test case for remove_group_participant

    Remove-Group-Participant
    """
    body = {"wa_ids":["{{Recipient-WA-ID}}"]}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/groups/{group_id}/participants'.format(group_id='group_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_set_group_icon(client):
    """Test case for set_group_icon

    Set-Group-Icon
    """
    headers = { 
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/groups/{group_id}/icon'.format(group_id='group_id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_group_info(client):
    """Test case for update_group_info

    Update-Group-Info
    """
    body = {"subject":"<New Group Subject>"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/groups/{group_id}'.format(group_id='group_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

