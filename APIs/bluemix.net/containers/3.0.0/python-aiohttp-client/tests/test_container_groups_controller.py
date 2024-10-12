# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.containers_groups_get_list_item import ContainersGroupsGetListItem
from openapi_server.models.containers_groups_name_or_id_get_details import ContainersGroupsNameOrIdGetDetails
from openapi_server.models.containers_groups_name_or_id_maproute_post_info import ContainersGroupsNameOrIdMaproutePostInfo
from openapi_server.models.containers_groups_name_or_id_patch_updated_info import ContainersGroupsNameOrIdPatchUpdatedInfo
from openapi_server.models.containers_groups_post_created_info import ContainersGroupsPostCreatedInfo
from openapi_server.models.containers_groups_post_required_attributes import ContainersGroupsPostRequiredAttributes
from openapi_server.models.route import Route


pytestmark = pytest.mark.asyncio

async def test_containers_groups_get(client):
    """Test case for containers_groups_get

    List all container groups in a space
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'x_auth_token_example',
        'x_auth_project_id': 'x_auth_project_id_example',
    }
    response = await client.request(
        method='GET',
        path='/v3/containers/groups',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containers_groups_name_or_id_delete(client):
    """Test case for containers_groups_name_or_id_delete

    Stop and delete all container instances in a container group.
    """
    params = [('force', 'force_example')]
    headers = { 
        'x_auth_token': 'x_auth_token_example',
        'x_auth_project_id': 'x_auth_project_id_example',
    }
    response = await client.request(
        method='DELETE',
        path='/v3/containers/groups/{name_or_id}'.format(name_or_id='name_or_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containers_groups_name_or_id_get(client):
    """Test case for containers_groups_name_or_id_get

    Inspect a container group.
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'x_auth_token_example',
        'x_auth_project_id': 'x_auth_project_id_example',
    }
    response = await client.request(
        method='GET',
        path='/v3/containers/groups/{name_or_id}'.format(name_or_id='name_or_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containers_groups_name_or_id_maproute_post(client):
    """Test case for containers_groups_name_or_id_maproute_post

    Map a public route to a container group.
    """
    body = {"domain":"domain","host":"host"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_token': 'x_auth_token_example',
        'x_auth_project_id': 'x_auth_project_id_example',
    }
    response = await client.request(
        method='POST',
        path='/v3/containers/groups/{name_or_id}/maproute'.format(name_or_id='name_or_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containers_groups_name_or_id_patch(client):
    """Test case for containers_groups_name_or_id_patch

    Update a container group.
    """
    body = {"Autorecovery":"Autorecovery","Environment":["Environment","Environment"],"NumberInstances":{"Min":1,"Max":6,"Desired":0}}
    headers = { 
        'Content-Type': 'application/json',
        'x_auth_token': 'x_auth_token_example',
        'x_auth_project_id': 'x_auth_project_id_example',
    }
    response = await client.request(
        method='PATCH',
        path='/v3/containers/groups/{name_or_id}'.format(name_or_id='name_or_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containers_groups_name_or_id_unmaproute_post(client):
    """Test case for containers_groups_name_or_id_unmaproute_post

    Unmap a public route from a container group
    """
    body = {"domain":"domain","host":"host"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_token': 'x_auth_token_example',
        'x_auth_project_id': 'x_auth_project_id_example',
    }
    response = await client.request(
        method='POST',
        path='/v3/containers/groups/{name_or_id}/unmaproute'.format(name_or_id='name_or_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containers_groups_post(client):
    """Test case for containers_groups_post

    Create and start a container group.
    """
    body = {"BluemixApp":"BluemixApp","Volumes":["Volumes","Volumes"],"Autorecovery":"Autorecovery","Memory":0,"Port":5,"NumberInstances":{"Min":5,"Max":1,"Desired":6},"Cmd":["Cmd","Cmd"],"Env":["Env","Env"],"Image":"Image","Route":{"domain":"domain","host":"host"},"Name":"Name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_token': 'x_auth_token_example',
        'x_auth_project_id': 'x_auth_project_id_example',
    }
    response = await client.request(
        method='POST',
        path='/v3/containers/groups',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

