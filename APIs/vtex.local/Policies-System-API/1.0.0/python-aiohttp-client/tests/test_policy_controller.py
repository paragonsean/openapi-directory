# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.evaluate_policy_request import EvaluatePolicyRequest
from openapi_server.models.policy_action_get_response import PolicyActionGetResponse
from openapi_server.models.policy_get_response import PolicyGetResponse
from openapi_server.models.policy_save_request import PolicySaveRequest


pytestmark = pytest.mark.asyncio

async def test_api_policy_engine_policies_id_put(client):
    """Test case for api_policy_engine_policies_id_put

    Update Policy
    """
    body = {"name":"name","description":"description","statements":[{"condition":{"conditions":[{"values":["values","values"],"conditions":["conditions","conditions"],"operation":"operation","key":"key"},{"values":["values","values"],"conditions":["conditions","conditions"],"operation":"operation","key":"key"}]},"resource":"resource","effect":"Allow","actions":["",""],"operation":"operation"},{"condition":{"conditions":[{"values":["values","values"],"conditions":["conditions","conditions"],"operation":"operation","key":"key"},{"values":["values","values"],"conditions":["conditions","conditions"],"operation":"operation","key":"key"}]},"resource":"resource","effect":"Allow","actions":["",""],"operation":"operation"}]}
    headers = { 
        'Accept': 'application/octet-stream',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/policy-engine/policies/{id}'.format(id='pa_test_001'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policy_create_or_update(client):
    """Test case for policy_create_or_update

    Create Policy
    """
    body = {"name":"name","description":"description","statements":[{"condition":{"conditions":[{"values":["values","values"],"conditions":["conditions","conditions"],"operation":"operation","key":"key"},{"values":["values","values"],"conditions":["conditions","conditions"],"operation":"operation","key":"key"}]},"resource":"resource","effect":"Allow","actions":["",""],"operation":"operation"},{"condition":{"conditions":[{"values":["values","values"],"conditions":["conditions","conditions"],"operation":"operation","key":"key"},{"values":["values","values"],"conditions":["conditions","conditions"],"operation":"operation","key":"key"}]},"resource":"resource","effect":"Allow","actions":["",""],"operation":"operation"}]}
    headers = { 
        'Accept': 'application/octet-stream',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/policy-engine/policies/{id}'.format(id='pa_test_001'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policy_delete(client):
    """Test case for policy_delete

    Delete Policy by ID
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/policy-engine/policies/{id}'.format(id='pa_test_001'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policy_evaluate(client):
    """Test case for policy_evaluate

    Evaluate Policies
    """
    body = {"resource":"vrn:vtex.promotions-alert:aws-us-east-1:kamila:master:/_v/promotions_alert","context":{"key":""}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/policy-engine/evaluate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policy_get(client):
    """Test case for policy_get

    Get Policy by ID
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/policy-engine/policies/{id}'.format(id='pa_test_001'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policy_list(client):
    """Test case for policy_list

    Get Policy List
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/policy-engine/policies',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

