# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_floating_ip_request import CreateFloatingIPRequest
from openapi_server.models.floating_ips_get200_response import FloatingIpsGet200Response
from openapi_server.models.floating_ips_id_get200_response import FloatingIpsIdGet200Response
from openapi_server.models.floating_ips_post201_response import FloatingIpsPost201Response
from openapi_server.models.update_floating_ip_request import UpdateFloatingIPRequest


pytestmark = pytest.mark.asyncio

async def test_floating_ips_get(client):
    """Test case for floating_ips_get

    Get all Floating IPs
    """
    params = [('name', 'name_example'),
                    ('label_selector', 'label_selector_example'),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/floating_ips',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_floating_ips_id_delete(client):
    """Test case for floating_ips_id_delete

    Delete a Floating IP
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v1/floating_ips/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_floating_ips_id_get(client):
    """Test case for floating_ips_id_get

    Get a Floating IP
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/floating_ips/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_floating_ips_id_put(client):
    """Test case for floating_ips_id_put

    Update a Floating IP
    """
    body = {"name":"Web Frontend","description":"Web Frontend","labels":{"labelkey":"value"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v1/floating_ips/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_floating_ips_post(client):
    """Test case for floating_ips_post

    Create a Floating IP
    """
    body = {"server":42,"name":"Web Frontend","description":"Web Frontend","home_location":"fsn1","type":"ipv4","labels":{"labelkey":"value"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/floating_ips',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

