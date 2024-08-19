# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.container import Container
from openapi_server.models.container_id import ContainerId
from openapi_server.models.container_info import ContainerInfo
from openapi_server.models.create_container import CreateContainer
from openapi_server.models.get_container_status import GetContainerStatus


pytestmark = pytest.mark.asyncio

async def test_containers_create_post(client):
    """Test case for containers_create_post

    Create and start a single container
    """
    body = {"BluemixApp":"BluemixApp","Volumes":"Volumes","Memory":0,"HostConfig":{"ExtraHosts":["ExtraHosts","ExtraHosts"],"Binds":["Binds","Binds"],"PortBindings":["PortBindings","PortBindings"],"Links":["Links","Links"]},"Cmd":["Cmd","Cmd"],"Env":["Env","Env"],"Image":"Image","ExposedPorts":["ExposedPorts","ExposedPorts"],"NumberCpus":6,"Cpuset":"Cpuset"}
    params = [('name', 'name_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_token': 'x_auth_token_example',
        'x_auth_project_id': 'x_auth_project_id_example',
    }
    response = await client.request(
        method='POST',
        path='/v3/containers/create',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containers_id_status_get(client):
    """Test case for containers_id_status_get

    List the current state of a container.
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'x_auth_token_example',
        'x_auth_project_id': 'x_auth_project_id_example',
    }
    response = await client.request(
        method='GET',
        path='/v3/containers/{id}/status'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containers_json_get(client):
    """Test case for containers_json_get

    List single containers in a space.
    """
    params = [('all', 'all_example'),
                    ('filters', 'filters_example')]
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'x_auth_token_example',
        'x_auth_project_id': 'x_auth_project_id_example',
    }
    response = await client.request(
        method='GET',
        path='/v3/containers/json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containers_name_or_id_delete(client):
    """Test case for containers_name_or_id_delete

    Remove a single container
    """
    params = [('force', True)]
    headers = { 
        'x_auth_token': 'x_auth_token_example',
        'x_auth_project_id': 'x_auth_project_id_example',
    }
    response = await client.request(
        method='DELETE',
        path='/v3/containers/{name_or_id}'.format(name_or_id='name_or_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containers_name_or_id_json_get(client):
    """Test case for containers_name_or_id_json_get

    Inspect a single container
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'x_auth_token_example',
        'x_auth_project_id': 'x_auth_project_id_example',
    }
    response = await client.request(
        method='GET',
        path='/v3/containers/{name_or_id}/json'.format(name_or_id='name_or_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containers_name_or_id_pause_post(client):
    """Test case for containers_name_or_id_pause_post

    Pause a single container
    """
    headers = { 
        'x_auth_token': 'x_auth_token_example',
        'x_auth_project_id': 'x_auth_project_id_example',
    }
    response = await client.request(
        method='POST',
        path='/v3/containers/{name_or_id}/pause'.format(name_or_id='name_or_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containers_name_or_id_rename_post(client):
    """Test case for containers_name_or_id_rename_post

    Rename a single container
    """
    params = [('name', 'name_example')]
    headers = { 
        'x_auth_token': 'x_auth_token_example',
        'x_auth_project_id': 'x_auth_project_id_example',
    }
    response = await client.request(
        method='POST',
        path='/v3/containers/{name_or_id}/rename'.format(name_or_id='name_or_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containers_name_or_id_restart_post(client):
    """Test case for containers_name_or_id_restart_post

    Restart a single container
    """
    params = [('t', 56)]
    headers = { 
        'x_auth_token': 'x_auth_token_example',
        'x_auth_project_id': 'x_auth_project_id_example',
    }
    response = await client.request(
        method='POST',
        path='/v3/containers/{name_or_id}/restart'.format(name_or_id='name_or_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containers_name_or_id_start_post(client):
    """Test case for containers_name_or_id_start_post

    Start a single container
    """
    headers = { 
        'x_auth_token': 'x_auth_token_example',
        'x_auth_project_id': 'x_auth_project_id_example',
    }
    response = await client.request(
        method='POST',
        path='/v3/containers/{name_or_id}/start'.format(name_or_id='name_or_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containers_name_or_id_stop_post(client):
    """Test case for containers_name_or_id_stop_post

    Stop a single container
    """
    params = [('t', 56)]
    headers = { 
        'x_auth_token': 'x_auth_token_example',
        'x_auth_project_id': 'x_auth_project_id_example',
    }
    response = await client.request(
        method='POST',
        path='/v3/containers/{name_or_id}/stop'.format(name_or_id='name_or_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containers_name_or_id_unpause_post(client):
    """Test case for containers_name_or_id_unpause_post

    Unpause a single container
    """
    headers = { 
        'x_auth_token': 'x_auth_token_example',
        'x_auth_project_id': 'x_auth_project_id_example',
    }
    response = await client.request(
        method='POST',
        path='/v3/containers/{name_or_id}/unpause'.format(name_or_id='name_or_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

