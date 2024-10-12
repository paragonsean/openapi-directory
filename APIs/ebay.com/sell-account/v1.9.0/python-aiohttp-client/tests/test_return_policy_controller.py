# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.return_policy import ReturnPolicy
from openapi_server.models.return_policy_request import ReturnPolicyRequest
from openapi_server.models.return_policy_response import ReturnPolicyResponse
from openapi_server.models.set_return_policy_response import SetReturnPolicyResponse


pytestmark = pytest.mark.asyncio

async def test_create_return_policy(client):
    """Test case for create_return_policy

    
    """
    body = {"returnShippingCostPayer":"returnShippingCostPayer","categoryTypes":[{"default":True,"name":"name"},{"default":True,"name":"name"}],"refundMethod":"refundMethod","description":"description","restockingFeePercentage":"restockingFeePercentage","returnInstructions":"returnInstructions","returnPeriod":{"unit":"unit","value":0},"marketplaceId":"marketplaceId","internationalOverride":{"returnShippingCostPayer":"returnShippingCostPayer","returnMethod":"returnMethod","returnsAccepted":True,"returnPeriod":{"unit":"unit","value":0}},"returnMethod":"returnMethod","name":"name","returnsAccepted":True,"extendedHolidayReturnsOffered":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sell/account/v1/return_policy',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_return_policy(client):
    """Test case for delete_return_policy

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/sell/account/v1/return_policy/{return_policy_id}'.format(return_policy_id='return_policy_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_return_policies(client):
    """Test case for get_return_policies

    
    """
    params = [('marketplace_id', 'marketplace_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/account/v1/return_policy',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_return_policy(client):
    """Test case for get_return_policy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/account/v1/return_policy/{return_policy_id}'.format(return_policy_id='return_policy_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_return_policy_by_name(client):
    """Test case for get_return_policy_by_name

    
    """
    params = [('marketplace_id', 'marketplace_id_example'),
                    ('name', 'name_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/account/v1/return_policy/get_by_policy_name',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_return_policy(client):
    """Test case for update_return_policy

    
    """
    body = {"returnShippingCostPayer":"returnShippingCostPayer","categoryTypes":[{"default":True,"name":"name"},{"default":True,"name":"name"}],"refundMethod":"refundMethod","description":"description","restockingFeePercentage":"restockingFeePercentage","returnInstructions":"returnInstructions","returnPeriod":{"unit":"unit","value":0},"marketplaceId":"marketplaceId","internationalOverride":{"returnShippingCostPayer":"returnShippingCostPayer","returnMethod":"returnMethod","returnsAccepted":True,"returnPeriod":{"unit":"unit","value":0}},"returnMethod":"returnMethod","name":"name","returnsAccepted":True,"extendedHolidayReturnsOffered":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/sell/account/v1/return_policy/{return_policy_id}'.format(return_policy_id='return_policy_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

