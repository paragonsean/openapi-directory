# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.action_response import ActionResponse
from openapi_server.models.assign_primary_ip_request import AssignPrimaryIPRequest
from openapi_server.models.change_dnsptr_request import ChangeDNSPTRRequest
from openapi_server.models.change_protection_request2 import ChangeProtectionRequest2


pytestmark = pytest.mark.asyncio

async def test_primary_ips_id_actions_assign_post(client):
    """Test case for primary_ips_id_actions_assign_post

    Assign a Primary IP to a resource
    """
    body = {"assignee_type":"server","assignee_id":4711}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/primary_ips/{id}/actions/assign'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_primary_ips_id_actions_change_dns_ptr_post(client):
    """Test case for primary_ips_id_actions_change_dns_ptr_post

    Change reverse DNS entry for a Primary IP
    """
    body = {"ip":"1.2.3.4","dns_ptr":"server02.example.com"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/primary_ips/{id}/actions/change_dns_ptr'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_primary_ips_id_actions_change_protection_post(client):
    """Test case for primary_ips_id_actions_change_protection_post

    Change Primary IP Protection
    """
    body = openapi_server.ChangeProtectionRequest2()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/primary_ips/{id}/actions/change_protection'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_primary_ips_id_actions_unassign_post(client):
    """Test case for primary_ips_id_actions_unassign_post

    Unassign a Primary IP from a resource
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/primary_ips/{id}/actions/unassign'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

