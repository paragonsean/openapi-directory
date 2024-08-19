# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.floating_ip import FloatingIP


pytestmark = pytest.mark.asyncio

async def test_containers_floating_ips_get(client):
    """Test case for containers_floating_ips_get

    List available public IP addresses in a space
    """
    params = [('all', True)]
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'x_auth_token_example',
        'x_auth_project_id': 'x_auth_project_id_example',
    }
    response = await client.request(
        method='GET',
        path='/v3/containers/floating-ips',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containers_floating_ips_ip_release_post(client):
    """Test case for containers_floating_ips_ip_release_post

    Release public IP address
    """
    headers = { 
        'x_auth_token': 'x_auth_token_example',
        'x_auth_project_id': 'x_auth_project_id_example',
    }
    response = await client.request(
        method='POST',
        path='/v3/containers/floating-ips/{ip}/release'.format(ip='ip_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containers_floating_ips_request_post(client):
    """Test case for containers_floating_ips_request_post

    Request a public IP address for a space
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'x_auth_token_example',
        'x_auth_project_id': 'x_auth_project_id_example',
    }
    response = await client.request(
        method='POST',
        path='/v3/containers/floating-ips/request',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containers_name_or_id_floating_ips_ip_bind_post(client):
    """Test case for containers_name_or_id_floating_ips_ip_bind_post

    Bind a public IP address to a single container
    """
    headers = { 
        'x_auth_token': 'x_auth_token_example',
        'x_auth_project_id': 'x_auth_project_id_example',
    }
    response = await client.request(
        method='POST',
        path='/v3/containers/{name_or_id}/floating-ips/{ip}/bind'.format(name_or_id='name_or_id_example', ip='ip_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_containers_name_or_id_floating_ips_ip_unbind_post(client):
    """Test case for containers_name_or_id_floating_ips_ip_unbind_post

    Unbind a public IP address from a container
    """
    headers = { 
        'x_auth_token': 'x_auth_token_example',
        'x_auth_project_id': 'x_auth_project_id_example',
    }
    response = await client.request(
        method='POST',
        path='/v3/containers/{name_or_id}/floating-ips/{ip}/unbind'.format(name_or_id='name_or_id_example', ip='ip_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

