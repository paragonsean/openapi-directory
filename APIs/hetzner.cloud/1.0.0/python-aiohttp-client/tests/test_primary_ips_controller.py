# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_primary_ip_request import CreatePrimaryIPRequest
from openapi_server.models.create_primary_ip_response import CreatePrimaryIPResponse
from openapi_server.models.primary_ip_response import PrimaryIPResponse
from openapi_server.models.primary_ips_response import PrimaryIPsResponse
from openapi_server.models.update_primary_ip_request import UpdatePrimaryIPRequest


pytestmark = pytest.mark.asyncio

async def test_primary_ips_get(client):
    """Test case for primary_ips_get

    Get all Primary IPs
    """
    params = [('name', 'name_example'),
                    ('label_selector', 'label_selector_example'),
                    ('ip', '127.0.0.1'),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/primary_ips',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_primary_ips_id_delete(client):
    """Test case for primary_ips_id_delete

    Delete a Primary IP
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v1/primary_ips/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_primary_ips_id_get(client):
    """Test case for primary_ips_id_get

    Get a Primary IP
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/primary_ips/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_primary_ips_id_put(client):
    """Test case for primary_ips_id_put

    Update a Primary IP
    """
    body = {"auto_delete":True,"name":"my-ip","labels":{"labelkey":"value"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v1/primary_ips/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_primary_ips_post(client):
    """Test case for primary_ips_post

    Create a Primary IP
    """
    body = {"assignee_type":"server","auto_delete":False,"name":"my-ip","datacenter":"fsn1-dc8","type":"ipv4","assignee_id":17,"labels":{"labelkey":"value"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/primary_ips',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

