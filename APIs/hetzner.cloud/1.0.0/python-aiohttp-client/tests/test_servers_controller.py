# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_server_request import CreateServerRequest
from openapi_server.models.create_server_response import CreateServerResponse
from openapi_server.models.load_balancers_id_metrics_get200_response import LoadBalancersIdMetricsGet200Response
from openapi_server.models.servers_get200_response import ServersGet200Response
from openapi_server.models.servers_id_delete200_response import ServersIdDelete200Response
from openapi_server.models.servers_id_get200_response import ServersIdGet200Response
from openapi_server.models.update_server_request import UpdateServerRequest


pytestmark = pytest.mark.asyncio

async def test_servers_get(client):
    """Test case for servers_get

    Get all Servers
    """
    params = [('name', 'name_example'),
                    ('label_selector', 'label_selector_example'),
                    ('sort', 'sort_example'),
                    ('status', 'status_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/servers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servers_id_delete(client):
    """Test case for servers_id_delete

    Delete a Server
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/servers/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servers_id_get(client):
    """Test case for servers_id_get

    Get a Server
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/servers/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servers_id_metrics_get(client):
    """Test case for servers_id_metrics_get

    Get Metrics for a Server
    """
    params = [('type', 'type_example'),
                    ('start', 'start_example'),
                    ('end', 'end_example'),
                    ('step', 'step_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/servers/{id}/metrics'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servers_id_put(client):
    """Test case for servers_id_put

    Update a Server
    """
    body = {"name":"my-server","labels":{"labelkey":"value"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v1/servers/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servers_post(client):
    """Test case for servers_post

    Create a Server
    """
    body = {"image":"ubuntu-20.04","automount":False,"volumes":[123],"firewalls":[{"firewall":38}],"datacenter":"nbg1-dc3","user_data":"#cloud-config\nruncmd:\n- [touch, /root/cloud-init-worked]\n","networks":[456],"public_net":{"enable_ipv4":True,"enable_ipv6":True,"ipv4":0,"ipv6":6},"labels":"{}","ssh_keys":["my-ssh-key"],"start_after_create":True,"name":"my-server","location":"nbg1","placement_group":1,"server_type":"cx11"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/servers',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

