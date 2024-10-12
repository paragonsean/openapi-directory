# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.action_response import ActionResponse
from openapi_server.models.actions_response import ActionsResponse
from openapi_server.models.apply_to_resources_request import ApplyToResourcesRequest
from openapi_server.models.remove_from_resources_request import RemoveFromResourcesRequest
from openapi_server.models.set_rules_request import SetRulesRequest


pytestmark = pytest.mark.asyncio

async def test_firewalls_id_actions_action_id_get(client):
    """Test case for firewalls_id_actions_action_id_get

    Get an Action for a Firewall
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/firewalls/{id}/actions/{action_id}'.format(id=56, action_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firewalls_id_actions_apply_to_resources_post(client):
    """Test case for firewalls_id_actions_apply_to_resources_post

    Apply to Resources
    """
    body = {"apply_to":[{"server":{"id":0},"label_selector":{"selector":"env=prod"},"type":"server"},{"server":{"id":0},"label_selector":{"selector":"env=prod"},"type":"server"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/firewalls/{id}/actions/apply_to_resources'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firewalls_id_actions_get(client):
    """Test case for firewalls_id_actions_get

    Get all Actions for a Firewall
    """
    params = [('sort', 'sort_example'),
                    ('status', 'status_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/firewalls/{id}/actions'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firewalls_id_actions_remove_from_resources_post(client):
    """Test case for firewalls_id_actions_remove_from_resources_post

    Remove from Resources
    """
    body = {"remove_from":[{"server":{"id":0},"label_selector":{"selector":"env=prod"},"type":"server"},{"server":{"id":0},"label_selector":{"selector":"env=prod"},"type":"server"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/firewalls/{id}/actions/remove_from_resources'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_firewalls_id_actions_set_rules_post(client):
    """Test case for firewalls_id_actions_set_rules_post

    Set Rules
    """
    body = {"rules":[{"protocol":"tcp","port":"80","description":"description","destination_ips":["28.239.13.1/32","28.239.14.0/24","ff21:1eac:9a3b:ee58:5ca:990c:8bc9:c03b/128"],"source_ips":["28.239.13.1/32","28.239.14.0/24","ff21:1eac:9a3b:ee58:5ca:990c:8bc9:c03b/128"],"direction":"in"},{"protocol":"tcp","port":"80","description":"description","destination_ips":["28.239.13.1/32","28.239.14.0/24","ff21:1eac:9a3b:ee58:5ca:990c:8bc9:c03b/128"],"source_ips":["28.239.13.1/32","28.239.14.0/24","ff21:1eac:9a3b:ee58:5ca:990c:8bc9:c03b/128"],"direction":"in"},{"protocol":"tcp","port":"80","description":"description","destination_ips":["28.239.13.1/32","28.239.14.0/24","ff21:1eac:9a3b:ee58:5ca:990c:8bc9:c03b/128"],"source_ips":["28.239.13.1/32","28.239.14.0/24","ff21:1eac:9a3b:ee58:5ca:990c:8bc9:c03b/128"],"direction":"in"},{"protocol":"tcp","port":"80","description":"description","destination_ips":["28.239.13.1/32","28.239.14.0/24","ff21:1eac:9a3b:ee58:5ca:990c:8bc9:c03b/128"],"source_ips":["28.239.13.1/32","28.239.14.0/24","ff21:1eac:9a3b:ee58:5ca:990c:8bc9:c03b/128"],"direction":"in"},{"protocol":"tcp","port":"80","description":"description","destination_ips":["28.239.13.1/32","28.239.14.0/24","ff21:1eac:9a3b:ee58:5ca:990c:8bc9:c03b/128"],"source_ips":["28.239.13.1/32","28.239.14.0/24","ff21:1eac:9a3b:ee58:5ca:990c:8bc9:c03b/128"],"direction":"in"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/firewalls/{id}/actions/set_rules'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

