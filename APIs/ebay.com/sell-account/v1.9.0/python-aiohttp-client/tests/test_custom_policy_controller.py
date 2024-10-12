# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.custom_policy import CustomPolicy
from openapi_server.models.custom_policy_create_request import CustomPolicyCreateRequest
from openapi_server.models.custom_policy_request import CustomPolicyRequest
from openapi_server.models.custom_policy_response import CustomPolicyResponse


pytestmark = pytest.mark.asyncio

async def test_create_custom_policy(client):
    """Test case for create_custom_policy

    
    """
    body = {"policyType":"policyType","name":"name","description":"description","label":"label"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_ebay_c_marketplace_id': 'x_ebay_c_marketplace_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sell/account/v1/custom_policy/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_custom_policies(client):
    """Test case for get_custom_policies

    
    """
    params = [('policy_types', 'policy_types_example')]
    headers = { 
        'Accept': 'application/json',
        'x_ebay_c_marketplace_id': 'x_ebay_c_marketplace_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/account/v1/custom_policy/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_custom_policy(client):
    """Test case for get_custom_policy

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_ebay_c_marketplace_id': 'x_ebay_c_marketplace_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/account/v1/custom_policy/{custom_policy_id}'.format(custom_policy_id='custom_policy_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_custom_policy(client):
    """Test case for update_custom_policy

    
    """
    body = {"name":"name","description":"description","label":"label"}
    headers = { 
        'Content-Type': 'application/json',
        'x_ebay_c_marketplace_id': 'x_ebay_c_marketplace_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/sell/account/v1/custom_policy/{custom_policy_id}'.format(custom_policy_id='custom_policy_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

