# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.action_response import ActionResponse
from openapi_server.models.assign_floating_ip_request import AssignFloatingIPRequest
from openapi_server.models.change_dnsptr_request import ChangeDNSPTRRequest
from openapi_server.models.change_protection_request import ChangeProtectionRequest
from openapi_server.models.floating_ips_id_actions_get200_response import FloatingIpsIdActionsGet200Response


pytestmark = pytest.mark.asyncio

async def test_floating_ips_id_actions_action_id_get(client):
    """Test case for floating_ips_id_actions_action_id_get

    Get an Action for a Floating IP
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/floating_ips/{id}/actions/{action_id}'.format(id=56, action_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_floating_ips_id_actions_assign_post(client):
    """Test case for floating_ips_id_actions_assign_post

    Assign a Floating IP to a Server
    """
    body = {"server":42}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/floating_ips/{id}/actions/assign'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_floating_ips_id_actions_change_dns_ptr_post(client):
    """Test case for floating_ips_id_actions_change_dns_ptr_post

    Change reverse DNS entry for a Floating IP
    """
    body = {"ip":"1.2.3.4","dns_ptr":"server02.example.com"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/floating_ips/{id}/actions/change_dns_ptr'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_floating_ips_id_actions_change_protection_post(client):
    """Test case for floating_ips_id_actions_change_protection_post

    Change Floating IP Protection
    """
    body = {"delete":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/floating_ips/{id}/actions/change_protection'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_floating_ips_id_actions_get(client):
    """Test case for floating_ips_id_actions_get

    Get all Actions for a Floating IP
    """
    params = [('sort', 'sort_example'),
                    ('status', 'status_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/floating_ips/{id}/actions'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_floating_ips_id_actions_unassign_post(client):
    """Test case for floating_ips_id_actions_unassign_post

    Unassign a Floating IP
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/floating_ips/{id}/actions/unassign'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

