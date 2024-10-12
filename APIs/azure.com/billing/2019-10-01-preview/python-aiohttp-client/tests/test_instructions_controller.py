# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.instruction import Instruction
from openapi_server.models.instruction_list_result import InstructionListResult


pytestmark = pytest.mark.asyncio

async def test_instructions_get(client):
    """Test case for instructions_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/billingProfiles/{billing_profile_name}/instructions/{instruction_name}'.format(billing_account_name='billing_account_name_example', billing_profile_name='billing_profile_name_example', instruction_name='instruction_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_instructions_list_by_billing_profile(client):
    """Test case for instructions_list_by_billing_profile

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/billingProfiles/{billing_profile_name}/instructions'.format(billing_account_name='billing_account_name_example', billing_profile_name='billing_profile_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_instructions_put(client):
    """Test case for instructions_put

    
    """
    parameters = {"properties":{"amount":0.8008281904610115,"endDate":"2000-01-23T04:56:07.000+00:00","startDate":"2000-01-23T04:56:07.000+00:00"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/billingProfiles/{billing_profile_name}/instructions/{instruction_name}'.format(billing_account_name='billing_account_name_example', billing_profile_name='billing_profile_name_example', instruction_name='instruction_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

