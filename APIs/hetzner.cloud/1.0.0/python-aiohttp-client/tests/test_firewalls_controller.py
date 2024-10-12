# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_firewall_request import CreateFirewallRequest
from openapi_server.models.create_firewall_response import CreateFirewallResponse
from openapi_server.models.firewall_response import FirewallResponse
from openapi_server.models.firewalls_response import FirewallsResponse
from openapi_server.models.update_firewall_request import UpdateFirewallRequest


pytestmark = pytest.mark.asyncio

async def test_firewalls_get(client):
    """Test case for firewalls_get

    Get all Firewalls
    """
    params = [('sort', 'sort_example'),
                    ('name', 'name_example'),
                    ('label_selector', 'label_selector_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/firewalls',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firewalls_id_delete(client):
    """Test case for firewalls_id_delete

    Delete a Firewall
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v1/firewalls/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firewalls_id_get(client):
    """Test case for firewalls_id_get

    Get a Firewall
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/firewalls/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firewalls_id_put(client):
    """Test case for firewalls_id_put

    Update a Firewall
    """
    body = {"name":"new-name","labels":{"labelkey":"value"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v1/firewalls/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firewalls_post(client):
    """Test case for firewalls_post

    Create a Firewall
    """
    body = {"name":"Corporate Intranet Protection","apply_to":[{"server":{"id":0},"label_selector":{"selector":"selector"},"type":"server"},{"server":{"id":0},"label_selector":{"selector":"selector"},"type":"server"}],"rules":[{"direction":"in","port":"80","protocol":"tcp","source_ips":["28.239.13.1/32","28.239.14.0/24","ff21:1eac:9a3b:ee58:5ca:990c:8bc9:c03b/128"]}],"labels":"{}"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/firewalls',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

